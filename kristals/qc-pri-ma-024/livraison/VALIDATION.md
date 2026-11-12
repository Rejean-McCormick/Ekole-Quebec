# Validation — `qc-pri-ma-024`

**État :** rédaction et corrigés calculés; contrôles techniques effectués le 8 octobre 2026. Revue pédagogique humaine nécessaire avant toute qualification.

## Périmètre du delta

14 chemins exactement sous `kristals/qc-pri-ma-024/` : 2 remplacements authoring et 12 ajouts. Aucun registre, norme, autre Kristal, objet canonique ou fichier du workspace central n'est livré.

## Contrôles techniques

- **13664 assertions préarchivage réussies**, sans échec; catégories : contract=22, coverage=70, identity=27, items=96, manifest=2, math_anchors=24, math_enumeration=5966, math_examples=36, overlay=7360, sections=12, structure=44, yaml=5.
- Parsing YAML/JSON : frontmatter et trois documents JSON exploitables; invariants v1.2 (objectif, preuve, préalables, famille, type) identiques aux originaux; 12 sections présentes.
- Dix items uniques, dont six paramétriques (q-005 à q-010). **Deux exemples calculés et contrôlés par item paramétrique**, plus 157 seeds échantillonnées pour q-005; **pour chaque famille** : échantillon 0..152 et seeds ancre/+1 et deux limites, avec contrôles d'exactitude et de grille.
- Validation indépendante : conservation de la coordonnée parallèle à l'axe, milieux sur l'axe, distances égales, segments perpendiculaires, absence de sortie de grille et figures non dégénérées.
- Simulation réelle en mémoire de fusion sur les fichiers de l'archive maîtresse : deux fichiers authoring remplacés, 12 ajoutés, **7355 fichiers originaux protégés dont les SHA-256 sont identiques**, aucun dossier global ou autre Kristal modifié.
- Droits : aucune image/vidéo/musique tierce intégrée; sources externes identifiées, aucune validation juridique exhaustive. Accessibilité documentée, pas testée sur des élèves.
- Le ZIP final et ses CRC, ses noms, son manifeste et ses trois JSON internes sont vérifiés après sa création.


## Limites

- Aucun essai sur une classe ni validation interévaluateurs; les rubriques restent `a_revoir`.
- Les supports tactiles ou aides techniques ne sont pas testés matériellement; équivalences à déterminer pour chaque situation d'apprentissage.
- Les exemples et grilles n'affirment aucune correspondance spécifique PFEQ; la qualification dépend d'une revue humaine.

## Modifications de structure proposées, non appliquées

- Normaliser dans une prochaine révision centrale la spécification des axes, invariants géométriques et contre-vérifications des générateurs d'items mathématiques.
- Prévoir un champ standard d'« adaptation d'accès non directive » et une trace de revue interévaluateurs, sans modifier `registry/`, `governance/` ni `canon/` dans ce delta.
