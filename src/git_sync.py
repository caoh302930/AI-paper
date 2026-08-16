"""Git commit + push results to GitHub."""
from __future__ import annotations

import subprocess
from pathlib import Path

from . import ROOT, env, now_iso


def _run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def commit_and_push(summary: str) -> str:
    if env("GIT_AUTO_PUSH", "1") not in {"1", "true", "True", "yes"}:
        return "GIT_AUTO_PUSH disabled"

    _run(["git", "add", "papers", "index.md", "state/seen.json", "config"])
    status = _run(["git", "status", "--porcelain"])
    if not status.stdout.strip():
        return "nothing to commit"

    msg = f"chore: paper digest {now_iso()} — {summary}"
    c = _run(["git", "commit", "-m", msg])
    if c.returncode != 0:
        return f"commit failed: {c.stderr or c.stdout}"

    remote = env("GIT_REMOTE", "origin")
    branch = env("GIT_BRANCH", "main")
    # ensure branch exists
    _run(["git", "branch", "-M", branch])
    p = _run(["git", "push", "-u", remote, branch])
    if p.returncode != 0:
        return f"push failed: {p.stderr or p.stdout}"
    return f"pushed to {remote}/{branch}"
