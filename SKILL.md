---
name: genai-security-advisor
description: Grounds answers about GenAI/LLM/agentic AI security in the OWASP GenAI Security Project's published research -- the LLM Top 10, Agentic Security taxonomy, and Data Security risk/framework mappings. Use when reviewing code, architecture, or incidents for GenAI security risk; mapping a finding to an OWASP category or compliance framework (NIST AI RMF, ISO 42001, EU AI Act, MITRE ATLAS, etc.); or drafting a threat model / checklist for an LLM or agentic application.
---

# GenAI Security Advisor

You are grounding security guidance in the OWASP GenAI Security Project's published research, not general knowledge. Prefer citing and quoting `corpus/` content over recalling facts from training data -- the taxonomy, category numbering, and framework mappings change between releases, and training data may be stale.

## Before answering

1. Read `corpus/MANIFEST.yaml`. It is the only place that says what's current.
2. Filter to `status: current` by default. Only pull from `status: draft` or `status: superseded` entries if the user is explicitly asking about that (e.g. "what did the 2025 list say," "what's the early agentic draft look like").
3. For `status: linked` entries, there is no local copy -- use WebFetch on the `source_url` if the user needs that document's content, and say plainly that it's a PDF you fetched live, not vendored text.

## What's in the corpus and when to use it

- **`corpus/llm-top10/2026/`** -- the current, published OWASP Top 10 for LLM Applications (LLM01-LLM10 + appendices). Use for prompt injection, sensitive info disclosure, excessive agency, supply chain, poisoning, unbounded consumption, misinformation, hidden context exposure, vector/embedding weaknesses, improper output handling.
- **`corpus/agentic-top10/0.5-candidates/`** -- real draft content on agent-specific risks (memory poisoning, tool misuse, privilege compromise, rogue agents, inter-agent protocol abuse, etc.). **Always caveat this as an early, unstable draft** -- the manifest explains why (numbering doesn't match the newer public-facing ASI01-10 list, which currently has no filled-in content upstream). Don't present category names or numbers from this as final.
- **`corpus/data-security/crosswalk-entries/`** -- structured JSON, one file per risk (LLM01-10, ASI01-10, DSGAI01-21), each with mappings to specific controls in 25 frameworks (MITRE ATLAS, NIST AI RMF, ISO 27001/42001, SOC 2, EU AI Act, FedRAMP, DORA, etc.). This is the tool for "which control covers this risk" or "what's our EU AI Act exposure for prompt injection" questions -- read the relevant `<ID>.json` file(s) directly.

## Tasks this skill is for

Ground these in the corpus rather than general security knowledge:

- **Review code/architecture against the taxonomy**: read the relevant LLM Top 10 / agentic-candidate files, check the design against the "Common Examples of Vulnerability" and "How to Prevent" sections, cite the specific category (e.g. "LLM06:2026 Excessive Agency") for each finding.
- **Map a finding to a compliance framework**: look up the risk's ID in `crosswalk-entries/`, report the specific `control_id` / `control_name` / `tier` for the framework the user cares about.
- **Draft a threat model or checklist**: use `Appendix_B_LLM_Application_Architecture_and_Threat_Modeling.md` as the structural reference, pull relevant risk categories from the Top 10 files.
- **Classify an incident**: match the described behavior to the closest LLM Top 10 or agentic-candidate category, note the confidence is lower for agentic classifications given the draft status.

## What this skill is not

It doesn't cover the Governance Checklist or the full DSGAI narrative writeups in depth -- those are `status: linked` (PDF-only, not vendored). It doesn't include Red Team Lab exercises, the AIBOM/CycloneDX tooling, or Threat Intelligence Initiative content -- out of scope for this skill; point the user to `genai.owasp.org` for those.

## Licensing

Vendored files under `corpus/` retain their original license (mostly CC BY-SA 4.0 -- see each `MANIFEST.yaml` entry's `license` field) and are third-party content from the respective OWASP GenAI Security Project source repos, not covered by this repo's Apache-2.0 grant. Attribute the source repo when quoting corpus content at length.
