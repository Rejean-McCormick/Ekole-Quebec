# Validation de livraison — delta `qc-pri-fr-003` v1.2

**Statut** : contrôles automatisés locaux effectués, **revue humaine encore requise**. Aucun item, examen ni parcours n'est « certifié », « homologué » ou publié.

## Origine et périmètre

- Source de référence lue **dans** `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`, à l'intérieur de l'arborescence intégrée `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`; cette extraction contient le workspace de base, son graphe et sa norme v1.2. **Ce n'est pas un nouveau repo**.
- Remplacements complets : `authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`. La structure YAML originelle et les clés/identités JSON natives ont été préservées; seul le statut de rédaction du JSON et les attributs manquants de la famille ont été actualisés.
- Douze nouveaux fichiers : six contenus, trois évaluations, une provenance, deux fichiers de livraison. Aucun fichier central ni autre ID empaqueté; les fichiers `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `kristal.workspace.json` restent intacts dans la base.

## Contrôles locaux réellement exécutés

Le script de construction a créé les 14 fichiers listés dans le manifeste; le script de contrôle a inspecté l'archive **après sa création** et vérifié :

1. Fichiers : **14 exactement**, tous non vides, sans fichier libre ni répertoire englobant, chemins strictement sous `kristals/qc-pri-fr-003/`, sans chemin absolu ni remontée `../`, premier chemin correct.
2. Manifeste : chemins identiques à la liste ZIP, identifiants et version de base cohérents.
3. JSON : `CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json`, `MANIFEST.json` parsables en JSON strict; champs v1.2 natifs conservés, même objectif, même préalable et même famille.
4. YAML : en-tête préservé (comparaison de texte avec l'original), 12 sections numérotées 1 à 12; valeurs identitaires, objectifs et métadonnées conservés.
5. Banque : 13 identifiants `q-001` à `q-013` uniques; chaque item contient les champs requis, une réponse, un feedback, une difficulté, une limite de variation, `obj-1`, `crit-1`, la famille `qc-pri-fr-003-ev-01`, et le statut `a_revoir`.
6. Deux manifestations de maîtrise : `q-009`/M-A et `q-010`/M-B, contextes et ensembles de mots non identiques, 4 mots chacun, preuve autonome avec justification; absence de seed et de paramètres aléatoires pour les items fixes.
7. Dépendances et liens : relation sortante `requires` pour `qc-pri-fr-002`, aucune dépendance supplémentaire dans ce delta; chemins internes des contenus, de l'évaluation et de la gouvernance repérés dans le workspace de base.
8. Contrôle éditorial scripté : aucun marqueur de rédaction provisoire ou section laissée vide; listes prévues pour deux diagnostics, trois tâches guidées, quatre pratiques autonomes, deux transferts et rappels différés retrouvées; aucune inclusion de média tiers.

## Points **non** validés par un test automatisé

- Les réalisations orales des enfants, la prononciation et la variation sociophonétique au Québec : aucune évaluation réelle avec élèves n'a été réalisée. Les transcriptions API et acceptabilités dialectales **demandent revue** par une personne compétente en français québécois.
- Validité empirique du seuil local **3/4 sur deux contextes**, équivalence de difficulté, robustesse des réponses, adéquation à des besoins langagiers particuliers : revues humaines et essais requis.
- Validité juridique exhaustive des droits et du traitement de données personnelles : seuls les contenus produits et les références ont été inventoriés; **pas d'audit juridique**. Pas d'audio/image/texte protégé recopié dans ce delta.
- Tests d'intégration au LMS/Framework et fusion effective dans l'archive maîtresse : **non réalisés**; seuls la structure du ZIP et les liens statiques ont été testés.
- Aucune homologation au PFEQ demandée ou testée; charte Québec limitée à l'appellation de la discipline.

## Propositions de changement structurel **sans** modification de base

1. Ajouter ultérieurement au schéma de famille une propriété optionnelle `preuve_orale_observee` et des champs d'acceptation explicite de variantes régionales (à proposer à la gouvernance, **non inclus** ici).
2. Prévoir dans le LMS un journal externe, soumis à consentement, pour prononciation observée, indices et deux contextes; **ne pas** stocker les traces élèves dans `canon/` ou dans ce delta.
3. Créer une procédure centralisée de revue humaine des corpus de remplacement, plutôt qu'un générateur libre d'étiquettes.
4. Proposer un test automatique de préservation de champs v1.2 à chaque fusion, sans éditer `registry/`, `governance/` ni `state/`.

**Fusion** : extraire `qc-pri-fr-003_livraison_v1.2.zip` à la racine **intérieure** de `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` pour superposer `kristals/qc-pri-fr-003/...` sans nouveau dossier parent.
