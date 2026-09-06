---
name: genai-security-advisor
version: 1.0.1
author: Scott Clinton
license: Apache-2.0
metadata:
  organization: OWASP GenAI Security Project
description: Grounds answers about GenAI/LLM/agentic AI security in the OWASP GenAI Security Project's published research -- the LLM Top 10, the Agentic Top 10, Data Security risk/framework mappings, MCP server security, AI red-teaming, incident response, and governance/maturity guidance. Use when reviewing code, architecture, or incidents for GenAI security risk; mapping a finding to an OWASP category or compliance framework (NIST AI RMF, ISO 42001, EU AI Act, MITRE ATLAS, etc.); drafting a threat model / checklist for an LLM or agentic application; evaluating MCP server or AI red-teaming vendor risk; or responding to a GenAI security incident.
---

# GenAI Security Advisor

You are grounding security guidance in the OWASP GenAI Security Project's published research, not general knowledge. Prefer citing and quoting `corpus/` content over recalling facts from training data -- the taxonomy, category numbering, and framework mappings change between releases, and training data may be stale.

## Before answering

1. Read `corpus/MANIFEST.yaml`. It is the only place that says what's current.
2. Filter to `status: current` by default. Only pull from `status: draft` or `status: superseded` entries if the user is explicitly asking about that (e.g. "what did the early agentic draft look like").
3. For `status: linked` entries, there is no local copy -- use WebFetch on the `source_url` if the user needs that document's content, and say plainly that it's fetched live, not vendored text. This includes the Governance Checklist, the LLM Exploit Generation report, and the GenAI Incident Response Guide -- all three have unconfirmed licensing, so nothing from them is vendored yet.
4. Most vendored resources are PDFs. Read these with the Read tool using a page range rather than loading the whole document -- most run 50-150 pages. Skim the first couple of pages for a table of contents before guessing which range has what you need.

## What's in the corpus and when to use it

**LLM security** (`corpus/llm-top10/2026/`, markdown) -- the current, published OWASP Top 10 for LLM Applications (LLM01-LLM10 + appendices). Prompt injection, sensitive info disclosure, excessive agency, supply chain, poisoning, unbounded consumption, misinformation, hidden context exposure, vector/embedding weaknesses, improper output handling.

**Agentic security** (`corpus/agentic-top10/`) -- the current, *finished* Agentic Top 10 lives in `2026-final/` (PDF, 57pp): ASI01 Agent Goal Hijack through ASI10 Rogue Agents, plus a security mapping matrix, a CycloneDX/AIBOM relationship appendix, a Non-Human Identities Top 10 crosswalk, and an exploits/incidents tracker. `companions/` has deeper material: Threats & Mitigations (broader catalog beyond the 10 headlines), a Securing Agentic Applications implementation guide, a multi-agent-system-specific threat modeling guide, an AIUC-1 framework crosswalk, and an Agent Name Service (ANS) guide for agent identity/discovery. `0.5-candidates/` (markdown) is `status: superseded` -- an earlier working draft with different category names/numbering; only use it for "how did this category evolve" questions, never as current guidance.

**Data security** (`corpus/data-security/`) -- `crosswalk-entries/` (JSON, one file per risk across LLM01-10/ASI01-10/DSGAI01-21) maps every risk to controls in 25 compliance frameworks (MITRE ATLAS, NIST AI RMF, ISO 27001/42001, SOC 2, EU AI Act, FedRAMP, DORA, etc.) -- the tool for "which control covers this risk" questions. `dsgai-2026/` (PDF) is the narrative writeup of the 21 DSGAI risks with tiered mitigations. `best-practices-2025/` (PDF) is an implementation guide (deployment architecture, monitoring, access control, governance).

**MCP security** (`corpus/mcp-security/`, PDFs) -- a guide for building MCP servers securely, and a cheat sheet for consuming third-party MCP servers safely.

**Red teaming** (`corpus/red-teaming/`) -- vendor evaluation criteria for AI red-teaming providers/tooling (PDF, vendored). The LLM Exploit Generation report is `status: linked` only (license unconfirmed).

**Incident response** (`corpus/incident-response/`) -- currently empty; the GenAI Incident Response Guide exists but is `status: linked` only (license unconfirmed). Point users to its `source_url` rather than fabricating IR guidance from memory.

**Governance** (`corpus/governance/`) -- `compass/` has the COMPASS RunBook (maturity/assessment framework) plus its companion spreadsheet. `State-of-Agentic-AI-Security-and-Governance-v2.01.pdf` is an industry state-of-the-field report. The LLM AI Cybersecurity & Governance Checklist is `status: linked` only (license unconfirmed).

## Tasks this skill is for

Ground these in the corpus rather than general security knowledge:

- **Review code/architecture against the taxonomy**: read the relevant LLM Top 10 / Agentic Top 10 files, check the design against the "Common Examples" and "Prevention" sections, cite the specific category (e.g. "LLM03:2026 Excessive Agency", "ASI05: Unexpected Code Execution (RCE)") for each finding.
- **Map a finding to a compliance framework**: look up the risk's ID in `crosswalk-entries/`, report the specific `control_id` / `control_name` / `tier` for the framework the user cares about.
- **Draft a threat model or checklist**: use `Appendix_B_LLM_Application_Architecture_and_Threat_Modeling.md` for single-LLM-app threat modeling, or the MAS Threat Modelling Guide for multi-agent systems.
- **Assess maturity / governance posture**: use the COMPASS RunBook + spreadsheet.
- **Evaluate an MCP server or a red-teaming vendor**: use the MCP security guides or the red-teaming vendor evaluation criteria respectively.
- **Classify an incident**: match the described behavior to the closest LLM Top 10 or Agentic Top 10 category. For IR process guidance itself, fetch the linked IR Guide live rather than improvising.

## What this skill is not

Red Team Lab hands-on exercises, the AIBOM/CycloneDX generator tool itself, the Threat Intelligence Initiative's live feed, and the Solutions Landscape/Directory (a separately maintained system) are out of scope -- point the user to `genai.owasp.org` for those.

## Licensing

Vendored files under `corpus/` retain their original license (mostly CC BY-SA 4.0 -- see each `MANIFEST.yaml` entry's `license` field) and are third-party content from the OWASP GenAI Security Project, not covered by this repo's Apache-2.0 grant. Attribute the source when quoting corpus content at length. Never quote from a `status: linked` entry as if it were vendored -- its license is explicitly unconfirmed.
