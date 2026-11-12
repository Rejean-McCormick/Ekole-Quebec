# Plan d'évaluation — `qc-pri-ma-001` (v1.2)

**Lien obligatoire pour tous les items :** `objectif_id = obj-1` (associer quantité, comptage exact et représentation); `critere_id = crit-1` (dénombrer deux collections inédites et vérifier autrement); `family_id = qc-pri-ma-001-ev-01`. **Mode de famille :** `paramétrique_controle` au niveau du blueprint; chaque item déclare indépendamment son mode compatible `fixe`, `parametrique` ou `scenario_controle`.

## Table de couverture et poids

| Item complet | Mode | Difficulté | Collection / contexte | Représentation essentielle | Usage |
|---|---|---|---|---|---|
| `qc-pri-ma-001-q-001` | `fixe` | initial | 4 disques | unités et groupes de 2 | formative |
| `qc-pri-ma-001-q-002` | `parametrique` | initial | jetons alignés | symboles → marques | formative |
| `qc-pri-ma-001-q-003` | `fixe` | initial | ensemble vide | zéro | formative |
| `qc-pri-ma-001-q-004` | `parametrique` | intermediaire | cartes en rangées | rangées → points | formative |
| `qc-pri-ma-001-q-005` | `parametrique` | intermediaire | pions par paquets | paquets → notation | formative |
| `qc-pri-ma-001-q-006` | `fixe` | intermediaire | six cercles; erreur simulée | repérage d’erreur | formative |
| `qc-pri-ma-001-q-007` | `parametrique` | intermediaire | étoiles en deux plateaux | deux rangées → dessin | formative |
| `qc-pri-ma-001-q-008` | `parametrique` | intermediaire | carrés à apparier | schéma → jetons | formative |
| `qc-pri-ma-001-q-009` | `fixe` | intermediaire | deux boîtes | conservation du cardinal | formative |
| `qc-pri-ma-001-q-010` | `parametrique` | transfert | cailloux en rangées | rangées → cases | transfert |
| `qc-pri-ma-001-q-011` | `scenario_controle` | transfert | bibliothèque : étiquettes | dessin, jetons, contrôle | preuve A |
| `qc-pri-ma-001-q-012` | `scenario_controle` | transfert | jardin : pots | manipulation, groupes | preuve B |


**Couverture :** correspondance terme à terme q-001/002/004/006/007/008; cardinalité q-001/003/009 et tous les autres; groupement disjoint et contrôle q-004/005/007/009/010/011/012; transfert réel fictif q-010/011/012. Tous les items exigent la justification ou trace du processus, pas une réponse choisie au hasard.

**Poids d'observation, sans moyenne décisive :** quatre dimensions par item — (C1) unités comptées une seule fois, (C2) cardinal exact, (C3) représentation exhaustive, (C4) deuxième contrôle distinct. Pour le suivi formative possible « acquis / en progrès / non observé » par dimension. **La décision finale exige séparément q-011 et q-012** selon la grille; elle ne se déduit pas d'une somme de points et aucune compensation inter-épreuve n'est permise pour une dimension critique.

## Paramétrage contrôlé et reproductibilité

Les **six** items `q-002`, `q-004`, `q-005`, `q-007`, `q-008`, `q-010` sont paramétriques. Pour tout entier `seed >= 0`, poser `r = (7*seed + 3) % 97`, puis `n = min + (r % (max-min+1))`; `%` désigne le reste euclidien non négatif. Le nombre `n` appartient donc toujours à la plage inclusive annoncée dans `BANQUE_ITEMS.json`. Par exemple, pour `seed = 0, min = 4, max = 9`, `r=3` et `n=7`. **Ce n'est pas un générateur cryptographique** : un algorithme simple de construction reproductible.

Le générateur matérialise `n` occurrences d'un seul symbole objet (sans compter les séparateurs), en ligne, deux rangées, groupes de cinq ou rangées de trois; l'algorithme, les paramètres, les exemples de seeds, l'instance source et la solution de chaque item figurent dans la banque. Les solutions sont `n` et une représentation de `n` unités; la partition contrôle le total par une somme. **La vérification indépendante** consiste à compter séparément les occurrences du symbole et à additionner les tailles de groupes, puis à comparer à `n`, sur tous les seeds de tests. Les données arbitraires et la génération libre par IA sont interdites.

**Bornes et cas limites :** contenus de 0 à 20 unités; q-003 teste explicitement 0 et son inspection; les paramétriques ont une borne minimale ≥4 et des maxima ≤19 pour éviter un ensemble vide au moment d'une tâche exigeant un comptage unitaire. Les groupes de cinq incluent leur **reste**, même 1 à 4. Toutes les pièces figurent exactement une fois, sans chevauchement. Les dispositions peuvent changer uniquement suivant l'algorithme indiqué; une variation nouvelle doit être soumise à revue.

## Preuves de maîtrise (deux manifestations indépendantes)

**A — q-011 : bibliothèque, 14 étiquettes.** La présentation à trois rangées (4,5,5) ne contient pas une réponse numérale. La correction cachée de l'élève est : cardinal **14**, 14 marques et contrôle dans une nouvelle organisation (par exemple 5 + 5 + 4). Procédure initiale et contrôle consignés séparément.

**B — q-012 : jardin, 17 pots.** Présentation différente, cinq plates-bandes (4,4,4,4,1). Correction cachée : cardinal **17**, 17 marques et regroupement nouveau (par exemple 5 + 5 + 5 + 2). Réponse et procédure doivent être **autonomes**. Les objets, le contexte, l'agencement et la quantité diffèrent de A et des exercices de modelage. Ne pas montrer à l'apprenant les parties `reponse_attendue`, `feedback` ni `parametres.instance` avant la passation.

**Critère de décision :** chaque preuve (A et B), sans aide de calcul, vérifie C1–C4 au niveau acquis. Si une échoue, restituer un feedback ciblé et administrer deux **nouvelles** collections de difficulté et modalités comparables après remédiation; les deux épreuves originales ne suffisent pas à elles seules à « certifier » un élève.

## Sécurité, équité, accessibilité et intégrité

- Symboles en police lisible, grand espacement et contraste; alternatives manipulables/tactiles, présentation orale neutre, cases adaptées; pas de dépendance à la vision des couleurs, à la lecture fluente ni à la calligraphie.
- Les labels de contexte ne doivent jamais ajouter d'unités fictives. `|`, titres, espaces et retours à la ligne **ne sont pas** comptés.
- Pas de données personnelles ni de gestes dangereux. Préférer de gros jetons stables; les scénarios jardin/bibliothèque sont fictifs et culturellement génériques.
- Les consignes peuvent être lues par un tiers, **sans indiquer les effectifs, les groupes du corrigé ni guider le contrôle**. Noter tout indice de calcul donné par inadvertance.
- Séparer la vue élève (consigne + stimulus) de la vue correcteur (attendu + rubrique); un intégrateur LMS doit gérer cette séparation. Aucun mécanisme technique de protection d'une banque JSON non chiffrée n'est fourni par cette livraison.
- Les items sont tous en statut `a_revoir`. Une revue mathématique et linguistique humaine, des essais réels, et une qualification du système restent requis.
