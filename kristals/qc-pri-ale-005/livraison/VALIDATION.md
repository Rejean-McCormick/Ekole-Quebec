# Delivery validation — `qc-pri-ale-005` (v1.2 delta)

**Scope:** Exactly one Kristal, `qc-pri-ale-005`. Root path: `kristals/qc-pri-ale-005/`. This package replaces only `authoring/PARCOURS.md` and `authoring/CONTRAT_PEDAGOGIQUE.json`; the other 12 files are additions. No workspace-level file or other Kristal is included.

## Technical check protocol and recorded run

1. Source archive opened; four authoring sources, four governance texts, and relevant frozen graph entries read. YAML metadata is reproduced from the original without changing its field values. All original assessment-contract properties, including nested existing fields, remain unchanged; additional generator fields are added to the existing family.
2. Filetree: **14 nonempty files** total, all underneath `kristals/qc-pri-ale-005/`, without an envelope folder, forbidden path traversal, unexpected entries or a second Kristal.
3. JSON: strict parsing of contract, bank, manifest; complete item schema and unique sequential identifiers `q-001` through `q-012`; all items target `obj-1`, `crit-1`, `qc-pri-ale-005-ev-01`.
4. Answer keys: line-numbered evidence excerpts and every detail's short supporting quotation are mechanically checked as verbatim substrings of the **matching** source line. Note: semantic suitability of a paraphrase still needs human review.
5. Two distinct independent mastery sources: `q-011` (museum) and `q-012` (story trail); source text hashes differ and their independent task settings are explicit.
6. Presence of 12 separately numbered sections, complete learning sequence, initial and faded support, four independent practices, two transfers, feedback and accessibility accommodations.
7. Rights/provenance: records original authored fictional stimuli; absence of media/external copied passages in package. No reverse plagiarism scan or legal rights clearance claimed.
8. Archive is reopened after creation for path, CRC, JSON parse, manifest equality, no traversal, nonempty content and first ZIP member requirements.

## Results of executed checks

On the complete archive, the independent automated test suite completed **846 assertions without failure**: 89 ZIP-path/integrity, 34 content presence/structure, 10 authoring/YAML, 100 preservation/extension of the original assessment contract, 5 graph/source cross-checks, 5 manifest, 359 assessment-bank schema/data, 216 answer-key/source-quote checks, 6 separate mastery-context, and 22 plan/rubric/reference-link checks. The checker verified **36 exact source-supported short quotations** (2 supporting details plus 1 evidence excerpt per item), without treating their pedagogical interpretation as machine-proven. All 12 items have unique sequential IDs and allowed modes; the two protected independent contexts have different texts. The final ZIP was reopened and passed CRC, membership, JSON-parsing and file-path tests. No learner study or actual LMS merge was performed.

## Outcome and limitations

**The checks do not qualify the lesson as published or certified.** A human must still judge semantic reliability of responses, grammar/register, pupil reading level, ambiguous alternate answers, local assessment fairness, and accessible delivery (including screen reader and neutral read-aloud). No field test with learners or live LMS merge was carried out.

## Suggested future structure changes (proposals only — not made)

- Consider a source-locator schema for locked corpus stimuli to keep student-facing texts and assessor-only keys in different access channels.
- Consider separate metadata recording human reviewer/date, accommodations used and failed-pass re-test source ID, all outside protected core IDs.
- Consider versioned rubric calibration and passage readability pilot results in runtime or an adapter, not in the canonical v1.2 register without governance approval.

**No change** to `kristal.workspace.json`, `AGENTS.md`, `authoring/ALIGNEMENT.md`, `registry/`, `governance/`, `canon/`, `state/`, `runtime/` or other Kristals.
