# GovScraper - Claude Code Configuration

## Superpowers

You have superpowers. The superpowers skills are installed in `~/.claude/skills/` and available via the Skill tool.

**Before responding to any task, check if a skill applies.** If there is even a 1% chance a skill might apply, invoke it via the Skill tool.

### Available Skills

- **brainstorming** - Socratic design refinement before writing code
- **writing-plans** - Detailed implementation plans with bite-sized tasks
- **executing-plans** - Batch execution with human checkpoints
- **subagent-driven-development** - Fast iteration with two-stage review
- **dispatching-parallel-agents** - Concurrent subagent workflows
- **test-driven-development** - RED-GREEN-REFACTOR cycle
- **systematic-debugging** - 4-phase root cause process
- **verification-before-completion** - Ensure it's actually fixed
- **requesting-code-review** - Pre-review checklist
- **receiving-code-review** - Responding to feedback
- **using-git-worktrees** - Parallel development branches
- **finishing-a-development-branch** - Merge/PR decision workflow
- **writing-skills** - Create new skills
- **using-superpowers** - Introduction to the skills system

### Skill Priority

1. **Process skills first** (brainstorming, debugging) - determine HOW to approach
2. **Implementation skills second** - guide execution

"Let's build X" -> brainstorming first, then implementation.
"Fix this bug" -> systematic-debugging first.

## Cross-Machine Continuity

This project is worked on from multiple computers via iCloud sync. At the start of each session, read `_status.md` for context on what was last worked on. At the end of each session, update `_status.md` with progress and next steps.

## Project Context

This is GovScraper - a web application for government contract bidding. The frontend is built with static HTML files using CSS custom properties for theming (light/dark mode), Plus Jakarta Sans + JetBrains Mono fonts.

### Key Pages
- `govscraper-dashboard.html` - Main dashboard with KPIs, charts, saved searches
- `govscraper-rfq-list.html` - RFQ listing page
- `govscraper-nsn-page.html` - NSN (National Stock Number) search
- `govscraper-cage-page.html` - CAGE code search
- `Final Redesign/Newest of New/` - Latest redesigned pages (multiple tiers, onboarding, modals, public pages)
