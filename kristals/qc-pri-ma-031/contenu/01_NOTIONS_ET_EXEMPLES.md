# 01 — Notions, exemples résolus et contre-exemples

**Kristal :** `qc-pri-ma-031` • `obj-1` : Lire, créer et critiquer une représentation graphique de données.  
Données de tous les exemples : **inventées à des fins d'apprentissage**, sans référence à un établissement réel.

## Définitions vérifiables

1. **Catégories** : étiquettes de groupes distincts, par exemple « jeu libre », « lecture », « dessin ». Chaque objet observé doit être classé selon une règle explicite; les groupes d'un même tableau ne se chevauchent pas.
2. **Axes** : repères du diagramme. Pour un diagramme à bandes verticales, l'axe horizontal affiche les catégories, tandis que l'axe vertical donne les quantités, l'unité et des graduations régulières. Une version horizontale inverse les rôles.
3. **Échelle** : correspondance fixe entre distance graphique et quantité. Sur le même axe, deux intervalles de même longueur doivent représenter la même augmentation. Pour les bandes représentant des effectifs, nous démarrons à **0**; exemple : 1 carré = 2 fiches, donc 3 carrés = 6 fiches.
4. **Diagramme à bandes** : dessin comparant les effectifs d'au moins deux catégories par des bandes de largeur uniforme dont la hauteur (ou longueur) est proportionnelle à la quantité. Les espaces entre les barres marquent les catégories distinctes. Une bonne représentation comprend titre, légendes d'axes, unité et échelle.

**Méthode de construction :** vérifier tableau et unités → nommer catégories → tracer le zéro sur l'axe numérique → choisir pas constant → reporter exactement les valeurs → vérifier chaque bande et formuler seulement ce que les données prouvent.

## Exemple résolu A — Midi inventé, échelle deux

Tableau : | Activité | Jeux | Lecture | Dessin |  
|---|---:|---:|---:|  
| Fiches | 4 | 6 | 2 |

Schéma textuel d'un diagramme **horizontal** (chaque `■` vaut 2 fiches) :

```text
Fiches (0, 2, 4, 6)
Jeux    |■■     = 4
Lecture |■■■    = 6
Dessin  |■      = 2
          0 2 4 6  (graduations régulières)
```

Résolution : Jeux = 2 × 2 = 4; Lecture = 3 × 2 = 6; Dessin = 1 × 2 = 2. Lecture dépasse Jeux de 6 − 4 = **2** fiches. Total = 4 + 6 + 2 = **12**. Une bande de trois blocs n'est pas égale à trois fiches.

## Exemple résolu B — Lecture inventée, échelle un

| Type de livre | Conte | Bande dessinée | Documentaire |
|---|---:|---:|---:|
| Prêts | 5 | 3 | 7 |

Chaque `■` représente 1 prêt : Conte `■■■■■` (5), Bande dessinée `■■■` (3), Documentaire `■■■■■■■` (7). Un diagramme vertical valide placerait les catégories en abscisse et **Prêts**, gradués de 0 à 7 par unités, en ordonnée. Total : 5 + 3 + 7 = **15**. L'affirmation « Les bandes dessinées sont les plus empruntées » est **fausse** : 3 < 7; les documentaires sont premiers **dans ce petit tableau fictif**, sans généralisation à toute bibliothèque.

## Contre-exemple 1 — Oublier l'échelle

On lit `■■■■` avec la légende « 1 bloc = 2 objets » et on écrit « 4 objets ». **Incorrect :** 4 × 2 = **8 objets**. Remédiation : associer deux jetons à chaque bloc, puis compter 2, 4, 6, 8.

## Contre-exemple 2 — Graduations déformées

L'axe montre 0, 2, 4, 8 sur quatre traits **également espacés**. Ce dessin ne respecte pas une échelle constante (les écarts sont 2, 2, 4). **Correction :** 0, 2, 4, 6, 8 sur cinq traits également espacés. Il serait trompeur de conclure que la dernière croissance est identique aux précédentes.

## Trois vérifications avant de conclure

- Les barres correspondent-elles aux catégories et nombres de la table, sans valeur inventée ?
- L'axe des quantités affiche-t-il le zéro, l'unité et un pas constant ?
- L'énoncé est-il vérifiable par une valeur, une différence ou une somme du tableau ? Si non, il reste une hypothèse.

## Références de méthode et droits

Faits généraux sur les barres : Statistique Canada, *5.2 Graphique à barres* (voir `sources/REFERENCES_CONTENU.md`). Tableaux, chiffres, schémas textuels et explications : créations originales destinées au présent Kristal.
