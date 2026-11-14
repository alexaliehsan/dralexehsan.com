# Website status, September 23, 2026

## Completed in this update

- Five main navigation destinations with a separate autoimmune section and homepage subject shortcuts.
- Existing Matthew-led athlete initiative and family team preserved.
- TikTok points to @bib55939; Instagram points to the latest user-confirmed @dralexehsan.
- Twenty sport-specific QR assets, stable anchors, downloadable codes, and individual print controls.
- Spanish mental-health entry point now restricts results to Spanish mental-health entries.
- Category entry points reset pagination, and mobile menu links close their menu.
- Audited 10,020 unique topic titles, 20,000 search phrases, 2,000 mental-health entries, and 1,000 athlete poster templates.
- Prominent count claims now distinguish short summaries and templates from independently reviewed clinical guidelines.
- Added autoimmune source links and an editorial policy; no fabricated clinician review dates.
- Social cards described as selected posts, not automatically current feeds.

## Verified

The dependency-free site validator checks script syntax, actual collection counts, duplicate titles, search-index references, internal anchors, local assets, and the 20 QR assets. A temporary jsdom check passed category/search behavior, pagination, empty state, Spanish mental-health scoping, navigation destinations, social URLs, sport deep links, and print-state cleanup. No runtime errors were observed. A real-browser visual review could not run because Chromium was unavailable and its download returned invalid archive data. Do not report mobile visual QA as completed.

## Remaining dependencies

- dralexehsan.com domain and TLS confirmed active September 27, 2026.
- Automatic social imports are not implemented. The site is static and platform authorization/import infrastructure has not been provided. Never describe selected links as a synchronized feed.
- The large collection consists mostly of brief template-based topic prompts. It is not 10,000 comprehensive clinical guidelines. Individual clinical expansion, condition-specific citations, and named professional review remain substantive editorial work.
- The educational question-review service remains planned and closed. No submissions are collected.
- No records or patient-specific information should be collected or published.

## September 27 social import

Imported 713 unique September post URLs from connected Metricool brand 6951175. Counts: Facebook 221, LinkedIn 104, TikTok 365, Instagram 20, YouTube 3. Added searchable, paginated social-updates.html and homepage entry. Excerpts capped at 420 characters; 226 posts have link-only cards because provider caption responses exceeded its response limit. Latest returned dates: September 26 for Facebook/LinkedIn/TikTok; September 8 for Instagram/YouTube. Pinterest returned no rows. X is absent from connected brand networks and returned no rows. This is an on-demand snapshot, not an automatic feed or proof of complete current coverage. Existing social links preserved.

## September 27 usability and search optimization

Removed floating athlete CTA and placed it in the hero action flow. Removed mobile credential-card negative margin; improved narrow-screen action wrapping and notice layout. Search now caches normalized text, ignores accents, matches multiple words, ranks titles before body matches, supports selected clinical abbreviations, and provides independent language selection and reset. Main URLs use dralexehsan.com canonical tags; added robots.txt and sitemap.xml. Validator and targeted search behavior checks passed. No browser visual QA was performed in this pass. External video availability, Search Console verification/submission, and expanded source-reviewed clinical articles remain outstanding.

## September 27 mobile, search, and editorial expansion
Google Search Console URL-prefix ownership verified; sitemap processed successfully before this pass. Preserve Google verification meta tag.
Added touch/readability refinements, narrow header wrapping, full-width expanded results, and search input semantics. Fixed stale language filters in shortcut navigation. Search expands abbreviations within phrases and indexes existing search phrases consistently. Added six substantive English explainers at health-guides.html, linked from search and added to sitemap, using NIH/CDC sources accessed September 27, 2026. These remain educational summaries without documented individual clinician review. Existing 10,020 entries are not replaced or represented as fully reviewed articles.
Validation: existing site validator and targeted phrase-alias, accent, language/category, empty-result, article-navigation checks passed. Visual mobile testing remains unavailable: the managed preview does not support this plain static site. No claim of browser visual QA.

## September 27 attributed source-guide expansion
Added 2,028 MedlinePlus English/Spanish full topic summaries with attribution, source links, data-edition/import dates, general care-team questions, and a pending individual clinical-review notice. Source-specific symptoms/testing/treatment links are included where available in the source export. This is a source-library expansion, not 2,028 original clinician-reviewed articles.
Linked 377 normalized base/language topics (4,297 existing search entries) to matched source guides; related background is explicitly labeled. The original AML guide remains linked. 1,145 base/language topics still await individual expansion; they are tracked in data/medical-review-queue.json. No claim of completing every topic is warranted.
Added searchable patient-guides.html, shared responsive styles, machine-readable provenance, and patient-guides-sitemap.xml advertised in robots.txt. Preserved Search Console verification. The separate source sitemap has not yet been submitted directly through Search Console.
Validation: static site validator, all 2,028 page links/markup/source checks, all 377 generated homepage mappings, preserved AML link, directory loading, search, Spanish filtering and empty state passed. No new browser visual review performed.

