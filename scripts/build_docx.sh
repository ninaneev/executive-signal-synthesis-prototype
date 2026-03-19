#!/bin/bash

set -euo pipefail

INPUT=${1:-}
OUTPUT=${2:-}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REFERENCE_DOC="$REPO_ROOT/templates/reference.docx"

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
  echo "Usage: ./scripts/build_docx.sh input.md output.docx"
  exit 1
fi

mkdir -p "$(dirname "$OUTPUT")"

pandoc "$INPUT" \
  -o "$OUTPUT" \
  --reference-doc="$REFERENCE_DOC"

echo "DOCX generated at $OUTPUT"
