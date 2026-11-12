# CONTRAT PÉDAGOGIQUE v1.2 — AUTORITÉ ACTIVE

**Statut : adopté pour la construction.** Remplace, pour les sujets pédagogiques, les prescriptions de la norme v1.1 conservée dans `governance/HISTORIQUE_Spec_v1.1/`.

## 1. Frontières

1. Le primaire québécois sert de **nomenclature et de structure de présentation** : six années, trois cycles, noms de disciplines.
2. Le système Kristal possède les décisions sur le savoir, l'ordre, la méthode, la progression, les préalables, les seuils et l'évaluation.
3. L'alignement à la Progression des apprentissages du Québec n'est **plus un gate de construction ni de publication**.
4. Une projection peut afficher la charte de conversion; elle **ne doit jamais affirmer** la conformité, l'approbation ou l'équivalence officielle sans procédure distincte.
5. `A-Kristal-ScolQc` demeure l'index descriptif du système scolaire, sans imposer ses prescriptions au moteur pédagogique.

## 2. Identités et portabilité

- 202 IDs `qc-pri-*` invariants et titres thématiques maintenus.
- 202 workspaces Kristal locaux; aucun objet canonique v9 n'est construit à partir des seules sources Markdown.
- Une feuille = un objectif principal observable, contenu structuré, diagnostic, enseignement, pratique, rétroaction, transfert et évaluation.
- Une notion dont le sens est partagé reste possédée par une source canonique; les autres feuilles référencent son ID.

## 3. Graphe

- `requires(A,B)` : pour viser A, B est normalement requis; un **diagnostic attestant un acquis équivalent** remplit la condition sans forcer la lecture préalable de B. Graphe acyclique.
- `recommends_before(A,B)` : séquence suggérée, jamais bloquante.
- `reinforces(A,B)` : réutilisation et transfert possibles; aucun verrou.
- Toutes les arêtes présentes dans `registry/GRAPHE_PEDAGOGIQUE_202.json` constituent **des choix de design validés en interne**. Ce ne sont ni des codes ministériels ni des relations prouvées universelles.
- Ne pas transformer les liens conseillés en conditions techniques d'accès.

## 4. Méthode commune

Diagnostic court → objectif explicite → modèle guidé → pratique accompagnée avec indices dégressifs → autonomie avec nouveau contexte → preuve de maîtrise → rappel différé → transfert.

**Adaptations par discipline :** langage oral/écrit, représentations mathématiques, investigation scientifique, analyse critique de sources, dialogue respectueux, création artistique ou performance motrice sécuritaire.

**Attention :** la mémorisation et l'automatisation soutiennent l'apprentissage, sans remplacer argumentation, exploration, création et collaboration.

## 5. Maîtrise et évaluations

- Chaque feuille fixe une preuve observable et une grille évaluant ce qui a été enseigné.
- Une maîtrise ne découle ni d'un score unique ni de l'âge : elle nécessite au minimum deux manifestations dans des contextes différents et une preuve d'autonomie ou d'adaptation.
- **Mathématique :** paramètres numériques contrôlés et corrigé calculé/testé.
- **Lecture/langues/sciences/univers social :** tâches sources et contextes fixés, critères explicites, revue des faits et des rubriques.
- **CCQ :** scénarios fictifs, aucun score sur croyances, vie privée ou identité.
- **Arts/EPS :** grilles critériées de processus, pas QCM forcé ni jugement esthétique ou corporel.
- Les questions créées par IA ne sont **pas des items certifiés** sans revue, contrôle de solution et essai.

## 6. Travail parallèle

- Une conversation possède exclusivement un lot d'IDs.
- Les objectifs et les relations sont **établis à l'échelle du programme** dans le registre v1.2; tout changement exige une proposition centralisée versionnée.
- Le rédacteur peut développer le cours, illustrations originales, exemples, items et feedback, mais ne modifie pas un autre workspace.
- La qualification implique une revue de contenu et des tests techniques, **pas un audit de conformité PFEQ**.