## September 27 poster opening fix
Replaced the immediate print action on all 1,000 athlete poster cards with Open poster. A native accessible dialog displays a generated PNG of the selected typographic poster, with Download poster, Print, and Close controls. The image can also be saved by long-press on mobile. Uses the existing card content and accent color; no new medical claims. Text wraps and image height grows to fit. Print is a separate optional action rather than a prerequisite for viewing. Static validation and targeted image-generation/wrapping checks passed. Android browser behavior awaits user confirmation; no browser visual QA claimed.

## September 27 illustrated locker-room poster
Added the first actual anatomical poster at posters/concussion-locker-room.png, generated with built-in imagegen and visually inspected. Teen/student-athlete audience, no doctor image, dominant head/brain anatomy, concise concussion action and emergency guidance checked against CDC HEADS UP response and signs/symptoms pages September 27, 2026. Source links and pending clinician-review statement accompany poster. Featured at #concussion-poster and used by Sports concussion cards. Preview uses original PNG and direct download rather than converting back to text. The other topics remain text templates; no claim that all 1,000 have illustrations. Static validator and image existence/syntax checks passed.

## September 27 illustrated category collection
Expanded the approved visual style into 20 anatomical/athlete safety designs, one per major poster category. Built illustrated-posters.html with category search, full-size images, direct PNG downloads, readable transcripts, sources and a pending individual-review notice. Related illustrated-category links are available from the original text entries; concussion imagery is not attached to unrelated eye/jaw/facial injuries. Text reminders remain separately labeled. This does not complete the 200 distinct condition topics or their 1,000 variants; data/illustrated-poster-review-queue.json tracks that remaining work. No claim of 1,000 unique illustrated posters.
Original raster assets generated with built-in image generation. Assets inspected for text and anatomy; targeted corrections made to evaluation/treatment knee anatomy and spine perspective. Illustrations are educational, not diagnostic images or substitutes for clinical evaluation. No doctor pictures. Sources include CDC HEADS UP, AAOS OrthoInfo, AAP HealthyChildren and NIAMS, checked September 27, 2026. No patient-specific information used.
Validation for this batch: all 20 PNG assets decode; all gallery local links and image downloads resolve; category search, reset and empty state pass; main site validator passes. Browser visual/mobile QA was not performed. User will perform clinical review. No clinical review attributed to user without explicit review.

## Individual injury poster collection — September 27, 2026

- Added 99 original anatomical PNG posters, completing individual coverage of the 100 base topics in the ten injury/body-area groups (10 topics each: head, neck, shoulder, elbow, wrist/hand, spine/core, hip/groin, knee, lower leg, ankle/foot). The original sports-concussion image supplies the hundredth.
- Gallery now contains 119 unique illustrated designs: those 100 topic-specific posters plus the 19 retained general athlete-safety designs. This is not 1,000 unique artworks or 200 individually illustrated base topics; the other 100 training, recovery, evaluation and broader themes retain general illustrations/text templates.
- Each of the 99 new posters connects to its exact existing topic. Five focus-angle entries share one individual poster; search deduplicates the resulting artwork and matches separated query terms (e.g. ACL treatment).
- PNG preview/download links, searchable gallery, text alternatives, primary clinical source links, and pending individual clinical-review status retained. Source briefs and image scope are recorded in data/injury-poster-briefs.json. Built-in ImageGen was used, with visual inspection and targeted corrections; this is not clinical validation.
- Two foot images were replaced with regional anatomical illustrations after exact attachment/fracture-site depictions proved unreliable. Their metadata describes this scope. All illustrations are educational concept art, not precise diagnostic or procedural diagrams. Individual review by Dr. Ehsan remains pending.
- Validation passed: site invariants (10,020 entries, 20,000 phrases, 1,000 athlete entries, 20 QR assets), routing for all 99 added topics, five-entry artwork deduplication, multiword/empty search, gallery anchors/download references, 119 distinct decoded portrait images, all 100 target topics available, sitemap XML. Static-site browser/mobile interaction QA was not available; no such QA claimed.

