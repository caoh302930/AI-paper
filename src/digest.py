"""Build DIGEST.md — themed overview of all digested papers."""
from __future__ import annotations

import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from . import PAPERS_DIR, ROOT
from .themes import THEME_ORDER, extract_blurb


DIGEST_PATH = ROOT / "DIGEST.md"


def _meta_field(meta: str, key: str) -> str:
    for line in meta.splitlines():
        if line.startswith(f"- {key}:"):
            return line.split(":", 1)[1].strip().strip("`")
    return ""


def _bilibili_link(meta: str) -> tuple[str, str]:
    m = re.search(r"- bilibili:\s*\[([^\]]+)\]\(([^)]+)\)", meta)
    if m:
        return m.group(1), m.group(2)
    return "", ""


def collect_entries() -> list[dict]:
    entries: list[dict] = []
    if not PAPERS_DIR.exists():
        return entries
    for meta_path in PAPERS_DIR.rglob("00_meta.md"):
        meta = meta_path.read_text(encoding="utf-8", errors="ignore")
        arxiv = _meta_field(meta, "arxiv")
        if not arxiv or arxiv == "N/A":
            continue
        parse_path = meta_path.parent / "02_解析.md"
        parse_md = parse_path.read_text(encoding="utf-8", errors="ignore") if parse_path.exists() else ""
        theme = _meta_field(meta, "theme") or "其他"
        blurb = _meta_field(meta, "blurb") or extract_blurb(parse_md)
        bvid, bili_url = _bilibili_link(meta)
        rel = meta_path.parent.relative_to(ROOT).as_posix()
        title = _meta_field(meta, "video_title")
        # prefer paper title from parse header
        m = re.search(r"^#\s+(.+)$", parse_md, flags=re.M)
        paper_title = (m.group(1).strip() if m else "") or title
        published = _meta_field(meta, "published")
        entries.append(
            {
                "theme": theme,
                "arxiv": arxiv,
                "paper_title": paper_title,
                "video_title": title,
                "blurb": blurb,
                "published": published,
                "bvid": bvid,
                "bili_url": bili_url,
                "dir": rel,
                "abs": _meta_field(meta, "abs"),
            }
        )

    def sort_key(e: dict):
        try:
            return datetime.fromisoformat(e["published"])
        except Exception:  # noqa: BLE001
            return datetime.min

    entries.sort(key=sort_key, reverse=True)
    return entries


def rebuild_digest() -> Path:
    entries = collect_entries()
    by_theme: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_theme[e["theme"]].append(e)

    lines = [
        "# AI Paper 主题总览",
        "",
        "先扫本文件了解每篇在讲什么，再点进具体目录读 `02_解析.md`。",
        "",
        f"- 论文数（有 arXiv）: **{len(entries)}**",
        f"- 更新时间: `{datetime.now().astimezone().isoformat(timespec='seconds')}`",
        "",
        "## 目录",
        "",
    ]
    for theme in THEME_ORDER:
        n = len(by_theme.get(theme) or [])
        if n:
            anchor = theme.replace(" ", "-").replace("/", "")
            lines.append(f"- [{theme}](#{anchor})（{n}）")
    # leftover themes
    for theme in sorted(by_theme.keys()):
        if theme not in THEME_ORDER and by_theme[theme]:
            lines.append(f"- [{theme}](#{theme.replace(' ', '-')})（{len(by_theme[theme])}）")

    lines.append("")

    for theme in THEME_ORDER:
        items = by_theme.get(theme) or []
        if not items:
            continue
        lines.append(f"## {theme}")
        lines.append("")
        for e in items:
            abs_url = e["abs"] if e["abs"] and e["abs"] != "N/A" else f"https://arxiv.org/abs/{e['arxiv']}"
            lines.append(f"### {e['paper_title']}")
            lines.append("")
            lines.append(f"- **一句话:** {e['blurb'] or '（待补）'}")
            lines.append(f"- **arXiv:** [{e['arxiv']}]({abs_url})")
            if e["bili_url"]:
                lines.append(f"- **视频:** [{e['bvid'] or 'bilibili'}]({e['bili_url']})")
            lines.append(f"- **发布:** {e['published'] or '未知'}")
            lines.append(
                f"- **精读:** [{e['dir']}/02_解析.md]({e['dir']}/02_解析.md) · "
                f"[可以做什么]({e['dir']}/03_可以做什么.md)"
            )
            lines.append("")

    for theme, items in sorted(by_theme.items()):
        if theme in THEME_ORDER:
            continue
        lines.append(f"## {theme}")
        lines.append("")
        for e in items:
            lines.append(f"### {e['paper_title']}")
            lines.append("")
            lines.append(f"- **一句话:** {e['blurb'] or '（待补）'}")
            lines.append(f"- **精读:** [{e['dir']}/02_解析.md]({e['dir']}/02_解析.md)")
            lines.append("")

    DIGEST_PATH.write_text("\n".join(lines), encoding="utf-8")
    return DIGEST_PATH
