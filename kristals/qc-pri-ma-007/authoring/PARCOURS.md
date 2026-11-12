---
format: qc.learning-path/1.0
id: qc-pri-ma-007
titre: Sens et stratégies de la soustraction
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Modéliser la soustraction comme retrait, différence ou complément.
objectifs_secondaires: []
criteres_reussite:
- Résoudre un problème de différence et vérifier par addition.
prealables_declares:
- qc-pri-ma-002
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-007-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-007`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Sens et stratégies de la soustraction  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** contenu pédagogique rédigé et corrigés locaux vérifiés par calcul; revue humaine et qualification technique encore requises. Le Kristal n'est pas déclaré cours publié.

## 1. Intention et frontières

- `obj-1` — **Résultat observable immuable :** Modéliser la soustraction comme retrait, différence ou complément.
- `crit-1` — **Preuve autonome immuable :** Résoudre un problème de différence et vérifier par addition.
- **Savoirs du présent Kristal :** retrait (enlever d'une quantité), comparaison (écart entre deux quantités de même nature), complément (quantité manquante pour atteindre une cible), relation inverse addition/soustraction.
- **Portée mathématique :** nombres naturels de 0 à 100, calculs sans résultat négatif; certaines situations utilisent des mesures entières en cm. Ne pas confondre le sens d'une opération avec l'écriture d'un calcul.
- **Frontière de possession :** aucune copie des contenus de `qc-pri-ma-002` ou de `qc-pri-ma-006`. Leurs ID sont uniquement des références de progression interne.

## 2. Notions et représentations

1. **Retrait.** On part de 14 jetons, on en retire 6 : il en reste 8; écriture `14 − 6 = 8`, contrôle `8 + 6 = 14`. Les 14 sont le total initial, pas les jetons restants.
2. **Comparaison.** Une boîte contient 23 billes et une autre 15; l'écart est 8 billes, car `15 + 8 = 23`. On n'enlève réellement aucune bille. La question « combien de plus ? » interroge une différence, pas la somme 38.
3. **Complément.** Pour passer de 9 à 17, il manque 8; `9 + 8 = 17` et `17 − 9 = 8`. L'inconnue peut être dessinée comme la partie vide d'une barre.
4. **Relation inverse.** Si `a − b = c` avec `0 ≤ b ≤ a`, alors `b + c = a` et `a − c = b`. **Attention :** la commutativité de l'addition ne rend pas la soustraction commutative; `14 − 6 = 8` mais `6 − 14` ne donne pas 8 dans le domaine travaillé.
5. **Représentations successives.** Matériel : déplacer des jetons, ou mettre côte à côte deux collections sans retrait. Schéma : barre totale et parties, ou deux bandes alignées. Notation : équation complète avec unité. Verbalisation : « je cherche l'écart entre… ».
6. **Choix de procédure.** Retrait par décomposition (`32 − 7 = 32 − 2 − 5 = 25`), comparaison par complément (`28 − 19 = 9` car `19 + 9 = 28`), vérification par addition.

Voir `../contenu/01_NOTIONS_ET_EXEMPLES.md`, incluant les contre-exemples expliqués, le cas zéro et les contraintes des représentations.

## 3. Préparation / diagnostic

- **Lien strict `requires` :** `qc-pri-ma-002` (lire, écrire et comparer des nombres naturels). L'acquis équivalent peut être attesté au diagnostic; ne pas bloquer automatiquement en raison d'un parcours non enregistré.
- **Ordre conseillé non bloquant :** `qc-pri-ma-006`; aucun `reinforces` ni transfert référencé sortant.
- `diag-1a` : représenter 18 et 13 par des paquets ou bandes, dire lequel est plus grand et de combien; attendu 5 et `13 + 5 = 18`.
- `diag-1b` : compléter `7 + □ = 15`, puis expliquer `15 − 7 = 8` avec une autre représentation; attendu 8.
- **Interprétation :** pour attester l'équivalence de lecture/comparaison, l'élève lit 18 et 13, ordonne correctement et explique par une représentation adaptée; si ce socle manque, orienter vers le lien `qc-pri-ma-002` ou une aide ponctuelle sur la lecture/ordre des nombres. Une erreur de calcul isolée ne démontre pas à elle seule l'absence de prérequis.
- **Décision pédagogique :** réponses justes expliquées : accès direct aux tâches d'apprentissage/validation; représentation fragile : enseignement guidé; comparaison impossible : soutenir le prérequis avant l'autonomie. Détails : `../contenu/02_DIAGNOSTIC.md`.

## 4. Enseignement guidé

- `teach-1` : annoncer l'objectif sans changer sa formulation.
- **Modelage à voix haute :** « 21 objets sont dans un bac, on en donne 8. Je pars de 21, je montre 8 donnés et 13 restants : `21 − 8 = 13`. Je vérifie : `13 + 8 = 21`. » Montrer matériel, barre `8 | 13 = 21`, écriture.
- **Deuxième modelage :** « Une étagère a 26 livres et l'autre 17. Je compare, je ne déplace pas de livres. L'écart est 9; `17 + 9 = 26`. » Dessiner deux bandes alignées, segment de différence 9.
- **Complément :** « J'ai 12 points, je vise 20 : il manque 8; `12 + 8 = 20`. » Lier les trois lectures du schéma partie-partie-tout.
- **Question d'arrêt :** « Dans le problème des étagères, qui a enlevé des livres ? » Attendu : personne; on compare des quantités. Confusion → retour au dessin à deux bandes.
- **Progression :** retrait explicite, comparaison, complément, puis relation inverse et disparition progressive du matériel. Guide pas-à-pas : `../contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- `guided-1` : 16 cubes, 5 retirés → 11, vérification `11 + 5 = 16`. Indices complets : total initial, cubes retirés, cubes restants.
- `guided-2` : 27 images contre 19 → écart 8, contrôle `19 + 8 = 27`. Indice modéré : aligner deux bandes; ne pas fournir l'opération.
- `guided-3` : 34 places, 28 occupées → complément 6, contrôle `28 + 6 = 34`. Indice minimal : « que faut-il ajouter à 28 ? » sans dessin ni équation fournis.
- **Feedback dégressif :** nommer la première confusion (sens, ordre des valeurs, calcul ou contrôle), faire réparer par l'élève, soumettre une autre valeur avant de retirer l'aide.
- **Adaptations :** manipulation, description orale, bande tactile ou dessin décrit textuellement; la justification et l'addition de vérification restent exigées. Voir `../contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- `independent-1` : quatre situations différentes du modelage : comparaison de quantités, retrait, complément et comparaison de mesures. Aucune solution ni indice pendant la tentative.
- Pour chacune : identifier la question et l'unité; choisir et nommer une représentation (dessin, matériel, équation expliquée); trouver la différence/manque; écrire l'addition de vérification.
- **Corrigés :** `../contenu/05_PRATIQUE_AUTONOME.md`, réservés au retour post-tentative.
- **Deux preuves distinctes de maîtrise (`crit-1`) :** item `qc-pri-ma-007-q-009` (comparaison de collections à la bibliothèque) ET `qc-pri-ma-007-q-010` (comparaison de longueurs dans un jardin), chacun sans indice et vérifié par addition. Des tâches équivalentes tirées de la famille contrôlée peuvent être utilisées après revue humaine.
- **Trace d'apprentissage :** conserver localement dans l'outil d'enseignement la production, le contexte, l'aide reçue et la date; ne jamais écrire de données d'élève dans un fichier canonique du Kristal.

