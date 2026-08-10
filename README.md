# GenAI-Security-Advisor

An [Agent Skill](https://agentskills.io) that grounds security guidance in the [OWASP GenAI Security Project](https://genai.owasp.org)'s published research -- the LLM Top 10, the Agentic Top 10, Data Security risk/framework mappings, MCP security, red-teaming, and governance guidance -- instead of relying on a model's general (and possibly stale) knowledge of the taxonomy.

- **Author:** Scott Clinton
- **Organization:** OWASP GenAI Security Project

See [`SKILL.md`](./SKILL.md) for the skill instructions themselves, and [`CHANGELOG.md`](./CHANGELOG.md) for version history.

## Works across platforms

`SKILL.md` uses the open [Agent Skills](https://agentskills.io) format (YAML frontmatter + Markdown instructions), which as of 2026 is supported by 30+ tools across vendors. There's one canonical file -- `SKILL.md` at the repo root -- discoverable via symlinks at each platform's expected path, so there's nothing to keep in sync:

| Tool | Discovery path (symlink to root `SKILL.md`) |
|---|---|
| Claude Code | `.claude/skills/genai-security-advisor/SKILL.md` |
| OpenAI Codex CLI | `.agents/skills/genai-security-advisor/SKILL.md` |
| GitHub Copilot | `.github/skills/genai-security-advisor/SKILL.md` (also reads `.claude/skills/` and `.agents/skills/` directly) |
| Gemini CLI | `.gemini/skills/genai-security-advisor/SKILL.md` |

Clone this repo and run any of the above from within it -- the skill and `corpus/` are discovered automatically. To edit the skill's instructions, edit root `SKILL.md`; the symlinks need no changes.

### Installing it into other projects

The table above is zero-config discovery *within this repo*. To use the skill while working somewhere else, each platform has its own install/registration mechanism -- verify exact flags against each tool's current `--help`, these are fast-moving CLI surfaces:

| Tool | Registration |
|---|---|
| Claude Code | `.claude-plugin/marketplace.json` at repo root -- `/plugin marketplace add GenAI-Security-Project/GenAI-Security-Advisor`, then `/plugin install`. Or just copy the skill folder into `~/.claude/skills/genai-security-advisor/`. |
| OpenAI Codex CLI | `npx skills add GenAI-Security-Project/GenAI-Security-Advisor -g` (global). The same installer can target multiple hosts at once, e.g. adding `-a codex -a claude-code -a copilot -a gemini-cli`. |
| Gemini CLI | `gemini-extension.json` at repo root + a top-level `skills/genai-security-advisor/SKILL.md` (the extension packaging convention, separate from the `.gemini/skills/` project-discovery path) -- `gemini extensions install https://github.com/GenAI-Security-Project/GenAI-Security-Advisor`. |
| GitHub Copilot | `gh skill install GenAI-Security-Project/GenAI-Security-Advisor` installs to `~/.copilot/skills/`. |

All of these fetch from GitHub, so they only work for whoever has read access to this repo.

## Independence from upstream repos

`corpus/` holds **frozen, point-in-time copies** of content from the OWASP GenAI Security Project's various initiative repos -- plain files, copied and committed, never git submodules or any other live reference. If an upstream repo changes, nothing here changes automatically. This is deliberate: the Advisor's answers shouldn't shift underneath users because someone edited a document in an unrelated repo. Pulling in an upstream update is always a manual, reviewed act -- see "Adding or updating a resource" below. Each vendored `MANIFEST.yaml` entry records the exact upstream commit (`vendored_commit`) it was copied from, purely for provenance -- not consulted at query time, not a sync pointer.

## Repository layout

- **`SKILL.md`** -- the skill's instructions (Apache-2.0, this repo's own work). Canonical copy; `.claude/`, `.agents/`, `.github/`, `.gemini/` each hold a `skills/genai-security-advisor/SKILL.md` symlink back to it -- see "Works across platforms" above.
- **`corpus/`** -- vendored and linked source content from the project's research. See [`corpus/MANIFEST.yaml`](./corpus/MANIFEST.yaml) for the catalog of everything in here, its status (current/draft/superseded/linked), and its license. **Content in `corpus/` is third-party and mostly CC BY-SA 4.0** -- it is not covered by this repo's Apache-2.0 license. See [Licensing](#licensing) below.
- **`scripts/validate_corpus.py`** -- checks that every `MANIFEST.yaml` entry has its required fields and that its `path` (if any) actually exists. Runs in CI on every PR that touches `corpus/`.

## Adding or updating a resource

1. Drop the new file(s) into the right `corpus/<initiative>/` subfolder. If this is a new version of something that already exists, put it in a new version-dated folder rather than overwriting the old one. Copy the files directly -- don't add a submodule or any other live link back to the source repo.
2. Add an entry to `corpus/MANIFEST.yaml` (see the comments at the top of that file for the schema). If you copied from a GitHub repo, record the commit SHA you copied from as `vendored_commit` and today's date as `vendored_date`.
3. If this supersedes an earlier entry, change that entry's `status` to `superseded` -- don't delete it.
4. Open a PR. CI validates the manifest automatically.

No code changes are needed to pick up new content -- the skill instructions read `MANIFEST.yaml` at query time rather than hardcoding file paths.

## Licensing

- This repo's own content (`SKILL.md`, `scripts/`, workflow and manifest files, this README) is licensed under **Apache-2.0** -- see [`LICENSE`](./LICENSE).
- Everything under `corpus/` is vendored or linked third-party content from the OWASP GenAI Security Project's various initiative repos, and retains its **original license** as recorded per-entry in `corpus/MANIFEST.yaml` -- predominantly **CC BY-SA 4.0**, confirmed against each source document's own license statement before vendoring. Check the manifest before redistributing corpus content outside this repo.
- A handful of resources are cataloged as `status: linked` rather than vendored specifically because their license couldn't be confirmed -- see `CHANGELOG.md` and `corpus/MANIFEST.yaml` for which ones and why.

## Versioning

Follows [Semantic Versioning](https://semver.org/) -- see [`CHANGELOG.md`](./CHANGELOG.md) for what changed at each release, and "Versioning" in [`CONTRIBUTING.md`](./CONTRIBUTING.md) for the process. The version is kept in sync across `SKILL.md` frontmatter, `.claude-plugin/marketplace.json`, and `gemini-extension.json`, since those are what each platform's own update-checking reads.

## Status

Public, v1.0.0. First milestone is shipping the Skill; a web-based surface is planned as a follow-on (see the Data Security Initiative's [live crosswalk app](https://genai-security-project.github.io/GenAI-Data-Security-Initiative/) for a working precedent of a fully GitHub-hosted app in this project).
