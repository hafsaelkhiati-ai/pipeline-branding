# Sub-Blueprint: 05 — Business Card

*Part of [pipeline-brand-strategy.md](../pipeline-brand-strategy.md). Read the global orchestrator first.*

**Status:** v0.2: validated on LauterMobil (card approved 2026-09-24, draft 2).

## Goal

Lay out a business card using the approved logo and the brand's contact/service info.

## Inputs

- Approved logo files (from Stage 4): the logo with slogan for the front, the reversed logo for dark backgrounds
- Contact info (phone, email, address, website) from intake, confirmed by Hafsa
- Tagline, services
- Brand colours (exact hex) and brand fonts from the logo stage

## Before Designing: Ask Hafsa

- **Personal name and title on the card, or a company card?**
- **Email and website:** only print them if the domain will be registered before printing.
- **Phone format:** Hafsa wants the international format, e.g. `+49 6301 252536`, with the leading 0 of the area code dropped.
- Confirm the format (default below).

## Default Print Spec (locked in 2026-09-24)

- **Size:** 85×55 mm (German standard), 2 sides
- **Bleed:** 2 mm on each side (canvas 89×59 mm). Background and stripes run into the bleed.
- **Safe margin:** 4 mm inside the trim for all text and logos
- **Text:** outlined to vector (no fonts needed at the printer), 7.5 pt minimum, larger for older audiences
- **Output:** 2-page print PDF (front and back), plus trimmed PNG previews
- **Colour:** the PDF is RGB. Tell Hafsa to order a proof or convert to the printer's CMYK profile.

## Steps

1. Draft the card copy from the confirmed inputs. **Never invent contact details.** If something is missing, stop and ask.
2. Build the card with the card generator (`equipment/make_business_card.py`). It embeds the approved logo SVGs, outlines the text and checks that everything sits inside the safe area.
3. Render and check the previews with the trim and safe lines drawn in. Fix any crowding or empty space before showing Hafsa.
4. Present the draft. Apply her changes one at a time ("change only X"), and archive rejected variants rather than deleting them.

## LauterMobil Reference Layout

- **Front:** white, centred logo with slogan, light-blue/green stripe along the bottom edge.
- **Back:** dark blue #043575, reversed logo, divider line, services with green bullets on the left, contact details right-aligned.

## Decision Point

Hafsa approves the card before it goes into the client package. If contact info is incomplete, stop at a draft and flag what's missing.

## Output

Print PDF (2 pages with bleed), front and back previews, front and back SVGs.

## Open Questions

- Decided 2026-09-24: the card should list the client's full service list, the same as the flyer. The back layout has to be redesigned to fit 8 services readably (LauterMobil card draft 3, pending).
*Resolved 2026-09-24: the card generator was promoted to `equipment/make_business_card.py`.*
