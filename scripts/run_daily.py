#!/usr/bin/env python3
"""Nightly pipeline: Bilibili UPs -> fulltext -> deep reading -> GitHub."""
from __future__ import annotations

import logging
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src import ensure_dirs, load_seen, now_iso, save_seen  # noqa: E402
from src.bilibili import collect_new_videos, load_config  # noqa: E402
from src.fulltext import fetch_fulltext  # noqa: E402
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


def process_one(v: dict, seen: dict) -> bool:
    paper = resolve_paper(v.get("title", ""), v.get("description", ""))
    aid = (paper.get("arxiv") or {}).get("arxiv_id")
    if aid and aid in seen["papers"] and not v.get("_force"):
        logging.info("skip duplicate paper %s (already digested)", aid)
        seen["videos"][v["bvid"]] = {"skipped": "dup_paper", "at": now_iso()}
        return False

    # prepare output dir early for fulltext cache
    from src.writer import paper_dir_for

    out_dir = paper_dir_for(v, paper)
    ft_dir = out_dir / "_fulltext_cache"
    fulltext = fetch_fulltext(
        arxiv_id=aid,
        title=(paper.get("arxiv") or {}).get("title") or v.get("title") or "",
        urls=(paper.get("extracted") or {}).get("urls") or [],
        out_dir=ft_dir,
    )
    logging.info(
        "fulltext ok=%s source=%s chars=%s",
        fulltext.get("ok"),
        fulltext.get("source"),
        fulltext.get("chars"),
    )

    parse_md, ideas_md = generate_analysis(video=v, paper=paper, fulltext=fulltext)
    out_dir = write_bundle(
        video=v,
        paper=paper,
        parse_md=parse_md,
        ideas_md=ideas_md,
        fulltext=fulltext,
    )
    seen["videos"][v["bvid"]] = {"dir": str(out_dir.relative_to(ROOT)), "at": now_iso(), "deep": True}
    if aid:
        seen["papers"][aid] = {"bvid": v["bvid"], "dir": str(out_dir.relative_to(ROOT)), "deep": True}
    logging.info("wrote %s", out_dir)
    return True


def main() -> int:
    setup_log()
    logging.info("=== AI-paper run start %s ===", now_iso())
    cfg = load_config()
    seen = load_seen()
    seen.setdefault("videos", {})
    seen.setdefault("papers", {})

    force = "--force" in sys.argv
    only_bvid = None
    for a in sys.argv[1:]:
        if a.startswith("BV"):
            only_bvid = a

    try:
        if only_bvid:
            from src.bilibili import fetch_user_videos, fetch_video_detail

            ups = [u for u in (cfg.get("ups") or []) if u.get("enabled", True)]
            mid = str(ups[0]["mid"]) if ups else "581897590"
            videos = [x for x in fetch_user_videos(mid) if x.get("bvid") == only_bvid]
            if not videos:
                logging.error("bvid not found in recent list: %s", only_bvid)
                return 1
            detail = fetch_video_detail(only_bvid)
            if detail.get("description"):
                videos[0]["description"] = detail["description"]
            if detail.get("title"):
                videos[0]["title"] = detail["title"]
            videos[0]["up_name"] = detail.get("owner") or ups[0].get("name")
            videos[0]["_force"] = True
        else:
            videos = collect_new_videos(seen["videos"], cfg)
            if force:
                for v in videos:
                    v["_force"] = True
    except Exception:
        logging.error("collect videos failed:\n%s", traceback.format_exc())
        return 1

    logging.info("candidate videos: %d", len(videos))
    processed = 0
    for v in videos:
        logging.info("processing %s | %s", v.get("bvid"), v.get("title"))
        try:
            if process_one(v, seen):
                processed += 1
        except Exception:
            logging.error("failed %s:\n%s", v.get("bvid"), traceback.format_exc())
            continue

    save_seen(seen)
    rebuild_index()
    push_msg = commit_and_push(f"{processed} deep")
    logging.info("git: %s", push_msg)
    logging.info("=== done processed=%d ===", processed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
