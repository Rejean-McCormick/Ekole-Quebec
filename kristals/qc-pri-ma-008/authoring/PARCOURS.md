---
format: qc.learning-path/1.0
id: qc-pri-ma-008
titre: Sens et stratégies de la multiplication
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Représenter la multiplication comme groupes égaux et calculer des produits.
objectifs_secondaires: []
criteres_reussite:
- Résoudre un problème de groupes égaux avec dessin et calcul.
prealables_declares:
- qc-pri-ma-006
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-008-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-008`

**Discipline :** Mathématique (appellation québécoise de présentation)  
**Titre :** Sens et stratégies de la multiplication  
**Gouvernance pédagogique :** v1.2, interne à Kristal; aucune homologation PFEQ revendiquée.  
**Statut :** cours rédigé, calculs soumis à des contrôles locaux; revue humaine et qualification Framework non effectuées.

## 1. Intention et frontières

- **`obj-1` (immuable) :** Représenter la multiplication comme groupes égaux et calculer des produits.
- **`crit-1` (immuable) :** Résoudre un problème de groupes égaux avec dessin et calcul.
- À la fin, l'élève transforme une situation de groupes égaux en dessin (groupes encerclés ou tableau de points), en addition itérée et en multiplication, puis explique et vérifie le total avec une unité (« billes », « plantes »).
- Notions explicites : **itération** d'une quantité égale; **tableau** rectangulaire de lignes/colonnes; **propriété distributive** `a × (b + c) = a × b + a × c`.
- Limites : facteurs entiers non négatifs; exercices courants avec 2 à 9 groupes et 2 à 10 éléments par groupe. Les groupes de tailles différentes ne sont pas représentés par une multiplication unique sans réorganisation. Ni division, ni algorithme écrit de multiplication, ni équivalence à un niveau scolaire officiel n'est présumée.

## 2. Notions et représentations

1. **Groupes égaux et itération.** `4 × 3` signifie ici **4 groupes de 3** : `3 + 3 + 3 + 3 = 12`. Premier facteur : nombre de groupes; second : taille de chaque groupe. Pour tout entier `a ≥ 0`, `a × b` est l'addition de `b` répétée `a` fois (ou 0 si `a = 0`). Un dessin peut montrer quatre cercles contenant chacun trois points. Éviter `4 + 3 = 7`, qui mélange deux quantités de rôles distincts.
2. **Tableau rectangulaire.** Un tableau de 3 lignes de 5 points par ligne représente `3 × 5 = 15`. On peut aussi compter 5 colonnes de 3 : le **produit** est identique, mais l'histoire « 3 groupes de 5 » n'est pas automatiquement la même que « 5 groupes de 3 ».
3. **Distributivité.** Découper **tous** les groupes de 7 en `5 + 2` : `4 × 7 = 4 × (5 + 2) = (4 × 5) + (4 × 2) = 20 + 8 = 28`. Chacun des deux sous-tableaux garde les quatre lignes. L'écriture `4 × 5 + 2 = 22` oublie de multiplier le 2 par 4.
4. **Représentations équivalentes.** Objets → croquis de groupes → tableau → somme répétée → écriture multiplicative. Distinguer exactitude du nombre et sens de l'unité. Voir `contenu/01_NOTIONS_ET_EXEMPLES.md` pour démonstrations et non-exemples.

## 3. Préparation / diagnostic

- `requires` : **`qc-pri-ma-006`** (Sens et stratégies de l'addition). L'acquis équivalent peut être attesté par diagnostic; ne pas rendre obligatoire la complétion formelle du Kristal.
- `recommends_before` : **`qc-pri-ma-003`**, ordre conseillé uniquement. Aucun lien `reinforces` imposé.
- **`diag-1` :** « Calcule `4 + 4 + 4` et explique ce que représente chaque 4. » Attendu : 12, trois quantités égales.
- **`diag-2` :** « Dessine 3 boîtes contenant chacune 2 cubes; combien de cubes? Écris une somme. » Attendu : 6; `2 + 2 + 2`; trois boîtes de deux.
- Décision : si l'addition itérée et l'unité sont comprises, avancer; si l'addition de nombres entiers fait obstacle, activer l'aide ciblée et référencer `qc-pri-ma-006` sans modifier ce Kristal. Voir `contenu/02_DIAGNOSTIC.md`.

## 4. Enseignement guidé

- **`teach-1` :** poser quatre collections concrètes de trois jetons, verbaliser « 4 groupes de 3 jetons », entourer chaque collection, écrire `3 + 3 + 3 + 3 = 12` puis `4 × 3 = 12 jetons`. Faire vérifier le total en comptant les jetons.
- Transformer le dessin en quatre rangées de trois; montrer la lecture par lignes et, avec précaution, par colonnes. Éviter d'échanger silencieusement les unités d'une situation.
- Décomposer un tableau de cinq lignes de six en colonnes `4 + 2` : `5 × 6 = 5 × 4 + 5 × 2 = 20 + 10 = 30`.
- Contrôles oraux : « Que compte le premier facteur? », « Pourquoi la somme a-t-elle quatre termes? », « Dans `5 × (4 + 2)`, pourquoi multiplier aussi le 2 par 5? ». Démonstrations complètes dans `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- **`guided-1`, indices dégressifs** (`contenu/04_PRATIQUE_ACCOMPAGNEE.md`) :
  1. Trois boîtes de quatre objets : matériel + cercles prétracés + modèle de somme. Corrigé `3 × 4 = 12`.
  2. Quatre rangées de cinq : grille vierge + question de guidage, mais sans somme donnée. Corrigé `4 × 5 = 20`.
  3. Six pots de sept graines : aucun canevas de calcul; demander un regroupement `5 + 2`. Corrigé `6 × 7 = 6 × 5 + 6 × 2 = 42`.
