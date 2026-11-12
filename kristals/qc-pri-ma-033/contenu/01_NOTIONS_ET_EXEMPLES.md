# 01 — Notions, exemples et contre-exemples

**Kristal :** `qc-pri-ma-033` · `obj-1` · Mathématique  
**Cible :** Communiquer un raisonnement mathématique vérifiable, au-delà du résultat.

## Qu'est-ce qu'une démarche mathématique vérifiable?

Une solution peut être juste sans que l'on sache *pourquoi*. Ici, on doit pouvoir retracer ce que chaque nombre représente et expliquer le passage d'une étape à la suivante. La trame commune est : **Je représente → je calcule en justifiant → je contrôle autrement → je conclus → je vérifie l'erreur proposée par quelqu'un.**

- **Justification** : raison fondée sur les données et une propriété ou une opération adaptée. « Il y a 4 groupes de 6, donc 4 × 6 » relie les données à l'opération; « parce que c'est la réponse » ne le fait pas.
- **Représentation** : dessin annoté, objets disposés en groupes, tableau structuré, expression ou langage symbolique donnant le même sens aux quantités. Chaque étiquette identifie une quantité et son unité; la représentation doit pouvoir être lue sans deviner.
- **Contrôle** : vérification *indépendante* de la démarche initiale. Exemple : après avoir trouvé 17 objets restant de 20 lorsqu'on en retire 3, faire 17 + 3 = 20. Un raisonnement peut comporter une erreur d'opération malgré une égalité arithmétiquement vraie.
- **Conclusion** : réponse complète à la question, avec la grandeur et l'unité appropriées : « Il reste 17 livres », et non « 17 m » ou « 17 » sans contexte.
- **Erreur d'autrui** : montrer où une opération perd le sens des nombres ou où une conclusion ne suit pas des étapes, **même si une réponse semble tomber juste par hasard**.

## Exemple résolu 1 — Groupes puis retrait

**Situation.** Il y a quatre paniers contenant chacun cinq pommes; on vend trois pommes. Combien en reste-t-il?

1. **Données et modèle concret** : dessiner 4 paniers; déposer mentalement 5 jetons par panier. L'étiquette « panier » donne le nombre de groupes; « pommes/panier » donne le contenu de chacun.
2. **Schéma textuel** : `[5 pommes] [5 pommes] [5 pommes] [5 pommes]` puis `− 3 pommes`.
3. **Calcul justifié** : `4 × 5 = 20 pommes` au départ; `20 − 3 = 17 pommes`. Le facteur 4 compte les paniers, le facteur 5 les pommes par panier.
4. **Contrôle distinct** : `17 + 3 = 20` et `5 + 5 + 5 + 5 = 20`. Les 17 restantes et les 3 vendues restituent bien le total initial.
5. **Conclusion** : « Il reste **17 pommes**. »
6. **Raisonnement fautif analysé** : « 4 + 5 − 3 = 6 pommes. » La première étape additionne des paniers et des pommes par panier comme s'il s'agissait d'objets de même unité. La réparation est de construire quatre groupes de cinq avant de retirer trois pommes.

## Exemple résolu 2 — Partage exact

**Situation.** On répartit 28 cartes également entre quatre équipes. Combien de cartes par équipe?

1. **Représentation** : 4 colonnes (équipes) et placer une carte successivement dans chaque colonne, jusqu'à utiliser les 28 cartes; chaque colonne en a 7.
2. **Relation** : `28 cartes ÷ 4 équipes = 7 cartes/équipe`. La division répond « combien pour chaque équipe? » et non « combien reste-t-il si on enlève quatre cartes? ».
3. **Contrôle** : `4 équipes × 7 cartes/équipe = 28 cartes`.
4. **Conclusion** : « Chaque équipe reçoit **7 cartes**. »
5. **Raisonnement fautif analysé** : « 28 − 4 = 24 cartes par équipe. » Le calcul 28−4 est exact en lui-même, mais ne représente pas un partage en quatre groupes égaux. Le contrôle 24×4=96, différent de 28, met l'erreur en évidence.

## Exemple résolu 3 — Le bon résultat ne garantit pas la bonne justification

**Situation.** Un rectangle mesure 6 m de longueur et 2 m de largeur. Quelle longueur de ruban faut-il pour entourer son bord?

- **Représentation** : parcourir ses quatre côtés : `6 m` (haut) + `2 m` (droite) + `6 m` (bas) + `2 m` (gauche).
- **Raisonnement correct** : `6 + 2 + 6 + 2 = 16 m`; également `2 × (6 + 2) = 16 m`.
- **Contrôle** : deux côtés longs totalisent `12 m`, deux petits `4 m`, donc `12+4=16 m`.
- **Conclusion** : « Il faut **16 m de ruban**. »
- **Erreur subtile** : « Le périmètre vaut longueur × largeur + 4. Donc 6 × 2 + 4 = 16 m. » Le **résultat coïncide**, mais la règle mélange des unités : `6 m × 2 m` donne une **aire** en m²; on ne peut pas y ajouter `4 m` pour obtenir une longueur. Un contre-test de `5 m × 3 m` donne `5×3+4=19` avec cette mauvaise règle, alors que `5+3+5+3=16 m` : ce n'est pas une justification valide.

## Contre-exemples commentés

**CE1 : résultat nu.** « Réponse : 17. » Même si 17 est juste, il manque l'unité, le sens du calcul et un contrôle. **Réparer** : identifier objets et transformation; fournir une ligne de calcul, un contrôle distinct et la phrase « Il reste 17 pommes ».

**CE2 : contrôle circulaire.** « J'ai vérifié 4×5−3 en refaisant 4×5−3. » Cela répète l'opération sans apporter un regard indépendant. **Réparer** : recomposer `17+3=20` ou dessiner les quatre groupes de cinq.

**CE3 : critique non diagnostique.** « L'autre élève s'est trompé; moi j'ai bon. » Aucune étape n'est identifiée. **Réparer** : « En écrivant 4+5, il confond quatre groupes et cinq éléments par groupe; on doit calculer 4×5 avant de retirer 3. »

## À retenir avant les exercices

Deux méthodes différentes peuvent être valables si elles traduisent les mêmes quantités. Une égalité arithmétiquement correcte peut décrire la **mauvaise opération** pour la situation. Dire *d'où vient chaque nombre* et vérifier la cohérence des unités vaut mieux que chercher seulement une réponse qui semble plausible.
