# commiter

Skill to create commits following **Conventional Commits** with detailed messages.

## What it does

- Generates commits using the conventional format (`type: subject`).
- Requires a descriptive body with motivation, implementation, and impact.
- Includes a required `CHANGELOG.md` update step before the final commit.

## Install with npx (single skill)

Install only this skill from the remote repository:

Flag reference:

- `-g`: installs the skill globally (user-level, available across projects).
- `-y`: auto-confirms prompts (non-interactive mode).

Default (workspace/project-local) install:

```bash
npx skills add juanjoarranz/JA-Agentic-Components@commiter -y
```

Workspace note: omitting `-g` keeps the installation scoped to the current workspace/project.

Global install (user-level):

```bash
npx skills add juanjoarranz/JA-Agentic-Components@commiter -g -y
```

## Quick usage

After installation, ask the agent something like:

- "Commit my staged changes using commiter"
- "Generate a detailed conventional commit message"
