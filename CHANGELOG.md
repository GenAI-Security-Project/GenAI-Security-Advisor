# Changelog

All notable changes to this skill are documented here. Versioning follows [Semantic Versioning](https://semver.org/): **patch** for doc/text fixes, **minor** for a new or updated corpus resource, **major** for a taxonomy-breaking change (e.g. a superseded Top 10). The version in `SKILL.md` frontmatter, `.claude-plugin/marketplace.json`, and `gemini-extension.json` are kept in sync at every bump -- see "Versioning" in `CONTRIBUTING.md`.

- **Author:** Scott Clinton
- **Organization:** OWASP GenAI Security Project

## [1.0.1] - 2026-08-10

### Changed

- Split the combined "Scott Clinton (OWASP GenAI Security Project)" author string into separate, distinct metadata fields everywhere it appeared: `SKILL.md` frontmatter now has `author: Scott Clinton` plus `metadata.organization: OWASP GenAI Security Project`; `marketplace.json`'s plugin entry `author` is now person-only (the org was already separately represented in its top-level `owner` field); `gemini-extension.json` gained standalone `author`/`organization` fields (not part of Gemini's documented extension schema, so likely inert metadata rather than something the installer reads -- included for consistency/transparency, not functional effect).

## [1.0.0] - 2026-08-10

Initial public release.

### Added

- `SKILL.md`: skill instructions grounding GenAI/LLM/agentic security guidance in OWASP GenAI Security Project research, covering the LLM Top 10, Agentic Top 10, Data Security, MCP security, red-teaming, incident response, and governance.
- `corpus/`: 19 cataloged resources across 6 initiative categories (15 vendored, 4 linked pending license confirmation) -- see `corpus/MANIFEST.yaml` for the full list. Highlights:
  - The published **OWASP Top 10 for LLM Applications 2026** (canonical markdown, one file per category).
  - The finished **OWASP Top 10 for Agentic Applications 2026** (ASI01-10), superseding an earlier unstable working draft (kept as `status: superseded` for historical reference).
  - The **GenAI Security Crosswalk**: 41 risks (LLM/Agentic/Data Security) mapped to controls across 25 compliance frameworks.
  - Data security, MCP security, red-teaming, and governance/COMPASS resources.
- Cross-platform skill discovery: symlinks and manifests so the same `SKILL.md` is discoverable by Claude Code, OpenAI Codex CLI, GitHub Copilot, and Gemini CLI without any content duplication.
- `scripts/validate_corpus.py` + CI workflow: validates every `MANIFEST.yaml` entry on every PR touching `corpus/`.
- Repository made public.

### Licensing

- This repo's own content (`SKILL.md`, `scripts/`, workflow and manifest files, docs) is licensed **Apache-2.0** -- see `LICENSE`.
- Vendored `corpus/` content is third-party and retains its **original license**, recorded per-entry in `corpus/MANIFEST.yaml`. The overwhelming majority is **CC BY-SA 4.0**, explicitly confirmed in each source document's own license statement before vendoring.
- Four resources are cataloged as `status: linked` rather than vendored, specifically because their license could not be confirmed from the source document text: the LLM AI Cybersecurity & Governance Checklist, the LLM Exploit Generation report, and the GenAI Incident Response Guide. These are linked to their `genai.owasp.org` pages, not copied into this repo, until confirmed with the respective initiative leads.
- Two Solutions Reference Guide documents were deliberately excluded from the corpus -- that content is maintained separately as the Solutions Landscape/Directory project, and duplicating it here would risk drift between two copies.
