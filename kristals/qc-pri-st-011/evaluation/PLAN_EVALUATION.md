# Plan d'évaluation — `qc-pri-st-011`

**Objectif immuable :** `obj-1` — Identifier la fonction d’éléments d’un objet technique usuel.  
**Critère / preuve immuable :** `crit-1` — Annoter un objet démontable ou documenté et expliquer ses fonctions.  
**Famille unique :** `qc-pri-st-011-ev-01` — `generee_sous_contraintes` (corpus de descriptions et scénarios fermés, **pas de génération libre**).  
**Banque :** `evaluation/BANQUE_ITEMS.json`, 10 items rédigés au statut `a_revoir`. Aucune certification ni validation humaine présumée.

## Couverture et ordre conseillé (non bloquant)

| Item | Difficulté | Représentation proposée | Preuve observable ciblée | Utilisation |
|---|---|---|---|---|
| `q-001` | initial | phrase + étiquette | besoin distinct de solution et fonction des mâchoires | diagnostic / formation |
| `q-002` | initial | tableau partie–fonction | couvercle, filets, limite de preuve | formation |
| `q-003` | initial | deux colonnes document/inférence | fait documentaire vs interprétation mécanique | formation |
| `q-004` | intermédiaire | explication cause-effet | action des filets et contrainte | formation |
| `q-005` | intermédiaire | tableau quatre parties | translation tiroir–glissières | formation accompagnée |
| `q-006` | intermédiaire | annotation + séquence | pivotement et rappel pince | formation accompagnée |
| **`q-007`** | **transfert** | **fiche A annotée + explication** | **trois fonctions, charnière/loquet, preuve, contrainte** | **maîtrise 1, autonome** |
| **`q-008`** | **transfert** | **fiche B annotée + explication** | **trois fonctions, roue/axe, preuve, contrainte** | **maîtrise 2, autonome** |
| `q-009` | transfert | fiche C annotée + argument | fonctions de la trousse et glissière | consolidation |
| `q-010` | transfert | fiche D annotée + explication | dévidoir sans lame : fonctions et limites | consolidation |

**Chaque item `q-001` à `q-010` pointe vers** `objectif_id: obj-1`, `critere_id: crit-1`, `family_id: qc-pri-st-011-ev-01` dans la banque JSON. Il s'agit d'évidences partielles pour les items initiaux; `q-007` et `q-008` seuls constituent la double preuve intégrée nécessaire à la décision de maîtrise, à apprécier avec la grille complète.

## Administration, représentations et conditions

1. Lire l'objectif. Diagnostic D1 et D2 de `contenu/02_DIAGNOSTIC.md`; adapter l'enseignement aux lacunes repérées. Aucun `requires`.
2. Modéliser la pince et le bocal (`contenu/03_ENSEIGNEMENT_GUIDE.md`), puis accompagner tiroir, porte-documents et cadre pliant avec indices dégressifs (`contenu/04_PRATIQUE_ACCOMPAGNEE.md`).
3. Laisser une période de séparation avant chacune des preuves. Présenter **A boîte articulée** puis **B chariot manuel**, chacun avec sa description fermée de `contenu/05_PRATIQUE_AUTONOME.md`; changer de date si possible. L'élève répond sans indice sur la fonction des parties. Les images sont facultatives; leur texte intégral est obligatoire et disponible.
4. Les pratiques C trousse et D dévidoir servent au transfert/entraînement et ne remplacent pas automatiquement l'une des preuves A/B. Après une preuve insuffisante, reprise ciblée puis tâche **nouvelle**, revue humainement et distincte des deux précédentes; ne pas relabeliser une copie corrigée comme preuve autonome.

## Rubrique, poids et décision

Pour chaque preuve A ou B : fonction des éléments **0–3**; interaction mécanique **0–2**; traces / limites de preuve **0–2**; contrainte **0–1**; autonomie cognitive **0–1** (9 unités descriptives, non une note de cours). Détails et conditions non compensatoires : `evaluation/GRILLE_MAITRISE.md`. Seuil qualitatif pour *chaque* contexte : F=3, M=2, P≥1, C=1, A=1, et aucune fonction inventée ni inférence risquée majeure. **Maîtrise = deux contextes distincts atteignant séparément les critères**, pas une moyenne ni une note unique; temporalité et traces conservées dans la plateforme d'apprentissage, pas dans le canon.

## Variabilité fermée / traçabilité

- `q-001` à `q-006`, `q-009`, `q-010` : mode `fixe`; `seed=null`, `parametres=null`. Le corrigé et les faits de la fiche sont fixés. Aucune génération paramétrique mathématique; pas de calcul nécessitant un solveur.
- `q-007` : mode `scenario_controle`, scénario `boite_articulee_A`, `seed=11007` (identifiant de traçabilité, **pas** un tirage effectué).
- `q-008` : mode `scenario_controle`, scénario `chariot_manuel_B`, `seed=11008` (identifiant de traçabilité, **pas** un tirage effectué).
- **Variables effectivement autorisées :** ordre typographique des questions, présentation grand caractère, réponses orales / dictées / écrites, annotations textuelles plutôt que dessin. Les faits, le choix A/B, le nombre d'éléments, la difficulté, la grille et les réponses défendables restent inchangés.
- **Variables non autorisées :** objets substitués automatiquement, scénarios inventés, IA générant un nouveau corrigé, mouvement non documenté, écran illustré sans description. Domaine des scénarios : seulement `A` pour `q-007`, seulement `B` pour `q-008`. Les seeds permettent d'identifier les scénarios figés, pas de simuler une randomisation.
- **Contrôle des solutions :** correction textuelle par lecture croisée du document et des réponses dans `contenu/05_PRATIQUE_AUTONOME.md`. Une inspection humaine reste requise pour l'équivalence des formulations.

## Sécurité, droits, accessibilité et limites

Les fiches sont fictives et originales, inspirées de mécanismes communs : **aucun appareil démonté, aucune lame, aucun ressort sous tension, aucune charge en mouvement ni circuit électrique**. Ne pas faire manipuler un tiroir lourd, des anneaux qui pincent ou un véhicule. Réponses multimodales équivalentes, lecture neutre permise, temps de réponse aménageable; ne pas noter l'orthographe, la dextérité ou l'habileté au dessin. Ne pas inférer un défaut de maîtrise des seules difficultés motrices. Contrôler les documents, la grille, les biais d'accessibilité, la durée réelle et la sécurité par revue humaine avant usage sommatif.

**Droits :** textes et descriptions de stimulus rédigés originalement pour ce Kristal; aucune image ni schéma tiers reproduit. Sources de notions publiques explicitement citées dans `sources/REFERENCES_CONTENU.md`; pas de revendication de licence sur les pages externes. Aucune revendication de conformité au PFEQ.
