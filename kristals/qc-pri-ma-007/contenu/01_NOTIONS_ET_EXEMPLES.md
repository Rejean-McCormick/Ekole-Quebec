# 01 — Notions, modèles et exemples (qc-pri-ma-007)

**But (`obj-1`) :** Modéliser la soustraction comme retrait, différence ou complément. Dans tout ce module, les valeurs sont des nombres naturels; une soustraction `a − b` s'utilise avec `a ≥ b`. On écrit les unités s'il y en a.

## A. Trois questions différentes, une relation

**Retrait** : une quantité est présente, puis une partie est enlevée. Un stock initial de `a` objets perd `b` objets : le reste est `d = a − b`. On vérifie que `d + b = a`. Les objets enlevés et restants forment ensemble le stock initial. Expliquer un retrait sans le confondre avec une comparaison qui ne déplace rien.

**Comparaison (différence)** : deux quantités de même nature existent simultanément; on recherche de combien la plus grande `a` dépasse la plus petite `b`. La différence est `d = a − b`. La représentation utile est celle de **deux bandes de même point de départ** : bande longue `a`, bande courte `b`, segment supplémentaire `d`. Personne n'a nécessairement retiré quoi que ce soit. On vérifie `b + d = a`.

**Complément** : on connaît une partie déjà obtenue `b` et une cible `a` : combien faut-il **ajouter** pour atteindre la cible ? `b + d = a`, donc `d = a − b`. Le segment manquant `d` n'est ni le total ni la partie déjà obtenue.

**Relation inverse** : `a − b = d` et `b + d = a` forment deux écritures qui se vérifient. La vérification n'est pas la répétition de la soustraction : c'est le calcul de l'addition inverse. L'addition permet `b + d = d + b` mais **pas** d'intervertir les termes de la soustraction. Exemple : `14 − 6 = 8`, `8 + 6 = 14`; ce n'est pas `6 − 14 = 8`.

## B. Deux exemples complets et commentés

### Exemple résolu 1 — Retrait et schéma partie-partie-tout

**Énoncé.** Un club possède 32 cartes. Il en distribue 7. Combien de cartes reste-t-il ?

1. **Sens :** on enlève 7 à une collection initiale de 32; on cherche le reste.
2. **Matériel :** imaginer ou disposer 32 jetons; isoler 7 jetons et compter 25 jetons non distribués.
3. **Schéma en texte :** barre totale de 32 cases, séparée en une partie « distribuées : 7 » et une partie « restantes : ? ».
4. **Calcul :** `32 − 7 = 32 − 2 − 5 = 30 − 5 = 25` cartes.
5. **Contrôle inverse :** `25 + 7 = 32`. **Réponse : 25 cartes.** Le contrôle reconstitue le total initial.

### Exemple résolu 2 — Comparaison sans retrait

**Énoncé.** Un présentoir A contient 28 cahiers, le présentoir B en contient 19. Combien de cahiers de plus se trouvent dans A ?

1. **Sens :** deux quantités existent ensemble; il s'agit d'un **écart**, aucun cahier n'est retiré.
2. **Schéma en texte :** deux bandes alignées à gauche, l'une de 28 unités et l'autre de 19 unités; la partie qui dépasse mesure l'écart recherché.
3. **Complément :** `19 + ? = 28`. De 19 à 20, il manque 1; de 20 à 28, il manque 8; total `1 + 8 = 9`.
4. **Écriture :** `28 − 19 = 9` cahiers. **Vérification :** `19 + 9 = 28`. **Réponse : 9 cahiers de plus.**

### Exemple résolu 3 — Complément et cas frontière

**Énoncé.** Pour remplir une tablette de 20 contenants, 12 sont déjà placés. Combien manque-t-il de contenants ?

- Schéma : barre-cible de 20 séparée entre « présents : 12 » et « manquants : ? ».
- `12 + 8 = 20` et `20 − 12 = 8`; **il manque 8 contenants**.
- Si 20 contenants sont déjà placés : `20 − 20 = 0` et `20 + 0 = 20`; aucun contenant ne manque. La réponse zéro est valide.

## C. Contre-exemples à analyser

**Contre-exemple 1 — Addition abusive.** « 23 affiches bleues, 15 rouges : de combien les bleues dépassent-elles les rouges ? » Réponse fautive : `23 + 15 = 38 affiches`. **Pourquoi c'est faux :** 38 est le total des affiches, non la différence demandée. **Correction :** `23 − 15 = 8` affiches; `15 + 8 = 23`.

**Contre-exemple 2 — Soustraction fausse sans contrôle.** « Il y a 25 places, 9 sont occupées. » Réponse fautive : `25 − 9 = 14 places libres`. **Pourquoi c'est faux :** `14 + 9 = 23` et non 25. **Correction :** `25 − 9 = 16` et `16 + 9 = 25`.

**Contre-exemple 3 — Inversion incorrecte.** « 14 jetons, on en retire 6 » ne s'écrit pas `6 − 14 = 8`. La première quantité est le total d'origine : `14 − 6 = 8`, contrôle `8 + 6 = 14`.

## D. Mini-synthèse active

Avant d'écrire une opération, demander : « Est-ce que quelque chose disparaît réellement (retrait), est-ce que deux quantités sont comparées (différence), ou cherche-t-on ce qui manque pour atteindre un total (complément) ? » Écrire ensuite l'opération et **obligatoirement l'addition inverse**. Les tâches du cours et de l'évaluation utilisent le même critère `crit-1`.
