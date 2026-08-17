"""Write paper folders and rebuild index.md."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from . import PAPERS_DIR, now_iso, slugify


def paper_dir_for(video: dict, paper: dict) -> Path:
    created = datetime.fromtimestamp(video["created"])
    arxiv = (paper.get("arxiv") or {})
    aid = arxiv.get("arxiv_id")
    if aid:
        slug = aid.replace(".", "_")
    else:
        slug = slugify(video.get("title") or video.get("bvid") or "video")
    d = PAPERS_DIR / f"{created:%Y}" / f"{created:%m}" / slug
    d.mkdir(parents=True, exist_ok=True)
    return d


def write_bundle(
    *,
    video: dict,
    paper: dict,
    parse_md: str,
    ideas_md: str,
    fulltext: dict | None = None,
    theme: str = "",
    blurb: str = "",
) -> Path:
    d = paper_dir_for(video, paper)
    arxiv = paper.get("arxiv") or {}
    extracted = paper.get("extracted") or {}
    ft = fulltext or {}

    meta = f"""# Meta

- fetched_at: `{now_iso()}`
- up: {video.get('up_name')} (mid={video.get('mid')})
- bilibili: [{video.get('bvid')}]({video.get('url')})
- video_title: {video.get('title')}
- published: {datetime.fromtimestamp(video['created']).isoformat(timespec='seconds')}
- arxiv: {arxiv.get('arxiv_id') or 'N/A'}
- abs: {arxiv.get('abs_url') or 'N/A'}
- pdf: {arxiv.get('pdf_url') or 'N/A'}
- theme: {theme or '其他'}
- blurb: {blurb.replace(chr(10), ' ') if blurb else ''}
- fulltext_ok: {bool(ft.get('ok'))}
- fulltext_source: {ft.get('source') or 'N/A'}
- fulltext_chars: {ft.get('chars') or 0}
"""
    (d / "00_meta.md").write_text(meta, encoding="utf-8")

    authors = ", ".join(arxiv.get("authors") or [])
    urls = "\n".join(f"- {u}" for u in (extracted.get("urls") or [])) or "- （简介中未解析到额外链接）"
    ft_status = (
        f"已获取（source={ft.get('source')}, chars≈{ft.get('chars')}）"
        if ft.get("ok")
        else f"未获取全文：{ft.get('error') or 'unknown'}"
    )
    original = f"""# 原文

## 视频来源

- UP: {video.get('up_name')}
- 标题: {video.get('title')}
- 链接: {video.get('url')}
- 发布时间: {datetime.fromtimestamp(video['created']).isoformat(timespec='seconds')}

### 视频简介

{video.get('description') or '（无）'}

## 论文原文信息

- 标题: {arxiv.get('title') or video.get('title')}
- 作者: {authors or '未知'}
- arXiv: {arxiv.get('arxiv_id') or '未知'}
- 摘要页: {arxiv.get('abs_url') or '无'}
- PDF: {arxiv.get('pdf_url') or '无'}
- 全文: {ft_status}

### Abstract

{arxiv.get('summary') or '（未获取到摘要；仅保留视频侧信息）'}

### 相关链接

{urls}

> 全文正文见同目录 `01b_全文.md`（若存在）。
"""
    (d / "01_原文.md").write_text(original, encoding="utf-8")

    if ft.get("ok") and ft.get("markdown"):
        (d / "01b_全文.md").write_text(
            f"# 全文\n\n> source: `{ft.get('source')}`\n\n{ft['markdown']}\n",
            encoding="utf-8",
        )

    (d / "02_解析.md").write_text(
        parse_md if parse_md.lstrip().startswith("#") else f"# 解析\n\n{parse_md}",
        encoding="utf-8",
    )
    (d / "03_可以做什么.md").write_text(
        ideas_md if ideas_md.lstrip().startswith("#") else f"# 可以做什么\n\n{ideas_md}",
        encoding="utf-8",
    )
    return d


def rebuild_index() -> None:
    rows: list[tuple[str, Path]] = []
    if PAPERS_DIR.exists():
        for meta in sorted(PAPERS_DIR.rglob("00_meta.md"), reverse=True):
            rel = meta.parent.relative_to(PAPERS_DIR)
            title = ""
            arxiv = ""
            bili = ""
            for line in meta.read_text(encoding="utf-8").splitlines():
                if line.startswith("- video_title:"):
                    title = line.split(":", 1)[1].strip()
                elif line.startswith("- arxiv:"):
                    arxiv = line.split(":", 1)[1].strip()
                elif "bilibili:" in line:
                    bili = line.strip()
            rows.append((f"| {rel} | {title} | {arxiv} | [打开](papers/{rel}/01_原文.md) |", meta.parent))

    lines = [
        "# AI Paper 速读索引",
        "",
        "由定时任务从指定 B 站 UP 采集论文信息，生成「原文 / 解析 / 可以做什么」。",
        "",
        "| 目录 | 视频标题 | arXiv | 链接 |",
        "|------|----------|-------|------|",
    ]
    lines.extend(r[0] for r in rows)
    lines.append("")
    (PAPERS_DIR.parent / "index.md").write_text("\n".join(lines), encoding="utf-8")
