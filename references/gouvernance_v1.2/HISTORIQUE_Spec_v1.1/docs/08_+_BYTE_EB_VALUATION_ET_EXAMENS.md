# 08 — Contrat des évaluations, banques de tâches et examens

## 8.1 Séparation stricte

- **Critère** : propriété observable associée à un objectif et à un référentiel applicable.
- **Famille de tâches** : gabarit abstrait de situations permettant de recueillir une preuve.
- **Item** : question, tâche pratique ou consigne particulière issue de la famille.
- **Instance** : réalisation concrète d'un item (paramètres, support, ordre, seed) avec solution/rubrique.
- **Plan d'épreuve** : couverture visée des objectifs/compétences, poids, types de tâches, conditions, équilibrage.
- **Épreuve** : sélection ordonnée d'instances et de rubriques issue d'un plan publié.

**Le plan d'épreuve gouverne la génération; l'aléa ne choisit jamais les attentes évaluées.**

## 8.2 Déclaration des familles dans une feuille

Chaque famille d'évaluation possède : `family_id`, `objectif_ref`, `competence_ref` si connue, `critere_ref`, `format`, `difficulte_cible`, `variables`, `contraintes`, `solution_ou_rubrique`, `strategie_feedback`, `generabilite`, `verification`, `accessibilite`, `risques`, `licence_support`.

`generabilite` peut être :

1. `fixe_valide` — support et corrigé approuvés, rien n'est généré sans requalification;
2. `parametrique_controle` — valeurs tirées dans un domaine borné, calcul de la réponse par vérificateur exact ou procédure déterministe;
3. `generee_sous_contraintes` — tâche nouvelle proposée par générateur, soumise à contrôle automatisé + relecture humaine selon risques;
4. `observation_ou_production` — production authentique ou tâche pratique, rubrique critériée; correction humaine lorsque nécessaire.

Une question `generee_sous_contraintes` n'est **jamais** admise à une épreuve sommative à enjeux significatifs sans qualification documentée de ses variantes et du modèle d'évaluation.

## 8.3 Plan d'épreuve obligatoire

À partir du [modèle](../modeles/MODELE_PLAN_EPREUVE.md), fixer AVANT génération : programme/édition, année/variante, compétences, résultats observables, matrice de couverture, poids et critères, nombre de tâches si justifié, supports accessibles, temps/modalités selon contexte, familles permises, niveaux de difficulté, règles de tirage, correction, tolérances et supervision humaine.

Sans cadre d'évaluation applicable, l'épreuve reste `entrainement_non_certifie` ou `brouillon`, jamais alignée comme officielle.

## 8.4 Aléatoire contrôlé

Chaque instance contient `blueprint_id`, `family_id`, `item_id`, `seed`, `parameters`, `generated_at`, `generator_version`, `content_revision`, `source_commitment`, `answer_key_revision`, `verification_result`.

- Geler `seed` et version du générateur pour **rejouer exactement** l'instance, à variables sources égales.
- Contraintes explicites : plage, type, nombre de décimales, unités, unicité ou multiplicité des réponses, évitement d'ambiguïtés, langue, niveau.
- Calcul numérique : vérifier la solution par code exact/rationnel lorsque pertinent et tester les frontières du domaine de paramètres.
- Textes / questions ouvertes : vérifier licence, lisibilité, couverture de la compétence, ambiguïtés, grille de correction. L'IA ne s'auto-homologue pas.
- Écarter les doublons et variantes trop proches si cela compromet l'équité; équivalence de difficulté **non présumée** sans preuves empiriques.
- Pour les évaluations à enjeux, conserver les exemplaires générés, les réponses attendues, les versions et la revue.

## 8.5 Barèmes et corrections

- QCM : clé de réponse et justification de chaque distracteur plausible.
- Réponse numérique : expression exacte attendue, unités, tolérances motivées et cas d'équivalence (ex. fractions).
- Production écrite/orale : grille analytique avec descripteurs; échantillons d'ancrage lorsque possible; intervention humaine.
- Arts/EPS/CCQ : grilles d'observation adaptées au programme, évaluation du processus/démarche et de critères observables, pas d'opinions intimes.
- Chaque preuve conserve ses **limites**; ne pas surinterpréter un exercice simple comme maîtrise entière d'une compétence transversale.

## 8.6 Deux sorties distinctes

- **Pratique formative** : rétroaction immédiate, reprises, tirages variés, faible enjeu.
- **Épreuve sommative locale** : plan de couverture, validation humaine, exactitude des corrections, conservation et audit de la version. Une épreuve produite par nous **n'est pas une épreuve ministérielle**.

Les formats Moodle (quiz, banque, XML/GIFT quand le format de tâche s'y prête) sont des **exports**. Les productions et observations non représentables dans un quiz requièrent d'autres activités Moodle ou une modalité externe.
