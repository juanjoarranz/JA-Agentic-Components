# changelogger

Skill to automatically update the `CHANGELOG.md` file **before** finalizing a commit.

## What it does

- Adds changelog entries grouped by date (`## [YYYY-MM-DD]`).
- Interprets Conventional Commit types and presents them with visual style (emoji per type).
- Supports detailed descriptions from the commit message body.
- Designed to run during the staging/pre-commit flow.

## Install with npx (single skill)

Install only this skill from the remote repository:

Flag reference:

- `-g`: installs the skill globally (user-level, available across projects).
- `-y`: auto-confirms prompts (non-interactive mode).

Default (workspace/project-local) install:

```bash
npx skills add juanjoarranz/JA-Agentic-Components@changelogger -y
```

Workspace note: omitting `-g` keeps the installation scoped to the current workspace/project.

Global install (user-level):

```bash
npx skills add juanjoarranz/JA-Agentic-Components@changelogger -g -y
```

## Quick usage

After installation, ask the agent something like:

- "Update the changelog before committing"
- "Run changelogger with this commit message"
