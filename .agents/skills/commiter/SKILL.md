---
name: commiter
description: Commits changes to git using Conventional Commits
---

# Instructions

When committing changes, you MUST follow the **Conventional Commits** specification with **highly detailed descriptions**.

## Commit Format

```
<type>[optional scope]: <description>

<detailed body>

[optional footer(s)]
```

## Specific Rules

### Title (Subject Line)

- **Language**: English only.
- **Tense**: Must start with a **past participle** (e.g., "Fixed", "Added", "Updated", "Refactored").
- **Length**: Maximum of **50 characters**.
- **Format**: `<type>: <Past Participle Message>`

### Detailed Description (Body) - REQUIRED

- **Content**: Provide an **extensive and thorough explanation** of the changes made.
- **Detail**: Explain the _why_ (motivation), the _how_ (technical implementation details), and any _consequences_ or _impact_.
- **Length**: At least 2-3 sentences. **Do not use placeholders.**

## Pre-Commit Step: Update Changelog

Before finalizing any commit, you **MUST** update the `CHANGELOG.md` using the full commit message (subject + body).

1.  **Prepare your message**: Construct a full conventional commit message with a detailed body.
2.  **Execute the update**:

    ```bash
    # Use a multi-line string or ensure newlines are preserved
    py .agents/skills/changelogger/scripts/update_changelog.py "feat: Added user authentication logic

    Implemented a full JWT-based authentication system. This includes secure password hashing with bcrypt, token generation, and middleware for protected routes. This change improves security by moving away from session-based auth."
    ```

3.  **Stage the changelog**:
    ```bash
    git add CHANGELOG.md
    ```
4.  **Finalize Commit**: Commit using the EXACT same message:

    ```bash
    git commit -m "feat: Added user authentication logic

    Implemented a full JWT-based authentication system. This includes secure password hashing with bcrypt, token generation, and middleware for protected routes. This change improves security by moving away from session-based auth."
    ```

## Examples

- `feat: Added user authentication logic`
- `fix: Resolved memory leak in data parser`
- `docs: Updated README with installation steps`

For more details on commit formatting, refer to the [CONVENTIONAL_COMMITS.md](./RESOURCES/CONVENTIONAL_COMMITS.md) resource.
