# Google Search Console alerts

Written by the Sunday report task from Search Console emails (sc-noreply@google.com).
The nightly website task works OPEN items first and marks each FIXED or EXPECTED.

## 2026-10-07 — Page with redirect
- Google's reason: "Page with redirect" (pages not indexed because they redirect).
- Example URLs: not listed in the email; check sitemaps list only final URLs (no redirecting pages, e.g. old "Moved" pages).
- Status: OPEN

## 2026-11-09 — Alternate page with proper canonical tag; Excluded by 'noindex' tag
- Google's reason: some pages not indexed because (a) they are alternates pointing to a canonical page and (b) they carry a noindex tag.
- Example URLs: not listed in the email.
- Likely expected: copied MedlinePlus guide pages are intentionally noindex, and EN/ES or .html duplicates may point to a canonical. Confirm canonicals and hreflang are correct, that no original page (homepages, medicines, visit guides, second opinion, help with costs, genetics, new pathway pages) is noindex or canonicalized away, and mark EXPECTED with the reason, or fix.
- Status: OPEN
