# Sub-Blueprint: 03 — Trademark Clearance

*Part of [pipeline-brand-strategy.md](../pipeline-brand-strategy.md). Read the global orchestrator first.*

**Status:** v0.2: validated on the MedPfalz Mobil run (2026-09-23).

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

No script yet. The method below is free.

1. **TMview API** (EU joint database: DE national, EUIPO, WIPO international):
   `POST https://www.tmdn.org/tmview/api/search/results?translate=false`
   Body: `{"page":"1","pageSize":"100","criteria":"C","basicSearch":"<term>","fOffices":["DE","EM","WO"]}`
   Send browser-style `User-Agent`, `Origin: https://www.tmdn.org` and `Referer: https://www.tmdn.org/tmview/` headers. Use Python (not Git Bash curl) for umlauts. Sanity-check against a known mark first (e.g. "viamedgo").
2. Focus on the relevant Nice classes. For patient transport those are **39** (transport) and **44** (medical/care services).
3. **North Data** (`https://www.northdata.de/<term>`) for companies trading under the name without a registered mark.
4. **Web search** for real-world use in the region and a view of local competitors.
5. The DPMAregister web form does **not** work for automated search (session-based). Use TMview, which includes DE marks.

This is a screening, not a legal clearance. Before print or filing, the final safeguard is a lawyer check or a formal DPMA application in the relevant classes.

## Open Questions

- Whether Pipeline Branding offers DPMA filing as part of the package, or only recommends it.

*Resolved 2026-09-23: trademark search tool (see Equipment above).*
