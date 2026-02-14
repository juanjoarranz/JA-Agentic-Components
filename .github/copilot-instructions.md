# Project Guidelines — JA-Skills

## Purpose

This workspace develops **AI agent skills**: reusable knowledge modules (SKILL.md files) consumed by GitHub Copilot, Claude Code, Cursor, and 14+ other AI coding agents. Skills follow the [Agent Skill Standard](https://agentskills.io).

## Skill Directory Layout

Every skill lives under `.agents/skills/<skill-name>/` with this structure:

```
skill-name/
├── SKILL.md           ← REQUIRED: Main agent instructions
├── README.md          ← OPTIONAL: Human/marketplace docs
├── references/        ← OPTIONAL: Templates, examples
└── scripts/           ← OPTIONAL: Helper scripts referenced by SKILL.md
```

See [project-memory/](.agents/skills/project-memory/) and [readme-maintainer/](.agents/skills/readme-maintainer/) as canonical examples.

## Available Project Skills

- [changelogger](.agents/skills/changelogger/SKILL.md): Updates `CHANGELOG.md` before commit finalization.
- [commiter](.agents/skills/commiter/SKILL.md): Creates Conventional Commits with detailed commit messages.
- [feature-docs](.agents/skills/feature-docs/SKILL.md): Generates verified, single-file feature documentation.
- [project-memory](.agents/skills/project-memory/SKILL.md): Sets up and maintains project memory under `docs/project_notes/`.
- [readme-maintainer](.agents/skills/readme-maintainer/SKILL.md): Creates or updates `README.md` following development conventions.

## SKILL.md Conventions

- **Frontmatter** in triple-backtick `skill` fences with `name` (kebab-case) and `description` (include trigger phrases so agents know _when_ to activate):
  ```skill
  ---
  name: my-skill
  description: What it does. Use when the user asks to...
  ---
  ```
- **Body**: Step-by-step workflows the agent follows verbatim — numbered procedures, inline code examples, and explicit output contracts (what the AI must return to the user).
- **Bilingual** descriptions (ES/EN) are supported when the audience benefits.
- Reference supporting files via **relative paths** from the SKILL.md location.

## Naming

- Directories and skill names: **kebab-case** (`readme-maintainer`, `project-memory`).
- The canonical entry point is always `SKILL.md` (uppercase).

## Scope Levels

| Level       | Path                | Example                        |
| ----------- | ------------------- | ------------------------------ |
| Project     | `.agents/skills/`   | This workspace                 |
| Global/User | `~/.agents/skills/` | `skill-creator` was moved here |

`Descripción.txt` at the root documents any structural moves between scopes.

## Build and Test

No build step. To validate a skill manually:

```powershell
# Ensure SKILL.md exists and has frontmatter
Get-ChildItem -Recurse -Filter SKILL.md | ForEach-Object { Write-Host $_.FullName; Get-Content $_ -First 5 }
```

## Key Patterns

- **Output contracts**: Every skill defines the exact summary/format the agent must present to the user after execution (e.g., totals copied/skipped/errors).
- **Template pattern**: Skills in `references/` provide markdown templates that get copied into target projects (see `project-memory/references/`).
- **Helper scripts**: Put executable tools in `scripts/` and reference them from SKILL.md with argument documentation (for example, `changelogger/scripts/update_changelog.py`).
- When creating or editing skills, use the global `skill-creator` skill for guidance on structure and best practices.
