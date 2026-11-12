---
format: qc.learning-path/1.0
id: qc-pri-ma-006
titre: Sens et stratégies de l’addition
discipline_code: MA
statut: en_rédaction
revision_contenu: 1.2.0
langue_contenu: fr-CA
resultat_principal: Modéliser l’addition et choisir une stratégie efficace pour calculer.
objectifs_secondaires: []
criteres_reussite:
- Résoudre deux additions distinctes et expliquer la stratégie adoptée.
prealables_declares:
- qc-pri-ma-002
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-006-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-006`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Sens et stratégies de l’addition  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** contenu et items proposés pour revue humaine, non qualifiés ni publiés.

## 1. Intention et frontières

- `obj-1` — **Objectif observable IMMUTABLE :** Modéliser l’addition et choisir une stratégie efficace pour calculer.
- `crit-1` — **Preuve autonome IMMUTABLE :** Résoudre deux additions distinctes et expliquer la stratégie adoptée.
- Développer **réunion, augmentation, décomposition, somme** en nombres naturels (y compris zéro), sur des situations sans retrait ni double comptage.
- Choisir une procédure compréhensible et exacte : tout compter, compter à partir du plus grand, compléter la dizaine, séparer dizaines et unités. Le « bon » choix dépend des nombres et doit être expliqué; plusieurs méthodes exactes sont acceptées.
- Bornes pédagogiques de cette unité : additions de 0 à 100, opérandes de 0 à 99, somme ≤ 100; pas de négatifs, fractions, monnaie décimale ou algorithme posé obligatoire. Le zéro et les franchissements de dizaine sont inclus.
- Le système ne revendique aucune équivalence ou homologation PFEQ : seule l'appellation « Mathématique » relève de la charte de conversion.

## 2. Notions et représentations

- **Réunion :** deux collections disjointes sont mises ensemble; total = cardinal du premier groupe + cardinal du deuxième. Exemple : 8 cartes bleues et 6 jaunes, aucune comptée deux fois → `8 + 6 = 14`.
- **Augmentation :** une quantité initiale croît d'une quantité ajoutée, sans élément enlevé; état final = état initial + ajout. Exemple : 17 billes, on en ajoute 5 → `17 + 5 = 22`. Les objets n'ont pas à changer de catégorie.
- **Décomposition additive :** réécrire un nombre comme somme de parties sans changer sa valeur; `8 = 3 + 5`, donc `27 + 8 = 27 + 3 + 5 = 35`. La séparation ne crée ni ne supprime d'unités.
- **Somme :** résultat de l'addition de deux ou plusieurs termes; dans `27 + 8 = 35`, 35 est la somme, non le nombre de termes.
- **Concret → schéma → notation :** jetons en deux groupes, cadres de dix/dizaines-unités, puis `a + b = s`. Chaque schéma est aussi décrit verbalement pour ne pas dépendre de la couleur ou de la vue.
- **Deux modelages résolus :** réunion `14 + 9 = 14 + 6 + 3 = 23`; augmentation `38 + 27 = (30 + 20) + (8 + 7) = 50 + 15 = 65`. Vérifier qu'aucun objet n'a été perdu ni compté deux fois.
- **Contre-exemples :** `9 + 4 = 13` n'illustre pas une diminution de 9 à 4; et `26 + 17 = 33` oublie la dizaine née de `6 + 7 = 13` : le résultat correct est 43.
- Détails, cas limites, corrections et descriptions textuelles : `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- **Lien strict `requires` :** `qc-pri-ma-002` (lire, écrire et comparer des nombres naturels); un diagnostic attestant une compétence équivalente suffit pour satisfaire le prérequis sans imposer une lecture répétitive.
- **Ordre recommandé non bloquant :** `qc-pri-ma-003`. Aucun `reinforces` déclaré pour ce Kristal; ne pas en créer.
- `diag-1` : réunir 4 jetons et 3 jetons, écrire `4 + 3 = 7`, puis reformuler en barres ou mots « quatre et trois font sept ». Résultat et seconde représentation sont recueillis séparément.
- `diag-2` : lire « trente-quatre », écrire `34`, lire `43`, placer le signe `<` dans `34 < 43` et expliquer au moyen des dizaines et unités.
- **Décision préalable :** diag-2 réussi (lecture, écriture, comparaison explicités) → acquis équivalent de `qc-pri-ma-002` attesté; sinon micro-remédiation sur valeur positionnelle puis nouvelle tâche avec 26 et 62. diag-1 oriente l'entrée en addition, mais son échec ne prouve pas une défaillance du prérequis.
- Réponses, critères et alternatives orales/visuelles : `contenu/02_DIAGNOSTIC.md`.

## 4. Enseignement guidé

