# Blueprint: Pipeline Brand Strategy (Global Orchestrator)

*Read this before every run. This is the hub — each stage's actual how-to lives in its own sub-blueprint under `blueprints/pipeline-brand-strategy/`.*

**Status:** v0.4. Stages 1–6 validated on the first live run (MedPfalz Mobil → LauterMobil). Stage 7 (Visual Consistency) is next.
**Owner:** Hafsa
**Replaces:** Manual process currently taking 1+ week per client.

---

## Trigger

Hafsa hands over a new project idea — a client or product that needs a full brand identity built.

## Required Inputs (intake checklist)

Before Stage 1 can start, collect:

| Field | Description |
|---|---|
| Industry | What the business does |
| Target Audience | Who the brand serves |
| Brand Values | The qualities the brand should communicate |
| Tagline | If one exists already, or leave blank for Stage 1 to help shape |
| Services | What's being offered — feeds flyer/business card content |
| Location | Where the business operates — informs domain TLD and local-market fit |
| Contact | Phone/email/address, as much as the client has provided |
| Language Target | What language(s) the name and copy should read naturally in |

This checklist was standardized from the MedPfalz Mobil intake brief (see `live/pipeline-branding/projects/medpfalz-mobil/status.md`).

If any field is missing, stop and ask — do not assume industry, audience, or a name candidate.

## Per-Project Tracking

Every project gets its own status file at `live/pipeline-branding/projects/<slug>/status.md`, created from `templates/pipeline-project-status.md`. That file is the single source of truth for which stage a project is at, what's been decided, and what's still open. Update it after every stage, not just at the end.

---

## The 7-Stage Sequence

| # | Stage | Sub-blueprint | Gate before moving on |
|---|---|---|---|
| 1 | Name | [01-name.md](pipeline-brand-strategy/01-name.md) | Produces 2–4 candidates |
| 2 | Domain | [02-domain.md](pipeline-brand-strategy/02-domain.md) | Checks each candidate |
| 3 | Trademark Clearance | [03-trademark-clearance.md](pipeline-brand-strategy/03-trademark-clearance.md) | Checks each candidate |
| — | **Name Selection Gate** | — | Hafsa picks the final name from candidates that passed Domain + Trademark. Owner-authority decision — never resolved unilaterally. If every candidate is blocked/high-risk, go back to Stage 1. |
| 4 | Logo | [04-logo.md](pipeline-brand-strategy/04-logo.md) | Logo approved before Stage 5 starts |
| 5 | Business Card | [05-business-card.md](pipeline-brand-strategy/05-business-card.md) | Uses approved logo |
| 6 | Flyer | [06-flyer.md](pipeline-brand-strategy/06-flyer.md) | Uses approved logo |
| 7 | Visual Consistency | [07-visual-consistency.md](pipeline-brand-strategy/07-visual-consistency.md) | Sign-off before client delivery |

**Dependency note:** Stages 2 and 3 both run against every candidate Stage 1 produces (not just one) — the Name Selection Gate needs comparative results to pick from, not a single pre-approved option.

---

## Escalation / Owner-Authority Points

Per `.claude/rules/permissions.md`, always stop and confirm before:
- Proceeding with a name that shows trademark/domain risk
- Sending any draft to a client
- Publishing anything publicly
- Making an API call or connecting an MCP/tool (once tools are picked for Stages 2–6)

## Change Log

- 2026-09-22 — v0.1 created. Single-file draft, structure only, stages 2–5 all TBD.
- 2026-09-22 — v0.2: restructured into this global orchestrator + 7 sub-blueprints, following a grill-me session with Hafsa. Received the MedPfalz Mobil pilot case (a real pending client — Non-emergency patient transportation, Katzweiler, Germany) and used it to standardize the intake checklist above and seed the first live project. Locked in: Canva + ChatGPT + Gemini for Stages 4–6 (no Adobe); domain/trademark tools stay open pending the live run; Stage 7 uses a manual checklist, not an undefined method.
- 2026-09-23: v0.3. First live run of Stages 1–4 (MedPfalz Mobil, final name **LauterMobil**).
  - 01–03 validated.
  - 01 gained an audience connotation check and industry naming rules (Krankenfahrten, never Krankentransport).
  - 02 and 03 now record the free tools that worked: Vercel + RDAP for domains; TMview API + North Data + web search for trademarks.
  - 04 now starts with a direction interview, uses Canva AI to explore concepts, and records Canva AI's limits (no exact hex codes, inconsistent pages, raster only), so the final logo is a vector master.
  - ChatGPT and Gemini aren't connected. Canva (connected MCP) is the working tool for Stages 4–6.
- 2026-09-24: v0.4. LauterMobil Stages 4–6.
  - **04:** the vector master must *reproduce* the approved design exactly (measure the symbol, trace the lettering, verify by pixel overlap). The first reinterpretation was rejected.
  - **05:** print spec locked in (85×55 mm, 2 sides, 2 mm bleed, 4 mm safe margin, outlined text, PDF). Ask about a personal name, and whether the email and website domain will be registered before print. Phone in +49 format. Card approved.
  - **06:** print spec locked in (A5, 2 sides, 2 mm bleed, 6 mm safe margin). Free stock photos failed; photos are now AI-generated to Hafsa's brief with Canva `generate-image` and validated one by one before layout. Ask for the client's full service list and only print facts she confirms.
  - Layout for 05 and 06 is built with generator scripts (promoted to `equipment/` on 2026-09-24) instead of Canva layouts, so the logo, colours and text stay exact.
