# Les invitations de Mila

Activité de démonstration locale, à relire avant un usage en classe. Le Kristal référence l’objectif `qc-pri-ma-009/obj-1` et l’étape `repartition` de la mission Kontexte `fete-sorciere`.

- Modifier les situations, paramètres et réalisations françaises ou anglaises dans `canon/domain/activity.json`.
- Vérifier le workspace avec `python outils/kristal_local.py check activites/invitations-mila` depuis `ekole-quebec`. Construire le candidat sémantique avec `build-v9` après une modification.
- Depuis `ekole-quebec`, exécuter `python outils/compiler_activite.py --out dist/invitations-mila-local`. Le compilateur lit les versions épinglées du contrat Québec et de la mission Kontexte. Il prépare la projection privée pour Ekole et une projection filtrée pour l’import Spek.
- La portée des questions compilées est `demo`. Les banques Ekole importées dans Inkuisite restent des brouillons à réviser.

La vue élève sert une pratique avec rétroaction immédiate et un bilan sur une autre situation avec revue humaine et diffusion explicite. Les réalisations sont des textes de démonstration fournis dans le Kristal.
