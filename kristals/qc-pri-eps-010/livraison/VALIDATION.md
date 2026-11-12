# Journal de validation — `qc-pri-eps-010`

**Archive :** `qc-pri-eps-010_livraison_v1.2.zip`. **Statut :** `a_revoir` (rédigé, non certifié, non homologué). **Contrat :** delta fusionnable sous `kristals/qc-pri-eps-010/` uniquement.

## Périmètre effectivement livré

Deux remplacements complets des fichiers existants `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`, dont les identifiants, l'objectif, la preuve, les liens du graphe, les champs natifs et la famille d'évaluation restent préservés; douze documents nouveaux. **Au total : 14 fichiers** exclusivement pour ce Kristal. Aucun fichier de gouvernance, graphe, registre global, workspace, canon, runtime, docs ou autre Kristal n'est livré.

## Contrôles effectivement exécutés

- **47/47 contrôles sur les fichiers de travail** au moment de préparation du paquet (programme `_qa_eps010.py` exécuté et terminé sans erreur). Ils vérifient la structure YAML, la conservation des identifiants et champs d'origine, les douze sections, le graphe local, la validité JSON, les douze items, la numérotation continue, les liens `obj-1`/`crit-1`/`qc-pri-eps-010-ev-01`, les paramètres et seeds de la variante fermée, les deux contextes, la présence des corrigés, les aides dégressives, le contenu de sécurité/accessibilité, les références, le manifeste et les liens documentaires.
- **Après construction du ZIP**, tests distincts exécutés par `_package_eps010.py` : exactement quatorze chemins identiques à `MANIFEST.json`, aucun préfixe parasite, aucun `../` ni chemin absolu, fichiers non vides et octets identiques aux fichiers de travail, CRC ZIP, première entrée valide, JSON à l'intérieur du ZIP analysables, YAML analysable, deux preuves disponibles et noms d'items uniques. Ces vérifications sont exécutées et rapportées par le script à la fin de la commande; aucune affirmation d'essai avec élèves.
- **Revue de cohérence par confrontation des corrigés aux scénarios** lors de la rédaction : fermetures de locaux, disponibilités, matériel, surveillance et remplacements sont décrits; les items `q-011` et `q-012` requièrent des productions différentes et indépendantes. La revue humaine externe n'est **pas réalisée**.

## Décompte et vérification des productions

Six documents de contenu; au moins deux exemples résolus, deux contre-exemples, deux diagnostics corrigés, trois exercices guidés à indices dégressifs, quatre pratiques autonomes avec corrections indicatives, deux transferts, quatre micro-remédiations et des rappels différés. Douze items (11 fixes, un scénario à 2 variantes intégralement rédigées) avec réponses/rubriques. `q-011` : contexte école; `q-012` : contexte centre communautaire. Des mesures d'activité réelle, photos, données médicales et performances corporelles ne sont pas demandées.

## Limites non résolues et revue humaine obligatoire

1. **Validité pédagogique :** vérifier durée d'administration, lisibilité, charge de planification selon les différents âges, exactitude et acceptabilité des diverses réponses libres, possibilité de réussir à l'oral et accord intercorrecteurs sur la grille 0–2.
2. **Sécurité contextualisée :** examiner chaque idée d'activité avant pratique dans un établissement réel; supervision, météo, accessibilité et besoins particuliers doivent être appréciés par une personne responsable. Les exemples de plans ne prescrivent aucune activité médicale et ne demandent **aucune exécution**.
3. **Équité et droits :** vérifier les adaptations en classe, la non-stigmatisation, les traductions éventuelles et les éventuelles politiques locales de droits d'auteur; textes, personnages et scénarios ont été créés pour ce mandat, sans actifs tiers intégrés.
4. **Aucun test auprès d'élèves, aucune validation clinique, aucune homologation PFEQ, aucune évaluation sommative étalonnée** n'ont été accomplis. Les sources de santé publique consultées ne fournissent pas des seuils de certification du plan hebdomadaire. La banque reste `a_revoir`.

## Propositions éventuelles pour une évolution centrale (non appliquées)

- Ajouter au schéma de famille un champ officiel séparant `état rédactionnel des items`, `validation pédagogique humaine` et `qualification technique`, au lieu d'inférer la qualité depuis un statut global.
- Prévoir dans l'adaptateur de passation des preuves non textuelles une transcription fidèle des réponses orales, avec journal d'aides et d'adaptations, sans collecte de données corporelles.
- Ajouter dans le registre de validation central une distinction « adaptation du plan si contexte impossible » / « volume final d'occasions prévues », afin de ne jamais inciter à remplacer une activité sûre par une activité dangereuse pour satisfaire un quota didactique.

**Fusion :** entrer dans la racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis extraire ce delta. Aucun chemin parent `Frames_202_...` n'est fourni dans l'archive.
