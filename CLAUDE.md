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

This is GovScraper - a web application for government contract bidding. The frontend is built with static HTML files using CSS custom properties for theming (light/dark mode), Manrope + Source Code Pro fonts.

### Color System (Monochrome Redesign)
- **Member Portal:** Blue monochrome (brand blue `#1B6CA8`). All metrics, charts, positive indicators use blue family.
- **Supplier Portal:** Red accent (`#BE1E2D`). Sidebar, badges, verified cards use brand red.
- **Tier Badges:** LITE (gray), PRO (blue), GOLD (amber), MAXX (purple) — unchanged.
- **Errors/warnings:** Red `#DC2626` preserved. Success feedback: green `#16A34A` preserved.

### Authentication
- Tier-based login: `lite@`, `pro@`, `gold@`, `maxx@govscraper.com` — password: `mendsourcing101`
- Tier/email stored in `sessionStorage` (`gs_tier`, `gs_email`)

### Key Pages (in `prototype/`)
- `sign-in.html` - Tier-based sign-in
- `dashboard.html` - Member Dashboard (Maxx tier, all features unlocked)
- `rfq-listing.html` - RFQ listing
- `nsn-search.html` - NSN (National Stock Number) search
- `cage-search.html` - CAGE code search
- `cage-detail.html` - CAGE detail page (claimed state)
- `cage-claim-register.html` / `cage-claim-pending.html` / `cage-claim-approved.html` - CAGE claim flow
- `cage-supplier-inventory.html` / `cage-rfq-alerts.html` - Supplier CAGE pages
- `fsc-lookup.html` - FSC lookup
- `awarded-contracts.html` / `nsn-watchlist.html` / `archived.html` / `rfq-alerts.html` - Results pages
- `account.html` / `password-change.html` / `subscription.html` / `fsc-cage-listing.html` / `email-integration.html` - Account pages
- `Final Redesign/Newest of New/` - Source redesigned pages (reference)
