````skill
---
name: readme-maintainer
description: Create or update a project README.md following development conventions and repository structure. Use when the user asks to "create README", "update README", "refresh project docs", "document setup", or "improve repository documentation".
---

# README Maintainer

Create or update the root `README.md` so it is accurate, concise, and aligned with project development conventions.

## Workflow

1. Discover project context
   - Inspect repository structure, key config files, and existing docs.
   - Identify stack, run/build/test commands, and contribution workflow.
   - If `README.md` exists, preserve valid sections and improve only what is outdated, missing, or unclear.

2. Gather evidence before writing
   - Derive commands from real files (for example: `package.json`, `pyproject.toml`, `requirements.txt`, `Makefile`, `Dockerfile`, `.env.example`, CI files).
   - Never invent commands, environment variables, ports, URLs, or tooling.
   - If critical facts are missing, explicitly mark a short `TODO` placeholder instead of guessing.

3. Build README structure
   - Use this section order unless the project clearly needs fewer sections:
     1) Title
     2) Short Description
     3) Tech Stack
     4) Prerequisites
     5) Installation
     6) Configuration
     7) Run (Development)
     8) Build / Production
     9) Testing
     10) Project Structure
     11) Development Conventions
     12) Troubleshooting (optional)
     13) Contributing
     14) License (or `TODO` if unknown)

4. Apply writing conventions
   - Use clear, direct language and short paragraphs.
   - Prefer copy-paste-ready command blocks.
   - Keep headings stable and scannable.
   - Keep examples minimal and realistic.
   - Do not duplicate deep internal docs; link to them.

5. Update with minimal disruption
   - Preserve existing content that is correct.
   - Avoid unrelated rewrites and stylistic churn.
   - Keep terminology consistent with the codebase.

6. Validate before finishing
   - Re-check every documented command against project files.
   - Ensure no section contradicts current implementation.
   - Ensure all internal links and referenced paths exist.

## README Content Rules

- Commands must be executable as documented.
- Environment variables must be listed with brief purpose notes.
- If multiple package managers/build tools are detected, prefer the one already used in project scripts and mention alternatives only when explicitly present.
- Security-sensitive values must never be committed; always reference `.env.example`-style patterns when available.
- For monorepos, document root workflow first, then per-package commands in a compact table.

## Output Contract

After creating/updating `README.md`, return:

1. A short summary of what changed.
2. The final section list included in the README.
3. Any unresolved `TODO` placeholders that need user input.
4. A verification note confirming documented commands were sourced from repository files.

## Reference Template

Use `references/readme-template.md` as the default skeleton and adapt it to the target project.
````
