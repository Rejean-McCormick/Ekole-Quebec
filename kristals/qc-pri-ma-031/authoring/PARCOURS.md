---
format: qc.learning-path/1.0
id: qc-pri-ma-031
titre: Lire et produire des diagrammes
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.3.0
langue_contenu: fr-CA
resultat_principal: Lire, créer et critiquer une représentation graphique de données.
objectifs_secondaires: []
criteres_reussite:
- Produire un diagramme et repérer une interprétation incorrecte.
prealables_declares:
- qc-pri-ma-030
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-031-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-031`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Lire et produire des diagrammes  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**État de livraison :** contenu rédigé; vérification technique effectuée, revue pédagogique humaine requise.

## 1. Intention et frontières

- `obj-1` — **Résultat vérifiable IMMUTABLE :** Lire, créer et critiquer une représentation graphique de données.
- `crit-1` — **Preuve autonome IMMUTABLE :** Produire un diagramme et repérer une interprétation incorrecte.
- **Concepts :** axes, catégories, échelle, diagramme (en particulier diagramme à bandes).
- Savoir lire un diagramme ne prouve pas à lui seul la compétence de le produire; celle-ci requiert choix d'une échelle, exactitude des barres et critique d'une affirmation.
- Les jeux de données sont entièrement fictifs et discrets; aucun fait réel n'est inféré.

## 2. Notions et représentations

- **Axe des catégories :** emplacement des modalités distinctes (sur l'horizontale dans nos diagrammes à bandes verticales; sur la verticale dans un diagramme horizontal).
- **Axe des quantités :** graduation numérique avec origine zéro et intervalle constant, avec unité (« objets », « prêts »...).
- **Catégorie :** groupe nommé et mutuellement distinguable; un effectif correspond à une catégorie, sans compter deux fois la même observation.
- **Échelle :** valeur représentée par un intervalle ou par un bloc, constante dans le même diagramme (p. ex. 1 bloc = 2 objets).
- **Diagramme à bandes :** représentation de catégories par des bandes de largeur uniforme dont la longueur est proportionnelle au nombre correspondant; source du nombre fournie par un tableau.
- **Représentations :** jetons/étiquettes → tableau d'effectifs → bandes tracées sur papier quadrillé ou texte structuré → lecture critique d'un énoncé. Voir `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- **Préalable strict :** `qc-pri-ma-030` (collecter et organiser des données); aucun autre préalable ajouté. Attester un acquis équivalent par `diag-1` et `diag-2` autorise l'entrée sans obliger l'étude du Kristal préalable.
- `diag-1` : compter les éléments d'une petite collection classée puis remplir un tableau d'effectifs sans double comptage.
- `diag-2` : interpréter une bande de trois unités à échelle 2, nommer sa catégorie et justifier le nombre.
- **Décision :** si le regroupement ne réussit pas, reprendre classement et tableau; si la conversion bloc→valeur pose problème, revenir à des jetons groupés; si les deux sont justes, enseignement direct ou tâche avancée.

## 4. Enseignement guidé

- `teach-1` : expliciter « que représentent les catégories ? », « que vaut une graduation ? », « les bandes sont-elles proportionnelles ? ».
- Démonstration commentée A : données fictives d'activités du midi, échelle 2, lecture des effectifs et contrôle du total.
- Démonstration commentée B : représentations de lectures en classe, échelle 1; repérer l'écart et vérifier une fausse interprétation.
- L'enseignant verbalise : *Je place le zéro, choisis une graduation constante, associe chaque bande au nombre du tableau et je vérifie les étiquettes.*
- L'élève explique pourquoi trois blocs à échelle deux représentent six objets et non trois.

## 5. Pratique accompagnée

