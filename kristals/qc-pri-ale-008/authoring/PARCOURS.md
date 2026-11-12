---
format: qc.learning-path/1.0
id: qc-pri-ale-008
titre: Vocabulaire et morphologie anglaise
discipline_code: ALE
statut: contenu_rédigé_à_revoir
revision_contenu: 0.3.0
langue_contenu: fr-CA
resultat_principal: Déduire le sens de mots anglais en utilisant contexte et morphologie.
objectifs_secondaires: []
criteres_reussite:
- Expliquer le sens de mots nouveaux dans deux phrases.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ale-008-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ale-008`

**Discipline (appellation québécoise) :** Anglais, langue d’enseignement  
**Intitulé éditorial :** Vocabulaire et morphologie anglaise  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** leçon et banque rédigées, contrôle technique effectué, validation linguistique et essai apprenant en attente. Les champs YAML canoniques initiaux sont conservés; seule la révision éditoriale et le statut de travail changent.

## 1. Intention et frontières

- `obj-1` — **Résultat vérifiable IMMUTABLE :** Déduire le sens de mots anglais en utilisant contexte et morphologie.
- `crit-1` — **Preuve autonome IMMUTABLE :** Expliquer le sens de mots nouveaux dans deux phrases.
- **Notions :** prefix, suffix, root, context. Le mot nouveau est toujours présenté dans une phrase anglaise entière; l'élève propose un sens plausible et justifie ce sens avec un élément du mot **et** un indice de la phrase. Le sens dépend de la situation, pas seulement de la découpe.
- **Frontière disciplinaire :** lecture et explication sémantique en anglais, non performance d'accent, ni analyse étymologique universitaire, ni simple copie de définitions.
- **Dépendances :** `requires: []`, `recommends_before: []`, `reinforces: []` pour cet ID. Le graphe central mentionne une arête **entrante** `qc-pri-ale-010/requires/qc-pri-ale-008`; elle ne bloque pas ce parcours.

## 2. Notions et représentations

- **prefix**: a meaningful part added **before** a base: `re- + write → rewrite` (write again). Not every initial letter group is a prefix (`uncle` is not `un- + cle`).
- **suffix**: a meaningful part added **after** a base: `care + -ful → careful` (showing care). A suffix may change the word class; the value of `-er` depends on the word and context.
- **root**: the central meaning-bearing element; for this course, use transparent examples (`help` in `helpful`). Not every English word can be split into obvious standalone English words.
- **context**: surrounding words, events and relationships in a sentence. E.g. `The lights were off, so the room was dark` supplies a clue about *dark*.
- **Four-step visual organizer:** `[whole sentence] → [target word / word parts] → [context clue] → [meaning in this sentence + because…]`. Learners underline context, box the prefix/suffix, circle the root, then state a plausible meaning. Printable and screen-reader compatible text versions in `contenu/01_NOTIONS_ET_EXEMPLES.md`.
- Present language orally as a reading scaffold if useful, then display and work on the original English spelling and sentence: do not replace assessment with oral fluency.

## 3. Préparation / diagnostic

- No mandatory Kristal prerequis. `diag-1` (oral explanation vs written annotation) and `diag-2` (two new sentences) in `contenu/02_DIAGNOSTIC.md` reveal if the learner understands contextual clues and meaningful word parts.
- Start from a worked example if the student cannot identify the target word; start directly with independent practice if the two diagnostic answers independently include meaning + morphology + a textual clue.
- If a learner gives meaning without evidence, run a brief annotation scaffold rather than imposing another course.

## 4. Enseignement guidé

- `teach-1` in `contenu/03_ENSEIGNEMENT_GUIDE.md` thinks aloud on `rewrite` and `careful` in complete, original English sentences; the teacher marks both the word part and neighboring clues.
- Demonstrate a rejected guess (`un-` does not automatically mean `again`) and revise using the same sentence, without presenting mistaken divisions as linguistically valid.
- Comprehension check: learner shows which part of `rewrite` signals repetition and which phrase in the sentence confirms it. Feedback uses exact words from the passage.
- Additional example contrasts a productive `-less` suffix with a word that only resembles an affix.

## 5. Pratique accompagnée

- Three guided pairs in `contenu/04_PRATIQUE_ACCOMPAGNEE.md`, with hints decreasing across G1, G2 and G3: colored explicit clues → questions only → no word-part hints until after response.
- Responses always name an inferred meaning for each target in **two sentences**, a morphological cue and a context cue. Do not score an isolated matching exercise as the final competency.
- On error, identify exactly whether the learner needs root recognition, affix meaning, or context checking, then retry on a different pair.

## 6. Pratique autonome

- Four fresh two-sentence pairs A1–A4 in `contenu/05_PRATIQUE_AUTONOME.md`, each with a teacher key. Students answer without lexical examples from the lesson on the sheet.
- Model the answer format separately: `Word: ... / My meaning here: ... / Part of the word: ... / Evidence in the sentence: ...`.
- Two further contexts in `contenu/06_REMEDIATION_ET_TRANSFERT.md` test transfer: instructions for a makerspace and a nature observation note.
- Record observable answers and annotations through the chosen learner platform; do not write individual learner data into the Kristal's canonical files.

## 7. Feedback et erreurs typiques

- `error-1`: meaning chosen without text evidence → highlight a phrase supporting or contradicting the guess.
- `error-2`: split arbitrary letters, e.g. `uncle = un- + cle` → compare `unkind` with `uncle`; treat `uncle` as a whole word here.
- `error-3`: treat `-less` as 'less than' in every case → use `wireless` in a sentence about a device with no wires and contrast comparative `less` as a separate word.
- `error-4`: attach one memorized gloss to any usage of an affix → ask whether the interpretation fits the actual sentence, then revise.
- Targeted repair and a different verification item are in `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Family** `qc-pri-ale-008-ev-01` ; `objectif_ref: obj-1` ; `critere_ref: crit-1`; preferred mode `réponse_argumentée` encoded as **fixed** items with argumentation rubric (not free AI generation).
- `evaluation/BANQUE_ITEMS.json`: 12 numbered complete two-sentence tasks, each fixed English stimulus, two distinct target words, expected English sense, word-part analysis and contextual evidence; answer variations limited to semantically equivalent phrases.
- **Two final independent evidence items**: `q-011` (community garden) and `q-012` (science/weather report), no definitions supplied in prompt and no teacher-provided root hints.
- **Scoring:** for each target: meaning right in context (2), valid morphological evidence (1), relevant textual evidence (1), total 8 per pair. Passing judgment additionally requires both target words reasoned successfully in both distinct final tasks; see `evaluation/GRILLE_MAITRISE.md`.
- All items `validation_status: a_revoir`; no exam or generator certified.

