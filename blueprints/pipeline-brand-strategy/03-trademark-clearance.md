# Sub-Blueprint: 03 — Trademark Clearance

*Part of [pipeline-brand-strategy.md](../pipeline-brand-strategy.md). Read the global orchestrator first.*

**Status:** Draft v0.1 — unvalidated until the MedPfalz Mobil run confirms it.

## Goal

Check rough trademark exposure for every name candidate from Stage 1, so the Name Selection Gate has real risk data, not a guess.

## Inputs

- 2–4 name candidates from Stage 1
- Industry (defines the relevant trademark class/category to search against)
- Location (defines which jurisdiction's registry matters most)

## Steps

1. For each candidate, search for existing marks in the same or adjacent industry/class, in the relevant jurisdiction.
2. Also do a basic web/social check for identical or near-identical brand usage in the same space — a mark doesn't have to be formally registered to be a real conflict risk.
3. Classify each candidate:
   - **Clear** — no meaningful conflicts found in the relevant class/jurisdiction
   - **Caution** — a similar mark exists but in a different class/market, or usage is weak/informal — flag it, don't auto-reject it
   - **Blocked** — an identical or near-identical registered mark exists in the same class/jurisdiction
4. Log the classification and what was found (even for Caution/Blocked) in the project status file.

## Decision Point

**Blocked candidates never proceed to the Name Selection Gate as a live option** — report them, don't recommend them. Caution-level candidates proceed but get flagged clearly, since choosing one is a risk call that belongs to Hafsa, not to be made unilaterally (per the decision tree — owner authority).

## Output

Clear/Caution/Blocked classification per candidate, with findings, logged in the project status file, feeding the Name Selection Gate.

## Equipment

None yet.

## Open Questions

- **Which trademark search tool/service to use** (e.g. a formal registry search like USPTO TESS / DPMA register for Germany, or a paid clearance service). Left open deliberately — no tool has been picked. Per `.claude/rules/permissions.md`, connecting any tool/MCP/API requires Hafsa's explicit approval before first use. Resolve this the first time this stage actually runs (MedPfalz Mobil).
