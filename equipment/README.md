# Equipment

Deterministic scripts, one job each. Promoted from the LauterMobil run on 2026-09-24 (approved by Hafsa).
All paths are relative to the repo. Project-specific settings (project folder, texts, colours) sit at the top of each script.

| Script | Stage | What it does | Output |
|---|---|---|---|
| `trademark_check_tmview.py` | 03 Trademark | Searches TMview (DE national + EUIPO + WIPO marks) for each term. Flags hits in Nice classes 39/44. Usage: `python equipment/trademark_check_tmview.py "name one" "name two"` | Console report |
| `build_exact_logo.py` | 04 Logo | Rebuilds the approved Canva logo as a vector: measured monogram polygons, lettering traced with potrace from `logo/reference/chosen-canva-logo-2000px.png`, exact brand hex colours. | 6 SVG variants in `logo/final/` |
| `make_business_card.py` | 05 Card | 85×55 mm card with 2 mm bleed, front and back. Embeds the approved logo SVGs, outlines all text, checks the safe area. | `business-card/card-*.svg` + `_print.html` → PDF |
| `make_flyer.py` | 06 Flyer | A5 flyer with 2 mm bleed, front and back. Hero and grid photos from `flyer/photos-generated/`, outlined text, safe-area checks. | `flyer/flyer-*.svg`; print HTML in `.tmp/flyer_print.html` |

## Requirements

- Python 3 with `uharfbuzz`, `fonttools`, `potracer`, `Pillow`, `numpy` (`pip install uharfbuzz fonttools potracer pillow numpy`)
- Google Chrome (headless) for PDF and PNG export
- Fonts in `equipment/fonts/`: Open Sans, Quicksand, Nunito. All SIL Open Font License; licence texts included.

## Export Commands (Chrome headless)

```
chrome --headless=new --no-pdf-header-footer --print-to-pdf=OUT.pdf file:///PATH/_print.html
chrome --headless=new --hide-scrollbars --window-size=W,H --screenshot=OUT.png file:///PATH/page.html
```

## Domain Check (no script yet)

Vercel MCP `get_bulk_availability`, then confirm with RDAP: `https://rdap.denic.de/domain/<d>` (.de) and `https://rdap.verisign.com/com/v1/domain/<d>` (.com). 404 = free.

## Known Limits

- The scripts are configured for LauterMobil (project path, texts, contact details). For a new client, copy the script and edit the settings block at the top. Making them fully parameterised is future work.
- Exported PDFs are RGB. Print shops convert to CMYK, so order a proof.
