# Rapport de validation — `qc-pri-st-012`

**État de livraison :** rédaction pédagogique structurée, revue humaine requise, pas d'homologation, pas de certification.

## Contenu et fusion

Exactement 14 fichiers listés dans `livraison/MANIFEST.json`, sous `kristals/qc-pri-st-012/` à la racine du ZIP. Les deux fichiers authoring existants sont des remplacements; les 12 autres sont nouveaux. Les chemins `AGENTS.md`, `authoring/ALIGNEMENT.md`, `authoring/BRIEF_REDACTION.md`, `kristal.workspace.json`, `canon/`, `registry/`, `state/`, `runtime/`, `governance/`, et les autres Kristals ne sont pas livrés ni modifiés.

## Contrôles réellement exécutés

- **527 assertions techniques préarchivage réussies** avec le script Python de contrôle, sans erreur : 14 fichiers non vides, JSON parsés, YAML initial préservé (14 invariants), 12 sections dans le bon ordre, objectif/critère/liens `requires`, `recommends_before` et famille natifs conservés, 10 items sans doublon, deux contextes de maîtrise, corrigés déterministes du dénombrement, traçabilité et provenance.
- **Fusion simulée à partir du dossier source original :** deux fichiers `authoring/` remplacés; 12 fichiers ajoutés; **34 fichiers sources protégés inchangés par comparaison SHA-256**. Aucun autre ID, canon, registre ou fichier de gouvernance n'est livré.
- **Qualité des corrigés :** dénombrements q003 et optimisation q007 recalculés; présence de réponses/rubriques et des champs obligatoires des 10 items vérifiée automatiquement. Leur validité expérimentale et leurs possibilités pédagogiques réelles ne sont **pas** attestées par ces tests.
- **Sécurité/accessibilité/droits :** audit documentaire des clauses de manipulation, des adaptations, de l'absence de médias externes et de la provenance; aucune manipulation physique ni revue juridique réalisée.
- **Archivage :** test CRC, JSON dans le ZIP, exactitude des 14 chemins sans dossier englobant et concordance manifeste vérifiés après production.


## Limites non résolues

- **Sciences :** aucune fabrication ni expérimentation avec de vrais matériaux; les performances P1/P2 affichées comme exemple sont fictives.
- **Sécurité :** aucun audit des matériaux locaux ni de la capacité individuelle des enfants; adulte responsable indispensable pour toute séance.
- **Évaluation :** aucune revue humaine d'items, cohérence psychométrique, fidélité interévaluateurs ou étude d'équité n'est attestée.
- **Accessibilité :** accommodements proposés mais non essayés avec personnes ayant des besoins différents. Si la fabrication avec aide modifie l'autonomie de décision, un évaluateur humain tranche.
- **Droits :** les liens sont documentés; aucune revue juridique exhaustive des productions originales et usages futurs.
- **Portée :** aucune conformité PFEQ, aucune modification du registre, aucune matérialisation canonique v9 ou publication.

## Propositions de changements centraux (non mises en œuvre)

1. Uniformiser dans une version future du schéma le champ canonique de la rubrique (`barreme_ou_rubrique` tel que prescrit dans la norme) et un type explicite d'optimisation au plafond; **proposition seulement**.
2. Définir à l'échelle du programme un contrat de consignation des aides instrumentales versus décisions de conception autonome; **ne rien écrire dans governance ou registry ici**.
3. Organiser un protocole humain de calibration de la grille M1–M5 à l'aide d'observations réelles faites en contexte sûr.
