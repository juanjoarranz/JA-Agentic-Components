---
name: changelogger
description: Updates the project's CHANGELOG.md file automatically with the intended changes BEFORE the commit is finalized. Use this skill during the staging process to ensure every commit is recorded in the changelog.
---

This skill automates the maintenance of a `CHANGELOG.md` file by adding changes **before** they are committed. It groups changes by date and uses emojis to represent different commit types, following a premium visual style.

## Key Features

- **Date Grouping**: Automatically groups entries under `## [YYYY-MM-DD]` headers.
- **Emoji Support**: Maps conventional commit types to corresponding emojis (e.g., ✨ for `feat`, 🐛 for `fix`, ♻️ for `refactor`).
- **Detailed Entries**: Supports multi-line commit messages, using the body as the entry description.

## Workflow

To ensure the `CHANGELOG.md` is included in the same commit as your changes, follow these steps:

### 1. Stage your changes

Stage the files you want to commit.

### 2. Determine your commit message

Construct a full conventional commit message with a detailed body (required for `commiter` skill).

### 3. Update the Changelog (PRE-COMMIT)

Run the script passing your intended full commit message as an argument:

```bash
py .agents/skills/changelogger/scripts/update_changelog.py "feat: Added premium styling

Implemented a new design system for the CHANGELOG.md. It now uses date headers, emojis for commit types, and supports detailed descriptions for each entry."
```

### 4. Stage and Review

The script updates `CHANGELOG.md`. You must now stage the changelog as well:

```bash
git add CHANGELOG.md
```

### 5. Finalize the Commit

Commit all staged changes using the EXACT same message.
