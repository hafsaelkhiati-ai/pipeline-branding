# Sub-Blueprint: 04 — Logo

*Part of [pipeline-brand-strategy.md](../pipeline-brand-strategy.md). Read the global orchestrator first.*

**Status:** v0.3: validated on LauterMobil (logo signed off 2026-09-24 after 3 Canva rounds and an exact vector rebuild).

## Goal

Produce an approved logo consistent with the brand's values, tagline, and audience, using the final name chosen at the Name Selection Gate.

## Inputs

- Final approved name (from the Name Selection Gate)
- Brand Values, Tagline, Target Audience, Industry (from intake)
- Any brand direction already given (colors, style references) — ask if none exists

## Steps

0. **Ask Hafsa about direction before generating anything.** The LauterMobil run needed 3 rounds because the direction wasn't pinned down first. Ask:
   - Style: warm and human, or premium and professional
   - Symbol type: monogram, minimal object, abstract mark, or illustration
   - Brand colours as exact hex codes
   - Typeface style
   - How the service should come across (in the symbol, or through the descriptor)
   - Slogan: part of the logo, a separate version, or not in the logo
1. Draft a short creative brief from the intake fields plus those answers: what the logo needs to communicate and to whom. Include the don'ts for the industry. For patient transport: no red cross (legally protected in Germany), no star of life, no ambulance or siren imagery.
2. **Explore concepts in Canva AI** (Canva MCP `create-design`, format "Logo"). Send 2 differently briefed proposals in parallel. Ask for page 1 = logo and page 2 = logo + slogan. Spell all text exactly in the brief. Export PNGs to `logo/` in the project folder and review them before showing Hafsa.
3. Present the proposals to Hafsa. Logo selection is her decision, never made unilaterally.
4. **Build the vector master as an exact reproduction of the design Hafsa picked.** Don't reinterpret it. The first LauterMobil redraw changed the M shape, the colours and the fonts, and was rejected.
   - Read the Canva design (`read-design` with a transaction, then cancel) to get the element types, font sizes and letter spacing.
   - **Symbol:** Canva embeds it as an image, so measure its geometry edge by edge from the exported PNG and rebuild it as clean shapes.
   - **Lettering:** try matching free fonts by pixel overlap first. If none matches (Canva often uses its own typefaces), trace the letters from the PNG with potrace.
   - Apply only the changes Hafsa asked for (e.g. her exact hex codes).
   - **Verify before presenting:** render at the reference's scale and check pixel overlap per layer (target ≥ 94%), plus a visual overlay image.
   - **Variants:** logo, logo + slogan, icon, reversed versions for dark backgrounds, single-colour. Export as SVG, transparent PNG (3600 px) and vector PDF.
5. Hafsa signs off a specific file. For LauterMobil that's `logo/final/logo-with-slogan.svg`. Later colour experiments get archived if she reverts.

## Known Limits of Canva AI (learned 2026-09-23)

- **It doesn't apply exact hex codes.** The symbol is an AI-generated image, so colours come out close but not exact (e.g. #113C76 instead of #043575). The layout AI also chooses its own text colours.
- **It ignores "identical on both pages".** The slogan page gets a different design every time.
- **Its output is raster, not vector.** Fine for card and flyer mock-ups. Car-door and large signage need a vector.
- Text elements *can* be corrected exactly afterwards with `edit-design` (e.g. to remove stray punctuation or fix colours).

## Decision Point

Hafsa approves the final logo before Stage 5 (Business Card) starts. Do not proceed to layout work on an unapproved logo.

## Output

Final logo file(s) — vector/high-res export, plus any color/format variants needed for print use.

## Equipment

None yet.

## Open Questions

- Promote the rebuild scripts (`.tmp/logo-generator/build_exact_logo.py`: measuring, tracing and verifying) to Equipment. Needs approval.

*Resolved 2026-09-24: export formats (SVG + transparent PNG 3600 px + vector PDF, 6 variants) and the vector tool (a hand-built SVG that reproduces the chosen design exactly).*
