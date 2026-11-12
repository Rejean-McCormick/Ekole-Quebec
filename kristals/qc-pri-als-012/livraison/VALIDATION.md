# Validation de livraison | qc-pri-als-012 v1.2

**Nature :** delta fusionnable du workspace source v1.2, contenu original non homologué; banque `a_revoir`.

## Résultats des tests exécutés localement

**Résultat : 71 assertions documentaires et de cohérence réussies (script Python), puis audit ZIP exécuté ci-dessous.** Les contrôles couvrent :

- Lecture de l'archive source et des huit chemins demandés, extraction de leurs versions de référence.
- Conservation stricte du front matter YAML (`yaml.safe_load`), des **12 sections originales** et des identités, objectifs, liens, métadonnées et familles de la base `qc.education-assessment-blueprint/1.2`.
- Parsage JSON standard du contrat et de la banque; **10 items** numérotés `001`–`010` sans doublon et chacun avec consigne, stimulus, production modèle, critères, feedback, difficulté, mode `fixe`, seed/paramètres nuls et statut `a_revoir`.
- Deux manifestations finales (`q-009`, `q-010`) dans des contextes différents, avec trois questions fixes chacune; contrôle de cohérence du plan fictif de `q-006` et du texte des deux relances finales.
- Vérification des chemins relatifs locaux des liens Markdown, des références de graphe, des mentions de droits et d'accès, et de l'exhaustivité du manifeste.
- **Contrôle de corrigés effectué :** examen rédactionnel interne des réponses modèles des dix items et vérification automatisée de la présence de réponses à chaque série de questions; **aucun contrôle linguistique indépendant, aucune cotation interjuges et aucun essai terrain** exécutés.
- **Droits :** inspection des seuls contenus textuels originaux et de la déclaration de provenance; cela ne constitue pas un audit juridique indépendant.

### Contrôle de l'archive finale

L'archive a été construite et rouverte dans le même script; le test vérifie le nombre d'entrées, leur ordre, leur préfixe, l'absence de répertoires parasites ou de traversée, la non-vacuité et les sommes de contrôle CRC de chaque entrée, ainsi que le manifeste inclus. Voir la sortie de test locale.

## Revue humaine et limites

- Évaluer la naturalité des dialogues et l'adéquation de l'anglais au niveau de la situation en contexte francophone québécois; aucun examen humain spécialisé n'est allégué.
- Faire une double cotation et un essai avec apprenants pour éprouver le barème et les deux contextes; ils n'ont pas été réalisés pendant cette production.
- Vérifier l'équivalence des adaptations sensorimotrices et des aides à la communication avant déploiement; cette vérification individualisée n'a pas été réalisée.
- Aucune conformité PFEQ, publication, certification ou homologation revendiquée.
- Vérifier les droits des supports multimédias si des illustrations ou voix externes sont ajoutées; le delta actuel est uniquement textuel et original.

## Propositions centralisées (non appliquées)

- Envisager dans une **version ultérieure approuvée** un champ normatif `conditions_accessibilite_oral` pour documenter les équivalences de sortie vocale, les questions répétées et les aménagements.
- Envisager dans une **version ultérieure approuvée** un champ `preuves_distinctes` structuré pour rattacher les deux observations et leurs dates au LMS, sans stocker ces données d'élève dans le canon du Kristal.
- Envisager un protocole interjuges commun à toutes les productions orales; proposition de gouvernance uniquement, pas de modification des registres.

## Consigne de fusion

Décompresser le maître, entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis extraire l'archive de livraison **à cet endroit**, afin de superposer les chemins `kristals/qc-pri-als-012/`. Les deux fichiers `authoring/` livrés remplacent complètement les anciens; les douze autres sont des ajouts. Ne pas extraire ce delta à un niveau englobant supplémentaire.
