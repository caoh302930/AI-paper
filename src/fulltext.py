"""Fetch paper full text for deep reading.

Priority:
1) paper-fetch CLI if installed (Dictation354/paper-fetch-skill)
2) arXiv HTML / e-print abstract page + PDF text extract
"""
from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

import requests

from . import env

MAX_CHARS = 120_000


def _arxiv_pdf_url(arxiv_id: str) -> str:
    return f"https://arxiv.org/pdf/{arxiv_id}.pdf"


def _arxiv_html_url(arxiv_id: str) -> str:
    return f"https://arxiv.org/html/{arxiv_id}"


def fetch_via_paper_fetch_cli(query: str, out_dir: Path) -> dict[str, Any] | None:
    """Call `paper-fetch` CLI when available. Returns None if not installed."""
    from . import ROOT

    candidates = [
        env("PAPER_FETCH_BIN"),
        str(ROOT / ".venv-pf" / "bin" / "paper-fetch"),
        shutil.which("paper-fetch") or "",
        shutil.which("paper_fetch") or "",
    ]
    exe = next((c for c in candidates if c and Path(c).exists()), "")
    if not exe:
        # try module form on current interpreter (may be 3.10 — usually fails)
        py = shutil.which("python3")
        try:
            chk = subprocess.run(
                [py, "-c", "import paper_fetch"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if chk.returncode != 0:
                return None
            cmd = [py, "-m", "paper_fetch", "fetch", query, "--save-markdown", str(out_dir)]
        except Exception:  # noqa: BLE001
            return None
    else:
        cmd = [exe, "fetch", query, "--save-markdown", str(out_dir)]

    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "source": "paper-fetch-cli", "error": str(e)}
    if r.returncode != 0:
        return {"ok": False, "source": "paper-fetch-cli", "error": (r.stderr or r.stdout)[:500]}

    md_files = sorted(out_dir.rglob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not md_files:
        return {"ok": False, "source": "paper-fetch-cli", "error": "no markdown written"}
    text = md_files[0].read_text(encoding="utf-8", errors="ignore")
    return {
        "ok": True,
        "source": "paper-fetch-cli",
        "path": str(md_files[0]),
        "markdown": text[:MAX_CHARS],
        "chars": len(text),
    }


def _pdf_to_text(pdf_path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError as e:
        raise RuntimeError("pypdf not installed") from e
    reader = PdfReader(str(pdf_path))
    parts: list[str] = []
    for page in reader.pages:
        try:
            parts.append(page.extract_text() or "")
        except Exception:  # noqa: BLE001
            continue
    return "\n\n".join(parts)


def fetch_arxiv_fulltext(arxiv_id: str, cache_dir: Path) -> dict[str, Any]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    sess = requests.Session()
    sess.headers.update(
        {
            "User-Agent": "AI-paper-digest/1.0 (+local research; contact: local)",
            "Accept": "application/pdf,text/html,*/*",
        }
    )

    # 1) try HTML (cleaner for LLM)
    try:
        hr = sess.get(_arxiv_html_url(arxiv_id), timeout=40)
        if hr.status_code == 200 and "html" in (hr.headers.get("content-type") or "").lower():
            html = hr.text
            # crude strip
            text = re.sub(r"(?is)<script.*?>.*?</script>", " ", html)
            text = re.sub(r"(?is)<style.*?>.*?</style>", " ", text)
            text = re.sub(r"(?is)<[^>]+>", " ", text)
            text = re.sub(r"\s+", " ", text).strip()
            if len(text) > 2000:
                md_path = cache_dir / f"{arxiv_id.replace('.', '_')}_html.md"
                md_path.write_text(text[:MAX_CHARS], encoding="utf-8")
                return {
                    "ok": True,
                    "source": "arxiv-html",
                    "path": str(md_path),
                    "markdown": text[:MAX_CHARS],
                    "chars": len(text),
                }
    except Exception as e:  # noqa: BLE001
        html_err = str(e)
    else:
        html_err = f"status={getattr(hr, 'status_code', '?')}"

    # 2) PDF extract
    pdf_path = cache_dir / f"{arxiv_id.replace('.', '_')}.pdf"
    try:
        pr = sess.get(_arxiv_pdf_url(arxiv_id), timeout=90)
        pr.raise_for_status()
        pdf_path.write_bytes(pr.content)
        text = _pdf_to_text(pdf_path)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        md_path = cache_dir / f"{arxiv_id.replace('.', '_')}_pdf.md"
        md_path.write_text(text[:MAX_CHARS], encoding="utf-8")
        return {
            "ok": True,
            "source": "arxiv-pdf",
            "path": str(md_path),
            "pdf_path": str(pdf_path),
            "markdown": text[:MAX_CHARS],
            "chars": len(text),
            "html_fallback_error": html_err,
        }
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "source": "arxiv", "error": str(e), "html_fallback_error": html_err}


def fetch_fulltext(*, arxiv_id: str | None, title: str, urls: list[str], out_dir: Path) -> dict[str, Any]:
    """Best-effort full text. Prefer paper-fetch CLI, then arXiv."""
    out_dir.mkdir(parents=True, exist_ok=True)
    query = None
    if arxiv_id:
        query = f"https://arxiv.org/abs/{arxiv_id}"
    elif urls:
        query = urls[0]
    elif title:
        query = title

    if query:
        with tempfile.TemporaryDirectory(prefix="pfetch_") as td:
            cli = fetch_via_paper_fetch_cli(query, Path(td))
            if cli and cli.get("ok"):
                # copy markdown into out_dir
                dest = out_dir / "fulltext_paper_fetch.md"
                dest.write_text(cli["markdown"], encoding="utf-8")
                cli["path"] = str(dest)
                return cli

    if arxiv_id:
        return fetch_arxiv_fulltext(arxiv_id, out_dir)

    return {
        "ok": False,
        "source": "none",
        "error": "no arxiv id / paper-fetch unavailable; only abstract+video desc available",
    }
