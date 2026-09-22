# Sub-Blueprint: 02 — Domain

*Part of [pipeline-brand-strategy.md](../pipeline-brand-strategy.md). Read the global orchestrator first.*

**Status:** Draft v0.1 — unvalidated until the MedPfalz Mobil run confirms it.

## Goal

Check domain availability for every name candidate from Stage 1, so the Name Selection Gate has real data to choose from.

## Inputs

- 2–4 name candidates from Stage 1
- Location / Language Target from the project intake (determines which locale TLD to check)

## Steps

1. For each candidate, check availability on:
   - The locale TLD implied by Location/Language Target (e.g. `.de` for a German-first, Germany-based brand)
   - `.com` as the default fallback
2. Record status per candidate: available / taken / taken-but-parked (worth a closer look) for each TLD checked.
3. Log results in the project status file next to each candidate.

## Decision Point

If a candidate is taken on both the locale TLD and `.com`, flag it as weak going into the Name Selection Gate — don't discard it outright, since Hafsa may still want it with a different TLD or a slight variation, but don't recommend it either.

## Output

Domain availability status per candidate, logged in the project status file, feeding the Name Selection Gate.

## Equipment

None yet.

## Open Questions

- **Which domain-check tool/service to use.** Left open deliberately — no registrar or WHOIS tool has been picked. Per `.claude/rules/permissions.md`, connecting any tool/MCP/API requires Hafsa's explicit approval before first use. Resolve this the first time this stage actually runs (MedPfalz Mobil).