- `guided-1` : tableau de quatre catégories → diagramme à échelle 1 (étiquettes et axes donnés; indices explicites).
- `guided-2` : interprétation à échelle 2 et comparaison (un seul indice de rappel de l'échelle).
- `guided-3` : production et détection d'une conclusion fausse (sans indice avant correction).
- Rétroaction dès l'erreur : « lis l'unité et l'échelle avant de comparer les barres »; reconstituer au besoin des groupes de deux jetons.
- Corrigés, dessins textuels et protocole des indices dégressifs dans `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- `independent-1` à `independent-4` : quatre jeux fictifs jamais repris tels quels dans le modelage : construire avec échelle 1, reconstruire avec échelle 2, critiquer une conclusion non fondée, corriger un diagramme aux graduations trompeuses.
- Réponse sous forme de graphique à bandes, tableau de couples (catégorie, hauteur) avec axes explicités, ou représentation tactile équivalente; toujours préserver l'information quantitative.
- Tâches et corrigés détaillés dans `contenu/05_PRATIQUE_AUTONOME.md`.

## 7. Feedback et erreurs typiques

- Confusion bloc/unité : 3 blocs avec 1 bloc = 2 sont 6 (pas 3) → manipuler six jetons par paires.
- Graduation irrégulière : ne pas écrire 0, 2, 4, 8 à intervalles égaux → reconstruire 0, 2, 4, 6, 8.
- Barres non proportionnelles : hauteur tracée ≠ effectif → comparer chaque barre au tableau, sans viser l'esthétique.
- Inférence excessive : « la catégorie la plus élevée est préférée par toute l'école » → distinguer « dans ce jeu de données » et généralisation injustifiée.
- Feedback descriptif suivi d'un nouvel essai sur d'autres nombres (`contenu/06_REMEDIATION_ET_TRANSFERT.md`).

## 8. Évaluation formative et preuves

- **Famille IMMUTABLE :** `qc-pri-ma-031-ev-01` ; objectif `obj-1` ; critère `crit-1`.
- Banque de 10 items (`evaluation/BANQUE_ITEMS.json`) : 6 fixes et 4 paramétriques contrôlés; lecture, réalisation, critique et transfert.
- Les items `q-009` (bibliothèque fictive) et `q-010` (atelier de réparation fictif) sont deux preuves de maîtrise indépendantes. Chacun exige un diagramme cohérent et l'identification argumentée d'une interprétation incorrecte.
- **Décision :** maîtrise après deux manifestations satisfaisantes en contextes distincts, toutes deux autonomes; jamais par simple note cumulée.
- Les variations numériques proviennent d'un catalogue fini, d'un index calculé à partir d'un seed entier, et de corrigés recalculés; validation humaine encore nécessaire.

## 9. Remédiation / enrichissement

- Axe/étiquette omis → gabarit axes et unités à compléter, puis retrait de l'aide.
- Échelle mal convertie → lots de deux jetons puis 1 bloc = 2, nouveaux nombres.
- Difficulté de comparaison → calculer la différence sur le tableau avant de la lire sur le graphique.
- Critique insuffisante → compléter « l'énoncé affirme… / les données montrent… / donc… ».
- Enrichissement : comparer deux échelles régulières pour les mêmes données et expliquer pourquoi les effectifs ne changent pas.

## 10. Accessibilité

- Énoncés en langage clair et données disponibles en tableau texte structuré; ne pas coder les catégories uniquement par couleur.
- Papier quadrillé à grands carreaux, règle, quadrillage tactile, bandelettes amovibles ou outil numérique accessibles selon besoin.
- Lecture orale des consignes, saisie assistée ou réponse dictée permises si les choix d'échelle, de catégorie et les justifications proviennent de l'élève.
- Adapter la motricité/vision sans diminuer la précision mathématique; informer des unités et de l'origine zéro.

## 11. Critères de sortie

1. Dans chacun de deux contextes inédits, produit une représentation correcte : catégories distinctes, axes/titres/unité indiqués, échelle constante à partir de zéro, toutes les hauteurs exactes.
2. Identifie une interprétation fausse et la remplace par un énoncé appuyé sur au moins deux valeurs chiffrées pertinentes ou une comparaison calculée.
3. Explique son choix d'échelle et peut vérifier sa production contre le tableau source sans indice portant sur la solution.
4. Si une condition manque dans l'une des deux preuves, remédiation ciblée puis nouvelle double vérification, sans conclure à la maîtrise sur la base du total de points.

## 12. Références pédagogiques et limites

- Fichiers normatifs v1.2 lus dans le ZIP maître : `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md` et graphe 202 (non copiés).
- Concepts de diagrammes étayés par Statistique Canada; accessibilité des équivalents textuels étayée par W3C WAI. Voir `sources/REFERENCES_CONTENU.md` pour URL, statut et droits.
- Production graphique, exercices, valeurs et rubriques sont originaux; pas de certification, d'homologation ni d'équivalence officielle PFEQ.
- **À revoir humainement :** niveau de difficulté, équité et accessibilité réelle des supports, qualité des consignes et cohérence des grilles; tester avec des élèves avant toute publication.
- **Rappel différé :** J+2 lire un diagramme à échelle 2 de données inédites; J+7 produire trois bandes à échelle 1 puis corriger une affirmation; J+21 créer et commenter un autre graphique sans rappel des exemples. Ces rappels ne constituent pas, seuls, une preuve de maîtrise.
