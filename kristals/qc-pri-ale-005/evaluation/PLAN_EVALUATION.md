# Assessment plan — `qc-pri-ale-005`

**Identity:** `obj-1` — Repérer et organiser les informations d’un texte informatif en anglais.  
**Criterion:** `crit-1` — Créer une fiche de synthèse d’un document nouveau.  
**Family:** `qc-pri-ale-005-ev-01` (`réponse_argumentée`, fixed source and analytically scored response).  
**Source:** Original fictional English mini-passages in `evaluation/BANQUE_ITEMS.json` only; not real-world school or park claims. Item status: `a_revoir`.

## Blueprint, coverage and administration

The 12 items cover notices, maps, schedules, procedural explanations, short reports, leaflets and informational panels. Questions vary in wording but all require selecting and organizing **source-based English information**. Q001–Q004 = initial; Q005–Q008 = intermediate; Q009–Q012 = transfer. Q011/Q012 are **protected, separately administered** independent mastery contexts, not teaching exemplars. All 12 map to `obj-1` / `crit-1` / `qc-pri-ale-005-ev-01` and use the same four score dimensions.

| Item | Difficulty | Primary representation | Use |
|---|---|---|---|
| `qc-pri-ale-005-q-001` | `initial` | notice | formative |
| `qc-pri-ale-005-q-002` | `initial` | information card | formative |
| `qc-pri-ale-005-q-003` | `initial` | information notice | formative |
| `qc-pri-ale-005-q-004` | `initial` | instructional information | formative |
| `qc-pri-ale-005-q-005` | `intermediaire` | explanatory report | formative |
| `qc-pri-ale-005-q-006` | `intermediaire` | display report | formative |
| `qc-pri-ale-005-q-007` | `intermediaire` | project explanation | formative |
| `qc-pri-ale-005-q-008` | `intermediaire` | procedural notice | formative |
| `qc-pri-ale-005-q-009` | `transfert` | visitor leaflet | formative |
| `qc-pri-ale-005-q-010` | `transfert` | event guide | formative |
| `qc-pri-ale-005-q-011` | `transfert` | museum workshop report | preuve protégée |
| `qc-pri-ale-005-q-012` | `transfert` | public information notice | preuve protégée |

## Expected response / correction

For each item, the scorer receives the **full original passage** with numbered sentences, a proposed fact sheet, an analytic rubric and a structured answer key containing two distinct details plus locatable short quotations. Do not demand verbatim reproduction: an accurate paraphrase supported by the source is equally correct. Scoring is on **main idea, two relevant details, locatable evidence and organized fact-sheet structure**, not vague fluency impressions or pupil background knowledge. See `evaluation/GRILLE_MAITRISE.md`.

## Fixed family and bounded variation

- Items Q001–Q010: `mode=fixe`, no parameters, no seed and **no passage substitution**.
- Q011–Q012: `mode=scenario_controle`, with exactly **one locked, enumerated scenario each**, specified in `parametres.sources_autorisees`. Their stable seed is an archive identifier, **not** a license for random text production. No automated variation of facts, source or answer.
- A future replacement passage requires separate human-approved source, hand-checked answer/rubric, explicit versioned registry and test; **none** is packaged. Do not present a free AI-generated sentence as independently validated evidence.
- Accept multiple semantically equivalent English summaries under the same rubric. Any unsupported factual addition is marked for correction even when plausible.

## Mastery criteria, settings, fairness

1. Administer **Q011, then Q012 on a separate occasion** under comparable access supports, after teaching. Do not expose source passages or answer keys in student lesson pages.
2. For both independently written/dictated fact sheets, require a score of **2/2 in each of four criteria** (8/8) from the analytic rubric, and no content-specific adult prompts. A single high mark never establishes mastery.
3. If one context falls below threshold, remediate that particular skill and reassess using a **new human-reviewed unseen source**; repeating a now-familiar item does not produce a second independent proof.
4. Student access: selectable text, sentence-numbered large print, neutral audio or read-aloud, assistive typing/dictation; no source translation, preselected central idea or teacher-chosen evidence. Track accommodations confidentially outside the Kristal.
5. Neither reading speed, accent, spelling-only differences, personal circumstances, technology access nor morphology is a criterion. The passage itself contains sufficient information; no cultural trivia is required.
6. All sources are fictional and contain no unsafe procedures or sensitive personal information. A qualified human should still pilot reading level, fairness, accuracy and feedback before release.

## Sampling and practical limits

A routine formative session may sample one short source from each difficulty band to guide instruction; those responses are **not** a substitute for the two protected source-specific fact sheets. The present 12-item bank is a controlled draft; no external corpus validation, learner trial, bias study, or human certification has been completed.
