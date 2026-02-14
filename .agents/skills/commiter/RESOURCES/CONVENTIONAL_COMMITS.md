# Conventional Commits Reference

This document outlines the commit convention used in this project.

## Specification

Commits should follow this structure:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **build**: Changes that affect the build system or external dependencies
- **ci**: Changes to our CI configuration files and scripts
- **chore**: Other changes that don't modify src or test files
- **revert**: Reverts a previous commit

### Title Rules

- **Maximum 50 characters**.
- **English only**.
- **Starts with a Past Participle** (e.g., *Fixed*, *Added*, *Updated*).

### Description Rules

- Mandatory for complex changes.
- Explain the motivation for the change and contrast this with previous behavior.
