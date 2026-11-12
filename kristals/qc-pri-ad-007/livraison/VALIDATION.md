# Rapport de livraison et validation — `qc-pri-ad-007`

**Base** : frame v1.2 du workspace source; **périmètre** : uniquement `kristals/qc-pri-ad-007/`. **Statut** : contenu rédigé et soumis à revue humaine; ni publié, ni certifié, ni homologué. Les deux fichiers `authoring/` sont des remplacements conservant le contrat natif; les douze autres sont des ajouts.

## Travaux effectués
- Parcours en 12 sections conservant l'en-tête YAML original et enrichi de diagnostics, modelages, exercices, autonomie, remédiation, rappels différés, accessibilité.
- Six dossiers `contenu/` avec exemples originaux, contre-exemples, deux diagnostics, trois tâches guidées à indices dégressifs, quatre tâches autonomes, deux transferts.
- Dix items fermés par des stimuli précis, quatre catalogues A/B = huit variantes figées, deux preuves finales P1/P2 distinctes; grille à quatre dimensions.
- Ressources et droits clarifiés; manifeste exactement aligné au filetree de livraison.

## Contrôles effectivement exécutés
**49 contrôles locaux effectivement exécutés et réussis**, détaillés ci-dessous. Les catalogues A/B ont été parcourus sur **24 sélections reproductibles** (4 items × 6 index de version). Ces tests portent sur la cohérence des fichiers, identités, contraintes déclarées et représentations; la correction libre d'un élève n'est pas automatisée.

- Manifest count 14 and exactly two authoring replacements : RÉUSSI
- Manifest exact expected tree : RÉUSSI
- All 14 files exist nonempty : RÉUSSI
- Only 14 target files generated : RÉUSSI
- Manifest correct identity and not certified : RÉUSSI
- 3 JSON strictly parse and dict root : RÉUSSI
- Original YAML frontmatter byte-exact : RÉUSSI
- Original YAML parsed, 1.2 format : RÉUSSI
- 12 original numbered sections retained : RÉUSSI
- All original top-level fields preserved : RÉUSSI
- All original family fields and nested generation fields preserved : RÉUSSI
- Immutable metadata values intact : RÉUSSI
- Immutable assessment family intact : RÉUSSI
- All generator fields completed in same family object : RÉUSSI
- Family review remains not certified : RÉUSSI
- Graph outgoing requires, recommends and reinforces empty : RÉUSSI
- Only inbound reference is future AD008 requires AD007 : RÉUSSI
- Objective and proof exact : RÉUSSI
- Discipline and family in path : RÉUSSI
- Bank schema and identity : RÉUSSI
- 10 numbered unique items : RÉUSSI
- All items fully formed and no empty prompts/rubrics : RÉUSSI
- All items target exact objective, criterion, family : RÉUSSI
- All item statuses noncertified and valid modes : RÉUSSI
- Four A/B catalog items and six fully fixed items : RÉUSSI
- All fixed items use null seed/params : RÉUSSI
- Catalog qc-pri-ad-007-q-003 full and consistent : RÉUSSI
- Catalog qc-pri-ad-007-q-004 full and consistent : RÉUSSI
- Catalog qc-pri-ad-007-q-005 full and consistent : RÉUSSI
- Catalog qc-pri-ad-007-q-006 full and consistent : RÉUSSI
- 24 reproducible controlled scenario selections : RÉUSSI
- Two distinct new mastery contexts P1/P2 : RÉUSSI
- Four observable rubric criteria every item : RÉUSSI
- Item representation and variation bounds : RÉUSSI
- Two examples and four counterexamples : RÉUSSI
- Two diagnostic tasks : RÉUSSI
- Three scaffolded exercises : RÉUSSI
- Four independent tasks with sample responses : RÉUSSI
- Two contextual transfers with feedback : RÉUSSI
- Four rubric dimensions and two proofs : RÉUSSI
- All items mapped in plan : RÉUSSI
- Rubric demands two autonomous distinct contexts : RÉUSSI
- Accessibility and rights in all 6 content files : RÉUSSI
- Rights provenance verified / derived / originals : RÉUSSI
- No openai-generated answer asserted certified : RÉUSSI
- All local internal references resolve in delta or unmodified source : RÉUSSI
- No misleading external Kristal links or other workspaces : RÉUSSI
- Files all UTF-8 : RÉUSSI
- No off-scope paths in manifest : RÉUSSI

**10 contrôles ZIP exécutés et réussis :**
- Exactement 14 fichiers : RÉUSSI
- Premier chemin au préfixe exigé : RÉUSSI
- Aucun autre ID ni répertoire englobant : RÉUSSI
- Aucun chemin absolu, traversal ni dossier libre : RÉUSSI
- Toutes entrées non vides : RÉUSSI
- Intégrité CRC : RÉUSSI
- 3 JSON parseables depuis ZIP : RÉUSSI
- Manifeste = 14 chemins réels et ID : RÉUSSI
- Aucune erreur de chemins autres fichiers non ciblés : RÉUSSI
- Contenu ZIP identique aux fichiers sources : RÉUSSI

Après insertion du présent rapport dans la livraison, le ZIP a été reconstruit puis **son intégrité et son contenu exact ont été recontrôlés**.

## Risques et limites connus
- Les corrigés de productions ouvertes sont des exemples fondés sur les sources de chaque vignette; ils n'imposent pas une phrase unique et requièrent le jugement d'un enseignant. Une procédure automatique ne sait pas juger parfaitement une paraphrase inédite.
- Aucune mise à l'essai sur élèves, aucune étude d'accord inter-correcteurs, aucune observation d'une représentation réelle, aucun avis juridique sur la conservation de productions d'élèves.
- Les vignettes textuelles structurent les observations mais ne remplacent pas toutes les dimensions d'un spectacle vivant; une mise à l'essai humaine des adaptations (sons/gestes/maquettes tactiles) est nécessaire.

## Revue humaine indispensable
- Vérification par enseignant ou praticien d'art dramatique : authenticité des notions, clarté des scènes, erreurs de compréhension fréquentes, pertinence des preuves P1/P2.
- Revue accessibilité, protection des mineurs, équité et gestion de données d'évaluation; expérimentation d'évaluation à deux personnes pour confirmer la rubrique.
- Vérifier que les quatre scénarios A/B et leur charge cognitive sont comparables avant une utilisation sommative; conserver `validation_status: a_revoir` tant que non revus.

## Propositions de changement de structure (non appliquées)
- Ajouter au schéma central des items des champs facultatifs `critere_id`, `family_id`, `adaptations_accessibles`, `source_stimulus` et `evidence_map`, car ils sont utiles aux rubriques ouvertes et à l'audit.
- Ajouter un protocole central de collecte séparée des deux preuves, accord entre correcteurs et revue des biais d'interprétation. Ne modifier ni la gouvernance ni le graphe dans cette livraison.

## Fusion
Entrer dans le dossier racine de la copie décompressée `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis décompresser l'archive de livraison **à cet endroit**. Ne jamais décompresser une seconde racine englobante. Les deux fichiers `authoring/` existants sont remplacés; les autres fichiers sont ajoutés; aucun autre ID ni répertoire global n'est touché.
