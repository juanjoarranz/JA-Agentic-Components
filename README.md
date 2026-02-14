# JA-Agentic-Components

Unified repository for building and maintaining reusable components of the agentic stack: Skills, Custom Agents, Hooks, and Orchestration assets.

## Project Objective

This project serves as a single source of truth for reusable AI agent building blocks.

Core goals:

- Centralize **Skills**, **Custom Agents**, **Hooks**, and **Orchestration** resources in one place.
- Make components easy to discover, reuse, and evolve across multiple AI coding environments.
- Document conventions and operational patterns so teams can compose reliable agentic systems.
- Support incremental growth from single skills to complete multi-agent workflows.
---
<img src="./Anatomy%20of%20the%20Agentic%20Stack.png" alt="Anatomy of the Agentic Stack" width="100%" />

## Tech Stack

- Language/runtime: Markdown-first repository (`SKILL.md`, `README.md`)
- Frameworks/standards: Agent Skill Standard ([agentskills.io](https://agentskills.io)) and agent workflow conventions
- Tooling: Git, PowerShell (manual validation), VS Code/Copilot-compatible agent workflows

## Prerequisites

- Git
- PowerShell (for manual validation commands)
- A compatible AI coding agent environment (for example GitHub Copilot, Claude Code, or Cursor)

## Installation

```bash
git clone <your-fork-or-repo-url>
cd <repo-folder>
```

## Components in this Repository

This repository includes reusable components across these domains:

- Skills
- Custom Agents
- Hooks
- Orchestration

Current implemented modules:

### 1) changelogger

- **Path:** `.agents/skills/changelogger/SKILL.md`
- **Description:** Automatically updates `CHANGELOG.md` with intended changes before commit finalization.
- **Example usage prompts:**
	- "Update the changelog before I commit these staged changes."
	- "Run changelogger with this conventional commit message."

### 2) commiter

- **Path:** `.agents/skills/commiter/SKILL.md`
- **Description:** Creates Git commits using Conventional Commits with detailed commit bodies.
- **Example usage prompts:**
	- "Commit my staged files using the commiter skill."
	- "Generate a conventional commit message with a detailed body for this change."

### 3) feature-docs

- **Path:** `.agents/skills/feature-docs/SKILL.md`
- **Description:** Generates single-file, verified feature documentation with code evidence for non-enterprise projects.
- **Example usage prompts:**
	- "Create quick feature docs for this module using feature-docs."
	- "Generate a verified single-file feature README with code references."

### 4) project-memory

- **Path:** `.agents/skills/project-memory/SKILL.md`
- **Description:** Sets up and maintains `docs/project_notes/` to track bugs, decisions, key facts, and work history.
- **Example usage prompts:**
	- "Set up project memory for this repository."
	- "Log this bug fix and update our project memory notes."

### 5) readme-maintainer

- **Path:** `.agents/skills/readme-maintainer/SKILL.md`
- **Description:** Creates or updates the root `README.md` based on repository conventions and verified project context.
- **Example usage prompts:**
	- "Update the repository README to match the current project structure."
	- "Refresh project documentation in README format."


## Project Structure

```text
.
├── .github/
│   └── copilot-instructions.md
├── .agents/
│   └── skills/
│       ├── changelogger/
│       ├── commiter/
│       ├── feature-docs/
│       ├── project-memory/
│       └── readme-maintainer/
└── .vscode/
```

As the repository evolves, component directories for custom agents, hooks, and orchestration assets are added under this same project scope.

## Development Conventions

- Skills live in `.agents/skills/<skill-name>/`.
- Skill required entry point: `SKILL.md` (uppercase).
- Skill names and directories use kebab-case.
- `SKILL.md` uses `skill` frontmatter with `name` and `description`.
- Keep instructions procedural and explicit, including output contracts.
- Apply the same clarity and reproducibility principles to custom agents, hooks, and orchestration definitions.

## Troubleshooting

- Skill not detected by agents: verify `SKILL.md` exists at `.agents/skills/<skill-name>/SKILL.md`.
- Parsing issues: check frontmatter fence format and required fields (`name`, `description`).
- General component issues: validate paths, naming, and integration points against the corresponding component specification.

## Contributing

1. Create or update a component (skill, custom agent, hook, or orchestration asset).
2. Follow the relevant naming and specification conventions.
3. Validate structure and references before opening a PR.
4. Open a PR with a clear summary of added/changed behavior.

## License

This project is licensed under the Apache License 2.0.

See the full text in [LICENSE](./LICENSE).
