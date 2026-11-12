# Plan d'évaluation — `qc-pri-ma-029` (v1.2)

**Contrat :** `obj-1` — Déterminer un volume par comptage ou structuration d’unités cubiques. **Critère :** `crit-1` — Évaluer le volume d’un assemblage de cubes en montrant le comptage. **Famille :** `qc-pri-ma-029-ev-01`, type natif `paramétrique_controle`. Tous les items `q-001` à `q-010` sont liés à `obj-1`, `crit-1` et `qc-pri-ma-029-ev-01` dans la banque JSON; 1 à 8 sont fixes, 9 et 10 sont paramétriques déterministes.

## Tableau de traçabilité et de couverture

| Item complet | Difficulté | Représentation | Critère principal | Rôle |
|---|---|---|---|---|
| `qc-pri-ma-029-q-001` | initial | rangée de cubes | dénombrer un cube entier, non une face | formatif |
| `qc-pri-ma-029-q-002` | initial | grille 3×2 d'un niveau | grouper par rangées | formatif |
| `qc-pri-ma-029-q-003` | intermédiaire | pavé 2×2×3 | couches identiques et produit | formatif |
| `qc-pri-ma-029-q-004` | intermédiaire | plans de niveaux inégaux | somme plutôt que faux produit | formatif |
| `qc-pri-ma-029-q-005` | intermédiaire | deux pavés | volumes égaux, formes différentes | formatif |
| `qc-pri-ma-029-q-006` | intermédiaire | cubes masqués déclarés | dénombrement exhaustif | formatif |
| `qc-pri-ma-029-q-007` | intermédiaire | cubes de 2 cm d'arête | distinguer comptage et cm³ | formatif |
| `qc-pri-ma-029-q-008` | transfert | solide avec un retrait | mise à jour de la quantité | formatif avancé |
| `qc-pri-ma-029-q-009` | transfert | **pavé complet d'entrepôt** | **preuve autonome A :** unité + couches + calcul + justification | **maîtrise A** |
| `qc-pri-ma-029-q-010` | transfert | **maquette de gradins irréguliers** | **preuve autonome B :** unité + plans + somme + justification | **maîtrise B** |

## Génération déterministe contrôlée (uniquement 009–010)

**Schéma A / seed=290038** : `L=2+seed%3`, `P=2+(seed//3)%2`, `H=2+(seed//6)%2`; domaines `L=2..4`, `P=2..3`, `H=2..3`; les `H` plans sont pleins; formule `V=L×P×H`. Pour le seed fixé : L=3, P=3, H=3, `V=27 cm³`. Exemples supplémentaires : seed 0 → 8 cm³, seed 3 → 12 cm³. Chaque instance validée par comptage indépendant de tous les triplets (x,y,z).

**Schéma B / seed=290035** : `L=3+seed%2`, `P=2+(seed//2)%2`; domaines `L=3..4`, `P=2..3`, exactement deux plans : bas P rangées de L cubes pleins; haut première rangée de L cubes pleins, les autres vides. Formule `V=L×P+L`. Seed fixé : L=4, P=3, bas 12 et haut 4, `V=16 cm³`. Exemples : seed 0 → 9 cm³, seed 3 → 16 cm³. Validation indépendante par coordonnées et grille.

Les descriptions du `stimulus` sont des **instances réellement figées** pour ces deux seeds; réexécuter le générateur est une action contrôlée exigeant recalcul du libellé, des plans et du corrigé, et contrôle humain avant toute diffusion. **Aucune génération libre IA n'est admise.** `seed` est un entier stable, `parametres` expose formule, contraintes, domaines, valeurs et exemples vérifiés.

## Passation, critères, maîtrise

Présenter chaque contexte **sans modèle de solution** ni indices de décomposition. L'élève peut préparer un plan, puis compter à voix haute, par notes, pointeurs ou matériel adapté. Vérifier séparément (C1) unité de volume, (C2) couverture de toutes les positions occupées, (C3) calcul correct, (C4) autonomie et justification du choix de somme/produit. Les épreuves 9 et 10 sont distinctes et nécessaires **toutes les deux** : une même note totale ne suffit pas à trancher la maîtrise. Voir `evaluation/GRILLE_MAITRISE.md`.

## Variabilité permise, accessibilité et sécurité

Seuls moyens d'accès (police, relief, lecture orale, dictée non directive, manipulation par l'adulte **sur instruction de l'élève**) et les seeds admissibles *après revalidation complète* peuvent varier. Ne pas varier les axes, l'unité de 1 cm d'arête, la présence des cubes ou le nombre de niveaux au hasard. Blocs sûrs, grands et stables; pas d'ingestion ni de risque lié au matériel; vidéos et données personnelles non nécessaires. Le calcul reste exigé quelle que soit la modalité.

**Limite :** les scores, rubriques et scénarios sont `a_revoir` pour révision pédagogique et validation humaine; les calculs ont fait l'objet des contrôles techniques explicités dans le journal de livraison.
