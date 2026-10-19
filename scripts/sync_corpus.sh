#!/bin/bash
# Mirrors GenAI-Security-Corpus's content into this repo's corpus/ directory.
#
# SOURCE_SUBDIR is the path *inside* the corpus repo that holds the actual
# content -- today that's "corpus" (the repo hasn't been flattened yet); if
# it's ever flattened to put content at the corpus repo's root, change this
# to ".". Either way this script strips that one level at copy time, so the
# skill repo's own corpus/ is never affected by how the corpus repo is laid
# out internally.
set -euo pipefail

CORPUS_REPO_URL="${CORPUS_REPO_URL:-https://github.com/GenAI-Security-Project/GenAI-Security-Corpus.git}"
SOURCE_SUBDIR="${SOURCE_SUBDIR:-corpus}"
DEST_DIR="${DEST_DIR:-corpus}"

workdir=$(mktemp -d)
trap 'rm -rf "$workdir"' EXIT

git clone --depth 1 "$CORPUS_REPO_URL" "$workdir/corpus-src"

src="$workdir/corpus-src/$SOURCE_SUBDIR"
if [ "$SOURCE_SUBDIR" = "." ]; then
  src="$workdir/corpus-src"
fi

if [ ! -d "$src" ]; then
  echo "error: source subdir '$SOURCE_SUBDIR' not found in $CORPUS_REPO_URL" >&2
  exit 1
fi

mkdir -p "$DEST_DIR"
rsync -a --delete --exclude='.git' "$src/" "$DEST_DIR/"

echo "Synced $CORPUS_REPO_URL:$SOURCE_SUBDIR -> $DEST_DIR"
