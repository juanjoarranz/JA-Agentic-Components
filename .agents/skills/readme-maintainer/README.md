# readme-maintainer

Skill to create or update a project `README.md` with verified information and consistent structure.

## What it does

- Discovers repository context (structure, stack, real commands).
- Updates the README with minimal changes and without inventing commands or variables.
- Maintains a clear section structure (installation, run, testing, contributing, etc.).
- Adds explicit `TODO` markers when critical information is missing.

## Install with npx (single skill)

Install only this skill from the remote repository:

Flag reference:

- `-g`: installs the skill globally (user-level, available across projects).
- `-y`: auto-confirms prompts (non-interactive mode).

Default (workspace/project-local) install:

```bash
npx skills add juanjoarranz/JA-Agentic-Components@readme-maintainer -y
```

Workspace note: omitting `-g` keeps the installation scoped to the current workspace/project.

Global install (user-level):

```bash
npx skills add juanjoarranz/JA-Agentic-Components@readme-maintainer -g -y
```

## Quick usage

After installation, ask the agent something like:

- "Update the project README"
- "Create a new README with real repo commands"