- `teach-1` : annoncer l'objectif, demander « Quelle quantité cherchons-nous ? Quels objets sont nouveaux ? » et résoudre avec jetons / tableau de dizaines / écriture.
- **Modèle A, réunion :** 14 livres + 9 livres, sans recouvrement; ajouter 6 à 14 pour atteindre 20, puis les 3 restants → `14 + 9 = 23`. Montrer 14 objets, 9 objets et le total; identifier **somme** et **décomposition de 9**.
- **Modèle B, augmentation :** 38 pas puis 27 autres; décomposer en dizaines/unités : `38 + 27 = 30 + 8 + 20 + 7 = 50 + 15 = 65` (une dizaine et cinq unités issues de 15). Faire comparer avec `38 + 2 + 25 = 65`.
- **Contrôle de compréhension :** « Est-ce une réunion de deux groupes disjoints ou un ajout à un état ? »; l'élève relie les mots, le schéma et l'égalité; question distincte sur pourquoi `8 + 7` vaut 15 et non 5.
- **Contre-modèle corrigé :** `26 + 17 = 33` néglige le report; regrouper `6 + 7 = 13` en 1 dizaine + 3 unités donne `43`.
- Déroulé oral exact et relances : `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- `guided-1` — réunion `6 + 5 = 11` : indices complets (deux groupes disjoints, jetons → dessin → égalité), puis vérifier le nombre d'objets.
- `guided-2` — augmentation `28 + 7 = 35` : indice réduit (« combien jusqu'à 30 ? »); `7 = 2 + 5`, donc `28 + 2 + 5 = 35`. Faire expliquer la conservation des sept ajoutés.
- `guided-3` — addition `37 + 26 = 63` : aucun indice d'abord; ne proposer « sépare dizaines et unités » qu'en cas de blocage. `30 + 20 = 50`, `7 + 6 = 13`, donc `63`.
- **Retrait des aides :** étapes 1, 2 et 3; au dernier exercice, demander un schéma indépendant ou une explication orale sans modèle visible. Ne pas compter une réussite très assistée comme autonome.
- **Feedback :** pointer le premier désaccord nombre–schéma–égalité, demander l'élève de le réparer, puis vérifier avec une seconde méthode. Exercices détaillés : `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- `independent-1` — quatre essais sans indices : réunion `13 + 9 = 22`, augmentation `46 + 8 = 54`, écriture seule `27 + 35 = 62`, contexte neutre `49 + 21 = 70`. Pour chacun : représentation libre lisible, égalité, explication du choix, contrôle du résultat.
- Aide technique permise (saisie, lecture audio, jetons vierges) ≠ aide mathématique; aucune suggestion de stratégie pendant une mesure autonome.
- **Preuve A en bibliothèque :** 24 livres sur une tablette et 18 sur une autre, sans doublons → 42, justification de la stratégie.
- **Preuve B dans un potager :** 37 semis, puis 25 nouveaux → 62, justification d'une stratégie adaptée.
- Les deux preuves portent sur deux additions **distinctes**, des **contextes différents** et un raisonnement observable, sans guidage; conserver des traces dans le LMS, pas dans `canon/`.
- Documents : `contenu/05_PRATIQUE_AUTONOME.md`, `evaluation/BANQUE_ITEMS.json` (q-007 et q-008), `evaluation/GRILLE_MAITRISE.md`.

## 7. Feedback et erreurs typiques

- `error-1` **Double comptage** : si 4 éléments appartiennent aux deux groupes, une réunion naïve donne un total surestimé; reconstruire des collections disjointes avant l'addition.
- **Confusion somme / dernier terme** : à `14 + 9`, répondre `9`; demander « combien en tout ? » et dessiner les deux parties.
- **Report omis** : `26 + 17 = 33`; étaler 13 unités, échanger 10 unités contre une dizaine, vérifier `43`.
- **Ajout incomplet** : `28 + 7 = 30` : l'élève a utilisé les 2 nécessaires pour atteindre 30 mais perdu 5; faire répartir physiquement les 7 en `2 + 5`.
- **Sens contrarié** : `17 + 5 = 12` n'est pas une augmentation; vérifier que résultat ≥ quantité initiale quand on ajoute des naturels.
- **Retour actif** : nouvelle question de même nature mais avec d'autres nombres, en l'absence d'indice; tableau erreur → rétroaction → remédiation dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Référence unique :** `family_id: qc-pri-ma-006-ev-01`, `objectif_ref: obj-1`, `critere_ref: crit-1`, préférence `paramétrique_controle`; banque mélange des ancrages fixes, scénarios contrôlés et deux paramétriques reproductibles.
- **Plan et banque :** `evaluation/PLAN_EVALUATION.md` et `evaluation/BANQUE_ITEMS.json` (10 items `q-001` à `q-010`). Paramètres bornés, graines stables, algorithmes et exemples vérifiables, sans génération libre d'IA.
- **Contrôle de maîtrise :** au minimum q-007 **et** q-008 ou deux tâches équivalentes nouvelles, dans deux contextes différents, solutions exactes, justification compréhensible et choix pertinent; aucune aide de résolution.
- **Rubrique :** exactitude, représentation/sens, stratégie et explication, transfert, autonomie. Une note isolée ne décide pas la maîtrise; des indices reçus pendant l'essai annulent le caractère autonome de la preuve.
- **Statut :** `a_revoir` pour chaque item; revue humaine du sens, du langage, de l'accessibilité, puis essai avant toute qualification.

