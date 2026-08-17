# JuneTrail — Site Structure

Static site, built for GitHub Pages. No build step required to view — every
`.html` file is deployable as-is.

## Folder structure

```
junetrail/
├── index.html                          Homepage
├── about.html
├── contact.html
├── robots.txt
├── sitemap.xml
├── README.md                           This file
│
├── assets/
│   ├── css/style.css                   Single shared stylesheet — all pages import this
│   ├── js/main.js                      Shared behaviour (nav toggle, newsletter form)
│   └── images/
│       ├── products/                   Product photography, by SKU-style filename
│       ├── articles/                   Article featured images
│       └── vehicles/                   Vehicle guide hero images
│
├── blog/
│   ├── index.html                      Blog listing (all articles, filterable by category)
│   └── <article-slug>.html             One file per article — flat, not nested by category
│
├── products/
│   ├── index.html                      Category grid (all 17 categories)
│   └── <category-slug>/
│       ├── index.html                  Category listing page
│       └── <product-slug>.html         Individual product page
│
├── vehicles/
│   ├── index.html                      Vehicle platform grid
│   └── <vehicle-slug>.html             One file per platform (e.g. toyota-hilux.html)
│
├── reviews/
│   └── index.html                      Review/comparison listing (pulls from blog/ comparison posts)
│
└── legal/
    ├── affiliate-disclosure.html
    ├── privacy-policy.html
    ├── terms.html
    └── editorial-policy.html
```

## Build helper (not deployed)

`_build.py` and `build_pages.py` are local authoring tools, not part of the
live site. They stitch a shared head/nav/footer around each page's body so
every page stays visually identical without copy-pasting the header 14 times.

To add a new page:
1. Open `build_pages.py`
2. Copy an existing `*_body = """ ... """` block as a starting point
3. Add a `write("path/to/page.html", title, description, canonical, "/", body)` call
4. Run `python3 build_pages.py`

This is a stopgap. If you outgrow copy/paste-style authoring, migrating to
**Jekyll** (which GitHub Pages runs natively, no extra config) gets you real
`_includes/header.html` / `_includes/footer.html`, front-matter per article,
and pretty URLs (`/blog/best-4wd-recovery-boards/` instead of `.html`) for
free. `_build.py`'s `HEAD` / `NAV` / `FOOTER` strings map directly onto
Jekyll includes if you go that route later.

## Naming conventions

- **Slugs**: lowercase, hyphen-separated, matches the H1 (`best-4wd-recovery-boards.html`)
- **Product images**: `assets/images/products/<category>-<product-slug>.jpg`
- **Categories**: match the 17 categories listed in `products/index.html` exactly —
  don't introduce a new category name without adding it there first
- **Article categories** (for the blog filter bar): Recovery · Touring · Suspension ·
  Maintenance · Off-Road Driving · Comparison

## URL structure (target, once on Jekyll / pretty permalinks)

```
/blog/best-4wd-recovery-boards/
/products/recovery-gear/
/products/recovery-gear/traction-recovery-board/
/vehicles/toyota-hilux/
```

Current static build serves these with `.html` extensions instead
(`sitemap.xml` reflects the real, current URLs — update it if you move to
pretty permalinks).

## Content status

Everything under `blog/`, `products/`, `vehicles/` beyond the one worked
example per type is **placeholder/demo content**, clearly labelled with a
`.demo-banner` on the page. Before publishing:

- [ ] Replace demo product specs/prices with real data (or wire to a feed)
- [ ] Replace placeholder `.prod-img` / `.art-img` blocks with real photography
- [ ] Add real Amazon affiliate tracking IDs to every `CHECK PRICE` link
- [ ] Fill in `legal/*.html` with reviewed copy, not placeholders
- [ ] Wire `.nl-form` submit to an actual email provider (currently a stub in `main.js`)

## Design tokens (for consistency across new pages)

| Token | Value | Use |
|---|---|---|
| `--slate` | `#2B3A48` | Nav, footer, hero background |
| `--lava` | `#B8442E` | Accent — CTAs, category labels, eyebrows |
| `--cream` | `#F4EFE3` | Card backgrounds, light text on dark |
| `--paper` | `#FBF8F1` | Page background |
| `--ink` | `#1C2229` | Body text |
| `--contour` | `#5C7080` | Muted/secondary text, topo-line motif |

Fonts: **Fraunces** (headings/wordmark), **Inter** (body), **IBM Plex Mono**
(eyebrows, specs, buttons — the "technical drawing" voice).
