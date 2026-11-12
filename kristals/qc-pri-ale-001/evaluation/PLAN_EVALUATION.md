# Plan d'évaluation — `qc-pri-ale-001`

## Objet, preuve et conditions
- Objectif invariant `obj-1` : **Segmenter et manipuler syllabes et phonèmes de mots anglais oraux.**
- Critère invariant `crit-1` : **Recomposer oralement des mots nouveaux après segmentation.**
- Famille : `qc-pri-ale-001-ev-01`, type natif **`réponse_argumentée`**. Argumentation = démonstration orale ou par jetons **de l'opération sonore**, pas rédaction écrite.
- Passation : un adulte prononce l'anglais cible avec accent intelligible et cohérent, sans montrer la graphie, l'IPA, ni la solution; l'élève répète les unités et prononce le mot. Les exemples sont destinés **au correcteur**, pas à l'élève.
- Modèle de décision : items q-001 à q-010 pour diagnostic/formatif; **q-011 et q-012** sont deux performances de maîtrise dans des contextes différents, sans aide révélatrice, avec variantes bornées.

## Table d'alignement exhaustif
| Item | Objectif | Critère | Famille | Difficulté | Représentation | Variabilité autorisée |
|---|---|---|---|---|---|---|
| q-001 | obj-1 | crit-1 | qc-pri-ale-001-ev-01 | initial | syllabes | stimulus fixé; répétition neutre |
| q-002 | obj-1 | crit-1 | qc-pri-ale-001-ev-01 | initial | syllabes | stimulus fixé; répétition neutre |
| q-003 | obj-1 | crit-1 | qc-pri-ale-001-ev-01 | initial | phonèmes | stimulus fixé; répétition neutre |
| q-004 | obj-1 | crit-1 | qc-pri-ale-001-ev-01 | intermediaire | phonèmes | stimulus fixé; répétition neutre |
| q-005 | obj-1 | crit-1 | qc-pri-ale-001-ev-01 | intermediaire | onset/rime | stimulus fixé; répétition neutre |
| q-006 | obj-1 | crit-1 | qc-pri-ale-001-ev-01 | intermediaire | onset absent | stimulus fixé; répétition neutre |
| q-007 | obj-1 | crit-1 | qc-pri-ale-001-ev-01 | intermediaire | substitution phonémique | stimulus fixé; répétition neutre |
| q-008 | obj-1 | crit-1 | qc-pri-ale-001-ev-01 | intermediaire | phonème /ʃ/ | stimulus fixé; répétition neutre |
| q-009 | obj-1 | crit-1 | qc-pri-ale-001-ev-01 | intermediaire | syllabes | stimulus fixé; répétition neutre |
| q-010 | obj-1 | crit-1 | qc-pri-ale-001-ev-01 | intermediaire | phonèmes | stimulus fixé; répétition neutre |
| q-011 | obj-1 | crit-1 | qc-pri-ale-001-ev-01 | transfert | 3 formats · objets de classe | A/B contrôlé (seed pair→A) |
| q-012 | obj-1 | crit-1 | qc-pri-ale-001-ev-01 | transfert | 3 formats · pique-nique | A/B contrôlé (seed impair→B) |

## Couverture, critères et preuves
- **Syllables** : q-001, q-002, q-009, q-011 (3e cible), q-012 (3e cible).
- **Phonemes** : q-003, q-004, q-007, q-008, q-010, q-011 (1re), q-012 (1re).
- **Onset / rime** : q-005, q-006, q-007, q-011 (2e), q-012 (2e).
- **Réponse attendue** : mot complet intelligible **et** trace du processus (répétition des unités, nombre de gestes, substitution ou brève justification); aucun point pour graphie ou accent natif.
- Rubrique par sous-cible : correct (mot + unités en ordre, ou autocorrection), partiel (parties justes mais non fusionnées / mot juste sans preuve exploitable), non démontré (autre mot, omission de segments, aide révélatrice). Une réponse inaudible déclenche une adaptation, non un zéro automatique.
- **Maîtrise (q-011 et q-012)** : dans chacun des contextes, au moins **2/3** cibles reconstruites, y compris la cible phonémique **et** l'une des deux autres formes; processus explicité ou montré pour deux cibles; **au moins un des deux contextes entièrement sans indices**, et l'autre sans aide révélatrice. Décision sur deux observations, pas sur une note globale.

## Variabilité verrouillée
- q-001 à q-010 : seuls débit/volume/voix de l'adulte et répétition identique autorisés; changement de phonème ou de mot interdit.
- q-011 et q-012 : chaque item possède **exactement** variantes A/B dans `BANQUE_ITEMS.json`; choisir A si `seed % 2 == 0`, B sinon. Seeds canoniques q-011=410 (A), q-012=421 (B), rejouables. Un autre seed entier peut sélectionner l'autre variante sans créer de nouveau mot.
- Un item rendu « guidé » par un indice révélant la réponse doit être marqué comme tel; le retest de maîtrise utilise un ensemble approuvé non révélé et une autre passation, jamais un tirage libre d'IA.

## Sécurité, droits, accessibilité
- Environnement sonore calme, niveau audio confortable, aucune application imposée; lecture labiale et jetons sans lettres possibles si cela ne révèle pas la solution.
- Les noms des objets ne sont pas affichés; présenter le vocabulaire de référence suffisamment tôt, sans pré-exposer les mots complets **au moment du test**.
- Variation dialectale anglophone acceptable si segmentation/fusion restent phonologiquement cohérentes. Si difficultés motrices, gestes alternatifs; si difficulté de parole, représentation sonore assistée avec validation d'équivalence par spécialiste ou évaluateur humain (preuve canonique orale conservée).
- Audio facultatif avec consentement institutionnel, durée/stockage limités par la politique locale; aucune donnée d'élève dans le ZIP. Les scripts et mots d'exemple sont des productions originales, non une transcription d'enregistrement tiers.
- Banc non certifié : revue phonétique (ex. voyelles), relecture anglophone, essais d'écoute et de biais/accessibilité indispensables avant usage sommatif.
