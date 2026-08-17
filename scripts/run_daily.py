#!/usr/bin/env python3
"""Nightly + backfill: only arXiv papers → deep reading → DIGEST by theme → GitHub."""
from __future__ import annotations

import logging
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src import ensure_dirs, load_seen, now_iso, save_seen  # noqa: E402
from src.bilibili import collect_arxiv_candidates, collect_new_videos, load_config  # noqa: E402
from src.digest import rebuild_digest  # noqa: E402
from src.fulltext import fetch_fulltext  # noqa: E402
from src.git_sync import commit_and_push  # noqa: E402
from src.llm_analyze import generate_analysis  # noqa: E402
from src.paper_fetch import resolve_paper  # noqa: E402
from src.themes import classify_theme, extract_blurb  # noqa: E402
from src.writer import paper_dir_for, rebuild_index, write_bundle  # noqa: E402


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


def process_one(v: dict, seen: dict, *, require_arxiv: bool = True) -> bool:
    paper = resolve_paper(v.get("title", ""), v.get("description", ""))
    aid = (paper.get("arxiv") or {}).get("arxiv_id") or v.get("arxiv_id")
    if require_arxiv and not aid:
        logging.info("skip %s: no arXiv id", v.get("bvid"))
        seen["videos"][v["bvid"]] = {"skipped": "no_arxiv", "at": now_iso()}
        return False
    if aid and aid in seen["papers"] and not v.get("_force"):
        logging.info("skip duplicate paper %s", aid)
        seen["videos"][v["bvid"]] = {"skipped": "dup_paper", "at": now_iso()}
        return False

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
    theme = classify_theme(
        v.get("title", ""),
        v.get("description", ""),
        (paper.get("arxiv") or {}).get("title") or "",
        (paper.get("arxiv") or {}).get("summary") or "",
        parse_md[:2000],
    )
    blurb = extract_blurb(parse_md)
    out_dir = write_bundle(
        video=v,
        paper=paper,
        parse_md=parse_md,
        ideas_md=ideas_md,
        fulltext=fulltext,
        theme=theme,
        blurb=blurb,
    )
    seen["videos"][v["bvid"]] = {
        "dir": str(out_dir.relative_to(ROOT)),
        "at": now_iso(),
        "deep": True,
        "arxiv": aid,
        "theme": theme,
    }
    if aid:
        seen["papers"][aid] = {
            "bvid": v["bvid"],
            "dir": str(out_dir.relative_to(ROOT)),
            "deep": True,
            "theme": theme,
        }
    logging.info("wrote %s theme=%s", out_dir, theme)
    return True


def main() -> int:
    setup_log()
    logging.info("=== AI-paper run start %s ===", now_iso())
    cfg = load_config()
    seen = load_seen()
    seen.setdefault("videos", {})
    seen.setdefault("papers", {})

    force = "--force" in sys.argv
    backfill = "--backfill" in sys.argv
    dry_run = "--dry-run" in sys.argv
    only_bvid = next((a for a in sys.argv[1:] if a.startswith("BV")), None)
    limit = None
    for a in sys.argv[1:]:
        if a.startswith("--limit="):
            limit = int(a.split("=", 1)[1])

    try:
        if only_bvid:
            from src.bilibili import fetch_user_videos, fetch_video_detail

            ups = [u for u in (cfg.get("ups") or []) if u.get("enabled", True)]
            mid = str(ups[0]["mid"]) if ups else "581897590"
            videos = [x for x in fetch_user_videos(mid, pages=5) if x.get("bvid") == only_bvid]
            if not videos:
                # try polymer deeper
                from src.bilibili import fetch_user_videos_polymer

                videos = [x for x in fetch_user_videos_polymer(mid, max_pages=30) if x.get("bvid") == only_bvid]
            if not videos:
                logging.error("bvid not found: %s", only_bvid)
                return 1
            detail = fetch_video_detail(only_bvid)
            if detail.get("description"):
                videos[0]["description"] = detail["description"]
            if detail.get("title"):
                videos[0]["title"] = detail["title"]
            videos[0]["up_name"] = detail.get("owner") or ups[0].get("name")
            videos[0]["_force"] = True
        elif backfill:
            videos = collect_arxiv_candidates(
                seen["papers"],
                cfg,
                max_pages=int(cfg.get("backfill_max_pages") or 30),
                limit=limit or int(cfg.get("max_new_videos_per_run") or 5),
            )
        else:
            # daily: recent window first, arXiv-only enforced in process_one
            recent = collect_new_videos(seen["videos"], cfg)
            # also chip away at historical arXiv backlog
            backlog = collect_arxiv_candidates(
                seen["papers"],
                cfg,
                max_pages=int(cfg.get("backfill_max_pages") or 30),
                limit=int(cfg.get("max_new_videos_per_run") or 5),
            )
            # merge unique by bvid, prefer recent order
            seen_b = set()
            videos = []
            for v in recent + backlog:
                if v["bvid"] in seen_b:
                    continue
                seen_b.add(v["bvid"])
                videos.append(v)
            max_n = int(cfg.get("max_new_videos_per_run") or 5)
            videos = videos[:max_n]
            if force:
                for v in videos:
                    v["_force"] = True
    except Exception:
        logging.error("collect videos failed:\n%s", traceback.format_exc())
        return 1

    logging.info("candidate videos: %d", len(videos))
    for v in videos:
        logging.info("  - %s | %s | arxiv=? pending", v.get("bvid"), (v.get("title") or "")[:70])

    if dry_run:
        # resolve arxiv for listing
        for v in videos:
            paper = resolve_paper(v.get("title", ""), v.get("description", ""))
            aid = (paper.get("arxiv") or {}).get("arxiv_id") or v.get("arxiv_id")
            logging.info("dry-run %s arxiv=%s | %s", v.get("bvid"), aid, v.get("title"))
        rebuild_digest()
        return 0

    processed = 0
    for v in videos:
        logging.info("processing %s | %s", v.get("bvid"), v.get("title"))
        try:
            if process_one(v, seen, require_arxiv=True):
                processed += 1
                save_seen(seen)
                rebuild_index()
                rebuild_digest()
        except Exception:
            logging.error("failed %s:\n%s", v.get("bvid"), traceback.format_exc())
            continue

    save_seen(seen)
    rebuild_index()
    rebuild_digest()
    push_msg = commit_and_push(f"{processed} papers")
    logging.info("git: %s", push_msg)
    logging.info("=== done processed=%d ===", processed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
