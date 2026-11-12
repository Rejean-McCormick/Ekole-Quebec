# Local v1.2 delivery validation — `qc-pri-ale-002`

**Scope:** exactly the 14 files listed in `MANIFEST.json`: full replacements of the existing `authoring/PARCOURS.md` and `authoring/CONTRAT_PEDAGOGIQUE.json` plus 12 new files, all owned by `kristals/qc-pri-ale-002/`. Technical checks were executed before packaging; see results below.

## Executed checks

- **563 Python assertions passed before packaging**, including 14-file scope, original unchanged YAML metadata and 12 numbered sections, unchanged native contract and family keys, registry links, bank item fields and identifiers, evaluation coverage, accessibility references and locked answer keys.
- Two distinct autonomous contexts were inspected and verified: A = `hen/pin/rug/shed`, B = `web/fin/mug/chip`. An independent table checked **8 pronunciations, 8 grapheme segmentations, 8 clues and 8 phonemic correspondences** plus a 1-to-1 grapheme/phoneme count.
- All six teaching content documents were scanned to ensure **no final-mastery words appear in teaching content**.
- Source overlay simulated: **2 native authoring replacements, 12 additions**; all other source-local files compared by SHA-256 and remained unchanged.
- Strict JSON parsing was successful for the contract, bank and manifest, and YAML frontmatter parsed and compared to the source. No parametric generators/AI grading are present.
- The archive was created **after** these checks; the packaging runner then checked file names, member count, JSON and CRC separately.
- These are **technical and bounded text checks**; classroom validity, accent acceptability and sound output accommodations have not been tested with actual pupils or independent human judges.

## Limitations unresolved after technical checks

- No teacher-led or pupil trial; the legitimacy of the four-word scale, mapping of speech variation, task difficulty and length still requires human validation.
- The eight mastery words are intended to be unseen; a real administering teacher must prevent premature disclosure and choose another independently reviewed set if these words were learned earlier.
- An access accommodation that turns printed words into pre-read audio would invalidate the target; equivalence of aided phoneme production requires human evaluation.
- No external audio is bundled; pronunciation guides are textual IPA and need a teacher with the required English phonemic competence. IPA itself is not expected from pupils.
- Neither the general bibliography nor an executable ZIP integrity check demonstrates a certified, approved or psychometrically standardised item bank.

## Human review before publishing

1. English literacy specialist: check all eight reserved pronunciations, vowel variants, sound-to-spelling mapping and lexical difficulty.
2. Accessibility / speech-language expert: ensure the decoding skill can be evidenced fairly in adapted response modes without a reader doing the job for a learner.
3. Classroom reviewer: rehearse instructions and assess scoring reproducibility across independent evaluators and contexts; protect the held-out word lists.
4. Rights/privacy steward: verify local handling of learner observations and downstream reuse, without unnecessary voice capture.

## Proposals for central schemas (not applied)

Propose optional standard fields `stimulus_holdout_group`, `pronunciation_variants_verified`, `access_equivalence_review` and `independent_evidence_count` for a future versioned item schema. This package **does not** modify any file in `governance/`, `registry/`, `canon/`, `state/`, `runtime/` or the workspaces of other Kristals.
