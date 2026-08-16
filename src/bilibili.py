"""Fetch recent videos from configured Bilibili UPs."""
from __future__ import annotations

import time
from datetime import datetime, timedelta, timezone
from typing import Any

import requests
import yaml

from . import CONFIG_DIR, env

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Referer": "https://www.bilibili.com",
}


def load_config() -> dict:
    path = CONFIG_DIR / "ups.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _session() -> requests.Session:
    s = requests.Session()
    s.headers.update(HEADERS)
    cookie = env("BILI_COOKIE")
    if cookie:
        s.headers["Cookie"] = cookie
    return s


def _parse_json_or_raise(r: requests.Response, mid: str) -> dict:
    ctype = (r.headers.get("content-type") or "").lower()
    text = r.text or ""
    if "application/json" not in ctype and text.lstrip().startswith("<"):
        raise RuntimeError(
            f"bilibili blocked mid={mid} (got HTML/captcha). "
            "Set BILI_COOKIE in .env (browser login cookie) or use RSSHUB_URL."
        )
    try:
        return r.json()
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(f"bilibili bad json mid={mid}: {e}; body={text[:200]}") from e


def fetch_user_videos_rss(mid: str) -> list[dict[str, Any]]:
    """Fallback via RSSHub when official API is captcha-blocked."""
    base = env("RSSHUB_URL", "https://rsshub.app").rstrip("/")
    url = f"{base}/bilibili/user/video/{mid}"
    sess = _session()
    r = sess.get(url, timeout=25)
    r.raise_for_status()
    # minimal RSS parse without extra deps
    import re
    from email.utils import parsedate_to_datetime

    items = re.findall(r"<item>(.*?)</item>", r.text, flags=re.S | re.I)
    out: list[dict[str, Any]] = []
    for raw in items:
        title = re.search(r"<title><!\[CDATA\[(.*?)\]\]></title>|<title>(.*?)</title>", raw, re.S)
        link = re.search(r"<link>(.*?)</link>", raw)
        desc = re.search(
            r"<description><!\[CDATA\[(.*?)\]\]></description>|<description>(.*?)</description>",
            raw,
            re.S,
        )
        pub = re.search(r"<pubDate>(.*?)</pubDate>", raw)
        title_s = (title.group(1) or title.group(2) if title else "") or ""
        link_s = (link.group(1) if link else "").strip()
        desc_s = (desc.group(1) or desc.group(2) if desc else "") or ""
        # strip html tags in desc
        desc_s = re.sub(r"<[^>]+>", " ", desc_s)
        desc_s = re.sub(r"\s+", " ", desc_s).strip()
        bvid_m = re.search(r"(BV[\w]+)", link_s)
        created = 0
        if pub:
            try:
                created = int(parsedate_to_datetime(pub.group(1)).timestamp())
            except Exception:  # noqa: BLE001
                created = 0
        out.append(
            {
                "mid": str(mid),
                "bvid": bvid_m.group(1) if bvid_m else link_s,
                "aid": None,
                "title": title_s.strip(),
                "description": desc_s,
                "created": created,
                "length": "",
                "play": None,
                "url": link_s or f"https://www.bilibili.com/video/{bvid_m.group(1) if bvid_m else ''}",
            }
        )
    return out


def fetch_user_videos(mid: str, pages: int = 2, page_size: int = 30) -> list[dict[str, Any]]:
    """List recent videos for a mid. Official API first, RSSHub fallback."""
    sess = _session()
    out: list[dict[str, Any]] = []
    try:
        for pn in range(1, pages + 1):
            url = "https://api.bilibili.com/x/space/arc/search"
            params = {"mid": mid, "ps": page_size, "pn": pn, "order": "pubdate"}
            r = sess.get(url, params=params, timeout=20)
            r.raise_for_status()
            data = _parse_json_or_raise(r, mid)
            if data.get("code") != 0:
                raise RuntimeError(f"bilibili api error mid={mid}: {data}")
            vlist = data.get("data", {}).get("list", {}).get("vlist", []) or []
            if not vlist:
                break
            for v in vlist:
                out.append(
                    {
                        "mid": str(mid),
                        "bvid": v.get("bvid", ""),
                        "aid": v.get("aid"),
                        "title": v.get("title", ""),
                        "description": v.get("description", "") or "",
                        "created": int(v.get("created") or 0),
                        "length": v.get("length", ""),
                        "play": v.get("play"),
                        "url": f"https://www.bilibili.com/video/{v.get('bvid', '')}",
                    }
                )
            time.sleep(0.4)
        return out
    except Exception as e:  # noqa: BLE001
        # official API often captcha-blocks datacenter IPs
        rss = fetch_user_videos_rss(mid)
        if not rss:
            raise RuntimeError(f"official API failed ({e}); RSSHub also empty") from e
        return rss


def fetch_video_detail(bvid: str) -> dict[str, Any]:
    """Enrich with full description when list API truncates."""
    sess = _session()
    url = "https://api.bilibili.com/x/web-interface/view"
    try:
        r = sess.get(url, params={"bvid": bvid}, timeout=20)
        r.raise_for_status()
        if (r.text or "").lstrip().startswith("<"):
            return {}
        data = r.json()
    except Exception:  # noqa: BLE001
        return {}
    if data.get("code") != 0:
        return {}
    d = data.get("data") or {}
    return {
        "title": d.get("title", ""),
        "description": d.get("desc", "") or "",
        "pic": d.get("pic", ""),
        "owner": (d.get("owner") or {}).get("name", ""),
        "pubdate": d.get("pubdate"),
    }


def keyword_hit(text: str, keywords: list[str]) -> bool:
    if not keywords:
        return True
    return any(k and k in text for k in keywords)


def collect_new_videos(seen_videos: dict, cfg: dict | None = None) -> list[dict[str, Any]]:
    cfg = cfg or load_config()
    keywords = cfg.get("title_keywords") or []
    lookback_days = int(cfg.get("lookback_days") or 14)
    max_new = int(cfg.get("max_new_videos_per_run") or 5)
    cutoff = datetime.now(timezone.utc) - timedelta(days=lookback_days)

    candidates: list[dict[str, Any]] = []
    for up in cfg.get("ups") or []:
        if not up.get("enabled", True):
            continue
        mid = str(up["mid"])
        name = up.get("name") or mid
        videos = fetch_user_videos(mid)
        for v in videos:
            bvid = v["bvid"]
            if not bvid or bvid in seen_videos:
                continue
            created = datetime.fromtimestamp(v["created"], tz=timezone.utc)
            if created < cutoff:
                continue
            blob = f"{v['title']}\n{v['description']}"
            if not keyword_hit(blob, keywords):
                continue
            detail = fetch_video_detail(bvid)
            if detail.get("description"):
                v["description"] = detail["description"]
            if detail.get("title"):
                v["title"] = detail["title"]
            v["up_name"] = detail.get("owner") or name
            candidates.append(v)
            time.sleep(0.3)

    candidates.sort(key=lambda x: x["created"], reverse=True)
    return candidates[:max_new]
