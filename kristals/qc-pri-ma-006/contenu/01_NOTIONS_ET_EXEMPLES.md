# 01 — Notions et exemples | qc-pri-ma-006

**Objectif `obj-1` :** Modéliser l’addition et choisir une stratégie efficace pour calculer. **Critère `crit-1` :** Résoudre deux additions distinctes et expliquer la stratégie adoptée.

## Les quatre notions (nombres naturels)

1. **Réunion.** On associe deux ensembles *disjoints* d'objets de même unité pour dénombrer leur total. Si A contient `a` objets et B contient `b` autres objets sans recoupement, la réunion contient `a + b` objets. Dire « 4 rouges et 3 bleus » ne suffit pas si un objet peut être dans les deux groupes : vérifier d'abord l'absence de doublon. On additionne des objets comparables (des livres avec des livres), non des mesures de types différents sans unité commune.
2. **Augmentation.** Une quantité de départ reçoit un ajout non négatif; l'état final est `départ + ajout`. Le mot « plus » ne donne pas seul le sens d'une situation : vérifier si l'on ajoute réellement des éléments. Quand l'ajout est 0, la quantité ne change pas.
3. **Décomposition additive.** On remplace un terme par des morceaux dont la somme égale exactement ce terme : `9 = 6 + 3` et `38 = 30 + 8`. Les parties peuvent être regroupées pour faciliter le calcul, sans perdre ni dupliquer de valeur : `(a + x) + y = a + (x + y)` si `b = x + y`.
4. **Somme.** Résultat d'une addition : les termes de `17 + 5 = 22` sont 17 et 5; leur **somme** est 22. Ajouter 0 ne change pas la somme; pour des naturels, elle est au moins aussi grande que chacun des termes.

**Domaine d'apprentissage proposé :** entiers naturels de 0 à 99 pour les deux termes, avec somme au maximum de 100. Ce bornage est un choix pédagogique interne, pas une règle scolaire officielle. Les calculs sont exacts; pas d'arrondi, pas de signes négatifs.

## Trois représentations de la même relation

- **Matériel.** Prendre `14` jetons et les séparer physiquement des `9` autres. Les rapprocher sans compter de jeton deux fois; on obtient 23 jetons.
- **Schéma textuel accessible.** Première barre « quatorze »; seconde barre « neuf », découpée en « six » et « trois ». Une barre réunie « vingt » + « trois ». Cette description remplace un dessin quand la vision, l'impression ou la couleur sont indisponibles.
- **Notation.** `14 + 9 = 14 + (6 + 3) = (14 + 6) + 3 = 20 + 3 = 23`. Les parenthèses signalent les regroupements et conservent exactement les neuf éléments ajoutés.

## Exemple résolu A — réunion de deux collections (matériel → schéma → symboles)

**Situation originale :** Dans un atelier, une boîte contient 14 pinces et une autre 9 pinces différentes. Combien y a-t-il de pinces en tout ?

1. Les deux groupes sont distincts et l'unité est la même (pince) : on fait une **réunion**. L'égalité cherchée est `14 + 9 = ?`.
2. On place 14 jetons sur une bande et 9 sur une autre. On déplace 6 des 9 vers les 14 pour constituer deux dizaines; il reste 3 jetons sur la deuxième bande.
3. `9 = 6 + 3`, donc `14 + 9 = 14 + 6 + 3 = 20 + 3 = 23` pinces.
4. **Contrôle indépendant :** compter 14, 15, 16, ... 23 en faisant 9 pas; le total est 23. Le résultat est plus grand que chaque groupe. La stratégie « compléter 20 » limite les comptages un par un.

## Exemple résolu B — augmentation et décomposition des dizaines

**Situation originale :** Un tracé compte déjà 38 cases; on lui ajoute 27 cases identiques. Quelle est sa longueur finale en cases ?

1. On part de 38 et on ajoute 27 : **augmentation**. On note `38 + 27`.
2. Représentation : 3 paquets de dix et 8 cases isolées; ajouter 2 paquets de dix et 7 isolées. Les 8 et 7 isolées forment 15 : un nouveau paquet de dix et 5 isolées.
3. `38 + 27 = (30 + 8) + (20 + 7) = (30 + 20) + (8 + 7) = 50 + 15 = 65` cases.
4. **Autre vérification :** `38 + 2 + 25 = 40 + 25 = 65` car `27 = 2 + 25`. Les deux procédures conservent 27 cases ajoutées. Ici « séparer dizaines et unités » explicite le report, et « compléter 40 » peut se faire mentalement.

## Contre-exemples argumentés

- **CE1 — oublier les unités regroupées :** « `26 + 17 = 33` parce que `20 + 10 = 30` et `6 + 7 = 3` ». *Incorrect :* 6 + 7 fait **13**, et non 3. Les 13 unités se recomposent en 1 dizaine + 3 unités. Ainsi `30 + 13 = 43` et `26 + 17 = 43`. Ce n'est pas une petite erreur de notation : une dizaine a disparu.
- **CE2 — appeler augmentation une diminution :** « Il y a 17 oiseaux, 5 s'envolent : j'écris `17 + 5 = 22` ». *Incorrect comme modèle de la situation :* des oiseaux ont quitté le groupe; la quantité finale est 12 (17 moins 5), donc ce n'est **pas** un cas d'augmentation. La phrase `17 + 5 = 22` est vraie arithmétiquement, mais elle ne représente pas l'histoire.
- **CE3 — doubler un objet :** « 3 élèves avec un chandail bleu et 4 avec un chandail à manches longues donnent forcément 7 élèves ». *Incorrect :* un même élève peut appartenir aux deux groupes. Pour additionner les tailles, les collections doivent être disjointes ou le recouvrement connu. Aucun total ne peut être affirmé avec ces seules données.

## Cas limites contrôlés

- `0 + 36 = 36` et `36 + 0 = 36` : zéro ajout ou groupe vide, pas de croissance.
- `9 + 1 = 10` : un nouveau paquet de dix; `48 + 12 = 60` : franchissement de dizaine avec unité finale zéro.
- `50 + 50 = 100` : somme maximale de ce microparcours; `99 + 2 = 101` dépasse volontairement le domaine **des items générés**, même si l'opération est mathématiquement définie.

**Question pour choisir une stratégie :** « Quel nombre est proche d'une dizaine ? Quels morceaux puis-je déplacer sans changer leur somme ? ». Accepter une méthode moins courte si elle est exacte, expliquée et vérifiable; l'efficacité se discute sans sanctionner un style cognitif.
