# Session State

*Updated at the end of each session. Read this FIRST on startup.*

## Last Session
- **Date:** 2026-09-24
- **Summary:** LauterMobil (MedPfalz Mobil) run, Stages 4–6. **Logo, business card and flyer are all approved.**
  - **Logo:** Hafsa's Canva pick rebuilt exactly as a vector (monogram measured, lettering traced, her colours #043575 / #2F8D27 / #0C75CB). Approved file: `logo/final/logo-with-slogan.svg`. The name stays one colour.
  - **Business card (draft 2):** 85×55 mm, 2 sides, Tel. +49 6301 252536, info@lautermobil.de, lautermobil.de, Kurpfalzstr. 3, 67734 Katzweiler.
  - **Flyer (draft 1):** A5, 2 sides, 4 AI photos made to Hafsa's brief (white VW Caddy Maxi, casual helpers, manual wheelchair ramp), all 8 LM services, 24/7, health-insurer billing, wheelchair-accessible vehicles, Katzweiler und Umgebung.
  - **Blueprints v0.4:** 04 exact-reproduction rule; 05 and 06 print-spec defaults; 06 AI-photo workflow.
  - **Equipment created** (Hafsa approved): `equipment/` has `trademark_check_tmview.py`, `build_exact_logo.py`, `make_business_card.py`, `make_flyer.py`, open-licence fonts and a README. Verified: rebuilt outputs match the approved files (1 pixel in 1.26 million differs, from edge smoothing).

## Open Tasks
- **Business card draft 3 (next session):** Hafsa approved listing all 8 services on the card. The back needs a redesign to fit them readably, then show her. Draft 2 stays the approved card until then.
- **Stage 7 (Visual Consistency):** run the checklist across logo, card and flyer, then Hafsa's final sign-off.
- **Register lautermobil.de before any print.** "Approve all" wasn't treated as a purchase go-ahead. It needs an explicit "buy it" plus the owner (Hafsa or client).
- **PDFs are RGB.** Order a proof or convert to the printer's CMYK profile.
- Consider a DPMA trademark filing for LauterMobil (classes 39 + 44).
- **Housekeeping:**
  - An empty `flyer/photo-candidates` folder was locked by Windows. Remove it.
  - The scratch Canva design "LauterMobil Flyer-Fotos (AI, zur Freigabe)" (DAHWJU113PU) holds the 4 photos.
  - The GitHub repo is public (Hafsa chose to keep it). Stock photos are gitignored.

## Current Priorities
- Build the Pipeline Branding automated pipeline itself
- Finish LauterMobil (card draft 3 → Stage 7 sign-off → client package), then generalise the Equipment for the next client

## Active Projects
- Pipeline Branding: active. This is both the business and the current build.
- MedPfalz Mobil → **LauterMobil**: active, first client run. Stages 1–6 done and approved; card draft 3 and Stage 7 remain.
