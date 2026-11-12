# Validation de livraison — `qc-pri-fr-014` (v1.2)

**État réel :** delta rédigé et tests automatisés de contenu/structure effectués, **sans** revue pédagogique humaine, sans épreuve étalonnée et sans qualification officielle.

## Contrôles effectivement réalisés

- Archive maître originale `initbundle(1).zip` ouverte; lecture préalable des trois documents de gouvernance, du registre pédagogique et des quatre sources locales obligatoires (`PARCOURS`, `CONTRAT_PEDAGOGIQUE`, `ALIGNEMENT`, `BRIEF_REDACTION`).
- **505 assertions de prévalidation réussies** : en-tête YAML v1.2 préservé à l'octet, YAML et JSON analysés, sections 1–12 présentes, identité/titre/objectif/critère inchangés, unique `requires: qc-pri-fr-013` confirmé dans le graphe, absence de recommande/renforce sortants, famille native conservée, champs de génération complétés, dix items numérotés sans doublons, deux preuves indépendantes à trois phrases chacune.
- **14 phrases d'évaluation** reconstruites automatiquement à partir de la segmentation GN sujet + verbe conjugué + GN CD; présence dans stimulus et corrigé; GV contient le GN CD; vérification automatisée de la place et de l'élision `l’` des pronoms CD. Les substitutions ont aussi fait l'objet d'une relecture rédactionnelle. **Aucun analyseur linguistique externe ni essai en classe exécuté** : qualité des corrigés à revoir par un spécialiste.
- 2 exemples entièrement résolus, 2 contre-exemples, 2 diagnostics, 3 guidages à soutien dégressif, 4 exercices autonomes, 2 tâches de transfert et rappel différé vérifiés quant à leur présence; feedback ciblé documenté.
- Sources linguistiques externes OQLF consultées, références et limites distinguées des constructions originales; aucun texte externe substantiel, visuel, audio ou donnée privée reproduit.
- Accessibilité : version lisible et lecture neutre, étiquettes, réponses orales/écrites équivalentes; décodage séparé de l'analyse syntaxique. Points documentaires contrôlés; pas d'essai d'accessibilité avec des apprenants.
- **Tests de ZIP exécutés après création :** 14 fichiers non vides, premier chemin sous `kristals/qc-pri-fr-014/`, liste exacte du manifeste, absence de traversée de répertoire et de dossier englobant, JSON parsables dans le ZIP, CRC valide, données ZIP identiques aux fichiers locaux. Le script échoue si une assertion de postvalidation est fausse.
- **Fusion simulée par comparaison de l'index de l'archive maître** : exactement deux chemins `authoring/` préexistants remplacés et douze nouveaux ajoutés. Aucun fichier protégé ou d'un autre Kristal n'est inclus; tout autre fichier de l'archive maîtresse demeure donc non ciblé.

## Limites non résolues et revue humaine indispensable

1. Faire vérifier les frontières de chaque GN/GV et les manipulations par un spécialiste de la grammaire du français québécois; évaluer d'éventuelles lectures grammaticales alternatives hors du corpus contrôlé.
2. Essayer les consignes et l'échelle analytique sur des élèves, comparer l'accord entre correcteurs et ajuster la durée.
3. Valider les modalités de lecture et de réponse alternatives dans le contexte d'enseignement réel.
4. Vérifier les droits d'une éventuelle redistribution de l'archive source par son propriétaire. Aucun contenu sous licence tierce n'est redistribué ici.
5. Tester la fusion réelle et une projection dans le LMS/Framework utilisé. Seule la forme du delta a été vérifiée; aucun canon v9, runtime ni registre central modifié.

## Proposition structurelle non appliquée

Un futur schéma commun versionné pourrait enregistrer explicitement la hiérarchie des groupes dans un champ optionnel `analyse_controlee` (déjà utilisé localement dans les items) et un outil de vérification des substitutions. Ne pas modifier les fichiers de gouvernance ni les identifiants avant décision centralisée.

**Statut de toutes les évaluations :** `a_revoir`; aucune affirmation de publication, certification ou homologation PFEQ.
