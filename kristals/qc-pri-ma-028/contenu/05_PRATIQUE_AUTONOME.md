# 05 — Quatre pratiques autonomes avec corrigés | `qc-pri-ma-028`

**Consigne constante :** écrire (ou communiquer) **nombre et unité**, montrer un comptage vérifiable et contrôler le résultat autrement. Pas de pointage de cases par l'enseignant pendant l'essai. La réponse peut être saisie, dite ou montrée sur un tableau accessible. `#` signifie carré occupé; `.` signifie vide.

## A1 — Couverture en rangées, unité non métrée

**Énoncé :** « Une couverture est représentée par un rectangle de cinq colonnes et deux rangées de cases carrées identiques. Aucune mesure de côté n'est donnée. Quelle est son aire ? »

```text
#####
#####
```

**Corrigé :** `5+5 = 2×5 = 10 u²`. **Justification attendue :** dix `#` recouvrent toute la figure, et l'unité n'est pas en cm² sans échelle. **Erreur à détecter :** écrire 10 cm² au lieu de 10 u².

## A2 — Mosaïque en escalier

**Énoncé :** « Trouve l'aire en unités carrées et donne le nombre de cases dans chaque rangée. »

```text
###.
##..
.#..
```

**Corrigé :** `3+2+1 = 6 u²`. Les cases vides ne comptent pas. **Contrôle :** quadrillage complet 4×3 = 12 positions dont six vides → six occupées. **Critères :** 6 u², rangées 3,2,1, justification de l'exclusion des `.`.

## A3 — Carreaux plus grands

**Énoncé :** « Une plaque contient six carreaux en rectangle de trois colonnes et deux rangées. Chaque carreau est un carré de côté **2 cm**. Quelle est l'aire en cm² ? »

```text
###
###
```

**Corrigé :** `6 cases × (2 cm × 2 cm) = 6 × 4 cm² = 24 cm²`. **Contrôle :** largeur réelle 6 cm, hauteur 4 cm, donc `6×4 = 24 cm²`. **Erreur typique :** répondre 12 cm² en confondant 2 cm et 2 cm².

## A4 — Plateau troué

**Énoncé :** « Un plateau est formé de quatre colonnes et trois rangées de carrés identiques; deux cases du milieu sont vides. Détermine l'aire de la partie occupée et donne deux méthodes. »

```text
####
#..#
####
```

**Corrigé :** `4+2+4=10 u²`; ou rectangle englobant `4×3=12 u²` moins deux cases vides = `10 u²`. **Critères :** soustraction de deux trous distincts, 10 u², justification par une autre méthode. **Erreur :** 12 u² compte le vide.

## Auto-contrôle pour les quatre essais

1. Ai-je compté uniquement les `#` ?
2. Ai-je évité de compter deux fois une case commune à des morceaux ?
3. Ai-je indiqué `u²` ou une unité physique carrée seulement si les dimensions de case sont données ?
4. Mes deux stratégies sont-elles cohérentes ?

**Interprétation :** ces exercices entraînent l'autonomie, mais la maîtrise finale est documentée séparément avec les contextes `q-009` et `q-010`.
