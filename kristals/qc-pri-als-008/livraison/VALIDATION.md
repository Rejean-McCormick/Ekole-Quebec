# Validation de livraison | `qc-pri-als-008`

**Statut :** contenu rédigé et items à revoir. Les vérifications effectivement exécutées sont consignées ci-dessous par le script de validation au moment de l'archivage. Aucune qualification institutionnelle, publication ou homologation PFEQ.

## Périmètre figé

- **Deux fichiers existants remplacés uniquement :** `authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`.
- **Douze fichiers ajoutés :** six `contenu/`, trois `evaluation/`, `sources/REFERENCES_CONTENU.md` et les deux `livraison/`.
- Aucun autre Kristal, document d'alignement, workspace, `AGENTS.md`, `canon/`, `docs/`, `state/`, `registry/`, `governance/` ni dossier central n'est modifié dans le ZIP.
- Objectif, préalables, ordre conseillé, preuve, famille d'évaluation et identité YAML conservés. Les trois notions sont approfondies sans introduire de nouveau lien.

## Vérifications réellement exécutées

- **509 assertions de préarchivage réussies** : exactitude du filetree, fichiers non vides, identité et YAML de la source, 12 sections numérotées, JSON natif et famille, relations du graphe, 10 items uniques et corrigés citant des indices présents, deux contextes de maîtrise, couverture du plan, critères, accessibilité, références et droits décrits. Aucune assertion préarchivage échouée.
- **Contrôle des indices :** les dix groupes de mots anglais utilisés dans les corrigés ont été vérifiés par correspondance textuelle avec les stimuli fixes correspondants; cette vérification ne constitue pas une revue pédagogique des inférences.
- **Fusion simulée sur le contenu cible de l'archive maîtresse :** seulement `PARCOURS.md` et `CONTRAT_PEDAGOGIQUE.json` remplacés; douze fichiers nouveaux; empreintes SHA-256 identiques pour chaque autre fichier local protégé.
- **ZIP final :** intégrité CRC, 14 chemins exacts, validité JSON et concordance du manifeste à vérifier après l'archivage, puis confirmées par le script; aucun dossier englobant prévu.


## Contrôles qualitatifs et limites

- Chaque item a un **stimulus anglais original**, une question accessible, une réponse corrigée avec segment anglais identifiable, des critères et une rétroaction. Les productions en français ou anglais simple sont permises lorsqu'elles montrent le même sens.
- Les deux preuves finales sont indépendantes : une lecture d'un avis de piscine et une écoute d'un message de club de musique. Le script oral est réservé à l'évaluateur; une transcription communiquée à l'élève change ce qui est effectivement évalué.
- Les deux scénarios ne sont pas paramétriques : aucun code de génération, aucun seed aléatoire, aucune IA correctrice libre.
- **Non testé :** apprentissage d'enfants en classe, intelligibilité réelle d'une personne lisant le script, fidélité interévaluateurs, étalonnage de M1–M5, efficacité des remédiations et équité d'adaptations individuelles. Une vérification structurelle ne remplace pas ces essais.
- **Droits :** scripts et stimuli fictifs originaux; aucune musique, image, vidéo ni voix tierce incluse; aucun audit juridique exhaustif de similarité mené.

## Revue humaine indispensable

1. Relecture par une personne compétente en anglais langue seconde pour vérifier l'anglais, la clarté, les inférences, la difficulté et la variété linguistique appropriée.
2. Essai des scripts lus en situation authentique, en assurant que l'élève n'aperçoit pas les réponses réservées à l'évaluateur.
3. Revue d'accessibilité : supports alternatifs, audiologie, situation de handicap et comparabilité de la preuve auditive lorsque la transcription est nécessaire.
4. Validation critériée avec plusieurs correcteurs des réponses équivalentes et des seuils analytiques.
5. Vérification locale des modalités de consentement et de conservation des traces sans collecte inutile de voix.

## Suggestions de structure — non appliquées

- Envisager un indicateur de **modalité réellement observée** (lecture, écoute, transcription comme aide) dans un futur schéma de traces LMS, mais ne pas modifier le contrat v1.2.
- Envisager une méthode institutionnelle de conservation séparée des **scripts réservés aux évaluateurs** dans les environnements de diffusion (le JSON contient les scripts à ce stade); aucun dossier runtime n'est ajouté.
- Prévoir une procédure de revue humaine de l'équivalence des accommodations et d'étalonnage des grilles avant décisions sommatives.
