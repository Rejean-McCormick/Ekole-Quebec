# Plan d'évaluation — `qc-pri-ma-027` (v1.2)

**Objectif unique `obj-1` :** Calculer et interpréter le périmètre d’une figure comme longueur du contour. **Critère unique `crit-1` :** Trouver le périmètre de deux figures et expliquer l’effet d’une modification. **Famille native :** `qc-pri-ma-027-ev-01` (`type=paramétrique_controle`). Les deux préalables stricts restent `qc-pri-ma-023`, `qc-pri-ma-025`; diagnostic équivalent admissible.

## Liens explicites de chaque item

| Item | Objectif | Critère | Famille | Difficulté | Représentation | Couverture | Utilité |
|---|---|---|---|---|---|---|---|
| `qc-pri-ma-027-q-001` | `obj-1` | `crit-1` | `qc-pri-ma-027-ev-01` | initial | côtés de polygone étiquetés + somme vérifiable | Choix du contour, pas de diagonale | formatif |
| `qc-pri-ma-027-q-002` | `obj-1` | `crit-1` | `qc-pri-ma-027-ev-01` | initial | rectangle coté + addition; segmentations cotées, addition numérique et explication vérifiable du contour | Addition des quatre côtés | formatif |
| `qc-pri-ma-027-q-003` | `obj-1` | `crit-1` | `qc-pri-ma-027-ev-01` | initial | côtés de polygone étiquetés + somme vérifiable | Distinction longueur/aire/unité | formatif |
| `qc-pri-ma-027-q-004` | `obj-1` | `crit-1` | `qc-pri-ma-027-ev-01` | intermediaire | liste ordonnée de six segments + regroupement; segmentations cotées, addition numérique et explication vérifiable du contour | Six côtés exacts d’un L | formatif |
| `qc-pri-ma-027-q-005` | `obj-1` | `crit-1` | `qc-pri-ma-027-ev-01` | intermediaire | côtés de polygone étiquetés + somme vérifiable | Côté inconnu par soustraction et vérification | formatif |
| `qc-pri-ma-027-q-006` | `obj-1` | `crit-1` | `qc-pri-ma-027-ev-01` | intermediaire | deux rectangles cotés + différence; segmentations cotées, addition numérique et explication vérifiable du contour | Modification d’une largeur, effet 2d | formatif |
| `qc-pri-ma-027-q-007` | `obj-1` | `crit-1` | `qc-pri-ma-027-ev-01` | transfert | rectangle puis L aux six côtés; segmentations cotées, addition numérique et explication vérifiable du contour | Encoche de coin, effet nul | formatif |
| `qc-pri-ma-027-q-008` | `obj-1` | `crit-1` | `qc-pri-ma-027-ev-01` | transfert | deux contours à l’échelle numérique, sans mesure de dessin; segmentations cotées, addition numérique et explication vérifiable du contour | Doublement de toutes les longueurs, effet ×2 | formatif |
| `qc-pri-ma-027-q-009` | `obj-1` | `crit-1` | `qc-pri-ma-027-ev-01` | transfert | plans de jardin avec quatre côtés étiquetés chacun; segmentations cotées, addition numérique et explication vérifiable du contour | Deux potagers rectangles : preuve autonome A complète | maîtrise A |
| `qc-pri-ma-027-q-010` | `obj-1` | `crit-1` | `qc-pri-ma-027-ev-01` | transfert | six côtés de chaque empreinte en L + schéma annoté; segmentations cotées, addition numérique et explication vérifiable du contour | Deux plateformes en L : preuve autonome B complète | maîtrise B |

## Progression, couverture et poids

Les items 001–003 établissent le contour, l'addition et l'unité; les items 004–006 ajoutent la figure concave, le côté manquant et la modification. Les items 007–008 forcent la comparaison causale; les items 009–010 évaluent **séparément** l'objectif complet dans des contextes réellement différents.

- **Formative :** `q-001` à `q-008`, sans décision terminale tirée d'un seul score.
- **Preuve A indispensable :** `q-009`, deux potagers rectangulaires avec largeur modifiée; deux périmètres, effet et justification.
- **Preuve B indispensable :** `q-010`, deux plateformes en L avec largeur extérieure modifiée et encoche conservée; six côtés par forme, deux périmètres, effet et justification.
- **Critères de maîtrise :** repérage du contour, exactitude et unités des deux calculs, explication mathématique de l'effet, autonomie. Tous doivent être suffisants dans chaque contexte, sans moyenne compensatoire.

## Moteur déterministe des sept items paramétriques

Les items `q-002`, `q-004`, `q-006`, `q-007`, `q-008`, `q-009`, `q-010` ont chacun **trois variantes fermées**. Chaque banque décrit les domaines, contraintes, formule, algorithme de résolution, variante initiale et corrigé de toutes les variantes. **Algorithme unique :** `index = seed % 3`; sélectionner exactement `parametres.variantes[index]`. Chaque `seed` vaut `27000 + numéro` et ne change pas; aucun appel aléatoire ou tirage d'IA. Les versions `parametres.variantes[*].resultats` sont recalculées et comparées à `verification_independante` pour les 21 variantes.

| Figures | Calcul direct par côtés | Vérification indépendante | Cas limites contrôlés |
|---|---|---|---|
| Rectangle W×H | `W+H+W+H` | `2(W+H)` | `W,H>0`, unité commune |
| Rectangle élargi de d | `W,H,W,H` puis `W+d,H,W+d,H` | effet `2d` | `d>0` |
| L orthogonal, encoche supérieure droite w×h | `W,(H−h),w,h,(W−w),H` | `2(W+H)` uniquement pour **cette** encoche de coin | `0<w<W`, `0<h<H` |
| L élargi en W, encoche w×h fixe | listes des six segments avant/après | `P₂−P₁=2d` | `d>0`, encoche conservée |
| Rectangle avec W,H doublés | deux listes de quatre côtés | `P₂=2P₁` | unités inchangées |

**Attention à la validité :** l'égalité `P_L = 2(W+H)` concerne ici un rectangle amputé **d'un coin**, pas une figure présentant un trou interne ou une encoche quelconque en plein milieu d'un côté. Les dessins ne sont jamais supposés à l'échelle. Tout item utilise un catalogue verrouillé, pas une variation contextuelle générée par IA.

## Consignes d'administration, sécurité et accessibilité

Les figures ont des longueurs données en `cm` ou `m`. Exposer sans préciser la réponse, permettre énoncé oral, gros caractères, schéma contrasté ou relief, lecture de la liste des côtés et dictée de la démarche; éviter d'évaluer l'écriture manuscrite. Consigner l'aide réellement donnée : aide d'accès **non directive** admise; choix des côtés, somme et interprétation faits par l'apprenant seul pour les preuves de maîtrise. Aucun couteau, ciseau ni manipulation dangereuse requis.

Deux essais autonomes de maîtrise idéalement séparés dans le temps, avec contextes distincts, sans solution modèle fournie; si l'un est insuffisant, remédier puis administrer un nouvel item de niveau comparable révisé humainement. Les rubriques restent `a_revoir` et doivent être examinées par un spécialiste avant utilisation sommative.
