# Plan d’évaluation — qc-pri-st-005

**Objectif invariant :** `obj-1` — Classer des matières selon leurs propriétés et leurs états.
**Preuve invariante :** `crit-1` — Classer des matériaux inconnus en justifiant deux critères.
**Famille :** `qc-pri-st-005-ev-01`, type natif `generee_sous_contraintes`.

## Couverture et modes

| Item | Liens | Niveau | Représentation / contexte | Mode | Rôle |
|---|---|---|---|---|---|
| `q-001` | `obj-1` + `crit-1` + `qc-pri-st-005-ev-01` | initial | cabinet de découverte de trois échantillons : fiches, tableau, justification | fixe | Formatif / transfert |
| `q-002` | `obj-1` + `crit-1` + `qc-pri-st-005-ev-01` | initial | atelier de comparaison de matières : fiches, tableau, justification | fixe | Formatif / transfert |
| `q-003` | `obj-1` + `crit-1` + `qc-pri-st-005-ev-01` | initial | dossier sur la translucidité et la transparence : fiches, tableau, justification | fixe | Formatif / transfert |
| `q-004` | `obj-1` + `crit-1` + `qc-pri-st-005-ev-01` | intermediaire | carnet de laboratoire fictif : fiches, tableau, justification | fixe | Formatif / transfert |
| `q-005` | `obj-1` + `crit-1` + `qc-pri-st-005-ev-01` | intermediaire | vitrine de fiches techniques : fiches, tableau, justification | scenario_controle | Formatif / transfert |
| `q-006` | `obj-1` + `crit-1` + `qc-pri-st-005-ev-01` | intermediaire | inventaire de matériaux destinés à un kiosque scientifique : fiches, tableau, justification | scenario_controle | Formatif / transfert |
| `q-007` | `obj-1` + `crit-1` + `qc-pri-st-005-ev-01` | transfert | catalogue de descriptions documentées : fiches, tableau, justification | scenario_controle | Formatif / transfert |
| `q-008` | `obj-1` + `crit-1` + `qc-pri-st-005-ev-01` | intermediaire | classement par état et propriété de surface : fiches, tableau, justification | scenario_controle | Formatif / transfert |
| `q-009` | `obj-1` + `crit-1` + `qc-pri-st-005-ev-01` | intermediaire | relecture critique de trois notes : fiches, tableau, justification | fixe | Formatif / transfert |
| `q-010` | `obj-1` + `crit-1` + `qc-pri-st-005-ev-01` | transfert | préparation d’un tableau de démonstration : fiches, tableau, justification | fixe | Formatif / transfert |
| `q-011` | `obj-1` + `crit-1` + `qc-pri-st-005-ev-01` | transfert | station fictive de conservation de collections de musée : fiches, tableau, justification | scenario_controle | Preuve autonome A |
| `q-012` | `obj-1` + `crit-1` + `qc-pri-st-005-ev-01` | transfert | centre fictif de documentation scientifique : fiches, tableau, justification | scenario_controle | Preuve autonome B |

## Architecture de l’épreuve et critères
- **Avant les preuves :** items 1–3 acquis élémentaires, 4–9 pratique et variation documentaire, 10 transfert préparatoire. Les deux preuves finales sont **11 et 12**, avec des codes et observations différents de l’enseignement et de l’entraînement.
- **État :** justification par une observation distinctive de forme propre / écoulement / occupation du volume fermé.
- **Deuxième critère :** propriété distincte consignée : souple, opaque, transparent, rugueux, viscosité relative, compressibilité rapportée, etc. Pas deux paraphrases du comportement d’état.
- **Raisonnement :** séparer données et inférences, refuser d’identifier la substance ou de déclarer son innocuité sans preuve.
- **Décision :** en preuves A **et** B, classer exactement les cinq fiches du contexte et donner deux observations pertinentes et non redondantes par fiche, sans aide de contenu. Une preuve insuffisante mène à une remédiation et à un nouveau contexte, pas à une moyenne compensatoire.

## Variabilité autorisée et contrôle
- Items **fixes** : codes, observations, réponses et difficulté verrouillés; seule la mise en page accessible varie.
- Items **scenario_controle** : ordre des cartes uniquement, par permutation circulaire avec `seed` stable et algorithme `shift = seed % n`; aucun nouveau cas ni propriété créé. Exemple q-011 (n=5, seed 5011) : ordre présenté après rotation de 1; le corrigé suit chaque code invariant. Les variantes +1 et +2 sont listées dans `parametres.exemples_valides`.
- Aucune génération IA libre, aucun scoreur automatique de justification présenté comme fiable; la correction textuelle est une grille humaine et une table de référence figée. Aucune famille « certifiée ».

## Représentation et sécurité/accessibilité
- Fiches descriptives lisibles, texte alternatif, gros caractères ou audio, tableau dicté; les observables scientifiques restent identiques. Lecture/écriture/vitesse ne sont pas l’objectif; une assistance neutre à la transcription est permise.
- Scénarios fictifs sans chimie réelle ni matériel inconnu. Les rapports d’enceintes fermées sont des **données déjà décrites**, jamais une expérience sous pression à effectuer. Aucun besoin de sentir, goûter, respirer, chauffer ou verser.
- Éviter la couleur comme seul discriminant; toute propriété optique est formulée dans la fiche en texte. La sécurité et la prudence face aux inférences sont évaluées descriptivement.

## Limites de qualification
- Les références factuelles sont dans `sources/REFERENCES_CONTENU.md`; les exemples sont originaux et fictifs. Les rubriques et les formulations restent `a_revoir` et requièrent une revue humaine scientifique, linguistique, pédagogique et d’accessibilité.
- Éviter de confondre les matériaux composites avec les trois états idéalisés. Voir `evaluation/GRILLE_MAITRISE.md` pour les niveaux et la décision.