## Practice schedule and independence notice · 2026-09-27
Added alternating California in-person and Texas telemedicine schedule, clinic calling links, appointment/social-message boundary, and independent free education disclaimer. No dated week assignment. Official Starling location pages list Downey 11525 Brookshire Ave Suite 202, 90241 and Culver City 9808 Venice Blvd Suite 603, 90232. Used official published addresses rather than conflicting typed street numbers.

## Twenty sport-specific illustrated posters · 2026-09-27
Added original anatomical safety PNGs for all 20 sports listed in the athlete center. Added sport-posters.html, preview/open/download links in every sport guide, gallery entries and homepage link. Total 139 illustrated posters. Sources per brief. Individual clinical review pending. Visual inspection and static route/PNG checks passed. Existing 119 posters and appointment section preserved.

Hosting size correction: existing PNGs losslessly recompressed; new sport posters served as full-resolution WebP at quality 100 to fit the archive limit. Original new PNGs remain in prior source commit 6f31f485dff415dab7943b4d2f5556f56227b26c.

## Expansion to 444 in progress · 2026-09-27
User authorized305 additional original athlete posters, organized15per20sports plus5general emergency safety posters. Live count remains139 until full integration and native publish succeeds. Assets/checkpoints in sibling expand444-a through e. Gallery now supports24at-a-time display, multiword search, sport query links, and hash target reveal. Existing119PNG assets palette-optimized at full dimensions to preserve URLs and allow hostingcapacity. Originals remain in sourcecommit17c522dab20c3f47449bc28f90855289d851a636. New delivery files plannedWebPquality94. All pendingindividualclinicalreview.

## 444-poster expansion completed — 2026-09-27
- Integrated305 distinct generated posters:15 additional focused posters per20 sports, plus5 shared emergency-safety posters.
- Collection totals444:320 sport-focused,100 injury/body-area,24 general safety. All images remain1024×1536 with individual clinician review pending.
- All five production groups visually inspected selected final images; safety-copy/anatomy corrections resolved in final manifests. Prompts, QA records and safety audit preserved in data/expansion444-production and data/expansion444-safety-audit.json.
- Gallery uses24-item progressive display, token search, sport filters and direct anchor reveal. Existing image URLs retained; new images use WebP delivery.
- Validation passed:444 unique image paths and hashes, full dimensions,320 sport cards,20 sport-specific links; core site and injury-poster validators pass. Dist size206,993,442 bytes, within hosting limit.
- Practice information, employer separation and Search Console verification preserved. Ready for native publication.

## Approved clinical poster revisions — September 28, 2026

- Alex Ehsan, MD, PhD explicitly approved the collection review and requested that the listed updates be applied and published. Scope is the 444 illustrated posters, not unrelated medical guides.
- Applied all 19 recommendations: six priority safety changes, one Jones-fracture illustration clarification, and twelve additional wording improvements. The preliminary scaphoid-side concern was withdrawn after full-size inspection and no scaphoid edit was made.
- Revised embedded image text, gallery text alternatives, source links and collection-review labels are kept in sync. User sign-off is recorded in data/poster-clinical-signoff.json, with exact revised copy and image checksums in data/poster-approved-revisions.json.
- Images edited using built-in image_gen and visually inspected. Original image URLs are preserved. The noncontact boxing poster replaces sparring imagery with solo bag training; the Jones image carries a prominent regional-illustration disclaimer.
- The underlying review was AI-assisted content screening followed by user approval, not an exhaustive anatomical certification. Educational and individual-care disclaimers remain.
- Validation passed for all 444 poster records, 19 changed image checksums and text alternatives, 320 sport cards, poster-only approval scope, core site invariants and individual injury routing. Static browser preview is unavailable for this buildless site in the current environment; no browser QA claimed.

## Matthew’s opening letter — September 28, 2026
Added a first-person purpose statement at the beginning of the athlete center, before the sport guides. Covers basketball, record-setting high-school powerlifting, varsity football captaincy, shoulder surgery and severe finger injury, kinesiology at Texas Tech, and aspirations in sports medicine or PM&R. Names support from Alex Ehsan, Sam Ehsan and Pasha Ehsan. No unconfirmed operation name, research experience or recovery outcome supplied. Student and clinician roles remain distinct.

## Homepage athlete placement — September 28, 2026
Moved the existing purpose quote and mission above the main content, followed by Matthew’s full story, young-athlete resources, the poster print center and future sports research. Search and purpose wording retained. Removed the family-list paragraph identified in the screenshot and renamed its remaining panel Clinical support and educational scope. Removed the redundant family-centered introduction from the homepage athlete section. Existing anchors, search inputs, poster controls and all sports pages preserved.

