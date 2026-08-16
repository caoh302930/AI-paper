#!/usr/bin/env python3
"""Nightly pipeline: Bilibili UPs -> papers -> LLM digest -> GitHub."""
from __future__ import annotations

import logging
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src import ensure_dirs, load_seen, now_iso, save_seen  # noqa: E402
from src.bilibili import collect_new_videos, load_config  # noqa: E402
from src.git_sync import commit_and_push  # noqa: E402
from src.llm_analyze import generate_analysis  # noqa: E402
from src.paper_fetch import resolve_paper  # noqa: E402
from src.writer import rebuild_index, write_bundle  # noqa: E402


def setup_log() -> None:
    ensure_dirs()
    log_path = ROOT / "logs" / "run.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def main() -> int:
    setup_log()
    logging.info("=== AI-paper run start %s ===", now_iso())
    cfg = load_config()
    seen = load_seen()
    seen.setdefault("videos", {})
    seen.setdefault("papers", {})

    try:
        videos = collect_new_videos(seen["videos"], cfg)
    except Exception:
        logging.error("collect videos failed:\n%s", traceback.format_exc())
        return 1

    logging.info("new candidate videos: %d", len(videos))
    processed = 0
    for v in videos:
        bvid = v["bvid"]
        logging.info("processing %s | %s", bvid, v.get("title"))
        try:
            paper = resolve_paper(v.get("title", ""), v.get("description", ""))
            aid = (paper.get("arxiv") or {}).get("arxiv_id")
            if aid and aid in seen["papers"]:
                logging.info("skip duplicate paper %s (already digested)", aid)
                seen["videos"][bvid] = {"skipped": "dup_paper", "at": now_iso()}
                continue

            parse_md, ideas_md = generate_analysis(video=v, paper=paper)
            out_dir = write_bundle(video=v, paper=paper, parse_md=parse_md, ideas_md=ideas_md)
            seen["videos"][bvid] = {"dir": str(out_dir.relative_to(ROOT)), "at": now_iso()}
            if aid:
                seen["papers"][aid] = {"bvid": bvid, "dir": str(out_dir.relative_to(ROOT))}
            processed += 1
            logging.info("wrote %s", out_dir)
        except Exception:
            logging.error("failed %s:\n%s", bvid, traceback.format_exc())
            continue

    save_seen(seen)
    rebuild_index()
    push_msg = commit_and_push(f"{processed} new")
    logging.info("git: %s", push_msg)
    logging.info("=== done processed=%d ===", processed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
