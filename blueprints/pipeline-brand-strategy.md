# Blueprint: Pipeline Brand Strategy (Global Orchestrator)

*Read this before every run. This is the hub — each stage's actual how-to lives in its own sub-blueprint under `blueprints/pipeline-brand-strategy/`.*

**Status:** v0.2 — Draft, unvalidated. Structure covers all 7 stages; several stages have open tool/spec decisions (see each sub-blueprint's Open Questions). First live run in progress: MedPfalz Mobil.
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
