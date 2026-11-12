---
format: qc.learning-path/1.0
id: qc-pri-ma-017
titre: Pourcentages et situations de proportionnalité
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Relier pourcentage, fraction de cent et situations proportionnelles simples.
objectifs_secondaires: []
criteres_reussite:
- Déterminer une quantité correspondant à un pourcentage simple et la vérifier.
prealables_declares:
- qc-pri-ma-013
- qc-pri-ma-015
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-017-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-017`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Pourcentages et situations de proportionnalité  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** contenus et items rédigés; revue pédagogique humaine requise avant usage qualifié.

## 1. Intention et frontières

- `obj-1` — **Résultat observable IMMUTABLE :** Relier pourcentage, fraction de cent et situations proportionnelles simples.
- `crit-1` — **Preuve autonome IMMUTABLE :** Déterminer une quantité correspondant à un pourcentage simple et la vérifier.
- Champ : pourcentages de base (5 %, 10 %, 20 %, 25 %, 50 %, 75 %, 100 %), totalité explicitement définie, parts entières dans les tâches évaluées, ratios et tableaux de proportion. L'élève explicite la valeur de la base et son unité; les variations d'items d'examen sont plus resserrées.
- Hors-champ : intérêt composé, variations de pourcentage successives, statistiques d'échantillonnage, extrapolation sans proportionnalité. Une situation fictive n'énonce pas de fait sur la population.
- L'âge, la classe et un code officiel de cours ne sont pas assignés à cette feuille.

## 2. Notions et représentations

1. **Part sur cent :** `p % = p/100`, une proportion de la *totalité*, non une soustraction de `p` unités. Sur 100 carreaux identiques, 25 % = 25 carreaux; sur 60 carreaux, 25 % = 15.
2. **Ratio :** relation multiplicative entre quantités comparables. Le ratio partie/tout est `q/N = p/100` pour `N > 0`; garder les mêmes unités et le même tout. Ne pas confondre un ratio avec une différence.
3. **Tableau de proportion :** chaque colonne est reliée par le même coefficient : passer de 100 % à `N` unités multiplie par `N/100`, donc de `p %` à `q` unités aussi; `q = N×p/100`.
4. **Trois voies :** matériel (100 jetons ou grille), schéma (barre en quarts/dixièmes), notation (fractions égales, tableau). Travailler d'abord sur des moitiés/quarts exacts puis vers le tableau.
5. **Contrôle :** `q/N = p/100` si `N > 0`; sinon `q = N×p/100` et somme part + complément = `N`. Interpréter `q` dans l'unité du problème.

**Contre-exemples :** `20 % de 80 = 80 − 20` est faux (20 est un nombre de parts *sur cent*, pas 20 objets); `25 % de 60 = 25` est faux (25 objets ne sont corrects que pour une base de 100). Voir `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- `requires` stricts : `qc-pri-ma-013` (fractions équivalentes) et `qc-pri-ma-015` (représentations décimales). **Diagnostic d'acquis équivalent autorisé**, même sans fréquentation de ces deux Kristals; ne pas confondre absence de trace de lecture et absence de compétence.
- `recommends_before` : aucun. `reinforces` : aucun.
- `diag-1` : écrire 1/4 sous forme équivalente sur 100, puis justifier par une grille ou un raisonnement : `1/4 = 25/100`.
- `diag-2` : sur une grille de 100 cases, repérer 0,5 unité; `0,5 = 50/100 = 50 %`. Repérer 50 %, et distinguer 50 % de 50 objets quand la base change.
- `diag-3` (vérification du sens) : 50 % de 18 jetons = 9, à montrer en deux groupes égaux; vérifier `9 + 9 = 18`.
- Décision : si l'équivalence fractionnaire ou la base décimale est fragile, revenir aux représentations concrètes du prérequis concerné, puis rediagnostiquer. Voir `contenu/02_DIAGNOSTIC.md`.

## 4. Enseignement guidé

- `teach-1` : annoncer `obj-1`, nommer explicitement la totalité et son unité.
- Modelage A : dessiner 100 cases, en colorier 25; passer à `25/100 = 1/4 = 25 %`.
- Modelage B : pour 25 % de 60 livres fictifs, faire quatre groupes égaux de 15 et poser le tableau `100 % ↔ 60`, `25 % ↔ 15`. Vérifier `4 × 15 = 60`.
- Modelage C : pour 20 % de 80, trouver 10 % (=8), doubler (=16); vérifier `16/80 = 1/5` et `20/100 = 1/5`.
- Faire préciser pourquoi `80 − 20` ne donne pas 20 %; montrer que 20 % indique une *fraction de la base*.
- Pause orale : « Quand la base passe de 100 à 80, est-ce que 20 % reste 20 objets? Pourquoi? »
- Les pas détaillés figurent dans `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- `guided-1` : 50 % de 34 billes fictives = 17; indices complets (deux groupes égaux, fraction, unité) et vérification `17+17=34`.
- `guided-2` : 25 % de 80 cartes = 20; indice réduit « pense à un quart »; vérification `4×20=80`.
- `guided-3` : 20 % de 150 pages = 30; seulement la question « quelle est la base? » puis retrait de toute aide; vérification `30/150=20/100`.
- Cesser les indices avant les preuves de maîtrise; la correction peut revenir à la barre fractionnée ou au tableau à double entrée. Détails : `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- `independent-1` : 10 % de 230 feuilles = 23; calcul et vérification `10×23=230`.
- `independent-2` : 25 % de 120 étiquettes = 30; vérifier `4×30=120`.
- `independent-3` : 75 % de 80 cartons = 60; vérifier `60+20=80` et `60/80=75/100`.
- `independent-4` : 20 % de 45 minutes = 9 minutes; `45÷5=9`, puis `5×9=45`.
- Réponses attendues et critères sont fournis en `contenu/05_PRATIQUE_AUTONOME.md`. Produire d'abord sans modèle visible.
- **Deux preuves de maîtrise indépendantes distinctes** : items `q-009` (atelier de maquettes) et `q-010` (pots dans un potager fictif), après entraînement, sans indice ni réponses modèles visibles. Chaque preuve exige quantité + vérification + unité.

