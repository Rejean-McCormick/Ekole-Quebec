# Delivery validation — qc-pri-ale-008 v1.2

**Scope:** Delta overlay only; exactly 14 files all under `kristals/qc-pri-ale-008/`. Two full authoring replacements preserve immutable v1.2 fields; the other 12 files are additions. Status: *technical prechecks; independent human/editorial review outstanding*. No school-program approval or certification claimed.

## Executed controls

The separate QA script reports **465/465 successful assertions** on the final package (before this small metadata-conservation edit, then re-executed): 14 exact nonempty files; first path and all paths correctly rooted; no `..` traversal, absolute path or wrapping folder; JSON parseable; YAML front matter parseable with exactly 12 numbered sections; frozen objective, proof, zero blocking prerequisites, family ID, and canonical keys compared against the source; 12 unique numbered bank items with all mandated fields, two meaningful evidence contexts and explicit target-specific keys; corpus has no duplicated target terms among bank items; checking that reference quotes actually appear in their corresponding sentences; integration overlay leaves unrelated workspace source files unchanged. The script also checks the listed paths against the manifest.

**No claim** of running a learner pilot, testing a live LMS, automated psychometric calibration, exhaustive linguistic fact-checking or human comprehension trial. Automated checks cannot determine whether all synonyms, difficulty classifications or accessibility accommodations are pedagogically optimal.

## Human reviews needed

1. Independent native-level English editorial review of all 24 scored word explanations and contextual evidence, especially less literal derived meanings such as *thoughtless*, *restless*, and *unpredictable*.
2. Learner trials for sentence readability, age suitability, teacher/scorer agreement, time and any cultural bias; revisit the strict two-evidence threshold after piloting without silently changing frozen objective or IDs.
3. Accessibility testing in the actual LMS: screen-reader reading order, audio/scribe conditions without revealing assessed morphemes, alternate output mode consistency.
4. Local sign-off for scoring open-response synonyms; do not delegate mastery solely to a free generative AI evaluator.

## Remaining limits and suggestions (no base files changed)

- The inherited YAML value `langue_contenu: fr-CA` is preserved exactly as source metadata even though the learner-facing lesson language is English. If a system-level localization policy needs it changed, propose that change through central governance rather than silently altering the canonical frame.
- A future **central** schema revision could standardize target-by-target meaning/morpheme/context score records, a mode code for fixed *argumented-response* tasks, and evidence context IDs across the 202 Kristals. This delivery makes **no** edits to `registry/`, `governance/`, `canon/`, `docs/`, `runtime/`, `state/` or any other Kristal.
- Suggested editorial process: create a new controlled replacement if an item is ambiguous; version and review the correction before administration. Current item `validation_status` remains `a_revoir`.

## Merge instructions

Unpack master `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip`; **enter** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` then extract `qc-pri-ale-008_livraison_v1.2.zip` at that level. Expect precisely the two authoring replacements and 12 additions. This ZIP must never be extracted one directory higher.
