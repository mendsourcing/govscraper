# GovScraper Unified Prototype — Design Spec

**Date:** 2026-03-19
**Status:** Draft
**Scope:** Unify all redesigned HTML pages into a single navigable prototype

---

## 1. Goal

Create a clickable, fully navigable prototype of GovScraper where a user can:
1. Sign in with dummy credentials
2. Land on the Member Dashboard (Maxx tier, everything unlocked)
3. Navigate all pages via the sidebar
4. Toggle between Member Portal and Supplier Portal
5. Experience the full product as if it were a working app

## 2. Constraints

- **Static HTML only** — no build tools, no frameworks
- **Redesigned files only** — Manrope + Source Code Pro typography, no legacy Plus Jakarta Sans files
- **Self-contained pages** — each page includes its own CSS (matching current pattern)
- **Maxx tier** — all features unlocked, no locked/gated sections
- **Dummy data** — all data is hardcoded/static, no backend

## 3. Entry Flow

```
Sign In Page → (enter any email + password) → Member Dashboard (Maxx)
```

- Sign In page adapted from `Sign In Page.html` in the onboarding folder
- Dummy auth: any non-empty email + password triggers redirect to dashboard
- No onboarding steps, no public pages in this version
- Login always lands on the **Member Portal** by default

## 4. Portal Toggle

A persistent toggle control in the **topbar** switches between Member and Supplier portals.

### Behavior:
- **Default on login:** Member Portal
- **Toggle location:** Topbar, near the user avatar area
- **Visual indicator:** Active portal is highlighted; Member uses blue accent, Supplier uses green accent
- **What changes on toggle:**
  - Sidebar navigation items update to match the active portal
  - Dashboard content swaps (Member Dashboard vs Supplier Dashboard)
  - Accent color shifts (`body.supplier-mode` applies green highlights)
- **What stays the same:**
  - Topbar structure (logo, toggle, notifications, avatar)
  - Account/settings pages are shared

## 5. Navigation Map

### 5.1 Member Portal (Blue Accent)

**Sidebar sections and pages:**

| Section | Item | Source File | Filename in Prototype |
|---------|------|-------------|----------------------|
| MAIN | Dashboard | 1D_Dashboard_Maxx_.html | dashboard.html |
| MAIN | My RFQs | 2A_RFQ_Listing.html | rfq-listing.html |
| INTELLIGENCE | NSN Search | 3A_NSN_Page_Member.html | nsn-search.html |
| INTELLIGENCE | CAGE Search | 5_CAGE_Search_Results.html | cage-search.html |
| INTELLIGENCE | FSC Lookup | 7_FSC_Lookup_Page.html | fsc-lookup.html |
| RESULTS | Awarded Contracts | 9_Awarded_Contracts.html | awarded-contracts.html |
| RESULTS | NSN Watch List | 8_NSN_Watch_List_Page.html | nsn-watchlist.html |
| RESULTS | Archived | 10_Archived_Page.html | archived.html |
| RESULTS | RFQ Alerts | 11_RFQ_Alerts_Member.html | rfq-alerts.html |
| ACCOUNT | Account Panel | 12_Account_Panel.html | account.html |
| ACCOUNT | Password Change | 12a_Password_Change.html | password-change.html |
| ACCOUNT | Subscription | 12b_Subscription_Page.html | subscription.html |
| ACCOUNT | FSC/CAGE Listing | 12c_FSC_CAGE_Listing.html | fsc-cage-listing.html |
| ACCOUNT | Email Integration | 12d_Email_Integration_Connect_Email.html / 12e | email-integration.html |

**Detail pages (linked from search/list pages):**

| Context | Source File | Filename in Prototype |
|---------|-------------|----------------------|
| CAGE Detail (claimed) | 4B_CAGE_Page_Claimed.html | cage-detail.html |
| CAGE Claim Registration | 6A_CAGE_Claim_Registration.html | cage-claim-register.html |
| CAGE Claim Pending | 6B_CAGE_Claim_Pending.html | cage-claim-pending.html |
| CAGE Claim Approved | 6C_CAGE_Claim_Approved_First_Time.html | cage-claim-approved.html |
| CAGE Supplier Inventory | 6D_CAGE_Supplier_Inventory_Upgrade_to_MAXX.html | cage-supplier-inventory.html |
| CAGE RFQ Alerts (Maxx) | 6E_CAGE_RFQ_Alerts_MAXX.html | cage-rfq-alerts.html |

