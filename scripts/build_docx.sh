#!/bin/bash

set -euo pipefail

INPUT=${1:-}
OUTPUT=${2:-}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REFERENCE_DOC="$REPO_ROOT/templates/reference.docx"

normalize_path() {
  if command -v cygpath >/dev/null 2>&1; then
    cygpath -w "$1"
  else
    printf '%s\n' "$1"
  fi
}

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
  echo "Usage: ./scripts/build_docx.sh input.md output.docx"
  exit 1
fi

mkdir -p "$(dirname "$OUTPUT")"

PANDOC_INPUT="$(normalize_path "$INPUT")"
PANDOC_OUTPUT="$(normalize_path "$OUTPUT")"
PANDOC_REFERENCE_DOC="$(normalize_path "$REFERENCE_DOC")"

pandoc "$PANDOC_INPUT" \
  -o "$PANDOC_OUTPUT" \
  --reference-doc="$PANDOC_REFERENCE_DOC"

echo "DOCX generated at $OUTPUT"
