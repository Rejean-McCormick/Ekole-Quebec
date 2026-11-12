# 01 — Notions et exemples : une observation, une catégorie

**Objectif `obj-1` :** Collecter des données selon une question et produire un tableau fiable.  
**Preuve `crit-1` :** Construire un tableau sans omission à partir d’observations brutes.

## Sens des quatre notions

1. **Catégorie.** Étiquette commune définie par la question (« forme : rond / carré / triangle »). Dans nos relevés fermés, toutes les observations admises se classent dans **une et une seule** catégorie. Si l'étiquette dépend d'une opinion ou chevauche une autre, elle est inadaptée à une lecture univoque.
2. **Relevé.** Suite des observations telles qu'elles arrivent, notées une par une. « rouge, bleu, rouge » contient **trois** observations, même si seulement **deux** mots différents apparaissent. Chaque occurrence compte.
3. **Effectif.** Nombre de fois qu'une catégorie apparaît dans le relevé. Il s'agit d'un entier de 0 au nombre total observé; le zéro est possible quand une catégorie prévue ne survient pas.
4. **Tableau d'effectifs.** Représentation avec une colonne pour les catégories, une pour le nombre d'observations de chacune, et éventuellement une ligne « Total ». Chaque catégorie autorisée a une ligne, même lorsque son effectif vaut 0.

**Algorithme humain contrôlable :** écrire la question et les catégories → numéroter mentalement ou matériellement chaque observation → une coche unique dans sa catégorie → compter les coches → construire le tableau → calculer la somme → contrôler avec un second parcours du relevé, par exemple en sens inverse. La somme seule est un signal nécessaire mais pas suffisant : deux erreurs opposées peuvent s'annuler.

## Exemple résolu 1 — Inventaire de crayons

Question : « Combien de crayons de chaque couleur? » Catégories : rouge, bleu, vert. Relevé dans l'ordre : `rouge, bleu, rouge, vert, bleu, rouge, vert`.

| Étape | Rouge | Bleu | Vert |
|---|---|---|---|
| Marques | `|||` | `||` | `||` |
| Effectifs | 3 | 2 | 2 |

| Catégorie | Effectif |
|---|---:|
| rouge | 3 |
| bleu | 2 |
| vert | 2 |
| **Total** | **7** |

**Vérification :** le relevé a 7 positions; rouge occupe 1, 3, 6; bleu 2, 5; vert 4, 7. Chaque position apparaît une fois et 3 + 2 + 2 = 7. Ne pas confondre **3 couleurs** avec **7 crayons**.

## Exemple résolu 2 — Étiquettes de formes

Question : « Combien d'étiquettes de chaque forme? » Relevé : `rond, carré, triangle, carré, rond, rond, triangle, carré`. Une case du tableau est créée pour chaque forme distincte proposée.

| Catégorie | Positions vérifiées | Effectif |
|---|---|---:|
| rond | 1, 5, 6 | 3 |
| carré | 2, 4, 8 | 3 |
| triangle | 3, 7 | 2 |
| **Total** | **1 à 8, chacune une fois** | **8** |

**Vérification indépendante :** cocher les huit positions de droite à gauche. Les mêmes catégories reçoivent 3, 3 et 2 marques, malgré l'ordre inversé.

## Deux contre-exemples commentés

**Erreur A — omission.** Relevé `rouge, rouge, bleu`; tableau proposé : rouge 1, bleu 1, total 2. Le second « rouge » a été ignoré. **Correction :** rouge 2, bleu 1, total 3. La répétition d'une même valeur est une nouvelle observation.

**Erreur B — catégories qui se chevauchent.** Relevé de fruits contenant deux pommes rouges et une poire verte; lignes « pomme = 2 » et « fruit rouge = 2 ». La même pomme peut compter deux fois. **Correction :** poser « Quelle sorte de fruit? » puis catégories `pomme = 2`, `poire = 1`, total 3; une observation par catégorie.

## Cas limites et vocabulaire utile

- Une catégorie prévue est absente : inscrire **0** (par exemple jaune 0, si jaune fait partie de la liste des catégories admissibles).
- Une même observation écrite deux fois correspond à deux occurrences **seulement si** ce sont bien deux observations brutes enregistrées (positions différentes); éviter une recopie accidentelle.
- Une valeur illisible ou hors catégories ne doit pas être attribuée arbitrairement : signaler l'incident et demander de clarifier la consigne avant de produire un tableau dit fiable.
- Un relevé doit permettre le contrôle de son effectif total. Les données d'apprentissage sont fictives et n'impliquent aucune information privée.
