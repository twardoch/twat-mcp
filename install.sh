#!/usr/bin/env bash
# install.sh — Install twat-mcp locally
# A MUD/MUSH/MUSE Multi-User Environment plugin for twat
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Installing twat-mcp..."
uv pip install -e . 2>/dev/null || pip install -e .
echo "Done."
