# feature-docs

Skill for generating **single-file feature documentation** with verified code evidence, following the GOLD STANDARD pattern.

## Goal

Generate comprehensive single-file feature documentation with verified test cases using the mandatory GOLD STANDARD template.

## What it does

- Produces comprehensive feature docs using a mandatory **26-section** structure.
- Covers **frontend + backend**: domain model, API, components, controllers, integration, security, testing, and operations.
- Requires evidence for claims using `file:line` references.
- Applies a **2-pass verification** process to reduce inaccuracies and hallucinations.
- Generates an optional AI companion file (`.ai.md`) optimized for agent consumption.

## When to use

Use this skill when the user asks for:

- "quick feature docs"
- "feature readme"
- "single file docs"
- "verified documentation"

Best for non-enterprise projects that need complete end-to-end feature documentation in a single markdown file. For enterprise module hierarchy, use `business-feature-docs`.

## Expected outputs

- Main documentation:
  - `.vscode/docs/features/{Module}/detailed-features/README.{FeatureName}.md`
- AI companion documentation:
  - `.vscode/docs/features/{Module}/detailed-features/README.{FeatureName}.ai.md`
- Feature analysis working file:
  - `.vscode/.ai/workspace/analysis/{feature-name}.md`

## Workflow summary

1. **Feature analysis**: discover entities, workflows, API, frontend, and cross-service integration.
2. **Code discovery**: map entities, commands, queries, events, controllers, and components.
3. **Documentation generation**: produce all 26 sections in mandatory order with code evidence.
4. **AI companion generation**: build compact, agent-friendly documentation (~300 lines max).
5. **Verification**: validate references and consistency with a strict 2-pass process.

## Mandatory structure highlights

The 26 sections include:

- Business-facing sections (Executive Summary, Business Value, Requirements, Rules, Flows)
- Technical design sections (System Design, Architecture, Domain Model, API, Frontend, Backend)
- Operational quality sections (Security, Performance, Testing, Troubleshooting, Runbook)
- Governance sections (Roadmap, Related Docs, Glossary, Version History)

## Quality and verification essentials

- All 26 sections must be present in exact order.
- Every key claim must include verifiable code evidence.
- Verification uses:
  - **First pass**: check every reference directly in source files.
  - **Second pass**: random sampling and completeness checks.
- If second pass finds more than 5 issues, re-run verification.

## AI companion rules

- Target size: up to 300 lines.
- Structure: 10 sections (Context, File Locations, Domain Model, API Contracts, Business Rules, Patterns, Integration, Security, Test Scenarios, Quick Reference).
- Compression principles: tables over prose, paths over descriptions, signatures over full examples, decisions over explanations.

## Gold standard references

- Example reference:
  - `.agents/skills/feature-docs/references/README.ExampleFeature1.md`
- Template:
  - `.agents/skills/feature-docs/references/detailed-feature-docs-template.md`
- AI companion template:
  - `.agents/skills/feature-docs/references/detailed-feature-docs-template.ai.md`

## Maintainer note

Keep this README aligned with `SKILL.md`. If phases, required sections, paths, or quality checklist items change, update both files together.
