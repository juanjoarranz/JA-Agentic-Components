# Changelog

All notable changes to this project will be documented in this file.

## [2026-02-14]

### ✨ feat: Added obsidian plugin helper skill

- Added a complete Obsidian plugin helper skill package, including the main SKILL definition, command prompts, detailed reference guides, and an interactive boilerplate generator script. Updated repository documentation to register and describe the new skill so it is discoverable from both project guidance and user-facing README sections. This improves the repository's coverage for Obsidian plugin workflows by providing opinionated best practices, accessibility requirements, and submission guidance in a reusable skill format.

### 🐛 fix: Fixed skill frontmatter parsing

- Removed non-standard frontmatter wrappers from the readme-maintainer skill and normalized its header format so the skills indexer can parse it consistently. Simplified the feature-docs frontmatter to the minimal compatible fields required by the installer scanner. This restores deterministic discovery behavior for skill installation flows and prevents false "No matching skills found" results for valid skills.

### 🔧 chore: Updated docs and changelog flow

- Standardized npx skill installation guidance across project and skill READMEs by documenting workspace-local as default, global as secondary, and clear -g/-y behavior with command examples.
- Refined CHANGELOG entries to bullet-point style and added a dedicated docs entry for the new npx installation instructions so release notes capture these onboarding changes.
- Enhanced changelogger script to transform commit body lines into bullets automatically, ensuring future changelog updates remain consistent and easier to scan.

### 📚 docs: Added npx install guidance (local + global)

- Added explicit `npx skills add <owner>/<repo>@<skill>` installation instructions in the project README and skill README files.
- Set workspace/project-local installation as the default option (without `-g`) and documented global installation as a second option (with `-g`).
- Documented flag behavior for `-g` and `-y`, including a CLI clarification about `npx -y ...` vs `... -y`.
- Added concrete examples for this repository using `juanjoarranz/JA-Agentic-Components@<skill>`.

### 📚 docs: Updated README image display width

- Expanded the architecture image width in README.md from 60% to 100%.
- Improved documentation usability by making key structure details easier to read on typical desktop viewports.
- Kept this as a presentation-only update with no behavior, build, or skill execution changes.

### 🔧 chore: Initialized repository baseline

- Established the first project snapshot as the source of truth for reusable agentic components.
- Added foundational documentation and licensing assets to accelerate contributor onboarding and standardize project conventions.
- Created a stable baseline for iterative additions of skills, custom agents, hooks, and orchestration resources.
