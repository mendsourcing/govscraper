#!/usr/bin/env python3
"""Transform source HTML files into prototype pages with standardized topbar/sidebar."""
import re, os

PROTO_DIR = os.path.dirname(os.path.abspath(__file__))

SIDEBAR_TEMPLATE = '''<nav class="sidebar sidebar-member">

  <div class="sidebar-label">MAIN</div>
  <a class="sidebar-item{a_dashboard}" href="{h_dashboard}">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>
    Dashboard
  </a>
  <a class="sidebar-item{a_rfq-listing}" href="{h_rfq-listing}">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14,2 14,8 20,8"/></svg>
    My RFQs <span class="sidebar-badge">47</span>
  </a>

  <div class="sidebar-label">INTELLIGENCE</div>
  <a class="sidebar-item{a_nsn-search}" href="{h_nsn-search}">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
    NSN Search
  </a>
  <a class="sidebar-item{a_cage-search}" href="{h_cage-search}">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>
    CAGE Search
  </a>
  <a class="sidebar-item{a_fsc-lookup}" href="{h_fsc-lookup}">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
    FSC Lookup
  </a>

  <div class="sidebar-label">RESULTS</div>
  <a class="sidebar-item{a_awarded-contracts}" href="{h_awarded-contracts}">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22,4 12,14.01 9,11.01"/></svg>
    Awarded Contracts
  </a>
  <a class="sidebar-item{a_nsn-watchlist}" href="{h_nsn-watchlist}">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
    NSN Watch List
  </a>
  <a class="sidebar-item{a_archived}" href="{h_archived}">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="21 8 21 21 3 21 3 8"/><rect x="1" y="3" width="22" height="5"/><line x1="10" y1="12" x2="14" y2="12"/></svg>
    Archived
  </a>
  <a class="sidebar-item{a_rfq-alerts}" href="{h_rfq-alerts}">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9M13.73 21a2 2 0 01-3.46 0"/></svg>
    RFQ Alerts
  </a>

  <div class="sidebar-label">ACCOUNT</div>
  <a class="sidebar-item{a_account}" href="{h_account}">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
    Account
  </a>

</nav>'''

TOPBAR_TEMPLATE = '''<header class="topbar">
  <div class="topbar-left">
    <a href="dashboard.html">
      <img src="https://govscraper.com/assets/BigLogo-7gv5uAxF.png" alt="GovScraper" class="topbar-logo" onerror="this.outerHTML='<span style=&quot;font-family:Manrope,sans-serif;font-size:18px;font-weight:800;color:var(--text);&quot;>GovScraper</span>'">
    </a>
    <div class="topbar-divider"></div>
    <div class="mode-switcher">
      <button class="mode-btn active-member"><span class="mode-dot blue"></span> Member</button>
      <button class="mode-btn inactive" onclick="window.location.href='dashboard.html'"><span class="mode-dot green"></span> Supplier</button>
    </div>
    <div class="topbar-divider"></div>
    <div class="breadcrumb">
      <a href="dashboard.html">Dashboard</a>
      <span style="color:#CBD5E1;margin:0 4px">&#8250;</span>
      <span style="color:var(--text-dim);font-weight:600">{breadcrumb}</span>
    </div>
  </div>
  <div class="topbar-right">
    <button class="topbar-icon-btn" title="Notifications">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9M13.73 21a2 2 0 01-3.46 0"/></svg>
    </button>
    <button class="avatar-btn" title="My Account">JD</button>
  </div>
</header>'''

PAGE_LINKS = {
    'dashboard': 'dashboard.html',
    'rfq-listing': 'rfq-listing.html',
    'nsn-search': 'nsn-search.html',
    'cage-search': 'cage-search.html',
    'fsc-lookup': 'fsc-lookup.html',
    'awarded-contracts': 'awarded-contracts.html',
    'nsn-watchlist': 'nsn-watchlist.html',
    'archived': 'archived.html',
    'rfq-alerts': 'rfq-alerts.html',
    'account': 'account.html',
}

OLD_LINK_MAP = {
    'govscraper-dashboard.html': 'dashboard.html',
    'govscraper-dashboard-pro.html': 'dashboard.html',
    'govscraper-rfq-list.html': 'rfq-listing.html',
    'govscraper-public-rfq-list.html': 'rfq-listing.html',
    'govscraper-nsn-page.html': 'nsn-search.html',
    'govscraper-cage-page.html': 'cage-search.html',
    'govscraper-fsc-lookup.html': 'fsc-lookup.html',
    'govscraper-nsn-watchlist.html': 'nsn-watchlist.html',
    'govscraper-awarded-contracts.html': 'awarded-contracts.html',
    'govscraper-archived-rfqs.html': 'archived.html',
}


def build_sidebar(active_key):
    replacements = {}
    for key, href in PAGE_LINKS.items():
        replacements[f'a_{key}'] = ' active' if key == active_key else ''
        replacements[f'h_{key}'] = '#' if key == active_key else href
    return SIDEBAR_TEMPLATE.format(**replacements)


def build_topbar(breadcrumb_label):
    return TOPBAR_TEMPLATE.format(breadcrumb=breadcrumb_label)


def process_file(filename, active_key, breadcrumb_label):
    filepath = os.path.join(PROTO_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find <body...> tag
    body_m = re.search(r'<body[^>]*>', content)
    if not body_m:
        print(f'ERROR: no <body> in {filename}')
        return
    body_end = body_m.end()

    # Find start of <div class="main"  (first occurrence after body)
    main_m = re.search(r'<div\s+class="main"', content[body_end:])
    if not main_m:
        print(f'ERROR: no .main div in {filename}')
        return
    main_pos = body_end + main_m.start()

    # Build new shell
    new_topbar = build_topbar(breadcrumb_label)
    new_sidebar = build_sidebar(active_key)
    new_content = content[:body_end] + '\n\n' + new_topbar + '\n' + new_sidebar + '\n\n' + content[main_pos:]

    # Replace old links throughout
    for old, new in OLD_LINK_MAP.items():
        new_content = new_content.replace(old, new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'OK  {filename}')


FILES = [
    ('fsc-lookup.html',        'fsc-lookup',        'FSC Lookup'),
    ('nsn-watchlist.html',     'nsn-watchlist',      'NSN Watch List'),
    ('awarded-contracts.html', 'awarded-contracts',  'Awarded Contracts'),
    ('archived.html',          'archived',           'Archived'),
    ('rfq-alerts.html',        'rfq-alerts',         'RFQ Alerts'),
]

for args in FILES:
    process_file(*args)

print('\nDone — all 5 files transformed.')
