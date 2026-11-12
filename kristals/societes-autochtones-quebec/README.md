# Nations et sociétés autochtones sur le territoire du Québec

Kristal **autonome**, non réductible au cours qc-pri-us-009.

Contenu : `30 assertions`, `13 relations` et `4 règles/mandats contextualisés`.

Les sources demeurent candidates à revue historique et culturelle. Aucun build v10 ni homologation. Le contrat commun est `urn:kristal:modele-organisation-humaine:modele`.

Pour vérifier : `py -3 tools\kristal.py check .`, puis `build-v9 .` dans ce répertoire (sous Windows).


## Extension encyclopédique v4 (2026-10-10)

`canon/domain/encyclopedie-v4.json` apporte 65 fiches contextuelles, 27 références, 20 activités et 57 liens de préalables. Elle constitue une propriété **autonome** du Kristal, indépendante de tous cours. Le graphe v3 historique est inchangé.

Voir `README_ENCYCLOPEDIE_AUTOCHTONES_V4.md` à la racine de l'overlay pour la méthode, la consultation sans IA et les limites. La référence du cours reste épinglée à la v3 tant qu'une évolution n'est pas explicitement validée.


## Extension v5 — Comportement, procédés et savoir-faire (2026-10-10)

Le fichier canonique `canon/domain/encyclopedie-v4.json` a été **enrichi sur place** sans changer les Semantic IDs préexistants ni le graphe v3. Il contient désormais des fiches supplémentaires sur les objets, la fabrication du canot d’écorce, les peaux, les aliments, la conservation et l’adaptation au territoire. Les procédures décrivent seulement les **étapes documentées**, jamais de proportions ni de durées inventées.

La catégorie primaire `comportement` regroupe explicitement **mœurs et coutumes, commerce, relations familiales, politique, diplomatie, entraide et transmission, rituels et respect, changements coloniaux**. Les anciennes catégories `gouvernance` et `echanges` demeurent signalées comme alias; les articles correspondants se retrouvent dans `comportement`, et les fiches liées aux familles et à la transmission y sont indexées de façon transversale. L’accès machine se fait par `index_categories_v5.comportement`.

Les sources nationales, muséales et pédagogiques sont intégrées en références bibliographiques; voir les champs `sources`, `precision`, `statut_revue`, `incertitudes_et_limites` et `etapes_documentees`. Une démonstration innue n’est jamais automatiquement attribuée aux Wendat ou aux Haudenosaunee. Ce contenu est un **candidat documentaire non homologué**; toute publication validée requiert une relecture par les nations concernées et une qualification indépendante.
