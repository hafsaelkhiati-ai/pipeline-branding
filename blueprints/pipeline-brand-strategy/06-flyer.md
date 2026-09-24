# Sub-Blueprint: 06 — Flyer

*Part of [pipeline-brand-strategy.md](../pipeline-brand-strategy.md). Read the global orchestrator first.*

**Status:** v0.2: first run on LauterMobil (draft 1 delivered 2026-09-24, waiting on approval).

## Goal

Lay out a flyer using the approved logo, brand assets, photos made to brief, and the client's full service list.

## Inputs

- Approved logo files (Stage 4) and the approved card (Stage 5) for consistency
- The client's full service list (ask for it. LauterMobil's full list of 8 only came in at this stage.)
- Contact info, tagline, target audience
- Facts the flyer may state. **Only what Hafsa confirms is true** (e.g. health-insurer billing, wheelchair-accessible vehicles, 24/7, service area). Never invent these.

## Before Designing: Ask Hafsa

- Format and sides (default below)
- Which facts may be stated, and the exact opening or booking hours
- Photo approach (see Photos)

## Default Print Spec (locked in 2026-09-24)

- **Size:** DIN A5 (148×210 mm), 2 sides, portrait
- **Bleed:** 2 mm (canvas 152×214 mm). Safe margin 6 mm inside the trim.
- **Text:** outlined to vector. Photos at ≥ 250 dpi.
- **Output:** 2-page print PDF, trimmed previews, front and back SVGs

## Photos (learned 2026-09-24)

- **Free stock didn't work** for a German local service. It looked American (shuttle vans, cones, badges), dated (COVID masks), wrong (ambulances) or generic.
- **What worked: AI photos generated to Hafsa's exact brief**, validated one by one before any layout:
  1. Look at a relevant competitor's site for the photo *style*. Never reuse their images.
  2. Agree the brief with Hafsa: number of photos, aspect ratio, vehicle make, model and colour (e.g. white VW Caddy Maxi, **no lettering**, since AI can't write logos), staff clothing, scenes, equipment details (e.g. manual wheelchair ramp, not an electric lift).
  3. Show her the prompts, then generate with Canva MCP `generate-image`. Every prompt includes "photorealistic, documentary style, natural daylight, German setting, no text, logos or lettering, no ambulance".
  4. **Full-resolution download:** the generated-image links are thumbnail-only. Put each image on a page of a scratch Canva design (a copy, never her real designs), then `export-design` as PNG.
  5. Check each photo at full size for AI errors (hands, faces, stray text, badges, vehicle geometry). Present them to Hafsa for approval.
- **Avoid** red cross, star of life, ambulance, blue lights and paramedics. These signal Krankentransport or emergency.

## Steps

1. Write the copy: headline, intro line, the services in scannable form, the approved facts, a call to action, contact details. Flag any wording you wrote yourself for Hafsa to check.
2. Build it with the flyer generator (`.tmp/logo-generator/make_flyer.py`, not yet Equipment): hero photo on the front, logo, headline, 3 key facts, a phone band; services, photo grid with captions, advantages and a contact band on the back.
3. Render with the trim and safe lines drawn in. Fix hidden text or unbalanced empty areas before presenting.
4. Present the draft for approval.

## Decision Point

Hafsa approves the flyer before it's added to the final client package. If required content is incomplete, stop and flag what's missing rather than inventing placeholder content.

## Output

Print PDF (A5, 2 pages, bleed), front and back previews, SVG sources, and approved photos in `flyer/photos-generated/`.

## Open Questions

- Promote `make_flyer.py` and the photo-export workflow to Equipment (needs approval).