## Searchable genetics section — September 28, 2026
Added genetics.html with 1,500 public-domain MedlinePlus gene-function excerpts, aliases and related-condition links, plus ten NCI-based summaries absent from that data set. Forty inherited-cancer educational starting points are numbered with CDH1 first. Order is expressly editorial, not a medical risk, prevalence or testing-priority ranking. Gene search is connected to the existing homepage search without changing its original medical-topic collection. Added homepage navigation and a genetics section, and a direct external ClinVar exact-variant lookup. Germline versus tumor findings, VUS limits, one/two gene copies, source dates and pending individual genetics review are explicit. Existing poster sign-off is not applied to genetics. Provenance and source hash are in data/genetics-provenance.json.
- Genetics validation passed for 1,510 unique genes, 40 ranked starting points, exact symbols, HER2 alias, Lynch syndrome search, no-results handling, homepage integration, direct CDH1 expansion and source metadata. Static browser preview unavailable in this environment; no browser QA claimed.

## Completion pass — September 29, 2026

- Reconciled the current source against the older version-49 poster review. All 19 approved corrections and the recorded 444-poster collection sign-off were already implemented. Genetics approval was also recorded. Preserved the distinct review scope of each collection.
- Finished poster navigation with visible sport selection and clear-search controls on both directories. Search URLs preserve selected topics; unknown sport URLs recover to all posters; direct links reveal the requested poster even from another sport; malformed fragments no longer break the gallery.
- Corrected preview downloads to retain the original PNG or WebP extension. Kept the approved medical text, artwork, and image URLs unchanged.
- Updated existing injury and source-guide validation to follow the extracted medical-library.js file. Previous validators were reading their former inline location.
- Validated all 2,045 HTML pages, 10,590 internal references, sitemaps, all 444 decodable poster assets, 20 sport filters, the 19 approved image checksums, 99 injury routes, 2,028 source guides, 377 source-guide mappings, 1,510 genes, and all 10,020 medical topic entries. Full homepage JavaScript execution and English/Spanish search behavior passed in a DOM-stub runtime.
- No real-browser visual/mobile QA was performed. The managed preview does not support this buildless static site; responsive CSS was retained and the new controls include narrow-screen layouts. Do not call these checks browser testing.
- This completes this implementation and navigation pass. It does not certify independent clinical review of every general medical summary or make the social snapshot an automatic feed. No new clinical approval is attributed to Dr. Ehsan. The educational topic link routes to the existing public education page; it does not collect private medical questions.

## Start Here patient pathway — 2026-11-14 (branch start-here-pathway, not published)
- Reviewed ChatGPT's "master project" brief. Implemented only the parts not already done: an original bilingual Start Here path (A–H) with six new plain-language guides (diagnosis, PET/CT/MRI, pathology report, staging, treatment options, clinical trials) plus hub pages; F/G link to the existing visit guide. Sources: NCI, ACS, RadiologyInfo, ClinicalTrials.gov, checked 2026-11-14. No individual medical recommendations; no claim of individual clinician review.
- Homepage Start Here tiles now point to the eight steps; "Start here" added to the top menu and footer (EN/ES). Scan FAQ links now go to the original scans page instead of a MedlinePlus copy.
- SEO: the 2,028 MedlinePlus copies carry noindex,follow (Nov 8 decision); their sitemap was removed from the sitemap index; 15 pages added to pages-sitemap.xml (incl. es.html). New pages have MedicalWebPage + BreadcrumbList structured data linked to the existing Physician entity, hreflang EN/ES, canonical tags and GA G-W67KPLQPDR.
- Declined from the brief: full redesign (owner decision: keep structure), research/publications/media sections (need verified source material from the owner), any change to DNS/hosting.
- Checks: validate-release.py passed (2,070 pages, 17,825 local references); 10 pages at 390px and 1366px with no horizontal overflow and no JS errors.
- 2026-11-14 (later): Reviewed Muse's tech check. Added: homepage search now suggests the Start Here guides first (start-here-index.json, visitor's language only); each new guide shows an honest status line ("source-checked Nov 14, 2026; not yet individually reviewed by Dr. Ehsan") and no lastReviewed claim in structured data. Verified live: homepage search already had live suggestions; sitemap live (200); no employer links. Declined: Starling appointment links (owner decision: site fully separate from employer, no call button); on-site suggestion form (collects messages/possible PHI; owner does not want patient contact through the site); OneDrive Oct 26–27 comparison (superseded by the Oct 31 and Nov 4 redesigns; live site = repo main).