- Pour toute erreur, demander d'abord le nombre de groupes et la taille de **chaque** groupe; retirer les indices lorsque l'élève représente, explique et calcule correctement.

## 6. Pratique autonome

- **`independent-1` :** quatre tâches indépendantes (`contenu/05_PRATIQUE_AUTONOME.md`) : cinq sacs de quatre billes (20), trois rangées de huit plots (24), quatre paquets de sept crayons (28), six tablettes de neuf livres (54).
- Pour chaque tâche, exiger un croquis valide, une expression multiplicative, le total et l'unité; ajouter somme répétée ou décomposition selon la consigne. Aucun indice de représentation, correction ou calculatrice pendant la preuve.
- Les contextes des deux **preuves de maîtrise distinctes** sont exclusivement `q-009` (boîtes de pièces à un atelier) et `q-010` (rangées de plants au jardin), pas les exemples enseignés. Productions déposées dans le LMS, non dans le canon. Voir `evaluation/PLAN_EVALUATION.md`.

## 7. Feedback et erreurs typiques

- `4 groupes de 3 → 4 + 3 = 7` : faire pointer le nombre d'objets **par groupe**, puis écrire quatre termes de 3.
- `2 + 3 + 4` représenté par `3 × 3` : tailles inégales; refaire le dessin puis compter exactement (`9`), sans prétendre que le produit décrit le problème initial.
- `4 × (5 + 2) = 4 × 5 + 2` : entourer les deux parties de **chaque** groupe; corriger en `20 + 8 = 28`.
- Réponse « 24 » sans unité ou sans dessin : exiger « 24 crayons » et une trace montrant les groupes ou rangées.
- Rétroaction située au **premier saut erroné**, nouvelle tentative analogue avec autres valeurs, puis retour à la preuve. Détails dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Famille immuable :** `qc-pri-ma-008-ev-01`; `objectif_ref: obj-1`; `critere_ref: crit-1`; type privilégié : `paramétrique_controle`.
- Banque de douze items `qc-pri-ma-008-q-001` à `q-012` : fixes et paramétriques déterministes bornés, avec algorithmes, `seed` stable, instances et corrigés vérifiables. Aucun générateur IA libre n'est un vérificateur.
- Critères : représentation fidèle des groupes égaux, écriture cohérente, produit exact avec unité, explication ou décomposition justifiée.
- **Maîtrise** : au moins deux démonstrations autonomes satisfaisantes, dans deux contextes distincts (`q-009`, `q-010`), avec dessin et calcul corrects; pas de décision à partir d'un seul total numérique. Revoir `evaluation/GRILLE_MAITRISE.md` et `evaluation/PLAN_EVALUATION.md`.
- Tous les items restent `a_revoir`; ils ne sont ni certifiés ni qualifiés pour publication.

## 9. Remédiation / enrichissement

- Erreur d'itération : deux collections visibles de trois, puis trois collections, reconstruire l'addition; refaire une tâche de 4 groupes de 2.
- Tableau mal formé : tracer d'abord une ligne, puis répéter exactement la même ligne; vérifier que chaque ligne possède le même nombre de colonnes.
- Distributivité incorrecte : matériel en deux couleurs par ligne; recomposer le tout pour constater `(a × b) + (a × c) = a × (b + c)`.
- Enrichissement : représenter un même produit comme deux tableaux orientés différemment ou comme deux décompositions; garder les unités et expliquer ce qui change ou non. Deux transferts indépendants sont proposés dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 10. Accessibilité

- Proposer objets tangibles, dessins contrastés, texte lisible, lecture orale de la consigne et verbalisation; ne pas imposer une vision des couleurs ni une motricité fine particulière.
- Accepter schéma en points, boîtes tracées, tableau tactile ou verbalisation structurée documentée (nombre de groupes et taille par groupe); conserver la **preuve d'une représentation** même avec aide à la transcription.
- Mettre à disposition les unités « objets », « jetons », « plants » dans l'énoncé; exclure les tâches basées sur des expériences privées ou des coûts réels. Pendant la preuve, pas d'aide de fond ni de correction fournie.

## 11. Critères de sortie

1. Pour `q-009`, faire une représentation correcte de groupes égaux, écrire la multiplication et le produit avec son unité, sans indice.
2. Refaire dans **un contexte différent** avec `q-010`, même indépendance et exactitude. Les nombres, objets et disposition changent.
3. Expliquer le nombre de groupes et la quantité par groupe; montrer pourquoi le total est plausible (somme répétée, comptage du tableau ou distributivité).
4. Si un des deux essais manque un critère essentiel, reprendre la notion ciblée puis demander une **nouvelle variante contrôlée** des deux contextes, sans considérer un score global comme acquis.
5. Prévoir rappel à J+2 (croquis sans modèle de `3 × 6`) et J+7 (nouveau mini-problème de `4 × 7`) en adaptant les données; retracer les corrections sans retransformer ces rappels en preuve unique.

## 12. Références pédagogiques et limites

- **Autorité technique interne :** `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md` et `CHARTE_CONVERSION_QC.md`. Références de principes pédagogiques recensées dans `REFERENCES_EVIDENCE.md`; cela ne prouve pas l'efficacité de chaque exercice.
- **Traçabilité :** `sources/REFERENCES_CONTENU.md` distingue règles internes consultées, calculs dérivés et textes/activités créés ici; tous les calculs cités dans les corrigés sont contrôlés localement.
- **Limites :** aucune correspondance détaillée PFEQ ni code scolaire officiel; `ALIGNEMENT.md` n'est pas modifié; la validation humaine (pédagogie, clarté, biais, accessibilité réelle) et les tests Framework restent nécessaires avant toute publication.
