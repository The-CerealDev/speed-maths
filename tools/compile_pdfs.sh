#!/bin/bash

# Navigate to the root of the project
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "Recompiling all PDFs. This may take a few seconds..."

for dir in algebra/sheets algebra/answers combinatorics/sheets combinatorics/answers; do
  if [ -d "$dir" ]; then
    echo "Compiling PDFs in $dir..."
    cd "$dir"
    for file in *.tex; do
      # Run pdflatex in batchmode to keep the terminal output clean
      pdflatex -interaction=batchmode "$file" > /dev/null
    done
    cd "$ROOT_DIR"
  fi
done

echo "All PDFs recompiled successfully!"
