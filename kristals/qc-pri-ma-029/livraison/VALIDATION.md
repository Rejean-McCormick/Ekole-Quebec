# Validation technique et limites — `qc-pri-ma-029`

**Statut :** rédaction complète; items paramétriques à `a_revoir`. **Non homologué, non certifié.**

## Vérifications effectivement réalisées

- **2623 assertions préarchivage réussies** : nomenclature, 14 fichiers, YAML canonique et 12 sections, 2 remplacements/12 additions, contrat et famille natifs, 10 items/numérotation, 2 contextes de maîtrise, plan et grille, droits et accès.
- **2000 générations recalculées indépendamment** (1000 seeds pour chaque algorithme); formule et cardinalité des coordonnées contrôlées, en plus de 8 exemples explicites et des 2 seeds opérationnels.
- **8 réponses fixes vérifiées** par calcul élémentaire indépendant, et **2 corrigés paramétriques** vérifiés par énumération de positions cubiques et comptes de couches.
- **Simulation de fusion** dans un répertoire temporaire : seuls les deux fichiers existants d’auteur remplacés et les douze fichiers nouveaux ajoutés; les autres fichiers originaux inchangés (SHA-256).
- **Test final ZIP** effectué après création : noms, non-vacuité, intégrité CRC, manifestes et JSON (voir journal d’exécution). Aucune observation en classe, validation humaine de barème ou audit PFEQ effectué.

## Couverture

- Deux remplacements v1.2 : `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`.
- Douze nouveaux fichiers : 6 `contenu/`, 3 `evaluation/`, 1 `sources/`, 2 `livraison/`.
- Aucun autre fichier, ID, registre, document central ou système canonique dans le ZIP.

## Limites et revue humaine

1. **Mathématique** : revoir les textes de stimuli et la distinction cubes de référence / cm³ / faces; même si les calculs sont vérifiés mécaniquement, la validité de l'interprétation par un enfant n'est pas établie.
2. **Didactique** : tester les rubriques d'autonomie, la charge de lecture, les cartes à niveaux et la différence réelle entre les deux épreuves.
3. **Accessibilité et sécurité** : examiner grosses pièces, risques liés aux petits objets, affichage de grilles, contraste, relief et communication assistée avec des personnes compétentes.
4. **Droits** : confirmer les licences si des images ou supports tiers sont ajoutés ultérieurement; aucun contenu de ce type livré.
5. **Qualification** : pas de tests auprès d'élèves ni de preuve de validité psychométrique, aucune référence de conformité PFEQ produite.

## Propositions de structure (sans modifier les bases centrales)

- Ajouter plus tard aux schémas communs des champs `seed_algorithm_version` et `independent_solver_test_id` pour les générateurs paramétriques, avec migration centralisée versionnée.
- Définir un protocole partagé de représentation accessible des niveaux de cubes, distinct des données canoniques du volume.
- Examiner un statut explicite `controle_numerique_passe_non_homologue` distinct de `validation_status` pour éviter toute confusion entre exactitude calculée et qualification humaine.
