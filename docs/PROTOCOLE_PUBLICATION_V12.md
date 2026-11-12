# Protocole qualité — v12

## Paliers contrôlés

**P0: source et plan de conception** — objectif, concepts et preuve originaux intacts; suggestions générées explicitement non revues.
**P1: prototype** — interaction déterministe avec rétroactions, aucune prétention de maîtrise; test automatique du scénario réussi.
**P2: revue pédagogique** — exactitude, représentations, erreurs typiques, qualité des consignes, variantes et transfert examinés par un enseignant et un responsable des contenus.
**P3: essai d'usage** — observations en contexte scolaire, accessibilité clavier et lecteur d'écran, qualité des indices, autonomie et charge cognitive mesurées.
**P4: publication institutionnelle** — approbation explicite du référentiel et des affectations par cycle/année, conformité des contenus et de la vie privée, politique de données, authentification école et procédures de correction.

Il est interdit de confondre une réussite de manipulation avec une preuve de maîtrise. Le simulateur peut exposer ses solutions dans les données publiques. Les évaluations sensibles demeurent du côté Enseignant, sans diffusion automatique dans un navigateur anonyme.

## Les 5 pilotes

- **Fractions** : trois représentations vérifiées par comptage de parts; justification du tout observée humainement. La grille algorithmique n'établit pas que les parts sont comprises sans explication.
- **Division** : répartition, équilibre et reste calculés. Comparaison partage / groupement reste une tâche de transfert à concevoir et observer.
- **Récit** : ordre et liens de causalité illustratifs. Justification originale en mots nécessite une revue humaine.
- **Sciences** : classifier observation / interprétation. La conception d'une question investigable n'est PAS validée par ce mini-monde et doit être ajoutée dans une étape de conception suivante.
- **Théâtre** : préparation par gestes/voix/espace et présentation à une personne. **Aucune évaluation automatique** de l'expression.

## Atelier d'auteur

L'atelier protégé est accessible par le serveur enseignant local et ne fournit pas de droits institutionnels. Les modifications sont exportées comme fichier proposition. `tools/appliquer_plan_v12.py` vérifie la concordance des sources et protège le travail existant par une sauvegarde idempotente. Une proposition ne peut pas modifier les objectifs source ni marquer une révision institutionnellement approuvée.

## Images

Le registre est exclusivement conceptuel. Une ressource visuelle n'est visible que si elle est **localement présente** et approuvée; à défaut, afficher le texte brut du prompt. Ne jamais imposer de style graphique, ni demander à une IA de générer des nombres ou diagrammes dont dépend une validation exacte. Favoriser le rendu HTML/SVG déterministe pour les constructions évaluées.
