# Validation du delta — `qc-pri-eps-009`

Statut : contenu pédagogique rédigé; revue humaine indispensable. **Aucune certification d'items ni qualification de cours**. Contrôles techniques renseignés par le script de validation après leur exécution.

## Périmètre protégé

Livraison locale exactement 14 fichiers sous `kristals/qc-pri-eps-009/` : deux remplacements préexistants (`authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`) et douze ajouts (6 contenus, 3 évaluations, sources et 2 éléments de livraison). Aucun `AGENTS.md`, `kristal.workspace.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `registry/`, `governance/`, `docs/`, `canon/`, `state/`, `runtime/` ni autre Kristal ne sont inclus.

## Tests techniques réellement exécutés

- **517 assertions pré-archivage réussies**, tests Python effectivement exécutés contre les huit fichiers sources et les 14 sorties locales.
- **YAML :** frontmatter natif conservé exactement, 12 sections numérotées présentes dans l’ordre.
- **JSON :** contrat, banque et manifeste décodés ; identifiants/objectifs/preuve/liens/contrat famille inchangés sur les invariants de v1.2.
- **Banque :** 10 items uniques, consignes/stimuli/rubriques/rétroactions explicites, deux épreuves distinctes A/B en modes fixes ; statut `a_revoir`. Contrôle technique de présence et cohérence de champs, **pas** revue du jugement pédagogique réel.
- **Contenus :** au moins 2 diagnostics, 2 exemples résolus, 2 contre-exemples, 3 guidages dégressifs, 4 pratiques autonomes, 2 transferts et rappel différé présents. Vérification lexicale et structurale, pas de simulation d’élèves.
- **Droits et accessibilité :** URL des références, originaux et limites des droits documentés ; présence des règles d’arrêt, supervision et adaptations contrôlée dans les documents. Aucune vérification juridique/clinique complète.
- **Fusion sur la base réelle :** superposition simulée avec **2 fichiers remplacés**, **12 fichiers ajoutés** et conservation octet pour octet des **34 autres fichiers de ce Kristal** ; aucun autre chemin n’est présent dans le delta.
- **ZIP final :** test CRC, exactitude des 14 chemins et absence de chemin absolu/traversée, tous les fichiers non vides et manifest identique, contrôles exécutés après création.

## Limites non résolues

- Aucun essai terrain avec des élèves ni étalonnage des critères M1–M5 ; la fiabilité d'observation doit être étudiée.
- Les signaux corporels et adaptations varient selon l'individu. Aucune décision médicale, prescription d'intensité, aptitude sportive, norme de sécurité du bâtiment ou conduite de premiers secours ne peut être conclue du présent dossier.
- Les activités demandent supervision, aménagements individualisés et droit à l'arrêt ; la sécurité réelle ne se vérifie pas dans un script.
- Les rubriques sont `a_revoir` et nécessitent revue humaine avant usage sommative. Pas d'équivalence ni homologation PFEQ revendiquée.
- Une production uniquement écrite ne peut être comptée comme une prestation motrice non observée; les aménagements d'équivalence relèvent d'une revue humaine.

## Points de revue humaine

1. Spécialiste EPS : adéquation des situations, pertinence des indices d'effort, absence de risque incité ou de compétition involontaire.
2. Responsable des adaptations : accessibilité de toutes les modalités et jugement d'équivalence de la preuve lorsqu'un mouvement ne peut être observé.
3. Enseignant/évaluateur : compréhension des dix consignes, stabilité de l'échelle, diversité A/B et interprétation des preuves autonomes.
4. Responsables des droits : confirmer les politiques de traces et de consentement avant tout enregistrement futur; aucun média tiers intégré.

## Propositions structurelles (non appliquées)

- Proposer au mainteneur central un champ stable `safety_override` pour interrompre une épreuve sans enregistrer d'échec et distinguer une preuve `non_concluante` d'une erreur de maîtrise.
- Ajouter ultérieurement à la norme, après décision centralisée, un registre des aménagements non directifs et de leur validation par personne compétente.
- Proposer une procédure interévaluateurs pour les productions motrices avant qualification sommative.