## 7. Feedback et erreurs typiques

- `error-1` **addition de comparaison** : à « 23 contre 15 », écrire 38. Question : « Cherches-tu tout réunir ou la partie qui dépasse ? » Réparation : bandes alignées, écart 8.
- `error-2` **ordre inversé** : `15 − 23` au lieu de `23 − 15`. Question : « Quelle barre est la plus longue ? » Écrire `15 + □ = 23`.
- `error-3` **calcul faux non détecté** : `25 − 9 = 14`. Tester `14 + 9 = 23 ≠ 25`; corriger en 16.
- `error-4` **unités perdues** : écrire « 17 » pour un écart de centimètres; reprendre l'unité et le sens.
- `error-5` **contrôle tautologique** : réécrire `25 − 9 = 16` sans addition; exiger `16 + 9 = 25`.
- Retour court, précis, non stigmatisant; faire refaire une situation modifiée avant de juger la correction. Voir `../contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Famille invariante :** `qc-pri-ma-007-ev-01` ; `objectif_ref: obj-1` ; `critere_ref: crit-1`.
- **Mode privilégié :** `paramétrique_controle` (paramètres entiers bornés, algorithme explicite, seed stable, solutions et contrôles arithmétiques testés); banque comprenant aussi des ancrages fixes et une variante contextuelle explicitement verrouillée.
- **Plan et banque :** `../evaluation/PLAN_EVALUATION.md` et `../evaluation/BANQUE_ITEMS.json`. Chaque item exige différence/manque, sens du contexte, vérification par addition et unité quand présente.
- **Décision :** ne jamais conclure sur une note unique. Exiger deux productions satisfaisantes dans des contextes différents, dont au moins une entièrement autonome; vérifier la stabilité, non la reconnaissance de la même histoire.
- **État de validation :** items au statut `a_revoir` même si les calculs locaux passent. Aucune certification ni homologation.

## 9. Remédiation / enrichissement

- **Sens non compris :** confronter « enlever 5 jetons » à « 5 jetons de plus »; trier les énoncés avec justification.
- **Différence mal calculée :** utiliser bande graduée/comptage du plus petit au plus grand puis `a − b`; pratiquer sur 12/8 puis 29/21.
- **Inverse absent :** fournir le gabarit `petite quantité + écart = grande quantité`, puis le retirer; contrôler un autre contexte.
- **Biais de contexte :** changer objets/mesures et noms, sans ajouter de vocabulaire non expliqué.
- **Enrichissement :** deux quantités égales (`19 − 19 = 0`, `19 + 0 = 19`), puis complément de 0 à 12; expliquer pourquoi il n'y a pas d'écart quand les quantités sont identiques.
- Voir `../contenu/06_REMEDIATION_ET_TRANSFERT.md`. Aucune passerelle `reinforces` sortante indiquée dans le graphe central.

## 10. Accessibilité

- Toutes les informations quantitatives sont données en texte; les dessins de barres sont décrits (« grande barre de 23, petite de 15, segment excédentaire »). Pas de couleur ou d'image nécessaire pour répondre.
- Autoriser lecteur vocal, consigne lue, matériel ordinaire, texte agrandi, dessin, oral enregistré, dictée à un adulte/saisie alternative; éviter de noter lecture courante, orthographe, dextérité ou vitesse.
- Accepter calcul écrit, schéma annoté ou explication orale avec équation transcrite, à condition que l'élève indique la différence correcte, le sens et la vérification par addition sans aide de contenu lors de la preuve autonome.
- Ni performance chronométrée ni exposition de données personnelles; contextes fictifs non stéréotypés, objets culturellement familiers ou explicités.

## 11. Critères de sortie

1. Résoudre un problème de différence et vérifier par addition, sans fournir seulement un résultat isolé (`crit-1`).
2. Relier une représentation à la structure retrait/comparaison/complément et préserver les unités.
3. Réaliser deux preuves satisfaisantes en **contextes différents** (`q-009` bibliothèque et `q-010` longueurs), avec au moins une sans indices, selon `../evaluation/GRILLE_MAITRISE.md`.
4. Si le calcul est bon mais la vérification absente, ne pas valider la maîtrise; reprendre seulement ce maillon puis recueillir de nouvelles preuves.
5. Le statut de sortie est **apprentissage local démontré**, distinct de « cours publié » ou d'une qualification du workspace.

## 12. Références pédagogiques et limites

- **Gouvernance lue dans le ZIP source :** `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`, registre des relations `GRAPHE_PEDAGOGIQUE_202.json`.
- **Principes de conception cités par la gouvernance :** exemples résolus, rappel, représentation et feedback (IES/WWC, EEF, CAST UDL); aucune prétention de mesure empirique de ce parcours. Source et statut détaillés : `../sources/REFERENCES_CONTENU.md`.
- **Nomenclature québécoise :** Mathématique, sans conformité ni homologation PFEQ; `ALIGNEMENT.md` demeure inchangé. Code administratif officiel non attribué (`null`).
- **Rappel différé :** à la séance suivante (suggestion éditoriale J+1) redessiner `18 − 11 = 7`, contrôler `11 + 7 = 18`; à J+7, comparer 30 et 22 sans indices, répondre 8 et contrôler `22 + 8 = 30`. Adapter l'intervalle au contexte; un rappel manqué déclenche une reprise ciblée sans annuler automatiquement les preuves antérieures.
- **Limites :** revue humaine de clarté, biais, rubriques et adéquation aux élèves, essai réel, intégration LMS/framework et qualification locale non exécutés. Voir `../livraison/VALIDATION.md`.
