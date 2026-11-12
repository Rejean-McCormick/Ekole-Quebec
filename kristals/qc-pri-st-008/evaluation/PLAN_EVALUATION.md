# PLAN D’ÉVALUATION — `qc-pri-st-008`

**Famille :** `qc-pri-st-008-ev-01` · **Objectif :** `obj-1` — Repérer des sources d’énergie et décrire les transformations observées.  
**Critère :** `crit-1` — Construire un schéma simple d’une chaîne énergétique observable.  
**Type v1.2 conservé :** `generee_sous_contraintes` · **Statut :** items `a_revoir`, pas d’examen certifié.

## Planification et couverture

| Item | Objectif | Critère | Famille | Difficulté | Représentation et tâche | Variabilité |
|---|---|---|---|---|---|---|
| `qc-pri-st-008-q-001` | `obj-1` | `crit-1` | `qc-pri-st-008-ev-01` | initial | pile → lampe / sonnette : source et usage | 2 scénarios finis, seed pair/impair |
| `qc-pri-st-008-q-002` | `obj-1` | `crit-1` | `qc-pri-st-008-ev-01` | initial | vent ou eau : transfert de mouvement sans production électrique | 2 scénarios finis, seed pair/impair |
| `qc-pri-st-008-q-003` | `obj-1` | `crit-1` | `qc-pri-st-008-ev-01` | intermediaire | panneau : lumière → électrique | 2 scénarios finis, seed pair/impair |
| `qc-pri-st-008-q-004` | `obj-1` | `crit-1` | `qc-pri-st-008-ev-01` | intermediaire | manivelle → générateur → lumière/son | 2 scénarios finis, seed pair/impair |
| `qc-pri-st-008-q-005` | `obj-1` | `crit-1` | `qc-pri-st-008-ev-01` | intermediaire | ressort : stock élastique → mouvement | 2 scénarios finis, seed pair/impair |
| `qc-pri-st-008-q-006` | `obj-1` | `crit-1` | `qc-pri-st-008-ev-01` | intermediaire | avertisseur/afficheur : observation et modèle | 2 scénarios finis, seed pair/impair |
| `qc-pri-st-008-q-007` | `obj-1` | `crit-1` | `qc-pri-st-008-ev-01` | intermediaire | réparer une fausse électricité du moulinet | aucune : fixe |
| `qc-pri-st-008-q-008` | `obj-1` | `crit-1` | `qc-pri-st-008-ev-01` | intermediaire | source vs usage et chaleur | aucune : fixe |
| `qc-pri-st-008-q-009` | `obj-1` | `crit-1` | `qc-pri-st-008-ev-01` | transfert | preuve A : vélo et dynamo | aucune : fixe |
| `qc-pri-st-008-q-010` | `obj-1` | `crit-1` | `qc-pri-st-008-ev-01` | transfert | preuve B : panneau solaire et ventilateur | aucune : fixe |

## Couverture vérifiable

- **Source :** q-001, q-003, q-005, q-006, q-008, q-009, q-010. **Transfert :** q-002, q-004, q-006, q-009, q-010. **Transformation :** q-001, q-003 à q-006, q-008 à q-010. **Usage :** q-001, q-003, q-006, q-008 à q-010.
- **Niveaux de preuve :** chaque item demande d’identifier observation et inférence, ou justifie explicitement ce qui est absent; q-007 confronte une interprétation non étayée.
- **Deux manifestations de maîtrise différentes :** q-009, mobilité/dynamo, et q-010, jardin/photovoltaïque. Chaque élève produit indépendamment les deux schémas; les deux doivent franchir tous les axes essentiels (voir `GRILLE_MAITRISE.md`). Aucune note unique ne suffit.

## Variation admissible et contraintes strictes

- q-001 à q-006 : **seul** `scenario_index ∈ {0,1}` varie; sélection exacte `index = seed % 2` avec seed dans `{base, base+1}`; toute autre graine est rejetée. Stimulus, observation, inférence et réponse sont **pré-rédigés** dans la banque. Chaque version possède son corrigé distinct, non dérivé d’une IA libre.
- q-007 à q-010 : scénarios fixes sans seed ni variables. Schémas différents mais scientifiquement équivalents acceptés selon les rubriques; impossible de coter fiable la vérité scientifique par similarité de mots seulement.
- Pas de variation sur l’objectif, les formes scientifiquement attestables, la distinction observation/modèle ou les appareils absents. Revue humaine obligatoire des formulations et des contextes avant usage sommatif.

## Cotation formative et maîtrise

- À chaque item : trois critères minimaux source/système, chemin/transformation, effet/observation/usage; q-009 et q-010 ajoutent la condition d’autonomie. Coter chaque dimension **0 non démontré, 1 partiel, 2 autonome exact**, avec justification écrite. Une omission grave (source inversée, création d’énergie, transfert électrique fictif ou constat inventé) entraîne remédiation ciblée.
- **Décision de maîtrise :** niveau 2 sur les quatre axes essentiels pour **chacune** des preuves q-009 et q-010, sans indice; un profil d’axes se conserve plutôt qu’une moyenne. Nouvelle tâche équivalente après remédiation si besoin.

## Accessibilité, équité et sécurité

- Lire les scènes et fournir transcription/descriptions alternatives; permettre schéma par mots, oral enregistré, cartes vierges ou dessin textuel; maintenir les mêmes décisions scientifiques et le sens des flèches. Ne pas accorder de point pour dessin esthétique, vitesse, capacité graphique, accent ou aisance linguistique hors notion visée.
- Aucun assemblage ni démontage électrique; aucune manipulation d’objet chauffant, de mouvement, d’élastique projeté, de pile ou d’appareil raccordé au secteur. Les scénarios sont **fictifs ou descriptifs**.
- Relecture humaine : exactitude des modèles, expressions « source » et « observation » selon la frontière du système, ambiguïtés de matériel, éventuel biais de familiarité technologique, niveau de lecture et durée de passation. Corrigés contrôlés conceptuellement, **pas** d’essai avec un groupe d’élèves.

## Sélection et traçabilité

- Choisir les items d’entraînement selon lacunes diagnostiquées. Pour les deux épreuves intégratrices, utiliser q-009 et q-010 en sessions séparées si possible, sans retour à la grille pendant l’essai. Une évaluation sommative locale demanderait une validation additionnelle; conserver les productions dans un LMS, non dans les fichiers canon.
- Source : `../sources/REFERENCES_CONTENU.md`. Famille native enrichie dans `../authoring/CONTRAT_PEDAGOGIQUE.json`.