### 5.2 Supplier Portal (Green Accent)

**Sidebar sections and pages:**

| Section | Item | Source File | Filename in Prototype |
|---------|------|-------------|----------------------|
| MAIN | Supplier Dashboard | 1G_SupplierPortal_GOLD and MAXX.html | supplier-dashboard.html |
| MAIN | My RFQs | 2A_RFQ_Listing.html (supplier variant) | supplier-rfqs.html |
| INTELLIGENCE | NSN Search | 3A (shared) | nsn-search.html |
| INTELLIGENCE | CAGE Search | 5 (shared) | cage-search.html |
| ACCOUNT | Account Panel | 12 (shared) | account.html |

Shared pages (NSN, CAGE, Account) are the same files — the portal toggle just changes which sidebar items are visible and the accent color.

### 5.3 Modals

| Modal | Source | Triggered From |
|-------|--------|----------------|
| Claim Code Popup | _POPUP for CLAIM CODE.html | CAGE detail page |
| Upgrade Modals | Modals_Showcase.html | Subscription page, contextual upsells |

## 6. Shared Components (per-page inline)

Since each page is self-contained HTML with inline CSS, the following components are standardized across all pages:

### 6.1 Topbar (56px height, sticky)
- Left: GovScraper logo (links to dashboard)
- Center-left: Breadcrumb trail
- Center-right: **Portal Toggle** (Member | Supplier)
- Right: Notification icon, settings icon, user avatar (gradient)

### 6.2 Sidebar (224px width, fixed)
- Sections: MAIN, INTELLIGENCE/TOOLS, RESULTS, ACCOUNT
- Active state: accent background + left border
- Badges: count indicators on RFQs, alerts
- Items change based on active portal (Member vs Supplier)

### 6.3 Typography
- Body: Manrope (400, 500, 600, 700, 800)
- Mono: Source Code Pro (400, 500, 600, 700)

### 6.4 Color System
- Member accent: `--accent: #2563EB` (blue)
- Supplier accent: `--accent: #16A34A` (green) via `body.supplier-mode`
- Full semantic palette: green, amber, red, cyan, purple
- Dark mode: supported via `[data-theme="dark"]` CSS variables

## 7. File Structure

```
prototype/
  sign-in.html              (entry point)
  dashboard.html             (Member Dashboard - Maxx)
  supplier-dashboard.html    (Supplier Dashboard - Maxx)
  rfq-listing.html
  supplier-rfqs.html
  nsn-search.html
  cage-search.html
  cage-detail.html
  cage-claim-register.html
  cage-claim-pending.html
  cage-claim-approved.html
  cage-supplier-inventory.html
  cage-rfq-alerts.html
  fsc-lookup.html
  nsn-watchlist.html
  awarded-contracts.html
  archived.html
  rfq-alerts.html
  account.html
  password-change.html
  subscription.html
  fsc-cage-listing.html
  email-integration.html
  modals-showcase.html       (for testing/demo)
```

**Total: 23 HTML files** (22 app pages + 1 sign-in)

## 8. Implementation Approach

1. Create `prototype/` directory
2. Adapt Sign In page with dummy auth (redirect to dashboard.html)
3. Copy each redesigned source file into prototype with:
   - Standardized topbar (with portal toggle)
   - Standardized sidebar (with correct active state and working links)
   - Consistent file naming and cross-linking
   - Manrope + Source Code Pro fonts only
4. Wire all navigation links between pages
5. Add portal toggle JavaScript (switches body class, updates sidebar)
6. Add dark/light theme toggle
7. Integrate modals where contextually appropriate

## 9. Success Criteria

- User can sign in and land on Member Dashboard
- Every sidebar link navigates to a real page
- Portal toggle switches between Member and Supplier views
- All pages use consistent Manrope + Source Code Pro typography
- Dark mode toggle works across all pages
- Breadcrumbs update to reflect current page
- Back/forward browser navigation works correctly
- No broken links or dead-end pages