## 9. Remédiation / enrichissement

- **Fragilité de lecture du nombre :** revenir à dizaines et unités sans présumer le prérequis `qc-pri-ma-002`; retester avec d'autres nombres; autoriser équivalence diagnostiquée.
- **Comptage instable :** jetons individuels et barre d'agrégation; exercice `5 + 4 = 9` puis `7 + 3 = 10`.
- **Décomposition perd des unités :** cadres de dix sur `29 + 6 = 35` avec `6 = 1 + 5`, vérifier que 1 + 5 vaut toujours 6.
- **Report de dizaine :** `27 + 15 = 42` après échange des 12 unités contre 1 dizaine et 2 unités.
- **Enrichissement :** comparer deux méthodes sur `48 + 12 = 60` et argumenter l'efficacité; explorer `0 + 36 = 36` et `36 + 0 = 36`.
- **Transferts construits :** bibliothèque (réunion) et potager (augmentation), `contenu/06_REMEDIATION_ET_TRANSFERT.md`. Aucun lien de renforcement inventé.

## 10. Accessibilité

- Présenter chaque problème **en texte** et, facultativement, en jetons tactiles, narration orale ou schéma à légende; aucune réponse ne dépend exclusivement d'une couleur, d'une image ou d'une vitesse de calcul.
- Permettre une explication vocale transcrite, dictée, clavier, écriture agrandie, blocs manipulables; la notation mathématique et la correspondance entre quantité et écriture doivent rester observables.
- Lire les consignes au besoin sans suggérer une méthode; fournir un espace de réponse clair, contrastes suffisants, police lisible et pauses raisonnables; éviter minuterie comme critère.
- Ne pas demander de données personnelles, de photographie ni de nombres associés à la vie familiale. Le matériel (jetons, papier, clavier) ne présente aucun danger particulier; adapter les petits objets si risque de mise en bouche.
- Les modalités de soutien sont consignées; une aide qui fournit le procédé rend l'essai **guidé**, pas autonome.

## 11. Critères de sortie

1. `obj-1` atteint : relier explicitement réunion ou augmentation à un modèle additif et choisir une stratégie valable.
2. `crit-1` établi : deux additions distinctes et résolues exactement avec stratégie expliquée, sur deux contextes différents (bibliothèque et potager ou équivalents non répétés).
3. Au moins deux représentations exploitables dans le parcours et compréhension du passage aux symboles; pas d'exigence arbitraire de dessin durant chacune des deux preuves si explication équivalente.
4. Autonomie réelle : aucune indication sur la décomposition ou le résultat pendant les preuves; assistance d'accès non mathématique autorisée.
5. Si une preuve échoue, identifier le maillon, remédier et demander **deux nouvelles situations**; ne jamais conclure à partir d'une moyenne ou d'un score unique.
6. Rappel différé au prochain temps d'apprentissage (indicativement 48–72 h) : `19 + 6 = 25` avec explication, puis 7–10 jours plus tard `24 + 17 = 41` avec vérification; adapter le calendrier, tracer l'évolution et remédier si nécessaire. Ces rappels ne remplacent pas les deux preuves initiales.

## 12. Références pédagogiques et limites

- **Autorité de conception :** `governance/Norme_Pedagogique_Autonome_v1.2/{CONTRAT_PEDAGOGIQUE_V1.2.md,GENERATEUR_ET_EXAMENS.md,CHARTE_CONVERSION_QC.md}` et `registry/GRAPHE_PEDAGOGIQUE_202.json` (consultation seule).
- **Repères déclarés dans la source :** `governance/Norme_Pedagogique_Autonome_v1.2/REFERENCES_EVIDENCE.md` renvoie à IES/WWC, EEF et CAST; les liens externes n'ont pas été vérifiés directement ici. Voir `sources/REFERENCES_CONTENU.md` pour provenance précise.
- **Statut non officiel :** charte québécoise utilisée pour la discipline seulement; pas de code de cours primaire administratif inventé ni d'alignement détaillé PFEQ.
- **Limites avant mise en production :** revue pédagogique et mathématique humaine, essai auprès d'élèves variés et validation de rendu LMS; aucune publication ou certification implicite.
