# Validation de livraison — qc-pri-fr-012 · v1.2

**Résultat technique :** contrôles automatiques ci-dessous effectués et réussis au moment de la construction du delta. **Statut pédagogique :** `a_revoir`; non certifié, non homologué, non publié. Les seuls fichiers livrés sont sous `kristals/qc-pri-fr-012/`.

## Contrôles effectivement exécutés sur les sources et le contenu

- Réussi — YAML frontmatter parsable.
- Réussi — native YAML metadata fields preserved.
- Réussi — 12 sections numbered and ordered.
- Réussi — immutable identity title and objective in PARCOURS.
- Réussi — native contract fields and fixed values preserved.
- Réussi — requires empty and only suggested FR-002.
- Réussi — assessment family v1.2 fields complete.
- Réussi — source graph relations concordant.
- Réussi — bank strict JSON and fixed IDs.
- Réussi — unique consecutively numbered item IDs.
- Réussi — all item fields, immutable links and safe statuses.
- Réussi — 2 distinct complete mastery contexts.
- Réussi — qc-pri-fr-012-q-009: target spellings present in dictation.
- Réussi — qc-pri-fr-012-q-009: all errors found in phase 2.
- Réussi — qc-pri-fr-012-q-009: rubric count matches answer key.
- Réussi — qc-pri-fr-012-q-009: keys conform to fixed target lexicon.
- Réussi — qc-pri-fr-012-q-010: target spellings present in dictation.
- Réussi — qc-pri-fr-012-q-010: all errors found in phase 2.
- Réussi — qc-pri-fr-012-q-010: rubric count matches answer key.
- Réussi — qc-pri-fr-012-q-010: keys conform to fixed target lexicon.
- Réussi — 13 prevalidation files nonempty.
- Réussi — manifest has exact 14 file paths.
- Réussi — exercises and transfer docs present and legible.
- Réussi — sources and accessibility documented.

## Couverture livrée et comptage

- Un seul identifiant : `qc-pri-fr-012` — Orthographe d’usage; **14 fichiers** attendus dans la racine fusionnable. Deux fichiers d'auteur existants remplacés; les douze autres ajoutés.
- Les **12 sections du PARCOURS.md** ont été développées. Métadonnées YAML d'origine préservées hors `revision_contenu` augmentée de `0.2.0` à `0.3.0`; `statut: en_rédaction` est maintenu par prudence.
- **15 graphies cibles**, au moins 2 exemples modelés, 4 contre-exemples, 2 tâches diagnostiques, 3 exercices guidés (indices dégressifs), 4 pratiques autonomes, 2 transferts, remédiation ciblée et rappels espacés.
- **10 items fixes** `qc-pri-fr-012-q-001` à `q-010`, avec corrigés éditoriaux ou rubriques et rétroactions; deux preuves distinctes `q-009` et `q-010`. Aucun mode paramétrique, aucun générateur libre, aucun calcul de solveur déclaré.

## Contrôles d'assemblage du ZIP (effectués lors du conditionnement)

- Comptage/ordre des 14 entrées; premier chemin `kristals/qc-pri-fr-012/authoring/PARCOURS.md`.
- Racine de toutes les entrées sous `kristals/qc-pri-fr-012/`, aucune enveloppe `Frames_202_...`, aucun parent absolu, aucune entrée `../`, aucun doublon ni fichier vide.
- Lisibilité de chacun des fichiers extraits du ZIP; JSON strict du contrat, de la banque et du manifeste; manifeste identique au contenu réel; test CRC de l’archive; comparaison d'octets entre les sources locales et le ZIP.
- Aucun autre Kristal ni fichier global (`registry/`, `governance/`, `canon/`, `state/`, `runtime/`, `AGENTS.md`, `kristal.workspace.json`) n'est inclus. Aucune fusion effective ni modification de l'archive maîtresse n'a été réalisée.

## Limites / revues humaines non effectuées

1. **Relecture linguistique experte** : graphies et explications morphologiques, acceptabilité du lexique pour l'élève, ambiguïtés des indices de sens, variation du français québécois. Les clés des tâches ont été contrôlées **mécaniquement** pour leur cohérence interne, pas certifiées par une autorité externe.
2. **Essai réel avec utilisateurs** : clarté, durée, charge de travail, accessibilité auditive, modalités de réponse, stabilité sur délai et équité. Aucun élève n'a été testé.
3. **Étalonnage des seuils** : valeurs 5/6 et 4/5, 2/2 justifications proposées **en interne**, sans données psychométriques.
4. **Audit de droits/diffusion** : matériel original livré, aucun tiers repris intentionnellement; la revue juridique et les licences éventuelles restent à effectuer.
5. **Tests d'intégration du moteur local** : aucun build-v9, check-ai, LMS, serveur, publication, déploiement ou activation exécuté. La présence de fichiers n'en tient pas lieu.
6. **Indépendance des preuves** : si les textes de transfert sont montrés pendant l'entraînement, ne pas les réutiliser comme preuves indépendantes sans nouvel ensemble validé par un humain.

## Propositions de structure, non appliquées

- Normaliser dans une version centrale future un champ `critere_id` de famille, une séparation formelle stimulus élève / script correcteur, et un champ `phase_de_divulgation` pour les deux étapes (dictée, correction).
- Normaliser les étiquettes de validation entre manifeste, plan, item et moteur sans modifier ici aucun schéma canonique.
- Ajouter ultérieurement un mécanisme d'administration empêchant l'affichage des champs `texte_dicte_lecteur`, `reponse_attendue` et `corrections_phase2` aux élèves avant la clôture des étapes.

**Fusion attendue :** décompresser le maître, entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis extraire le ZIP **à cet endroit**. Ne pas mettre un dossier portant le nom du ZIP entre le maître et `kristals/`.
