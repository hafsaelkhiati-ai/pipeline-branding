# Sub-Blueprint: 02 — Domain

*Part of [pipeline-brand-strategy.md](../pipeline-brand-strategy.md). Read the global orchestrator first.*

**Status:** v0.2: validated on the MedPfalz Mobil run (2026-09-23).

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

No script yet. The method below is free and read-only.

1. **Vercel MCP `get_bulk_availability`**: up to 50 domains per call. Check the plain, hyphenated and descriptor forms (e.g. `name.de`, `name.com`, `name-krankenfahrten.de`).
2. **Verify with registry RDAP** (404 = unregistered, 200 = taken):
   - `.de`: `https://rdap.denic.de/domain/<domain>`
   - `.com`: `https://rdap.verisign.com/com/v1/domain/<domain>`
3. Write umlauts as ae/oe/ue (e.g. `pfaelzer-geleit.de`).

**Never register or buy a domain without Hafsa's explicit go.** It's a purchase, and it's still open whether Hafsa or the client should own it.

## Open Questions

- Who owns and pays for the client's domain: Hafsa (bundled into the service) or the client directly? Decide per project until there's a standard.

*Resolved 2026-09-23: domain-check tool. Hafsa authorised running this stage on my own with free research tools.*
