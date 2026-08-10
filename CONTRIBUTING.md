# Contributing

## Adding a corpus resource

See the "Adding or updating a resource" section in [README.md](./README.md). In short: drop the file(s) in `corpus/<initiative>/`, add a `corpus/MANIFEST.yaml` entry, open a PR -- CI validates the manifest.

## Changing the skill instructions

Edit `SKILL.md` directly. Keep it pointed at `corpus/MANIFEST.yaml` rather than hardcoding paths to specific files, so future corpus updates don't require instruction changes.

## License

By contributing, you agree that:
- Contributions to `SKILL.md`, `scripts/`, and other repo-native files are licensed under this repo's Apache-2.0 license.
- Contributions to `corpus/` are either your own original work under a compatible license, or vendored content from an OWASP GenAI Security Project source repo whose license is recorded accurately in the `MANIFEST.yaml` entry.
