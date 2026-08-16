"""Extract paper identifiers and fetch arXiv metadata."""
from __future__ import annotations

import re
from typing import Any
from xml.etree import ElementTree as ET

import requests

ARXIV_RE = re.compile(
    r"(?:arxiv\.org/(?:abs|pdf)/|arxiv[:\s]+)(\d{4}\.\d{4,5})(?:v\d+)?",
    re.IGNORECASE,
)
ARXIV_BARE_RE = re.compile(r"\b(\d{4}\.\d{4,5})\b")
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)
URL_RE = re.compile(r"https?://[^\s\)\]（）]+")


def extract_from_text(title: str, description: str) -> dict[str, Any]:
    text = f"{title}\n{description}"
    arxiv_ids = []
    for m in ARXIV_RE.finditer(text):
        arxiv_ids.append(m.group(1))
    if not arxiv_ids:
        # only accept bare ids near paper-ish context to reduce false positives
        if re.search(r"arxiv|论文|paper", text, re.IGNORECASE):
            arxiv_ids.extend(ARXIV_BARE_RE.findall(text))

    # dedupe preserve order
    seen = set()
    arxiv_ids = [x for x in arxiv_ids if not (x in seen or seen.add(x))]

    dois = list(dict.fromkeys(DOI_RE.findall(text)))
    urls = list(dict.fromkeys(URL_RE.findall(text)))
    paper_urls = [
        u
        for u in urls
        if any(
            k in u.lower()
            for k in ("arxiv.org", "openreview.net", "aclanthology.org", "doi.org", "github.com")
        )
    ]

    return {
        "arxiv_ids": arxiv_ids,
        "dois": dois,
        "urls": paper_urls,
        "primary_arxiv": arxiv_ids[0] if arxiv_ids else None,
    }


def fetch_arxiv_meta(arxiv_id: str) -> dict[str, Any]:
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    root = ET.fromstring(r.text)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entry = root.find("a:entry", ns)
    if entry is None:
        return {"arxiv_id": arxiv_id}

    def text(path: str) -> str:
        el = entry.find(path, ns)
        return (el.text or "").strip() if el is not None else ""

    authors = [
        (a.find("a:name", ns).text or "").strip()
        for a in entry.findall("a:author", ns)
        if a.find("a:name", ns) is not None
    ]
    return {
        "arxiv_id": arxiv_id,
        "title": re.sub(r"\s+", " ", text("a:title")),
        "summary": re.sub(r"\s+", " ", text("a:summary")),
        "authors": authors,
        "published": text("a:published"),
        "updated": text("a:updated"),
        "abs_url": f"https://arxiv.org/abs/{arxiv_id}",
        "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
    }


def resolve_paper(title: str, description: str) -> dict[str, Any]:
    extracted = extract_from_text(title, description)
    meta: dict[str, Any] = {"extracted": extracted}
    aid = extracted.get("primary_arxiv")
    if aid:
        try:
            meta["arxiv"] = fetch_arxiv_meta(aid)
        except Exception as e:  # noqa: BLE001
            meta["arxiv_error"] = str(e)
            meta["arxiv"] = {"arxiv_id": aid, "abs_url": f"https://arxiv.org/abs/{aid}"}
    else:
        meta["arxiv"] = None
        meta["fallback_title"] = title
    return meta
