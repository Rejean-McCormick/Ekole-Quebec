# Validation et livraison — `qc-pri-ccq-002` (v1.2)

**Objet :** proposition éditoriale de delta fusionnable pour un seul Kristal. Deux fichiers existants **remplacés** (authoring), douze fichiers **nouveaux** (contenu, évaluation, sources, livraison). **Statut :** vérification technique locale; **revue humaine toujours requise**. Aucun canon v9 ni objet central construit, aucune publication.

## Contrôles effectivement exécutés

Les vérifications ont été réalisées localement par le script de construction/validation du présent mandat. Détails synthétiques :

- [x] Sources gouvernance + graphe + quatre documents authoring de base lus dans l'archive fournie.
- [x] YAML d'origine conservé champ pour champ, et douze titres numérotés de `PARCOURS.md` maintenus.
- [x] `CONTRAT_PEDAGOGIQUE.json` : chaque champ natif et valeur non ciblée v1.2 conservés, avec compléments de la famille requise.
- [x] Identifiant, titre, discipline, objectif, critère, preuve, absence de préalables et famille comparés avec les sources.
- [x] 12 items uniques, JSON parsable, quatre scénarios à deux variantes, réponses exemples et rubriques cohérentes; deux contextes de preuve indépendante.
- [x] Caractère original des scènes vérifié par inspection éditoriale interne; aucun texte externe, média tiers ni licence externe incorporé.
- [x] Accessibilité : texte et lecture orale / transcription / schéma prévus, aucune obligation de révélation personnelle dans les consignes.
- [x] Manifeste et ZIP : 14 chemins exacts non vides, sous un unique dossier Kristal, aucun `../`, chemin absolu, dossier parent additionnel ou autre ID.
- [x] Simulation d'extraction à la racine du workspace et de collision : uniquement 2 fichiers existants ciblés; 12 créations.

## Limites et revue humaine nécessaire

- **Non réalisé :** test d'efficacité sur élèves, consultation externe de sources sur psychologie sociale, audit d'équité, publication ou qualification Framework.
- Les réponses ouvertes ne peuvent être considérées comme corrigé automatique exact; une personne doit apprécier **les arguments documentés**, les alternatives recevables, la compréhension de chaque récit et les dimensions de la grille.
- À vérifier : sensibilité à la diversité de situations, âge/niveau de lecture du groupe, équité des variantes A/B, traduction en pictogrammes, durée réelle, protocoles locaux de confidentialité.
- Aucune conformité au PFEQ, certification ni homologation déclarée.

## Propositions sans modification des structures centrales

1. Un validateur central pourrait comparer, pour chaque livraison, le manifeste aux 14 chemins et aux métadonnées canoniques.
2. Ajouter à une version future du schéma un champ d'ancrage explicite des deux preuves, sans changer maintenant `obj-1`/`crit-1`.
3. Organiser une revue contradictoire des rubriques de productions ouvertes et la traçabilité des variantes choisies.

**Fusion attendue :** extraire à l'intérieur du répertoire `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` du workspace maître; aucun écrasement ailleurs. La liste exacte figure dans `MANIFEST.json`.
