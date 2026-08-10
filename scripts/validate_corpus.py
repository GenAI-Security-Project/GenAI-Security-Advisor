#!/usr/bin/env python3
"""Validate corpus/MANIFEST.yaml: required fields present, referenced paths exist."""
import argparse
import os
import sys

import yaml

REQUIRED_FIELDS = {"id", "title", "initiative", "version", "status", "format", "license"}
VALID_STATUS = {"current", "draft", "superseded", "linked"}


def die(msg: str) -> None:
    print(f"[validate_corpus] ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--manifest", default=None)
    args = ap.parse_args()

    repo_root = os.path.abspath(args.repo_root)
    manifest_path = args.manifest or os.path.join(repo_root, "corpus", "MANIFEST.yaml")

    if not os.path.isfile(manifest_path):
        die(f"manifest not found: {manifest_path}")

    with open(manifest_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    resources = data.get("resources")
    if not isinstance(resources, list) or not resources:
        die("MANIFEST.yaml must contain a non-empty 'resources:' list")

    seen_ids = set()
    for i, r in enumerate(resources):
        if not isinstance(r, dict):
            die(f"resources[{i}] must be a mapping")

        missing = REQUIRED_FIELDS - set(r.keys())
        if missing:
            die(f"resources[{i}] missing required fields: {sorted(missing)}")

        rid = str(r["id"]).strip()
        if not rid:
            die(f"resources[{i}].id is empty")
        if rid in seen_ids:
            die(f"duplicate resource id: {rid}")
        seen_ids.add(rid)

        status = r["status"]
        if status not in VALID_STATUS:
            die(f"resource '{rid}': status '{status}' not one of {sorted(VALID_STATUS)}")

        path = r.get("path")
        if status == "linked":
            if path not in (None, "null"):
                die(f"resource '{rid}': status 'linked' should have path: null")
            if not r.get("source_url") and not r.get("source_repo"):
                die(f"resource '{rid}': linked resource needs source_url or source_repo")
        else:
            if not path:
                die(f"resource '{rid}': status '{status}' requires a path")
            abs_path = os.path.join(repo_root, path)
            if not os.path.exists(abs_path):
                die(f"resource '{rid}': path does not exist: {path}")

        for key in ("license", "title", "initiative", "version"):
            if not str(r[key]).strip():
                die(f"resource '{rid}': {key} is empty")

    print(f"[validate_corpus] OK: {len(resources)} resources validated from {manifest_path}")


if __name__ == "__main__":
    main()
