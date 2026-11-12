# Plan d’évaluation — `qc-pri-ma-028` (v1.2)

**Objectif commun immuable :** `obj-1` — Mesurer ou calculer une aire en unités carrées adaptées.  
**Critère commun immuable :** `crit-1` — Déterminer l’aire de figures quadrillées et expliquer la méthode.  
**Famille unique :** `qc-pri-ma-028-ev-01`; type natif `paramétrique_controle` : la banque comprend des items fixes et une génération paramétrique par **catalogues finis vérifiés**, jamais un tirage IA libre.

## Matrice de traçabilité de chaque item

Pour **chaque ligne**, les identifiants référencés sont exactement **`obj-1`**, **`crit-1`**, **`qc-pri-ma-028-ev-01`**; les items comportent de plus ces trois références en JSON.

| Item exact | Difficulté | Représentation | Critères observables / résultats de l’instance choisie | Utilisation |
|---|---|---|---|---|
| `qc-pri-ma-028-q-001` | initial | rectangle 2×3 en cases non métrées | 6 u²; comptage par rangées; unité correcte | formative |
| `qc-pri-ma-028-q-002` | initial | grille 4×3, deux trous | 10 u²; compter `#`, pas `.` | formative |
| `qc-pri-ma-028-q-003` | initial | rectangle 2×4, côtés 1 cm | 8 cm²; case de 1 cm² | formative |
| `qc-pri-ma-028-q-004` | intermédiaire | rectangle métrique paramétrique | sélection `2028 % 3 = 0` : 4 colonnes × 5 rangées = 20 cm² | formative, variation contrôlée |
| `qc-pri-ma-028-q-005` | intermédiaire | figure en L, unité abstraite | 5 u²; absence de double comptage du coin | formative |
| `qc-pri-ma-028-q-006` | intermédiaire | bandes et rectangle englobant | 8 u²; éliminer quatre cases vides | formative |
| `qc-pri-ma-028-q-007` | intermédiaire | figure composée paramétrique | sélection `2030 % 3 = 2` : 3+3+3+1 = 10 u² | formative, variation contrôlée |
| `qc-pri-ma-028-q-008` | transfert | aire métrique, côté des cases 2 cm | 24 cm²; `6×(2²)`; refuser 6 ou 12 cm² | préparation au transfert |
| `qc-pri-ma-028-q-009` | transfert | **panneau d’exposition**, rectangle de cases de 1 cm | sélection `2027 % 3 = 2` : 5×3 = **15 cm²**, justification par deux calculs | **maîtrise A** |
| `qc-pri-ma-028-q-010` | transfert | **jardinière communautaire**, surface composée sans échelle physique | sélection `2029 % 3 = 1` : 5+4+3 = **12 u²**, rangées et complément | **maîtrise B** |

## Paramètres, domaines, contraintes et reproductibilité

- Les items **004, 007, 009 et 010** sont `mode=parametrique`; leurs tableaux `parametres.instances` contiennent **trois cas approuvés chacun**, avec grilles, valeurs et corrigés. Les autres sont `mode=fixe` et portent `seed=null`, `parametres=null`.
- La sélection est **mathématiquement déterministe** : `index = seed modulo 3`, indices 0, 1 ou 2. Seeds stables : 2028, 2030, 2027, 2029 dans cet ordre. On ne dépend d'aucun générateur pseudoaléatoire externe.
- **Variables** : nombres de cases pleines par rangée (entiers positifs, ici de 1 à 5), rangées en nombre borné, mesure de côté de case soit `1 cm` soit inconnue. Les limites et instances admissibles propres à chaque item sont contenues dans `BANQUE_ITEMS.json`.
- **Construction** : toutes les lignes ont la largeur maximale `W` (complétées de `.`); `#` représente une case occupée entière et `.` une case vide. Nombre de cases `S = somme(des largeurs de rangées)`. Aire = `S×c² cm²` si côté `c` connu; sinon `S u²`.
- **Vérification indépendante de toutes les variantes** : recompter `#` et vérifier `S = W×H − nombre_de_points`. Une erreur entre les méthodes invalide le cas; la graine ne suffit jamais à rendre un corrigé sûr sans cette vérification.
- **Variations interdites** : fractions de cases non prévues, tirage libre, changements d'échelle sans recalcul carré, nouveau dessin non audité ou remplacement contextuel modifiant la cible.

## Conditions des deux manifestations de maîtrise

1. **A (`q-009`)** : affiche d'exposition, quadrillage **métré**, figure rectangulaire pleine, deux stratégies addition et multiplication.
2. **B (`q-010`)** : jardinière fictive, quadrillage **sans unité physique**, figure composée avec cases vides, somme des rangées et complément.
3. Exiger **autonomie sans indice sur les cases, l'opération ou le résultat** pendant chaque prestation; lecture à voix haute ou aide matérielle non directive permise.
4. Pour chaque preuve, noter : résultat, unité, méthode, deuxième vérification, aide éventuelle. **Deux preuves satisfaisantes sont nécessaires; une bonne moyenne ne suffit pas.**
5. Si un résultat/une unité/un raisonnement essentiel est faux, cibler la remédiation, puis administrer une **nouvelle instance prévalidée** après entraînement; ne pas transformer rétroactivement la même copie.

## Difficulté, accessibilité et sûreté

**Initial** : unité, comptage; **intermédiaire** : soustraction de cases vides et décomposition; **transfert** : échelle de case et contextes distincts. Tous les visuels peuvent être lus rangée par rangée et présentés en relief ou imprimés agrandis, avec la **même géométrie** et la même longueur de côté. L'évaluateur n'exige ni précision graphique de motricité fine ni vitesse : dictée à scribe neutre et contrôle oral acceptables. Aucun objet coupant ou mesurage physique risqué requis; activité sur papier. Pas de photos d'élèves nécessaires.

## Statut et limites

Les dix items sont `a_revoir`. Le calcul et la structure peuvent être vérifiés automatiquement, mais les seuils, la formulation, la validité en classe et l'équité des aides requièrent une révision humaine. Aucune conformité ou approbation PFEQ n'est inférée.
