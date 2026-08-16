"""Shared paths and helpers."""
from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

CONFIG_DIR = ROOT / "config"
PAPERS_DIR = ROOT / "papers"
STATE_DIR = ROOT / "state"
STATE_FILE = STATE_DIR / "seen.json"


def ensure_dirs() -> None:
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    (ROOT / "logs").mkdir(parents=True, exist_ok=True)


def load_seen() -> dict:
    if not STATE_FILE.exists():
        return {"videos": {}, "papers": {}}
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))


def save_seen(data: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def slugify(text: str, max_len: int = 60) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\u4e00-\u9fff\-]+", "-", text, flags=re.UNICODE)
    text = re.sub(r"-+", "-", text).strip("-")
    return (text or "paper")[:max_len]


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def env(key: str, default: str = "") -> str:
    return os.getenv(key, default).strip()
