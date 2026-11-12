# Validation de la livraison v1.2 — `qc-pri-us-015`

**Statut :** contenu et évaluation rédigés, **revue humaine nécessaire**, ni « homologué », ni « publié », ni items « certifiés ». Rapport dressé après les contrôles techniques, le 8 octobre 2026.

## Journal des changements

- **Remplacement** : `authoring/PARCOURS.md`, rédaction des 12 sections tout en préservant les champs YAML canoniques.
- **Remplacement** : `authoring/CONTRAT_PEDAGOGIQUE.json`, famille native enrichie des champs de gouvernance sans perte de ses champs initiaux.
- **Ajouts** : six leçons `contenu/`, trois fichiers d'évaluation (plan, banque, grille), références, manifeste et validation.
- **Hors périmètre intouché** : graphes, registres, gouvernance, canon, `ALIGNEMENT.md`, autres Kristals et bases runtime/state/docs.

## Contrôles réellement exécutés

- **485 assertions préarchivage réussies** par vérificateur Python : arborescence, non-vacuité, chemins sûrs, YAML parsable, 12 sections, conservation des métadonnées, familles et préalables, JSON des dix items, modes fixes, références, critères, sécurité, accessibilité, contenu pédagogique et cohérence de leurs sources fictives. Les assertions portent sur le texte et la structure, pas sur la qualité scientifique testée en classe.
- **Deux manifestations autonomes distinctes contrôlées** : q-009 (presse manuelle/mécanique et réparation des livres en 1910/1940/1970), q-010 (charrette/camion et denrées du marché en 1920/1950/1980). Aucun corpus de maîtrise préexposé dans les huit items formatifs.
- **Analyse des corrections** : contrôle explicite des codes/dates, des différences et continuités dans les deux corpus originaux, puis inspection sémantique du texte des dix corrigés. Aucun oracle d'histoire réelle n'est attribué à ces scénarios fictifs.
- **Conservation de la frame** : deux fichiers authoring remplacés, douze nouveaux fichiers; simulation de superposition sans changement des autres fichiers source (SHA-256).
- **Provenance et droits** : sources institutionnelles externes vérifiées pour le seul exemple postal; aucun document/image sous licence externe n'est recopié. Les six corpus historiques sont décrits comme **fictifs**.
- **Archive finale** : contrôles de 14 chemins exacts, manifeste, données JSON et intégrité CRC exécutés après écriture (voir résultat du validateur terminal).

## Limites non résolues

- Les pièces L/B/E/J/R/M sont des **scénarios fictifs**; leurs dates ne sont pas des événements historiques réels. Le contrôle exact vérifie la cohérence **interne du récit**, non la véracité externe.
- Les citations institutionnelles externes sont vérifiées seulement pour l'exemple postal, sans droits de reproduction d'images sollicités.
- Aucune calibration psychométrique ni fidélité intercorrecteur testée, aucun essai sur élèves, aucune validation de la compréhension par différents âges, aucune enquête sur un patrimoine ou une communauté réelle.
- Les grilles d'arguments et les seuils restent des **propositions éditoriales** à réviser avant toute décision d'évaluation.

## Revue humaine recommandée

1. **Historien(ne)/didacticien(ne)** : pertinence du vocabulaire, distinction entre travail sur corpus inventés et enquête sur archives authentiques, justesse des limites.
2. **Évaluateur(trice)** : validité des items fixes, rubriques des deux preuves distinctes, clarté des feedbacks et jugement sans note unique.
3. **Accessibilité** : lisibilité, lecture assistée, effets de la dictée, versions tactiles et communication alternative; exigences cognitives inchangées.
4. **Provenance/droits** : vérifier toute future importation d'images ou documents historiques authentiques.

## Propositions de structure, non appliquées

- Ajouter ultérieurement un champ contrôlé `source_type` (« authentique/secondaire/didactique_fictive ») à un schéma partagé, avec procédure de revue externe.
- Définir une banque versionnée de pièces datées authentiques et leurs licences après validation des droits.
- Ajouter un journal de revue intercorrecteurs pour les rubriques d'analyse de sources, **sans toucher aux fichiers centraux**.
