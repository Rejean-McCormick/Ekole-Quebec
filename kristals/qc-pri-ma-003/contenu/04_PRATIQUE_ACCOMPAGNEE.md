# 04 — Trois exercices guidés et indices dégressifs

**Consigne commune :** deux décompositions de même valeur, puis regroupement **inverse** qui retrouve exactement les quantités initiales. À chaque passage, écrire la somme 100C+10D+U pour vérifier.

## G1 — 264 : soutien concret complet

**Tâche :** « Écris 264 en C-D-U. Décompose-le d'une seconde façon en défaisant une dizaine. Refais le regroupement inverse. »

**Indices initiaux :** tableau `C = 2 | D = 6 | U = 4`; dessiner six bandes, en barrer **une**, ajouter **dix** points. Questions « combien reste-t-il de bandes? de points? »

**Corrigé commenté :** `2 C + 6 D + 4 U = 200 + 60 + 4 = 264` ; `2 C + 5 D + 14 U = 200 + 50 + 14 = 264` ; **inverse :** regrouper 10 U -> 1 D, restituer `2 C + 6 D + 4 U`. **Contrôle :** 264 = 264.

**Feedback d'erreur :** si 2C+5D+5U (255), demander ce qu'une bande fournit réellement (10 jetons) avant tout autre indice.

## G2 — 317 : indice unique puis retrait

**Tâche :** « Écris 317 de deux façons différentes en échangeant une centaine contre dix dizaines, puis effectue le retour. »

**Indice uniquement au besoin :** « Une plaque de cent correspond à combien de bandes de dix? » Aucune colonne remplie à l'avance.

**Corrigé :** `3 C + 1 D + 7 U = 300 + 10 + 7 = 317` ; `2 C + 11 D + 7 U = 200 + 110 + 7 = 317` ; **inverse :** 10 des 11 D -> 1 C, restituer `3 C + 1 D + 7 U`.

**Feedback d'erreur :** si 2C+10D+7U (307), montrer que la dizaine initiale doit rester : `1 D + 10 D = 11 D`.

## G3 — 580 : aucune aide en premier essai

**Tâche :** « Trouve deux décompositions de 580 en conservant la valeur et démontre le regroupement inverse. Choisis un échange entre centaine et dizaines. »

**Rétroaction graduée :** 1) demander de comparer les sommes; 2) seulement en cas de blocage, rappeler `1 C = 10 D`; 3) en dernier recours, montrer une plaque remplacée par 10 bandes. Retirer tout appui sur une seconde tentative.

**Corrigé :** `5 C + 8 D + 0 U = 500 + 80 = 580` ; `4 C + 18 D + 0 U = 400 + 180 = 580` ; **inverse :** 10 D -> 1 C, `5 C + 8 D + 0 U`. Zéro unité conservé.

**Feedback d'erreur :** si 5C+18D (680), l'élève a ajouté dix dizaines **sans retirer** une centaine; marquer la plaque retirée.

## Observation et sortie

Noter séparément : représentation initiale, exactitude de la seconde, preuve de conservation, inverse, et niveau d'indice (`détaillé`, `bref`, `aucun`). L'étape suivante exige au moins un essai complet sans suggestion de méthode; sinon reprendre l'échange précis, puis proposer un nouveau nombre.
