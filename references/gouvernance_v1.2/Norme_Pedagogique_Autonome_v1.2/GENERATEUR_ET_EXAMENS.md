# Génération de questions et d'épreuves

## Contrat minimum d'une famille
`family_id`, `kristal_id`, `objectif_id`, `critere`, `type`, `niveau_complexite`, `representation`, `variables`, `contraintes`, `barreme_ou_rubrique`, `source`, `seed`, `validation_status`.

## Trois modes

- **Fixe contrôlé** : stimulus, tâche, corrigé/rubrique verrouillés; idéal pour ancrage et comparaison.
- **Paramétrique déterministe** : plages de valeurs, contraintes mathématiques, solution vérifiée par solveur indépendant, filtrage des équivalences, seed reproduisible.
- **Variations contextuelles encadrées** : texte, image ou cas de situation substitués uniquement dans un corpus approuvé; score sur grille d'arguments ou performance.

Ne jamais utiliser de tirage libre d'une IA comme seul contrôleur de la réponse. Les items sont liés aux preuves de chaque microparcours. Chaque plan d'épreuve fixe d'abord les objectifs, compétences internes, poids et niveaux, puis autorise une variation du contexte.

## Décisions de maîtrise

- Vérifier la stabilité de la performance dans des contextes distincts, pas la chance à un QCM.
- Feedback descriptif et remédiation ciblée après erreur.
- Pour un examen sommatif local : validation humaine des rubriques, biais culturels, clarté et durée.
- Pour CCQ : ne pas inférer croyances ou convictions. Pour arts/EPS : ne pas noter goûts, morphologie ou divulgations personnelles.

**État actuel :** 202 blueprints de familles, **aucune banque d'items finale ni examen certifié** dans ce lot.
