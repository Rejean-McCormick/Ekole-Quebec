# Assessment plan — `qc-pri-ale-002` | Phonics et décodage

**Binding for every item below:** `obj-1` (Apply English letter–sound correspondences to decoding); `crit-1` (Read new regular words and identify the cue); family `qc-pri-ale-002-ev-01`; native mode **réponse_argumentée**, implemented as **fixed** controlled text stimuli (`mode=fixe`) with spoken reading plus evidence. No probabilistic generation, no free-form AI adjudicator, no seed for fixed items.

## Controlled progression, representation and coverage

| Full item ID | Difficulty | Locked printed stimulus | Representation and evidence expected | Use |
|---|---|---|---|---|
| `qc-pri-ale-002-q-001` | initial | `map` | CVC oral reading + m/a/p clue | formative |
| `qc-pri-ale-002-q-002` | initial | `bed` | e /ɛ/ clue, CVC blending | formative |
| `qc-pri-ale-002-q-003` | initial | `cash` | three grapheme boxes `c|a|sh`, final digraph | formative |
| `qc-pri-ale-002-q-004` | intermediate | `chin` | `ch` one consonant phoneme and read word | formative |
| `qc-pri-ale-002-q-005` | intermediate | `sit/set` | distinct short middle vowel graphemes | formative |
| `qc-pri-ale-002-q-006` | intermediate | `slip` | consonant cluster sl versus digraph sh | formative |
| `qc-pri-ale-002-q-007` | intermediate | `pet/fish` | two readings, e and sh printed evidence | formative |
| `qc-pri-ale-002-q-008` | transfert | `mud/chat` | transfer to story labels with u and ch clue | practice transfer |
| `qc-pri-ale-002-q-009` | transfert | `hen/pin/rug/shed` | **Mastery A**: journal labels, 4 novel printed words, 4 clues; sh target | decision evidence A |
| `qc-pri-ale-002-q-010` | transfert | `web/fin/mug/chip` | **Mastery B**: workshop labels, 4 distinct novel printed words, 4 clues; ch target | decision evidence B |

Every item has a complete `reponse_attendue`, exact correspondence criteria, a distinct descriptive correction, a specified difficulty and `validation_status=a_revoir` in `BANQUE_ITEMS.json`. Phoneme symbols in answers are for adult evaluators; students never need to write IPA.

## Administration: two independent proofs

**A:** fictional discovery journal (item 009). **B:** fictional makers’ workshop (item 010). Give the actual printed word cards only at assessment time; do **not** show them as examples or on practice sheets beforehand. The contexts motivate different reading tasks but contain **no illustrative answer**. Collect per-word printed spelling, actual first spoken reading (or an authorized phoneme-sound output), the grapheme pointed to/named, sound claimed, cue source, amount of help, and a neutral note on articulation/access.

**Criteria independently required for A and B:** ≥3/4 words decoded, ≥3/4 valid clues, accurate identification *and reading* of the distinctive digraph (`sh` in A; `ch` in B), voluntary sound blending without giving the printed word or its phonemes as prompts. Single wrong word cannot be offset by high scores on a different context; all five mastery dimensions must be considered on **each** proof. Decision grid: `evaluation/GRILLE_MAITRISE.md`.

## Variation, limits and accessibility

- **Permitted:** print size, card size, order of presentation, response tempo, pointer/tactile support that does not encode answers, usual hearing accommodations, or a pre-reviewed phoneme selection/output aid on which the pupil constructs the sounds sequentially.
- **Not permitted:** substituting words, presenting a printed illustration that reveals meaning, reading printed words aloud for the pupil, using text-to-speech to pronounce a whole target word, assigning a random generated list, or judging by familiar sentence context.
- English phonemic cues must be verified against the controlled word forms. Dialectal variations and speech-production/access difficulties must not be conflated with grapheme mapping errors. The pupil may indicate the clue in English, in French, by a sign/pointer, or by an approved device; the **English decoding** remains the target.
- No camera, audio recording, copyrighted worksheet or external image is required. A teacher may note observed reading on a protected sheet only.

## Status and review limitations

This is an editorially prepared local test bank, not a certified test or proof of psychometric validity. Human review is required for English dialect acceptability, hearing/speech access equivalence, the 3-of-4 threshold, rubrics, and classroom administration. The two proofs are scored by humans with the locked answer bank, not a generative model.
