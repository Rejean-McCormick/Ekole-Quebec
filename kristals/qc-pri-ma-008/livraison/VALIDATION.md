# Rapport local de livraison — qc-pri-ma-008 | v1.2

**Archive produite :** `qc-pri-ma-008_livraison_v1.2.zip`. **Racine relative de fusion :** `kristals/qc-pri-ma-008/`. **Statut :** contrôles techniques locaux exécutés, contenu `a_revoir` et revue humaine requise; pas de certification, homologation, publication ou qualification Framework.

## Contenu et modifications effectives

- **2 remplacements intégraux** issus de la frame v1.2 : `authoring/PARCOURS.md` (YAML d'origine conservé, 12 sections remplies) et `authoring/CONTRAT_PEDAGOGIQUE.json` (champs natifs préservés, famille enrichie).
- **12 ajouts** : six contenus de leçon, trois fichiers d'évaluation, un fichier de sources, un manifeste, et le présent rapport.
- **Banque : 12 items**, dont 5 déterministes paramétriques avec seed stable et 15 exemples alternatifs calculés; tous `validation_status: a_revoir`.
- **Deux preuves** : `q-009`, boîtes de pièces en atelier; `q-010`, rangées de plants au jardin, sans aide de fond; dessin + calcul + justification obligatoires.
- Les fichiers `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `AGENTS.md`, `kristal.workspace.json` et toute la gouvernance, registry, canon, state, runtime et autres Kristals restent inchangés et **absents** du delta.

## Tests exécutés automatiquement sur ce delta

Les contrôles ont été exécutés dans un script local Python (stdlib : `zipfile`, `json`, `re`) avant empaquetage, puis sur le ZIP réellement écrit. Les vérifications effectuées incluent :

- Identité canonique (`id`, titre, `obj-1`, `crit-1`), preuve et relations du graphe (`requires: qc-pri-ma-006`, `recommends_before: qc-pri-ma-003`).
- Comparaison du front matter YAML d'origine **octet logique pour octet logique** (mêmes caractères entre marqueurs `---`), présence des 12 sections numérotées; conservation des champs initiaux du JSON natif et présence des 13 champs de famille prescrits.
- JSON strict analysable; `q-001` à `q-012` sans doublons, liens `obj-1`, `crit-1`, `qc-pri-ma-008-ev-01`, énoncés/réponses/critères/feedback non vides.
- Données paramétriques : fonctions par `%` et `//`, seed stable, instances correctes, **15 variantes contrôlées**; produits comparés à l'addition itérée et aux décompositions, tests de domaines entiers **148 combinaisons** (30 groupes, 30 tableaux, 60 distributivité, 16 atelier, 12 jardin); 17 produits d'illustration vérifiés.
- Couverture des exemples/contre-exemples, deux diagnostics, trois exercices guidés, quatre pratiques autonomes, deux transferts et deux contextes de maîtrise distincts.
- Vérification des chemins internes mentionnés, cohérence des ID, traçabilité des droits et des accommodements d'accessibilité; absence de balises `TODO` et d'autres identifiants de Kristals que les deux relations permises.
- Simulation de superposition avec les chemins source : **2 remplacements, 12 ajouts**; `testzip` CRC réussi; arborescence ZIP **14 fichiers non vides**, première entrée sous `kristals/qc-pri-ma-008/`, aucun chemin absolu, traversée `../`, ni dossier parent englobant; manifeste identique à la liste réelle du ZIP.

## Contrôles de fond et limites (ne pas confondre)

- **Mathématiques :** les sommes et produits indiqués dans les exemples et les instances paramétriques ont été recalculés localement, sans sortie libre d'IA comme correcteur. La pertinence didactique et la variété suffisante ne sont pas des propriétés garanties par un test numérique.
- **Droits :** rédaction originale et absence de médias externes dans ces 14 fichiers; aucun audit juridique de licence du workspace complet n'a été fait.
- **Accessibilité :** vérification textuelle des modalités offertes (oral, tactile, gros points, scribe neutre); **aucun essai utilisateur**, audit ergonomique ni audit WCAG d'une interface livrée.
- **Liens :** vérification statique des chemins internes et des identifiants; **aucun test de navigation LMS**. Les liens externes mentionnés dans le registre de sources n'ont pas été ouverts.
- **Non exécutés :** relecture par enseignant, test avec élèves, audit de biais, tests d'intégration applicative ou de migration réelle du workspace, validation Framework `check`/`build-v9`/`check-ai`, homologation PFEQ, qualification ou publication.

## Revue humaine et suggestions structurelles (sans modification des bases)

1. Faire relire la progression, les contre-exemples de groupes inégaux, la consigne de distributivité et le seuil 4/4 par un spécialiste de l'enseignement primaire de la mathématique.
2. Observer au moins deux élèves dans les deux contextes et vérifier que lecture orale et représentation tactile gardent la même exigence de compréhension.
3. Tester l'intégration réelle de la banque, notamment les champs supplémentaires `critere_id`, `family_id`, `representation` et `preuve_maitrise` par rapport au schéma de l'importeur. **Proposition non appliquée :** formaliser dans un futur schéma central la validation des variantes paramétriques, des unités et des deux preuves indépendantes.
4. Conserver `a_revoir` jusqu'à la relecture des énoncés, rubriques et biais et jusqu'aux tests de l'importeur.

**Fusion :** décompresser le workspace maître, se placer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, extraire le ZIP à cet endroit. Le delta ne contient que `kristals/qc-pri-ma-008/...`; ne pas créer un second dossier `Frames_202_.../` lors de l'extraction.
