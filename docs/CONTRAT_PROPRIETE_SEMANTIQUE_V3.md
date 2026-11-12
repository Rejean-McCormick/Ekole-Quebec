# Contrat de propriété et de référence v3

## Propriété

- `modele-organisation-humaine` **définit** seulement les types et règles du modèle; il ne détient aucun événement de l'histoire du Québec.
- `societes-autochtones-quebec` **détient** les assertions sur les pratiques, institutions, langues, territoires et continuités des nations représentées, dans des périodes définies. Ce n'est pas « la société autochtone » unique.
- `rencontres-coloniales-quebec` **détient** les faits relatifs aux rencontres, conflits, négociations, documents coloniaux et transformations; il peut faire référence à des sociétés autochtones sans devenir propriétaire de leur modèle interne.
- `qc-pri-us-009` **détient** l'objectif, la progression, les sélections de faits et activités. Il ne détient pas les contenus historiques externes en v3.

## Référence logique

Le cours pointe vers les deux `state_ref` v9 et leurs empreintes logiques; pour empêcher une mise à jour silencieuse, il mémorise aussi les empreintes logiques de chaque artefact et un SHA-256 des fichiers canoniques correspondants. Toute divergence stoppe la compilation. Les anciennes inscriptions v1/v2 doivent être détachées explicitement par `--detach-legacy`.

Les `sources` et `periodes` peuvent être lues localement comme vocabulaire de référence dans chaque corpus. Elles ne forcent pas la possession exclusive d'une nation, d'une date, ni d'un savoir culturel.

## Séparation des responsabilités

Une connaissance n'est pas un exercice. L'absence d'une assertion ne démontre aucune impossibilité. Les distracteurs sont des fiches positives documentées, pas des contrevérités historiquement présumées. Les traces de clic ne mesurent pas à elles seules la capacité à comparer deux perspectives.

## Exemple de réutilisation

La lecture `--search` du Kristal autochtone peut soutenir une exposition muséale, un parcours géographique, la découverte des langues ou un autre cours, sans importer `qc-pri-us-009`. Chaque nouveau consommateur doit établir ses propres objectifs et référencer la version précise du corpus.
