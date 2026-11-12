# Validation de livraison — `qc-pri-ale-006`

**Statut :** revue technique locale effectuée; banque `a_revoir`; **aucune homologation, qualification psychométrique ou validation humaine prétendue**.

## Vérifications réellement effectuées

Le script de construction/contrôle a vérifié après création :

- Identité de l'archive de base: frame originale v1.2 chargée depuis le ZIP fourni; frontmatter YAML original identique caractère par caractère, 12 sections numérotées dans l'ordre, et champs canoniques du contrat JSON préservés.
- Graphe de provenance: `requires = qc-pri-ale-004`, `recommends_before = qc-pri-ale-005`, pas de renforcement. Objectif et preuve stricts inchangés.
- Schéma JSON vérifié localement par analyse syntaxique de `CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json` et `MANIFEST.json`; familles et IDs croisés, champs minimaux présents, types cohérents.
- Banques: 12 items, indices séquentiels uniques, des stimuli/consignes/réponses/critères/rétroactions non vides, `mode=fixe`, `seed=null`, `parametres=null`, statut `a_revoir`; deux épreuves finales dans genres différents demandant chacune deux inférences justifiées. Aucun algorithme mathématique/paramétrique n'est employé.
- Couverture pédagogique: 2 exemples résolus, 2 contre-exemples, 2 diagnostics, 3 guidages dégressifs, 4 pratiques autonomes, 2 transferts, feedback et rappel différé explicités dans les six contenus.
- Liens locaux contenus / contrats / plans contrôlés comme chemins relatifs présents; référence du graphe contrôlée contre le fichier source. Droits: textes déclarés originaux et absence d'attribution de sources externes inventées; cela n'équivaut pas à un audit juridique de droits.
- ZIP: 14 fichiers exactement, non vides, entrées ordonnées, sans dossier parent, sans `../`, chemin absolu, lien symbolique, autre Kristal, ni fichier hors `kristals/qc-pri-ale-006/`; correspondance exacte avec le manifeste; CRC `testzip()` réussie.

## Contrôles éditoriaux et limites

- **Corrigés argumentés:** vérification de cohérence des réponses modèles **par lecture/révision de rédaction**, y compris la distinction inférence vs fait et les limites; pas de solveur numérique applicable. Aucun outil informatique ne peut certifier toutes les variantes ouvertes admissibles.
- **Accessibilité:** présence de consignes sur version texte, support audio fidèle, transcription/oral sans orientation de réponse, faible surcharge et scénarios non stigmatisants; **aucun test utilisateur ni audit de lecteur d'écran** réalisé.
- **Sécurité et équité:** aucune donnée privée ni exposition au risque demandée; analyse du biais narratif et de compréhension à faire par personnel humain.
- **Droits:** textes originaux de cette livraison; **aucune vérification de licences tierces, d'originalité juridique exhaustive ou de conformité institutionnelle**.
- **Revue humaine encore nécessaire:** fluidité et niveau du texte anglais, ambiguïtés/équivalences des inférences, adéquation à l'âge, clarté du barème, équité culturelle, validation multi-évaluateurs et essai de durée/administration. Pas de prétention de conformité détaillée au PFEQ.

## Fusion sans mutation du système central

Extraire ce delta à l'intérieur du répertoire maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` après décompression de l'archive source. Ne remplacer que `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json` de ce Kristal; les 12 autres fichiers sont ajoutés. `AGENTS.md`, `ALIGNEMENT.md`, `kristal.workspace.json`, `registry/`, `governance/`, `canon/`, `state/`, `runtime/`, `docs/` restent inchangés.

**Évolution proposée, NON appliquée :** envisager un emplacement de validation humaine multi-correcteurs et des consignes partagées pour coder les inférences alternatives; soumettre au registre central si cela exige un changement de schéma.
