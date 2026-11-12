# Assessment plan — qc-pri-ale-008

**Immutable mapping:** `obj-1` = Déduire le sens de mots anglais en utilisant contexte et morphologie. **`crit-1`** = Expliquer le sens de mots nouveaux dans deux phrases. **Family:** `qc-pri-ale-008-ev-01` (preferred `réponse_argumentée`). **Bank:** `evaluation/BANQUE_ITEMS.json` (12 controlled, FIXED items). Every row below is explicitly linked to the same `obj-1`, `crit-1` and family; no item tests oral accent or grammatical terminology alone.

## Blueprint and coverage

| Item (obj-1 / crit-1 / qc-pri-ale-008-ev-01) | Difficulty | Context | Target words | Representation | Use |
|---|---|---|---|---|---|
| `qc-pri-ale-008-q-001` | initial | Sports and reuse | unfair, reuse | Two English sentences; written/typed/dictated reasons | `formative` |
| `qc-pri-ale-008-q-002` | initial | Conversation and plans | thoughtless, hopeful | Two English sentences; written/typed/dictated reasons | `formative` |
| `qc-pri-ale-008-q-003` | initial | School teamwork | disagree, helpful | Two English sentences; written/typed/dictated reasons | `formative` |
| `qc-pri-ale-008-q-004` | intermediaire | Home and drawing | misplaced, colorless | Two English sentences; written/typed/dictated reasons | `formative` |
| `qc-pri-ale-008-q-005` | intermediaire | Letters and repair | unkind, rebuild | Two English sentences; written/typed/dictated reasons | `formative` |
| `qc-pri-ale-008-q-006` | intermediaire | Clinic and gallery | painless, preview | Two English sentences; written/typed/dictated reasons | `formative` |
| `qc-pri-ale-008-q-007` | intermediaire | Birds and a long bus ride | unusual, restless | Two English sentences; written/typed/dictated reasons | `formative` |
| `qc-pri-ale-008-q-008` | intermediaire | Gym and celebration | misjudged, joyful | Two English sentences; written/typed/dictated reasons | `formative` |
| `qc-pri-ale-008-q-009` | intermediaire | Arrival at camp | unpacked, safely | Two English sentences; written/typed/dictated reasons | `formative` |
| `qc-pri-ale-008-q-010` | transfert | Kitchen and friendship | overcook, friendship | Two English sentences; written/typed/dictated reasons | `formative` |
| `qc-pri-ale-008-q-011` | transfert | Community garden — independent evidence 1 | replant, unprotected | Two English sentences; written/typed/dictated reasons | `preuve 1` |
| `qc-pri-ale-008-q-012` | transfert | Weather science report — independent evidence 2 | unpredictable, refreeze | Two English sentences; written/typed/dictated reasons | `preuve 2` |

**Coverage:** prefix (`un-`, `re-`, `mis-`, `dis-`, `pre-`, `over-`), suffix (`-less`, `-ful`, `-ly`, `-ship`, `-able`), transparent roots, and local sentence-based evidence. Each item contains exactly two original English sentences and two distinct targets; the learner explains both. Items `q-011` and `q-012` are held back during lessons and are assessed as two different independent contexts. Do not use their answer key as scaffolding.

## Correction rule and distribution

For **each target**: accurate contextual sense = 2 (1 approximate/ambiguous, 0 inaccurate); valid meaningful word part with a correct role and recognizable base/root = 1; an accurately quoted relevant English context phrase explaining why the sense fits = 1. **Total 8 points per pair.** The full expected explanation for every item is stored in `reponse_attendue` and `rubrique`; the example words quoted there are not mandatory formulaic student wording. An otherwise correct synonym with supported evidence is allowed; a literal translation without both sources of evidence is insufficient.

**Difficulty:** initial 001–003, intermediate 004–009, transfer 010–012. This is planned editorial difficulty, not a calibrated psychometric value. For formative teaching, use 001–010 selectively; do not use the same pair unchanged after detailed solution feedback to declare independent mastery.

## Variation and generative safety

- All items use `mode: fixe`, `seed: null`, `parametres: null`. This deliberately constrains the requested `réponse_argumentée`: the evidence is open-response, **not** uncontrolled item generation.
- **Permitted only in responses:** semantically equivalent English explanations and a different correctly quoted clue actually in the sentence, judged by the same rubric. Presentation accommodations (font, line breaks, response modality) may change without rewriting either text.
- **Not permitted:** automatic sentence swaps, invented word derivations, free-form AI scoring as the sole judge, changed targets, or unverified new contexts. A new version requires a new human-reviewed item with fresh keys.
- Neutral accessibility: text screen-reader friendly; teachers may provide print enlargements, audio rendering of the unchanged sentences if decoding is not targeted, and a neutral scribe for reasoning. Do not add definitions, translations or segmented morphemes in proof items.
- Safety/privacy: school-appropriate fictional situations only, no personal disclosures, stereotypes or sensitive data. No copyrighted stimuli reproduced.

## Two evidence decisions

1. `q-011` community garden: student independently explains **replant** and **unprotected**, with morphology and quoted clues.
2. `q-012` weather report: on another occasion or separate unseen passage, independently explains **unpredictable** and **refreeze**, with morphology and quoted clues.

Decision is based on **both** productions and qualitative errors, not an arithmetic average. A complete performance has correct context meanings and appropriate parts/evidence for BOTH targets in each context (4/4 per target pair, 8/8 per item). If either attempt misses an essential component, label “in development,” run targeted remediation and collect a new equivalent *human-reviewed* context before reconsidering. The rubric is strict by design and needs classroom piloting.

**Validation not claimed:** No learner trials, independent item editor review, or reliability calibration. Each JSON item remains `a_revoir` until a human has reviewed actual use.
