# Plan d'évaluation — qc-pri-ma-009

**But :** mesurer `obj-1` (« Représenter le partage et le groupement pour résoudre des divisions. ») et `crit-1` (« Effectuer un partage justifié et vérifier quotient et reste. »), famille `qc-pri-ma-009-ev-01`. Discipline : Mathématique. **Aucun alignement détaillé au PFEQ revendiqué.**

## Couverture de la banque et représentations

Chaque item vise **uniquement `obj-1`, `crit-1` et `qc-pri-ma-009-ev-01`**. Le tableau suivant est un registre opérationnel :

| ID | Complexité | Représentation / mode | Liens | Fonction |
|---|---|---|---|---|
| `qc-pri-ma-009-q-001` | `initial` | `partage` / `parametrique` | `obj-1`, `crit-1`, `qc-pri-ma-009-ev-01` | entraînement/diagnostic |
| `qc-pri-ma-009-q-002` | `initial` | `groupement` / `fixe` | `obj-1`, `crit-1`, `qc-pri-ma-009-ev-01` | entraînement/diagnostic |
| `qc-pri-ma-009-q-003` | `initial` | `groupement` / `fixe` | `obj-1`, `crit-1`, `qc-pri-ma-009-ev-01` | entraînement/diagnostic |
| `qc-pri-ma-009-q-004` | `intermediaire` | `groupement` / `parametrique` | `obj-1`, `crit-1`, `qc-pri-ma-009-ev-01` | entraînement/diagnostic |
| `qc-pri-ma-009-q-005` | `intermediaire` | `groupement` / `fixe` | `obj-1`, `crit-1`, `qc-pri-ma-009-ev-01` | entraînement/diagnostic |
| `qc-pri-ma-009-q-006` | `intermediaire` | `partage` / `parametrique` | `obj-1`, `crit-1`, `qc-pri-ma-009-ev-01` | entraînement/diagnostic |
| `qc-pri-ma-009-q-007` | `intermediaire` | `groupement` / `fixe` | `obj-1`, `crit-1`, `qc-pri-ma-009-ev-01` | entraînement/diagnostic |
| `qc-pri-ma-009-q-008` | `intermediaire` | `groupement` / `parametrique` | `obj-1`, `crit-1`, `qc-pri-ma-009-ev-01` | entraînement/diagnostic |
| `qc-pri-ma-009-q-009` | `intermediaire` | `partage` / `fixe` | `obj-1`, `crit-1`, `qc-pri-ma-009-ev-01` | entraînement/diagnostic |
| `qc-pri-ma-009-q-010` | `intermediaire` | `partage` / `parametrique` | `obj-1`, `crit-1`, `qc-pri-ma-009-ev-01` | entraînement/diagnostic |
| `qc-pri-ma-009-q-011` | `transfert` | `partage` / `fixe` | `obj-1`, `crit-1`, `qc-pri-ma-009-ev-01` | A (74/6) |
| `qc-pri-ma-009-q-012` | `transfert` | `groupement` / `fixe` | `obj-1`, `crit-1`, `qc-pri-ma-009-ev-01` | B (91/8) |

- `q-001` à `q-003` : identifier l'unité, construire ou visualiser des groupes et vérifier l'égalité.
- `q-004` à `q-010` : inclure reste nul, reste non nul, repérage d'une erreur et deux interprétations de mêmes données.
- **Deux preuves autonomes distinctes** : `q-011`, répartition de fiches entre équipes (*partage*) et `q-012`, rangement de gourdes en caisses (*groupement*). Les administrer séparément; ne pas laisser les corrigés ouverts.

## Critères et barème non compensatoire

Les **quatre dimensions** de la grille sont évaluées chacune : (C1) représentation et unités, (C2) quotient et reste exacts, (C3) identité et borne du reste, (C4) justification adaptée au contexte. Chaque dimension vaut `acquis`, `en développement` ou `non montré`; aucune moyenne ne remplace une preuve. Deux tâches de contextes distincts doivent chacune atteindre **acquis dans les quatre dimensions**, sans indice de résolution et avec adaptations non guidantes permises. Une seule production correcte ne suffit pas.

## Mode et variabilité autorisée

- **Fixe** (`q-002`, `003`, `005`, `007`, `009`, `011`, `012`) : énoncé et nombres verrouillés, correction exacte fournie. Si une version parallèle est nécessaire, elle doit être construite, testée et revue avant usage.
- **Paramétrique** (`q-001`, `004`, `006`, `008`, `010`) : `seed` entier fixé dans chaque item et domaines bornés `d=3..10`, `q=3..12`, reste `0` ou `1..d−1`; `N=d×q+r ≤ 130`. Générateur arithmétique déterministe et trois exemples par item décrits dans `BANQUE_ITEMS.json` sous `parametres`. **Ne pas** laisser une IA inventer le contexte, la division ou la réponse. La seule variation admise sans rédaction supplémentaire concerne ces nombres sous contrôle exact; toute nouvelle instance doit subir le recalcul `divmod` et une revue de l'énoncé.
- Le dénominateur/diviseur zéro, les restes négatifs et `r≥d` sont interdits. Aucun arrondi vers le haut de « groupes complets » n'est admis; les restes doivent être interprétés.

## Conditions d'administration, sécurité et accessibilité

Présenter les énoncés par lecture, texte agrandi ou matériel tactile; les productions peuvent être orales, écrites ou représentées par des objets **si elles restent observables et vérifiables**. Pour les preuves autonomes, ne pas donner d'indice procédural, de formule partiellement remplie, ni de confirmation de q/r avant la fin. Les situations sont imaginaires, non sensibles, sans divulgation personnelle ni action dangereuse. Journaliser le mode de réponse, les accommodations non guidantes et les éventuels indices, pour ne pas interpréter une aide comme une autonomie.

## Décision et reprise

Corriger les items à l'aide de `GRILLE_MAITRISE.md`; `a_revoir` demeure le statut de chaque item. Si une dimension échoue, documenter l'erreur, activer `contenu/06_REMEDIATION_ET_TRANSFERT.md`, puis recueillir **une nouvelle production** sur des nombres et un contexte non vus. La vérification arithmétique est automatisée; la qualité du langage, des adaptations et des rubriques attend une revue humaine.
