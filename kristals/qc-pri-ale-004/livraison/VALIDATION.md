# Validation / livraison — qc-pri-ale-004 v1.2

**Scope:** this single Kristal only. **Technical status:** scripted checks executed; pedagogical and accessibility review pending. **Not a certified, officially approved or published course.**

## Input and changes

The provided archive contained a nested v1.2 frame with governing files, registry and required authoring files. The original `authoring/PARCOURS.md` YAML header is retained verbatim, followed by twelve authored sections. The original `CONTRAT_PEDAGOGIQUE.json` values (IDs, title-related goal, concepts, evidence, graph links, family) and native structure are preserved, with additional controlled-family parameters and a candidate status. The other 12 files listed in `MANIFEST.json` are new. The delta does not include nor modify registry, governance, ALIGNEMENT, BRIEF, workspace manifest or other Kristals.

## Technical checks actually performed

**Actual execution (local automated checks):** `python /mnt/data/ale004_work/check.py` completed **439/439 checks**, with 0 failures before packaging. Following ZIP creation, `python /mnt/data/ale004_work/check.py /mnt/data/qc-pri-ale-004_livraison_v1.2.zip` completed **473/473 checks**, 0 failures, including **34 ZIP-specific checks**. Tested: exact source YAML-header preservation, 12 sections, original JSON fields/immutable data and evaluation family, strict JSON parsing, unique sequential 12-item IDs, fixed stimuli with ≥50 words each, quote occurrence in the actual item passage, unique story texts, mastery proof items `q-011` and `q-012` in distinct contexts, file cross-references, exactly 14 nonempty safe relative paths, ZIP CRC integrity, and byte-for-byte extraction simulation. These are reproducible script checks, not an independent qualified language assessment.

**Test limits:** a quotation found inside a story is mechanically verified, but its appropriateness as *evidence* and the correctness of an open-ended model summary still require a human reviewer; no automated semantic correctness claim, classroom pilot or screen-reader application test was performed.

## Limitations / human sign-off still needed

1. English-language review: check meaning, syntax, idiom, age range, vocabulary load, possible ambiguities and source-to-rubric consistency on every independent story.
2. Human review of correctness of model summaries and alternative legitimate answers; a script's quotation-presence check is *not* sufficient proof of narrative interpretation.
3. Accessibility test with actual LMS and assistive technology (screen reader, text reflow, oral/verbatim scribing logistics), and fair comparison of supported versus independent reading.
4. Learner piloting and response-based rubric calibration; no reliability estimates, psychometrics, or certification have been produced.
5. Clarify the source YAML field `langue_contenu: fr-CA`: retained *unchanged* for strict metadata preservation, while this English teaching leaf has English learner-facing material. **Proposed schema change only**: support separate `langue_interface` and `langue_enseignement` or a versioned override after central approval.
6. Original fictional texts require normal deployment review; no third-party rights grants or externally verified literature claims are made.

## Proposed governance follow-up (not applied)

- Version and centrally approve any language-metadata adjustment if the platform renders language choice from the preserved YAML `fr-CA` field.
- Define metadata for human-reviewed alternative model answers, reading modality and accommodations to prevent automatically conflating audio comprehension with autonomous reading.
- Establish calibration and human review workflow before changing any `validation_status` from `a_revoir`.

## Completion criteria

Technical checks + actual ZIP extraction + qualified language/editorial and accessibility approval + two real independent learner demonstrations are separate milestones. This delivery completes **only authored candidate material and local mechanical checks**.
