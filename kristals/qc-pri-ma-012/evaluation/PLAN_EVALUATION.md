# Plan d'évaluation — `qc-pri-ma-012` / `qc-pri-ma-012-ev-01`

**Alignement immuable** : `obj-1` — « Représenter une fraction comme partie d’un tout ou d’une collection. »; `crit-1` — « Produire trois représentations correctes d’une même fraction simple. » Tous les items visent `obj-1` et alimentent `crit-1`. **Mode privilégié** : paramètres numériques contrôlés (catalogue fini + seed reproductible), construction et justification observables; aucune sortie générée librement.

## Matrice de couverture (10 items distincts)

| Item | Objectif / critère / famille | Difficulté | Représentation demandée | Contrôle attendu | Variation permise |
|---|---|---|---|---|---|
| `q-001` | `obj-1` / `crit-1` / `qc-pri-ma-012-ev-01` | initial | lire une surface | tout, `3/4`, rôle de 3 et 4 | fixe uniquement |
| `q-002` | mêmes liens | initial | lire une bande | `a/b`, parts égales | trois variantes du catalogue, seed |
| `q-003` | mêmes liens | intermédiaire | collection → groupes | `N=b*m`, `K=a*m`, `a/b` | trois lots exacts du catalogue |
| `q-004` | mêmes liens | intermédiaire | surface + bande | `a/b` sur deux touts | trois fractions exactes du catalogue |
| `q-005` | mêmes liens | intermédiaire | surface + bande + collection | correspondance de trois modèles | trois fractions/lots exacts du catalogue |
| `q-006` | mêmes liens | intermédiaire | contre-exemple d'aire | refuser trois aires inégales; corriger | fixe uniquement |
| `q-007` | mêmes liens | intermédiaire | collection → bande | 10/15 et 2/3 dans ce cas | fixe uniquement |
| `q-008` | mêmes liens | transfert | deux collections → aires | fraction identique, tout différent | fixe uniquement |
| `q-009` | mêmes liens | transfert, **preuve A** | jardin : surface + bande + collection | 3 représentations cohérentes sans indice | trois variantes jardin, seed |
| `q-010` | mêmes liens | transfert, **preuve B** | matériel : collection + surface + bande | 3 représentations cohérentes sans indice | trois variantes matériel, seed |

Tous les `item_id` complets sont préfixés `qc-pri-ma-012-` dans la banque JSON. Les « mêmes liens » signifient textuellement `obj-1`, `crit-1`, `qc-pri-ma-012-ev-01`; les métadonnées de chaque item enregistrent `objectif_id: obj-1`, le critère et la famille étant ancrés par la banque, ce plan et le contrat familial.

## Spécification de variation reproductible

Pour chaque item `mode=parametrique`, le JSON contient son **catalogue ordonné** de tuples `{a,b,m}`, une `seed` entière non négative, les domaines et l'algorithme. Calculer `i = seed % len(catalogue)` (modulo euclidien), puis `N=b×m` et `K=a×m`. Montrer `a` sur `b` parts d'aire égale, `a` sur `b` parts de longueur égale et/ou `K` sur `N` objets en `b` groupes de `m`, selon la consigne. Validation arithmétique **exacte** : `Fraction(K,N) == Fraction(a,b)`. Les textes d'items stockés sont les **instances concrètes déjà résolues** correspondant à leur seed; aucune génération de langage ou de variantes hors catalogue n'est autorisée.

- Domaines bruts : `b ∈ {2,3,4,5,6,8}`, `1 ≤ a < b`, `1 ≤ m ≤ 4` (entiers).
- Contraintes : parties contiguës ou non **d'aires égales** pour surface, **de longueurs égales** pour bande, **de même effectif** pour les groupes de collection; nommer l'unité.
- Ne pas remplacer une variante par un nombre pris « au hasard » : il faut un nouvel examen des contraintes, du calcul et du texte.
- Une seed identique et un catalogue identique redonnent exactement le même `a,b,m,N,K`; il ne s'agit pas d'une méthode cryptographique ni d'une véritable création d'items multiples.

## Règles de correction et preuves

**Grille dimensionnelle** dans [GRILLE_MAITRISE.md](GRILLE_MAITRISE.md). Pour `q-001` à `q-008`, relever erreurs par catégorie (unité, aire/longueur égales, lecture, collection, justification) et rétroagir. **Aucune somme de points** sur ces huit tâches ne prouve automatiquement la maîtrise. Pour `q-009` et `q-010`, valider **séparément** : trois représentations de natures distinctes pour la même fraction, unités explicites, conditions d'égalité respectées, regroupement exact et justification sans indice. Les deux sont nécessaires; ce sont des contextes **jardin** et **distribution de matériel** distincts.

**Barème de préparation facultatif** : sur chaque preuve, 5 dimensions notées `0` (absent/faux), `1` (partiel/après aide) ou `2` (valide autonome). La décision de maîtrise exige `2` pour les cinq dimensions **sur chacune des deux preuves**; aucun total compensatoire n'est permis. En cas de réussite d'une seule preuve, sélectionner une remédiation puis une nouvelle variante dans le contexte non maîtrisé, avec traçabilité de seed.

## Sécurité, accessibilité, impartialité

- Les supports peuvent être dessinés, tactiles, décrits oralement, pointés ou manipulés; la **relation mathématique** et la distinction entre surface/bande/collection demeurent vérifiables. Les symboles colorés ont toujours une variante par motif/étiquette; n'évaluer ni motricité fine ni acuité visuelle.
- Lecture de l'énoncé, police agrandie, temps ajusté, papier quadrillé et matériel non dangereux sont possibles. **Pas d'indice conceptuel pendant q-009/q-010**; sinon le statut est « accompagné » et on recommence à une autre séance.
- Contextes fictifs, aucune donnée personnelle, aucune tâche physique dangereuse, aucune production externe protégée intégrée.
- Revue humaine encore nécessaire : lisibilité des supports réels, biais contextuels, durée, clarté des conditions d'autonomie, étalonnage de la grille et essai apprenant. Statut `a_revoir`, jamais « certifié ».
