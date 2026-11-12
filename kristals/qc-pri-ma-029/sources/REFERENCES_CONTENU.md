# Références, provenance et droits — `qc-pri-ma-029`

## Sources vérifiées sur pièces

- **Source maîtresse du workspace** : archive `initbundle(1).zip`, dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Les textes source ci-dessous ont été lus et **n'ont pas été copiés dans le delta** :
  - `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — deux manifestations de maîtrise, méthode pédagogique et frontières hors PFEQ détaillé.
  - `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — champs de famille et paramètres vérifiés.
  - `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — appellation conservée « Mathématique », sans statut ministériel.
  - `registry/GRAPHE_PEDAGOGIQUE_202.json` — seuls `requires(qc-pri-ma-029,qc-pri-ma-022)` et `requires(qc-pri-ma-029,qc-pri-ma-025)` pour cet ID; aucun nouveau lien établi.
  - `kristals/qc-pri-ma-029/authoring/PARCOURS.md` et `CONTRAT_PEDAGOGIQUE.json` — identité, objectif, preuve, concepts, famille et métadonnées conservés et enrichis.
  - `kristals/qc-pri-ma-029/authoring/ALIGNEMENT.md`, `BRIEF_REDACTION.md` — titre, discipline, pistes et interdiction de prétendre à l'homologation. Fichiers conservés intacts dans le workspace.

- **Source externe vérifiée** : National Institute of Standards and Technology (NIST), *SI Units – Volume*, https://www.nist.gov/pml/owm/si-units-volume (consultée le 8 octobre 2026). Décrit le volume comme espace tridimensionnel et l'utilisation des unités cubiques; le mètre cube est l'unité SI dérivée. Cette référence ne certifie pas les items du projet.
- **Source externe vérifiée** : CAST (2024), *Universal Design for Learning Guidelines version 3.0*, « Action & Expression », https://udlguidelines.cast.org/action-expression/ (consultée le 8 octobre 2026). Sert à justifier des moyens d'expression multiples, pas une modification de l'objectif mathématique ni la validation d'une grille de scores.

## Raisonnements dérivés (non cités comme prescriptions institutionnelles)

- Une couche de L colonnes × P rangées **pleines** contient L×P cubes sans chevauchement; H couches identiques contiennent L×P×H; des couches inégales sont additionnées par les cases réellement occupées. Il s'agit de comptage combinatoire élémentaire sur le modèle déclaré.
- Un cube d'arête 1 cm mesure 1 cm³; d'arête 2 cm, 8 cm³. Aucune conversion de capacité non enseignée n'est requise pour maîtriser ce module.
- Les formules modulo et division entière dans `evaluation/BANQUE_ITEMS.json` sont des choix éditoriaux reproduisibles; les corriger par énumération indépendante des triplets occupés permet de contrôler les deux familles de cas, sans prétendre qu'elles reflètent un examen officiel.

## Productions originales et statut des droits

Sont rédigés spécifiquement ici : tous les tableaux et plans `■`/`·`, les scènes des colis, de la maquette et des gradins, les dix items et leurs corrigés, les matrices de paramètres, les rubriques et les remédiations. Aucune image, photographie, musique, police, modèle tridimensionnel tiers ni extrait d'un manuel n'est redistribué. Les symboles Unicode usuels ne portent pas ici une revendication de licence sur une image externe. Une revue des droits peut néanmoins être nécessaire avant toute publication commerciale; aucune garantie juridique absolue n'est donnée.

## Limites

Les corrigés numériques sont vérifiés dans le programme de test, mais la pertinence pédagogique des seuils, l'accessibilité réelle et la sécurité des objets doivent être évaluées par des personnes qualifiées. Aucune observation d'enfant, validation psychométrique, épreuve sommative certifiée ou conformité détaillée au PFEQ n'est revendiquée.
