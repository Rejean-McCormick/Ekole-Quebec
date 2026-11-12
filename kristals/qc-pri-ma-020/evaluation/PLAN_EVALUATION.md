# Plan d'évaluation — qc-pri-ma-020

## Autorité et mesure

- Objectif **inchangé** `obj-1` : « Modéliser une situation multiplicative ou de partage et contrôler la solution. »
- Critère **inchangé** `crit-1` : « Construire une représentation et résoudre un problème multiplicatif inédit. »
- Famille **inchangée** `qc-pri-ma-020-ev-01`, mode privilégié `paramétrique_controle`.
- **Un item n'est pas une preuve réussie sans modèle, réponse interprétée et contrôle**. Les nombres changés ne suffisent pas si la structure du raisonnement a été copiée.

## Couverture et traçabilité

| Item | Mode | Difficulté | Représentation attendue | Alignement |
|---|---|---|---|---|
| `001` | `fixe` | initial | dessin de cinq corbeilles et écriture symbolique | `obj-1` / `crit-1` / `qc-pri-ma-020-ev-01` |
| `002` | `fixe` | initial | sept parts égales; équation inverse | `obj-1` / `crit-1` / `qc-pri-ma-020-ev-01` |
| `003` | `parametrique` | initial | schéma de boîtes égales et équation | `obj-1` / `crit-1` / `qc-pri-ma-020-ev-01` |
| `004` | `parametrique` | intermediaire | tableau 1, 2 et n unités puis équation | `obj-1` / `crit-1` / `qc-pri-ma-020-ev-01` |
| `005` | `parametrique` | intermediaire | d groupes avec q dans chacun, équation inverse | `obj-1` / `crit-1` / `qc-pri-ma-020-ev-01` |
| `006` | `parametrique` | intermediaire | q groupes complets, r objets isolés | `obj-1` / `crit-1` / `qc-pri-ma-020-ev-01` |
| `007` | `parametrique` | intermediaire | barres de longueur égale comparées | `obj-1` / `crit-1` / `qc-pri-ma-020-ev-01` |
| `008` | `parametrique` | transfert | g groupes de p moins x objets retirés | `obj-1` / `crit-1` / `qc-pri-ma-020-ev-01` |
| `009` | `fixe` | intermediaire | correction de modèle; sacs et reste | `obj-1` / `crit-1` / `qc-pri-ma-020-ev-01` |
| `010` | `fixe` | intermediaire | barres de longueurs 4, 6, 7; somme | `obj-1` / `crit-1` / `qc-pri-ma-020-ev-01` |
| `011` | `scenario_controle` | transfert | piles de livrets, schéma/barres et équation | `obj-1` / `crit-1` / `qc-pri-ma-020-ev-01` |
| `012` | `scenario_controle` | transfert | tableau proportionnel, 13 groupes et opération | `obj-1` / `crit-1` / `qc-pri-ma-020-ev-01` |

**Fonctions couvertes.** Groupes : q-001, q-003, q-007, q-008, q-010 et q-012; proportion : q-004, q-007 et q-012; partages : q-002 et q-005; division euclidienne/reste : q-006, q-009, q-011. Toutes les tâches ont un énoncé, une réponse justifiée, une grille et un feedback propres. q-010 vérifie spécifiquement les groupes *non égaux*.

## Rubrique commune, critères et décisions

1. **Modèle (M)** : relation et quantités visibles, groupes/parts identifiés avec unités.
2. **Calcul (C)** : égalité vraie, opération adaptée, résultat exact, `0≤r<d` en division euclidienne.
3. **Interprétation (I)** : répond à la demande, distingue groupes complets, reste et contenants nécessaires; réponse annotée.
4. **Contrôle (V)** : vérification indépendante/inverse cohérente (`q×d+r=N` ou division inverse) et vraisemblance.

Chacun est observé aux niveaux absent, en développement, satisfaisant, solide. Pour maîtrise : les quatre dimensions satisfaisantes sur **les deux épreuves q-011 et q-012**, en contextes différents, avec au moins une sans aucune aide de méthode; si épreuve assistée, refaire sur nouveau problème avant décision. Une erreur de calcul ponctuelle corrigée spontanément avant remise, avec contrôle explicite, est documentée et jugée selon la cohérence finale; une aide indiquant l'opération disqualifie l'autonomie de cette tentative. Ne pas convertir automatiquement un total de points en maîtrise.

## Variabilité permise et contrôle

- q-001, q-002, q-009 et q-010 : stimuli et corrigés fixes.
- q-003 à q-008 : **six fonctions arithmétiques explicitement déterministes**, domaine entier borné, seed immuable propre à l'item; `BANQUE_ITEMS.json` conserve paramètres, algorithme, stimulus d'exemple calculé, solution et contraintes. Changer la seed exige recalcul exact, mise à jour du stimulus/corrigé et nouveaux tests, sans substitution libre par modèle génératif.
- q-011 et q-012 : **contextes et valeurs fixés**, administrés sans indices, réponses alternatives acceptées si elles représentent la même structure et la vérifient. Ne pas remplacer leur texte par un scénario généré librement.
- Réponses acceptées sous forme de barres, dessins, jetons, tableaux, schémas tactiles ou explications orales consignées, avec les **mêmes invariants mathématiques**. L'ordre des facteurs peut être inversé si leurs unités sont correctement interprétées.

## Épreuves autonomes distinctes

- **Preuve A q-011, centre communautaire :** capacité de piles, quotient entier, reste et décision de nombre total de piles. `47=6×7+5`; sept piles complètes et huit piles pour tout ranger.
- **Preuve B q-012, ferme pédagogique :** rapport constant de pommes par panier, tableau pour 1, 5 et 13 paniers, `13×4=52`, contrôle inverse.
- Conditions : textes inédits par rapport aux modèles/entraînements, sans solution visible; nommer les unités et expliquer le schéma. Les deux preuves doivent être conservées dans le système de suivi autorisé et non dans le canon.

## Équité et sécurité

- Aucun risque matériel : jetons fictifs, textes de situations ordinaires, aucune donnée réelle ou personnelle requise.
- Lecture orale permise, police ajustable, matériel de substitution accessible, tableaux décrits verbalement, réponses orales transcrites. Ne jamais fournir une opération ou une valeur en guise d'adaptation lors des preuves autonomes.
- Revue humaine requise avant utilisation sommative : clarté, difficulté, acceptabilité de chaque représentation, culture, biais, accessibilité réelle et durée. Aucune certification revendiquée.
