# GenAI Security Advisor

## Currently In Preview

Get security guidance for Generative AI, LLMs, agents, MCP, and related technologies grounded in the published research of the **OWASP GenAI Security Project**.

The **GenAI Security Advisor** is an [Agent Skill](https://agentskills.io) that gives your AI coding assistant access to a curated, versioned knowledge base of OWASP GenAI Security Project research rather than relying only on the model's general knowledge.

It can help you research, assess, explain, and apply GenAI security guidance across areas including:

- LLM security
- Agentic AI security
- Data security for GenAI
- MCP security
- AI red teaming
- GenAI governance
- Security frameworks and mappings
- Secure AI adoption
- Related OWASP GenAI Security Project research and guidance

> **In short:** install the skill once, then ask your AI assistant GenAI security questions in your normal workflow.

---

## What can I use it for?

Once installed, you can ask your AI assistant questions such as:

### Understand a security risk

```text
What are the primary security risks associated with prompt injection?
```

```text
Explain the security risks of excessive agency in an AI agent.
```

```text
What security concerns should I consider when using MCP?
```

### Assess an architecture

```text
Review this GenAI architecture and identify the security risks I should consider.
```

```text
What GenAI security controls should I consider for an application
that uses an LLM with access to internal company data?
```

### Apply GenAI Security Project guidance

```text
How does this application map to the OWASP LLM Top 10?
```

```text
Which OWASP GenAI security guidance applies to this AI agent?
```

```text
What security controls should I implement to mitigate this risk?
```

### Compare risks and controls

```text
Compare the security risks of an LLM application and an autonomous AI agent.
```

```text
What are the recommended mitigations for this GenAI security issue?
```

### Work with your code or design

You can provide code, architecture diagrams, configuration, requirements, or other project information and ask the Advisor to help identify relevant GenAI security considerations.

For example:

```text
Review this code for GenAI security risks and identify which
OWASP GenAI guidance is relevant.
```

```text
Here is the architecture for our AI agent. Identify potential
security risks and recommend mitigations.
```

---

## Why use the GenAI Security Advisor?

GenAI security guidance changes quickly. General-purpose AI models may have incomplete, outdated, or inconsistent knowledge of the latest OWASP GenAI Security Project research.

The Advisor addresses this by grounding its guidance in a **versioned, curated corpus of OWASP GenAI Security Project research**.

The corpus covers areas such as the LLM Top 10, Agentic Top 10, Data Security risk and framework mappings, MCP security, red teaming, and governance guidance.

The corpus is intentionally maintained as point-in-time copies rather than live links to upstream repositories. This means the guidance you receive does not unexpectedly change because an unrelated upstream document was modified.

---

# Getting Started

## Choose your AI assistant

The GenAI Security Advisor works with multiple Agent Skill-compatible tools.

| AI Assistant | Supported |
|---|---|
| Claude Code | Yes |
| OpenAI Codex CLI | Yes |
| GitHub Copilot | Yes |
| Gemini CLI | Yes |

The skill uses the open [Agent Skills](https://agentskills.io) format, with a single canonical `SKILL.md` that can be discovered by supported platforms.

---

# Install the Skill

To install the skill use the method for your AI assistant.

### Claude Code

Use the repository's plugin marketplace:

```text
/plugin marketplace add GenAI-Security-Project/GenAI-Security-Advisor
```

Then install the skill:

```text
/plugin install
```

Alternatively, copy the skill into your Claude skills directory:

```text
~/.claude/skills/genai-security-advisor/
```

### OpenAI Codex CLI

Install the skill globally:

```bash
npx skills add GenAI-Security-Project/GenAI-Security-Advisor -g
```

The same installer can target multiple supported hosts, for example:

```bash
npx skills add GenAI-Security-Project/GenAI-Security-Advisor \
  -g \
  -a codex \
  -a claude-code \
  -a copilot \
  -a gemini-cli
```

### Gemini CLI

Install the Gemini extension:

```bash
gemini extensions install https://github.com/GenAI-Security-Project/GenAI-Security-Advisor
```

### GitHub Copilot

Install the skill with the GitHub CLI:

```bash
gh skill install GenAI-Security-Project/GenAI-Security-Advisor
```

The skill is installed into:

```text
~/.copilot/skills/
```

The repository documents these platform-specific registration methods. Because AI coding tools and their CLI interfaces can change, check the current tool documentation or `--help` output if an installation command has changed.

---

# Using the Advisor

Once the skill is installed, you don't need to learn a new command language.

**Just ask your AI assistant a GenAI security question.**

For example:

```text
What OWASP GenAI security guidance should I consider when
building an AI agent that can execute tools?
```

Or:

```text
Review this AI agent design and identify the security risks.
For each risk, explain the relevant OWASP guidance and
recommended mitigations.
```

Or:

```text
I'm building an MCP-enabled application. What security
controls should I consider?
```

The skill determines which research resources are relevant and uses the included corpus to ground its response.

---

# Getting Better Answers

The more context you provide, the more useful the Advisor can be.

Instead of:

```text
How do I secure AI?
```

Try:

```text
I'm building an internal enterprise application that uses an LLM
to summarize confidential documents. The model can retrieve
documents from our internal knowledge base.

What are the key GenAI security risks I should consider?
Map the risks to relevant OWASP GenAI guidance and recommend
practical mitigations.
```

Useful context can include:

- Your application architecture
- The type of AI model you're using
- Whether you're using agents
- Tools available to the model or agent
- Data sources
- Authentication and authorization mechanisms
- MCP servers
- External APIs
- Deployment environment
- Trust boundaries
- Security requirements
- Code or configuration

---

# Ask for Evidence and Sources

When security guidance matters, you can ask the Advisor to explain where its recommendation comes from.

For example:

```text
Which OWASP GenAI Security Project resource supports this recommendation?
```

```text
Show me the relevant OWASP GenAI security guidance for each risk.
```

```text
Explain how this recommendation maps to the OWASP LLM Top 10.
```

This can help you distinguish OWASP GenAI Security Project guidance from general security recommendations.

---

# What is included?

The repository contains the skill itself and a curated research corpus.

## `SKILL.md`

This is the Agent Skill's instruction set. It tells your AI assistant how to use the GenAI Security Advisor and how to work with the included research.

There is one canonical `SKILL.md` at the repository root. Platform-specific paths point back to this canonical version.

## `corpus/`

This contains the research resources used by the Advisor.

The resources are maintained as frozen, point-in-time copies so that the Advisor's knowledge does not unexpectedly change when an upstream repository changes.

The `corpus/MANIFEST.yaml` file provides information about the resources included in the corpus, including their status and licensing.

---

# Keeping the Advisor Current

The research corpus is intentionally versioned.

Updates to upstream OWASP GenAI Security Project resources are not automatically pulled into your installation. Updates are reviewed and incorporated into the Advisor's corpus deliberately.

This design provides a more predictable experience: the guidance you're using is tied to a known version of the Advisor rather than silently changing underneath you.

When a new version of the Advisor is released, update your installed skill using the update mechanism provided by your AI assistant.

---

# Important: This is Security Guidance

The GenAI Security Advisor is intended to help you understand and apply GenAI security research and guidance.

It should **not** be treated as a substitute for:

- Your organization's security policies
- Security architecture review
- Threat modeling
- Penetration testing
- Legal or regulatory review
- Risk acceptance processes
- Professional security expertise

Use the Advisor as a research and decision-support tool, and validate recommendations against your specific environment and requirements.

---

# Contributing and Asking Questions

The GenAI Security Advisor is an open project and welcomes contributions from the community.

## Ask a Question

If you have questions about using the GenAI Security Advisor, installing the skill, interpreting its guidance, or getting started, join the **OWASP GenAI Security Project Slack** and use the:

**`#team-genai-security-advisor`** channel

This is the recommended place to ask questions, discuss how the Advisor works, and connect with others using or contributing to the GenAI Advisor project.

## Contribute

Contributions are welcome, including:

- Improving the Agent Skill instructions
- Adding or improving examples
- Identifying gaps or issues in the research corpus
- Suggesting additional OWASP GenAI Security Project resources
- Improving documentation
- Reporting bugs or unexpected behavior
- Proposing enhancements to the Advisor

Before making a contribution, consider discussing the proposed change in **`#team-genai-security-advisor`** so the community can provide feedback and help coordinate the work.

When contributing research or other material to the corpus, please review the applicable licensing information in `corpus/MANIFEST.yaml` and preserve the original licensing requirements.

---

# Licensing

The GenAI Security Advisor repository contains both project-owned content and third-party research content.

The repository's own content—including `SKILL.md`, scripts, workflow files, manifest files, and this README—is licensed under **Apache-2.0**.

Content in `corpus/` retains its original license. Much of the included OWASP GenAI Security Project content is licensed under **CC BY-SA 4.0**.

If you redistribute material from the corpus, check `corpus/MANIFEST.yaml` for the applicable license for each resource.

---

# Version

The current public release is **v1.1.0**.

The project follows Semantic Versioning. See [`CHANGELOG.md`](./CHANGELOG.md) for release history.

---

# Learn More

- [OWASP GenAI Security Project](https://genai.owasp.org)
- [Agent Skills](https://agentskills.io)
- [`SKILL.md`](./SKILL.md)
- [`CHANGELOG.md`](./CHANGELOG.md)
- [`corpus/MANIFEST.yaml`](./corpus/MANIFEST.yaml)

---

## Quick Start

If you just want to get started:

1. **Install the GenAI Security Advisor** for your AI assistant.
2. **Open your project** in that AI assistant.
3. **Ask a GenAI security question.**
4. **Provide your architecture, code, or other context** when you want a more specific assessment.
5. **Ask for the relevant OWASP guidance and mitigations** when you need to understand the basis for a recommendation.

That's it.

**The GenAI Security Advisor brings OWASP GenAI Security Project research into the AI-assisted development workflow you're already using.**
