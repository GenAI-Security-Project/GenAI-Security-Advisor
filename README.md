# GenAI-Security-Advisor

A Claude Skill that grounds security guidance in the [OWASP GenAI Security Project](https://genai.owasp.org)'s published research -- the LLM Top 10, Agentic Security taxonomy, and Data Security risk/framework mappings -- instead of relying on the model's general (and possibly stale) knowledge of the taxonomy.

See [`SKILL.md`](./SKILL.md) for the skill instructions themselves.

## Repository layout

- **`SKILL.md`** -- the skill's instructions (Apache-2.0, this repo's own work).
- **`corpus/`** -- vendored and linked source content from the project's research. See [`corpus/MANIFEST.yaml`](./corpus/MANIFEST.yaml) for the catalog of everything in here, its status (current/draft/superseded/linked), and its license. **Content in `corpus/` is third-party and mostly CC BY-SA 4.0** -- it is not covered by this repo's Apache-2.0 license. See [Licensing](#licensing) below.
- **`scripts/validate_corpus.py`** -- checks that every `MANIFEST.yaml` entry has its required fields and that its `path` (if any) actually exists. Runs in CI on every PR that touches `corpus/`.

## Adding or updating a resource

1. Drop the new file(s) into the right `corpus/<initiative>/` subfolder. If this is a new version of something that already exists, put it in a new version-dated folder rather than overwriting the old one.
2. Add an entry to `corpus/MANIFEST.yaml` (see the comments at the top of that file for the schema).
3. If this supersedes an earlier entry, change that entry's `status` to `superseded` -- don't delete it.
4. Open a PR. CI validates the manifest automatically.

No code changes are needed to pick up new content -- the skill instructions read `MANIFEST.yaml` at query time rather than hardcoding file paths.

## Licensing

- This repo's own content (`SKILL.md`, `scripts/`, workflow files, this README) is licensed under **Apache-2.0** -- see [`LICENSE`](./LICENSE).
- Everything under `corpus/` is vendored or linked third-party content from the OWASP GenAI Security Project's various initiative repos, and retains its **original license** as recorded per-entry in `corpus/MANIFEST.yaml` (predominantly CC BY-SA 4.0). Check the manifest before redistributing corpus content outside this repo.

## Status

Private, pre-release. First milestone is shipping the Skill; a web-based surface is planned as a follow-on (see the Data Security Initiative's [live crosswalk app](https://genai-security-project.github.io/GenAI-Data-Security-Initiative/) for a working precedent of a fully GitHub-hosted app in this project).
