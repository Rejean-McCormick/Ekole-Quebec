# Plan d'évaluation — `qc-pri-ma-014` · famille `qc-pri-ma-014-ev-01`

**Objectif unique `obj-1` (immuable) :** Effectuer des opérations élémentaires sur les fractions en conservant leur sens.  
**Critère/proof `crit-1` (immuable) :** Résoudre une situation illustrée sur des fractions et vérifier le résultat.  
**Mode privilégié :** `paramétrique_controle` (famille native v1.2). Items `fixe` ou `parametrique` selon le format `qc.learning-item-bank/1.0`; statut de tous les items `a_revoir`.

## Matrice exhaustive des 12 items

Tous les items portent explicitement **`objectif_id: obj-1`**, **`critere_id: crit-1`** et **`family_id: qc-pri-ma-014-ev-01`**, sans autre référence de cible. Les items `q-011` et `q-012` sont les **deux preuves de maîtrise** (ne pas substituer une bonne réponse à `q-001` à l'une des preuves).

| Item complet (suffixe de `qc-pri-ma-014-`) | Difficulté | Représentation | Couverture et réponse attendue | Variabilité permise |
|---|---|---|---|---|
| `q-001` | initial | bande de quatre segments | fraction unitaire `1/4` et recomposition | fixe, aucun changement |
| `q-002` | initial | bande additive commune | addition compatible, instance `1/6+2/6=3/6` | 3 triplets énumérés, seed contrôlée |
| `q-003` | intermediaire | bande décomposée | `4/8=1/8+3/8` | 3 triplets énumérés |
| `q-004` | intermediaire | rubans de longueurs différentes | refus de l'unité mal définie, `5 cm + 10 cm` sans `1/2` justifiée | fixe |
| `q-005` | intermediaire | bande et retrait | `5/8−2/8=3/8` | 3 triplets énumérés |
| `q-006` | intermediaire | rectangle complet | `3/6+3/6=6/6=1` | 3 triplets énumérés |
| `q-007` | intermediaire | erreur écrite et dessin | corriger `5/12` en `5/6` | fixe |
| `q-008` | intermediaire | surface décomposée | `5/6=2/6+3/6` | 3 triplets énumérés |
| `q-009` | intermediaire | deux bandes de même longueur | `4/8=1/2` expliqué et vérifié | fixe |
| `q-010` | intermediaire | ruban et moitié | `2/8+2/8=4/8=1/2` | 3 triplets énumérés |
| `q-011` | transfert | **surface d'un parterre** | `3/8+2/8=5/8`; contrôle par retrait | 3 triplets énumérés; preuve A |
| `q-012` | transfert | **longueur d'un parcours** | `7/10−3/10=4/10=2/5`; contrôle par addition | 3 triplets énumérés; preuve B |

### Critères et barème communs

Pour chaque tâche, observer quatre dimensions : (1) même tout et parts égales, (2) opération et fraction exactes, (3) schéma/notation compatibles, (4) vérification arithmétique correctement interprétée. Niveaux **0 absent/erroné**, **1 partiel ou assisté**, **2 explicite et correct sans indice**; la grille documente les indices et les adaptations accessibles. Le résultat numérique exact **sans** illustration/explication et contrôle ne suffit pas. Les items initiaux servent au diagnostic et à l'apprentissage; la sortie utilise **q-011 puis q-012 dans des contextes et occasions différents**, au niveau 2 sur toutes les dimensions dans les deux prestations et avec autonomie attestée. En cas d'écart, remédiation ciblée + nouveau double essai de même difficulté, sans réutiliser à l'identique les solutions présentées.

### Spécification de la génération et validité de contenu

Chaque item paramétrique déclare : trois triplets `(d,a,b)` **autorisés exhaustivement et dans un ordre fixe**, des domaines, des contraintes spécifiques, un algorithme déterministe, une seed stable, les réponses exactes **des trois candidats** et le candidat choisi par `index = seed modulo 3`. Aucun « nombre au hasard » et aucune variation textuelle non documentée. Les contrôles d'addition, de retrait et de recomposition utilisent l'arithmétique rationnelle exacte et l'identité inverse; le pilote pédagogique reste une revue humaine nécessaire. Tout nouveau candidat, toute permutation, tout changement de taille de l'unité ou de contexte doit faire l'objet d'un nouvel examen et d'une nouvelle version de banque.

### Couverture, administration, sécurité et accessibilité

- **Couverture :** fraction unitaire (`q-001`), addition compatible (`q-002`,`q-006`,`q-007`,`q-010`,`q-011`), décomposition (`q-003`,`q-008`), retrait du même type de parts (`q-005`,`q-012`), comparaison d'unités/équivalence (`q-004`,`q-009`); les deux transferts couvrent les opérations dans des contextes distincts.
- **Sécurité :** scénarios fictifs sans collecte de renseignements personnels, sans objets coupants ni activité physique risquée; contexte du parcours = relevé de tronçons, pas incitation à marcher selon un résultat.
- **Accessibilité :** descriptions des bandes en plus des caractères/figures, sections de tailles déclarées égales, gros caractères, textures/tactile, dictée ou réponse orale avec scripteur neutre si requis. Aucun code couleur nécessaire. Les aides qui révèlent opération, résultat ou contrôle invalident la condition autonome même si la modalité d'accès est adaptée.
- **Limites :** droits des illustrations simplifiées : graphismes textuels originaux; aucune source image externe. Relecture humaine de la lisibilité, de la charge langagière et de la grille nécessaire. Pas de conformité PFEQ ou d'examen certifié alléguée.
