# Plan d'évaluation — `qc-pri-st-020` (v1.2)

**Objectif `obj-1` :** Représenter des interactions alimentaires et environnementales d’un habitat.  
**Critère `crit-1` :** Construire un réseau simple et prédire l’effet d’un changement de ressource.  
**Famille v1.2 inchangée :** `qc-pri-st-020-ev-01`, type `generee_sous_contraintes` exécuté par **items fixes et deux scénarios contrôlés**. Tous les items ont `objectif_id=obj-1`, `critere_id=crit-1`, `family_id=qc-pri-st-020-ev-01` dans le JSON. Les exercices partiels sondent une dimension de cette même cible, ils ne démontrent pas la maîtrise à eux seuls.

## Plan de couverture et difficulté

| Item exact | Difficulté | Représentation | Ce qui est évalué | Utilisation |
|---|---|---|---|---|
| `qc-pri-st-020-q-001` | initial | chaîne à partir de phrases | Sens aliment→consommateur, deux arêtes | formatif |
| `qc-pri-st-020-q-002` | initial | tableau vers graphe | Deux chemins, bifurcation, quatre arêtes | formatif |
| `qc-pri-st-020-q-003` | initial | graphe et note | Séparer ressource environnementale et alimentaire | formatif |
| `qc-pri-st-020-q-004` | intermédiaire | réseau 4 liens + texte | Effets directs/indirects prudents | formatif |
| `qc-pri-st-020-q-005` | intermédiaire | critique d'un réseau | Lien sans preuve vs donnée explicite | formatif |
| `qc-pri-st-020-q-006` | intermédiaire | chaîne + classement | Observation manquante, modèle, inférence | formatif |
| `qc-pri-st-020-q-007` | intermédiaire | réseau convergent | Deux aliments d'un consommateur et compensation possible | formatif |
| `qc-pri-st-020-q-008` | transfert | réseau + critique d'affirmation | Limite d'un impact prétendu certain | préparation transfert |
| `qc-pri-st-020-q-009` | transfert | graphe de prairie A + justification | **Preuve autonome A** : cinq arêtes, deux chaînes, ressources, effets et incertitude | décision A |
| `qc-pri-st-020-q-010` | transfert | graphe de mare B + justification | **Preuve autonome B** : 5 arêtes, chemins alternatifs, effets et incertitude | décision B |

## Représentations et réponses attendues

La consigne fournit toujours toutes les relations alimentaires retenues; l’élève rend soit un graphe orienté, soit une liste d'arêtes « consommé→consommateur » avec regroupements en chaînes. Les justifications peuvent être écrites, orales, en pictogrammes soutenus par langage, ou dictées à un scribe **non directif**. L'exactitude scientifique repose sur le sens du lien et sur une inférence **proportionnée aux données**, pas sur la qualité du dessin ni la reconnaissance d'espèces locales.

**M1 :** sens et exhaustivité des arêtes autorisées, sans extrapolation. **M2 :** au moins deux chaînes interconnectées. **M3 :** effet direct et effet indirect plausibles, chemin causal montré. **M4 :** distinction explicite donnée/prediction et incertitude. **M5 :** autonomie de construction et de justification. Se reporter à `evaluation/GRILLE_MAITRISE.md`.

## Exécution reproductible des scénarios contrôlés

- Le fichier JSON contient un **catalogue fermé** `prairie_A` / `mare_B` avec organismes, cartes, cinq arêtes exactes, deux chemins, modification de ressource et conditions des réponses.
- **Règle déterministe :** `q-009` reçoit toujours `prairie_A`; `q-010` reçoit toujours `mare_B`. Aucune valeur ou espèce n'est tirée au hasard. `seed=null`, `parametres=null` sont donc explicites. Réaffecter le scénario au hasard n'est pas autorisé.
- **Algorithme de correction structurelle :** parser les flèches comme paires ordonnées; comparer *l'ensemble exact* à `aretes_attendues`; contrôler les deux listes de `chaines_attendues` (un chemin s'obtient par succession de paires); la prédiction reçoit une grille humaine M3/M4 selon la carte et l'incertitude citée. Une réponse alternative exprimant les mêmes paires et les mêmes réserves est recevable, pas de notation lexicale automatique aveugle.
- **Cas limites :** une arête en sens inverse est fausse; ajouter eau→poisson comme flèche alimentaire sans carte est faux; une prédiction de mortalité certaine ne découle pas du graphe; un chemin alimentaire ne dit rien des effectifs futurs. Aucun générateur IA libre ni probabilité chiffrée.

## Deux preuves autonomes et décision

1. Présenter la totalité du scénario A, puis B à une autre occasion ou dans un moment distinct. Les supports d'accès sont décidés **avant** la prestation; aucun exemple de flèche ni commentaire de solution pendant.
2. Consigner séparément pour chaque épreuve arêtes, deux chaînes, effet direct, effet indirect, condition/incertitude et aide réellement reçue.
3. Exiger une démonstration complète de M1–M5 sur chaque contexte. Une faiblesse sur B ne se compense pas par une note élevée sur A; diagnostic de l'écart et nouvelle observation après remédiation.

## Accessibilité, sûreté et limites

Les chaînes des scénarios sont **des cartes didactiques fictives** dont la validité est interne à la tâche. Sources sur transferts d'énergie et dépendances : National Geographic Education et NASA (voir `sources/REFERENCES_CONTENU.md`). Aucune expérience sur un organisme ou manipulation hors papier n'est prescrite. Variations **d'accès seulement** : taille du texte, tableau d'arêtes, schéma tactile, enregistrement oral si consentement approprié; le corrigé scientifique ne varie pas. Items `a_revoir`, revue humaine, vérification écologique et essai des grilles toujours requis avant usage institutionnel.
