#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CRON_LINE="0 0 * * * $ROOT/scripts/run.sh >> $ROOT/logs/cron.log 2>&1"

mkdir -p "$ROOT/logs"
chmod +x "$ROOT/scripts/run.sh" "$ROOT/scripts/run_daily.py" "$ROOT/scripts/install_cron.sh"

# idempotent install
TMP="$(mktemp)"
crontab -l 2>/dev/null | grep -v "$ROOT/scripts/run.sh" >"$TMP" || true
echo "$CRON_LINE" >>"$TMP"
crontab "$TMP"
rm -f "$TMP"
echo "installed cron:"
crontab -l | grep "$ROOT/scripts/run.sh" || true
