# Plan d’évaluation — qc-pri-eps-002

**Autorité interne :** `obj-1` Adapter marche, course, saut ou déplacement à un espace et une consigne. **Preuve `crit-1` :** Réaliser un parcours varié avec contrôle des déplacements. **Famille :** `qc-pri-eps-002-ev-01` (`observation_ou_production`). **Aucun préalable bloquant**; `qc-pri-eps-001` conseillé seulement.

## Méthode, couverture et modes

Évaluer une **production motrice observable** : consigne compréhensible → plan de trajet → déplacement réel en zone sûre → justification brève → observation documentée. Les 12 items sont tous liés aux trois identifiants. Couverture : trajectoires droites/courbes/U; allure stable/ralentie; choix de voie; arrêt; vigilance; choix justifié; pratique en salle et en extérieur si sûr. Difficulté `initial` = un repère/ajustement; `intermediaire` = virage ou choix combiné; `transfert` = contexte changé, décision de sécurité et explication.

**Rubrique commune T/A/S/J**, modulée par les critères de chaque item : T = trajectoire voulue suivie et virage(s) maîtrisé(s); A = allure volontairement ajustée; S = contrôle des voies, arrêt, sécurité; J = explication/pointage d’un choix pertinent. La grille `GRILLE_MAITRISE.md` décrit l’autonomie. **Jamais** de barème sur temps, vitesse maximale, capacité brute, morphologie ou comportement relatif aux pairs. Les essais où une intervention est requise pour sécurité sont interrompus et **ne comptent pas** comme autonomes.

## Matrice item ↔ objectif ↔ critère ↔ famille

| Item | Liens invariants | Difficulté | Contexte / mode | Représentation | Critères |
|---|---|---|---|---|---|
| `qc-pri-eps-002-q-001` | `obj-1` / `crit-1` / `qc-pri-eps-002-ev-01` | initial | Tâche fixe | pratique_avec_plan | T/A/S/J; voir critères précis dans banque |
| `qc-pri-eps-002-q-002` | `obj-1` / `crit-1` / `qc-pri-eps-002-ev-01` | initial | Tâche fixe | pratique_avec_plan | T/A/S/J; voir critères précis dans banque |
| `qc-pri-eps-002-q-003` | `obj-1` / `crit-1` / `qc-pri-eps-002-ev-01` | initial | Tâche fixe | pratique_avec_plan | T/A/S/J; voir critères précis dans banque |
| `qc-pri-eps-002-q-004` | `obj-1` / `crit-1` / `qc-pri-eps-002-ev-01` | intermediaire | Tâche fixe | pratique_avec_plan | T/A/S/J; voir critères précis dans banque |
| `qc-pri-eps-002-q-005` | `obj-1` / `crit-1` / `qc-pri-eps-002-ev-01` | intermediaire | Scénario fermé | pratique_avec_plan | T/A/S/J; voir critères précis dans banque |
| `qc-pri-eps-002-q-006` | `obj-1` / `crit-1` / `qc-pri-eps-002-ev-01` | intermediaire | Scénario fermé | pratique_avec_plan | T/A/S/J; voir critères précis dans banque |
| `qc-pri-eps-002-q-007` | `obj-1` / `crit-1` / `qc-pri-eps-002-ev-01` | intermediaire | Scénario fermé | pratique_avec_plan | T/A/S/J; voir critères précis dans banque |
| `qc-pri-eps-002-q-008` | `obj-1` / `crit-1` / `qc-pri-eps-002-ev-01` | transfert | Scénario fermé | pratique_avec_plan | T/A/S/J; voir critères précis dans banque |
| `qc-pri-eps-002-q-009` | `obj-1` / `crit-1` / `qc-pri-eps-002-ev-01` | transfert | Tâche fixe | pratique_avec_plan | T/A/S/J; voir critères précis dans banque |
| `qc-pri-eps-002-q-010` | `obj-1` / `crit-1` / `qc-pri-eps-002-ev-01` | intermediaire | Tâche fixe | plan_et_action | T/A/S/J; voir critères précis dans banque |
| `qc-pri-eps-002-q-011` | `obj-1` / `crit-1` / `qc-pri-eps-002-ev-01` | transfert | Preuve A, salle polyvalente | pratique_avec_plan | T/A/S/J; voir critères précis dans banque |
| `qc-pri-eps-002-q-012` | `obj-1` / `crit-1` / `qc-pri-eps-002-ev-01` | transfert | Preuve B, cour autorisée | pratique_avec_plan | T/A/S/J; voir critères précis dans banque |

## Variation autorisée et contrôles

- `q-001`–`q-004`, `q-009`–`q-012` : tâches **fixes** (8); variations d’accessibilité admises : largeur/longueur/angle des courbes, modalité sûre, forme accessible de la consigne et justification. Le noyau T/A/S/J ne change pas.
- `q-005`–`q-008` : **scénarios contrôlés** (4) avec **exactement deux textes complets et deux rubriques attendues liées** stockés en `parametres.corpus_variantes`. Aucune génération de texte libre. Sélection reproductible : `index = seed % 2`; seeds respectives 205, 206, 207, 208; banque affiche le stimulus et la réponse de l’instance sélectionnée et documente aussi la seed suivante. Les résultats réels demeurent des observations humaines, jamais des prédictions factuelles sur la personne.
- Limite impérative : ne jamais modifier le sens de « arrêt », la sécurité, la règle de variation ni introduire de surprise motrice ou d’obstacle. Toute différence d’aménagement documentée n’influence pas la cote, à critères équivalents.

## Deux manifestations distinctes de maîtrise

1. **Preuve A (`q-011`)** : parcours salle polyvalente avec deux virages et arrêt, aide d’accès permise, **sans indice de solution** pendant l’essai.
2. **Preuve B (`q-012`)** : parcours en U en cour autorisée après inspection, ou **autre espace intérieur clairement distinct** si l’extérieur est non sûr, sans indice de solution pendant l’essai.

Conserver deux traces réelles, datées et contextualisées : voie/dispositif, adaptations, faits observés T/A/S/J, degré d’aide de solution, décision de sécurité. Deux contextes, sécurité dans les deux et autonomie sont nécessaires; pas de déduction d’une note unique. Les deux tâches sont indépendantes des exemples E1/E2 du cours.

## Sécurité, protection et accessibilité

Supervision de l’adulte, surface libre/stable, un seul passage par voie ou voies disjointes, repères plats, aire d’arrêt ample et signaux annoncés assez tôt. Aucun saut obligé, aucune compétition, chronométrage, course contre un autre, obstacle dangereux ou dévoilement de données médicales. Entrée orale/visuelle/pictographique équivalente, trajets élargis et locomotion avec aide admis. Si l’adaptation motrice sûre n’est pas encore faisable, la preuve est **différée**, non remplacée silencieusement par un QCM ou un plan.

## Qualification et limites

Items rédigés et contrôles structurels exécutés; `validation_status = a_revoir` pour tous. Revue humaine de faisabilité, sécurité des lieux, âge des participants, clarté et fidélité de la grille obligatoire avant déploiement. Aucun examen certifié par une IA. Voir `livraison/VALIDATION.md`.
