# Contributing

## Adding a corpus resource

See the "Adding or updating a resource" section in [README.md](./README.md). In short: drop the file(s) in `corpus/<initiative>/`, add a `corpus/MANIFEST.yaml` entry, open a PR -- CI validates the manifest.

## Changing the skill instructions

Edit `SKILL.md` directly. Keep it pointed at `corpus/MANIFEST.yaml` rather than hardcoding paths to specific files, so future corpus updates don't require instruction changes.

## Versioning

This skill follows [Semantic Versioning](https://semver.org/). Any PR that changes `corpus/` or `SKILL.md`'s behavior must bump the version:

- **patch** (1.0.x) -- doc/text fixes, no behavioral change (e.g. fixing a typo in a manifest note).
- **minor** (1.x.0) -- a new resource added, or an existing resource updated to a newer edition without changing the taxonomy other content depends on.
- **major** (x.0.0) -- a taxonomy-breaking change: a Top 10 gets superseded, category numbering changes, or something the skill previously cited as current is now wrong.

On every bump:
1. Update `version` in **all three** places -- `SKILL.md` frontmatter, `.claude-plugin/marketplace.json` (`metadata.version` and the plugin entry's `version`), and `gemini-extension.json`. These three are what Claude Code, Codex CLI/`npx skills update`, and Gemini CLI's `--auto-update` actually read to detect there's something new -- an untouched version number tells those tools nothing changed even if the corpus did.
2. Add a `CHANGELOG.md` entry under the new version, following the existing format (Added/Changed/licensing notes as relevant).
3. Once merged, tag the commit (`git tag vX.Y.Z`) and cut a GitHub Release with the changelog entry as the release body -- that's what notifies anyone watching the repo.

## License

By contributing, you agree that:
- Contributions to `SKILL.md`, `scripts/`, and other repo-native files are licensed under this repo's Apache-2.0 license.
- Contributions to `corpus/` are either your own original work under a compatible license, or vendored content from an OWASP GenAI Security Project source repo whose license is recorded accurately in the `MANIFEST.yaml` entry.