## 9. Remédiation / enrichissement

- For affix confusion: sort four transparent words into before/after base and mark the position; repair with a novel example, not the original item.
- For shaky root identification: find a repeated base (`play`, `playing`, `replay`) then compare its meaning; avoid claims about every possible English root.
- For context neglect: ask the learner to quote 2–5 neighboring words and check whether the proposed meaning makes the sentence coherent.
- Enrichment: multiple affixes (e.g. `un + help + ful`) with the warning that word formation can be irregular; no new prerequisite is established.

## 10. Accessibilité

- Accessible plain-text equivalents for every annotation; optional color/shape does not carry meaning alone. Adjustable font and spacing; text-to-speech for reading access when decoding fluency is not the assessed construct. Preserve the displayed spelling and the English sentence during responses.
- Permit typing, handwriting, dictation to a neutral scribe or speech-to-text for explaining, with documentation of accommodations; do not give away clues by paraphrasing the target words.
- Avoid penalties for handwriting, accent or spelling slips that do not change the demonstrated meaning. Teachers must decide whether reading aloud changes construct validity in a local summative use.

## 11. Critères de sortie

1. The learner **independently** explains the sense of both new targets in two English sentences, in each of two different unseen contexts (`q-011` and `q-012`).
2. Each explanation includes an appropriate meaningful word part and exact contextual evidence that supports, rather than contradicts, the interpretation.
3. The learner handles the different contexts without guided segmentation, leading questions, dictionaries or teacher correction during the evidence attempts.
4. A single score, prior grade, or a fluent oral answer alone does not establish mastery. Use the level table and targeted remediation rules in `evaluation/GRILLE_MAITRISE.md`.
5. Rappel différé: 2–7 days later, present two fresh sentences orally or in writing (`contenu/06_REMEDIATION_ET_TRANSFERT.md`), check maintenance without counting repeated exposure as independent evidence.

## 12. Références pédagogiques et limites

- Internal source-of-truth: unchanged frame's `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, base assessment contract, and governance v1.2. Do not call this a PFEQ-approved course.
- External grammar checked against *Cambridge Dictionary, English Grammar Today, Word formation* and *Suffixes*; see exact URLs and verification scope in `sources/REFERENCES_CONTENU.md`.
- Definitions, modelled examples, exercise sentences, word-pair choices and rubrics are original educational writing, not extracts from dictionaries.
- Limits: no classroom pilot, independent editorial proofreading, calibrated item difficulty or professional psychometric validation completed. Optional proposals for schema changes are documented only in `livraison/VALIDATION.md`.