## 7. Feedback et erreurs typiques

- Mauvaise base (« 20 % vaut toujours 20 ») : faire nommer le tout, puis dessiner un quart/dixième; comparer 20 % de 100 et 20 % de 60.
- Soustraction additive (« 80 − 20 ») : demander le sens de `%`, convertir en `20/100` et utiliser `10 %` comme étape.
- Pourcentage sans unité (« 25 % de 60 = 15 % ») : distinguer `p` en pour cent et `q` en objets/minutes.
- Tableau non proportionnel : identifier l'unique coefficient utilisé; vérifier une deuxième colonne et l'égalité des ratios.
- Arrondi injustifié : se limiter aux valeurs exactes du corpus, représenter une fraction de cent, vérifier par multiplication.
- Réponse juste sans justification : demander une preuve indépendante (complément, fraction équivalente ou tableau). Voir `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- Famille `qc-pri-ma-017-ev-01`, objectif `obj-1`, critère `crit-1`, type natif `paramétrique_controle`.
- Items `q-001` à `q-003` fixes (diagnostic-formatif), `q-004` à `q-008` paramétriques sur jeux fermés, `q-009` et `q-010` preuves autonomes distinctes également paramétriques contrôlées.
- Un item paramétrique = seed entier fixé, couples `(p,N)` autorisés uniquement, algorithme `index=seed mod taille_du_corpus`, solution rationnelle exacte `q=pN/100`. Tous les couples sont vérifiés; aucune génération libre.
- Barème : interprétation du tout et de l'unité, quantité calculée correctement, stratégie proportionnelle explicite, vérification indépendante. Dans les deux preuves, axes essentiels ≥ 2/3 chacun, sans indice, sinon remédiation et nouvelle passation.
- Plan, banque et grille : `evaluation/PLAN_EVALUATION.md`, `evaluation/BANQUE_ITEMS.json`, `evaluation/GRILLE_MAITRISE.md`.

## 9. Remédiation / enrichissement

- Élève confond % et nombre : commencer par 100 cases puis modifier la base (40, 80), verbaliser « chaque part est sur 100 du tout ».
- Élève calcule additivement : apparier deux tableaux 100%/50% puis 100%/25%, explorer le coefficient et débusquer l'erreur sur une variation de base.
- Élève confond ratio partie/tout et partie/partie : étiqueter explicitement numérateur, dénominateur et unité.
- Élève réussit le calcul mais ne le vérifie pas : faire reformuler le tableau inversé ou le complément, sur d'autres nombres.
- Enrichissement : explorer 0 % et 100 % et identifier pourquoi une situation « + 5 objets à chaque étape » ne suffit pas à constituer une proportionnalité.
- Deux transferts originaux (affichage et fanions fictifs) : `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 10. Accessibilité

- Texte en français clair, quantités lues oralement sur demande, typographie des unités, tableau linéarisable, symboles accompagnés de mots et graphiques décrits en texte.
- Autoriser jetons, grille de 100, barre à segments, calcul écrit/oral, clavier, papier quadrillé et outil de lecture; pas d'obligation de discerner des couleurs.
- Ne pas pénaliser lecture, orthographe, vitesse d'écriture ou motricité quand l'objectif est la proportionnalité. L'oral avec trace du raisonnement est valide.
- Matériel : aucun achat ni donnée personnelle; situations fictives; éviter d'évaluer capacités d'achat des familles.
- Le critère numérique et de vérification reste identique quelle que soit la modalité de réponse.

## 11. Critères de sortie

1. L'élève identifie la totalité (`N`) et la portion demandée (`p %`) sans confondre `p` et `q`.
2. Pour chacun des **deux contextes différents**, calcule `q = pN/100` exactement, avec son unité et une explication proportionnelle.
3. Vérifie sa réponse autrement qu'en recopiant l'opération initiale : quarts/dixièmes complémentaires, ratio, recomposition.
4. Réalise les deux tâches sans indice ciblant la solution; s'il manque un axe essentiel sur une tâche, il reçoit une remédiation et une **nouvelle** preuve (pas une moyenne compensatoire).
5. Rappel différé prévu à J+7 et J+21 (dates indicatives ajustables), avec valeurs différentes; un rappel n'est pas automatiquement une nouvelle décision de maîtrise.

## 12. Références pédagogiques et limites

- Sources de gouvernance du workspace : `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md` (voir `sources/REFERENCES_CONTENU.md`).
- Faits mathématiques établis par définition et égalités rationnelles, calculs soumis à des tests exacts décrits dans `livraison/VALIDATION.md`.
- Tous les contextes, images mentales, tableaux et exercices sont des productions rédactionnelles originales, sans emprunt de fiche externe ni revendication de licence sur un tiers.
- Le vocabulaire institutionnel de « Mathématique » est une projection de présentation; aucune conformité PFEQ, homologation ni certification des items n'est revendiquée.
- Statut d'usage : `a_revoir`; une revue humaine des consignes, de la charge cognitive, des adaptations et du niveau des élèves reste nécessaire.
