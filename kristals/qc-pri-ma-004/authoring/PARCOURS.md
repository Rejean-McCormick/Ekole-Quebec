---
format: qc.learning-path/1.0
id: qc-pri-ma-004
titre: Suites et régularités numériques
discipline_code: MA
statut: en_révision_pédagogique
revision_contenu: 0.3.0
langue_contenu: fr-CA
resultat_principal: Identifier, poursuivre et décrire une régularité numérique.
objectifs_secondaires: []
criteres_reussite:
- Compléter une suite et expliciter une règle qui permet d’en prévoir la suite.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-004-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-004`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Suites et régularités numériques  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** rédaction pédagogique complète à soumettre à une revue humaine; non publié et non certifié.  
**Ancrages immuables :** `obj-1` — « Identifier, poursuivre et décrire une régularité numérique. »; `crit-1` — « Compléter une suite et expliciter une règle qui permet d’en prévoir la suite. »

## 1. Intention et frontières

- **Résultat observable `obj-1` :** Identifier, poursuivre et décrire une régularité numérique.
- **Preuve autonome `crit-1` :** Compléter une suite et expliciter une règle qui permet d’en prévoir la suite.
- **Cible :** reconnaître une organisation numérique répétée, nommer un *motif*, déterminer un *pas* constant lorsqu'il existe, énoncer une *règle* vérifiable, retrouver un *terme manquant* et prévoir des termes suivants.
- **Frontière de validité :** quelques nombres ne déterminent pas une règle unique. Dans les activités de pas constant, la consigne l'indique ou demande une règle compatible; vérifier tous les intervalles connus. Pour un motif cyclique, nommer sa période et ne pas inventer de pas constant.
- **Hors cible :** formalisme des suites générales, preuve d'unicité d'une loi à partir d'une liste finie, apprentissage d'autres Kristals, nomenclature scolaire officielle.

## 2. Notions et représentations

- **Motif :** partie minimale qui se répète dans une organisation régulière, p. ex. `2, 5 | 2, 5 | …` (motif de deux termes). Dans une suite arithmétique, les **écarts** peuvent suivre le motif constant `+3` sans que les nombres se répètent.
- **Pas :** différence entre deux termes consécutifs lorsque cet écart reste constant : `d = terme suivant − terme précédent`. Si la suite vaut `4, 7, 10, 13`, le pas est `+3`; si elle vaut `18, 14, 10, 6`, le pas est `−4`.
- **Règle :** consigne permettant de calculer les termes et de contrôler les transitions : « partir de 4, ajouter 3 à chaque fois ». Pour les suites à pas constant, au rang `n ≥ 1`, `t(n) = a + (n−1)d` avec premier terme `a`.
- **Terme manquant :** valeur occupant une place masquée, déterminée *dans la règle retenue*, pas simplement le prochain nombre. Exemple `6, 10, __, 18` sous l'hypothèse d'un pas constant : `14`.
- **Représentations :** jetons ajoutés en quantités égales → flèches `+3` entre cases → écriture `4,7,10,13` et équation facultative. Tableau `rang/valeur` pour repérer une position.
- Voir `contenu/01_NOTIONS_ET_EXEMPLES.md` pour deux démonstrations, trois contre-exemples et bornes de validité.

## 3. Préparation / diagnostic

- **Requires :** `[]` — aucun préalable bloquant.
- **Ordre recommandé seulement :** `qc-pri-ma-002` (aucune vérification technique obligatoire et aucune copie de son cours).
- **`diag-1` :** `5, 8, 11, __, __` : compléter (`14,17`), puis montrer `+3` sur la droite ou avec des groupes de trois jetons.
- **`diag-2` :** `20, 16, __, 8, 4` avec pas constant : trouver `12` et justifier par les écarts `−4` (y compris `12→8`).
- **Observation :** distinguer erreur de calcul, erreur de direction, incompréhension du rang et simple absence de vocabulaire. Les réponses orales, écrites ou manipulées sont équivalentes si le calcul et la règle sont vérifiables.
- **Décision :** si les deux tâches sont exactes et expliquées sans aide, passer directement à des situations nouvelles puis évaluer; sinon, ne travailler que la difficulté diagnostiquée (`contenu/02_DIAGNOSTIC.md`).

## 4. Enseignement guidé

- **`teach-1` :** annoncer l'objectif en termes d'action : « Je peux prolonger une suite et dire comment je l'ai prolongée. »
- **Concret :** construire 3, puis 6, puis 9 jetons; faire constater trois jetons supplémentaires à chaque étape.
- **Schéma :** représenter les groupes par cases et flèches `+3`, puis remplacer la dernière case par `?` : `3 → 6 → 9 → ?`.
- **Symbolique :** calculer `9+3=12`, produire `3,6,9,12,15` et prononcer « premier terme 3, j'ajoute toujours 3 ». Vérifier chaque transition, pas seulement la dernière.
- **Contraste raisonné :** `2,5,2,5,…` est une répétition du motif `[2,5]`, **pas** une suite à pas constant : les différences sont `+3,−3,+3`.
- **Contrôle immédiat :** « Quel est le motif observé : les valeurs ou les écarts? Pourquoi le pas est-il +3 dans le premier cas? » Représentations et corrections détaillées dans `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- **`guided-1` (indice complet) :** `7, 11, 15, __, __` : tracer deux flèches `+4` et prévoir `19, 23`. L'enseignant questionne « Quelle différence revient? ».
- **`guided-2` (indice partiel) :** `24, 19, 14, __, __` : seul le repère « calcule la différence entre deux termes » est proposé; réponse `9,4`, règle `−5`.
- **`guided-3` (sans indice préalable) :** `6, __, 16, 21, __` à pas constant : réponses `11,26`; l'apprenant explique les deux écarts et vérifie la case intérieure.
- **Retrait d'aide :** consigne → question sur la différence → aucun indice. Toute intervention est annotée pour ne pas confondre accompagnement et maîtrise indépendante.
- **Feedback :** « Tu as pris le saut de 6 à 16 comme un seul pas; combien y a-t-il d'intervalles? » plutôt que d'offrir directement le nombre. Voir `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- **`independent-1` :** 4 tâches sans indices données dans `contenu/05_PRATIQUE_AUTONOME.md`, sur suites croissantes, décroissantes, terme intérieur et motif répétitif.
- **Exigence de réponse :** indiquer chaque terme manquant, décrire une règle initiale et répétable, vérifier au moins deux sauts dont un près du terme masqué et prévoir un terme encore plus loin quand demandé.
- **Trace :** feuille, photo de jetons annotée ou enregistrement oral et transcription des nombres/règle par l'évaluateur dans le LMS; aucune modification du canon.
- **Différenciation :** lecture des consignes, jetons et gros caractères autorisés; aucune indication de la règle pendant la preuve autonome.

## 7. Feedback et erreurs typiques

- **`error-1` — direction** : `18, 14, 10` poursuivie par `14` → pointer les écarts `−4` et faire soustraire à partir de 10.
- **`error-2` — rang sauté** : `6, __, 16` rempli par `16` ou `26` → matérialiser les deux intervalles entre 6 et 16; un seul pas vaut `(16−6)/2 = 5`.
- **`error-3` — motif confondu avec pas** : `2,5,2,5` décrite « toujours +3 » → vérifier `5→2 = −3`, puis nommer le motif de deux éléments.
- **`error-4` — hypothèse non testée** : annoncer « +3 » en voyant seulement `4→7` pour `4,7,11,14` → contrôler **tous** les sauts; ne pas forcer une règle à pas constant incompatible.
- **`error-5` — règle incomplète** : dire « ajouter 3 » sans valeur initiale pour générer une suite → demander le premier terme et la direction; accepter toute expression mathématiquement équivalente et vérifiable.
- Vérifier l'amélioration sur **un nouvel exemple**, pas sur la seule correction (`contenu/06_REMEDIATION_ET_TRANSFERT.md`).

## 8. Évaluation formative et preuves

- **Famille unique :** `qc-pri-ma-004-ev-01` ; `objectif_ref: obj-1` ; `critere_ref: crit-1`.
- **Mode prioritaire :** `paramétrique_controle`, avec seed fixe, plages et algorithmes documentés; items fixes lorsque le contraste conceptuel exige une formulation verrouillée.
- **Banque :** douze items complets, huit paramétriques à instanciation vérifiable et quatre fixes. Toutes les réponses numériques instanciées sont calculées et testées; les rubriques nécessitent une revue humaine.
- **Deux manifestations :** item `q-010` (longueur de rubans) et `q-011` (quantité de chaises par rangée), dans deux contextes distincts, sans indices, avec réponse ET règle.
- **Barème descriptif :** exactitude des valeurs, règle initiale et itérative, vérification des écarts, transfert; aucune maîtrise inférée d'un total de points seul.
- Voir `evaluation/PLAN_EVALUATION.md`, `evaluation/GRILLE_MAITRISE.md` et `evaluation/BANQUE_ITEMS.json`.

## 9. Remédiation / enrichissement

- **Défaillance du pas :** matérialiser `3,6,9,12`, ajouter trois jetons à chaque étape, traduire par `+3`, puis résoudre `5,8,11,__`.
- **Défaillance du terme intérieur :** tracer les places `1,2,3`, distinguer **deux** bonds entre positions 1 et 3, répartir une différence paire (`8,__,18` → `13`).
- **Défaillance du motif :** construire les cartes `1,4,1,4`, entourer les blocs, distinguer écarts alternants des valeurs répétées.
- **Enrichissement :** discuter pourquoi `2,4,6,8` accepte plusieurs prolongements en général, mais `+2` est la règle additive la plus simple énoncée ici; introduire le tableau de rang et la vérification d'un 6e terme.
- **Transfert :** bandes de papier à longueur croissante et préparation de sachets, décrits et corrigés dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`. Aucune nouvelle relation de graphe créée.

## 10. Accessibilité

- Consignes courtes, espaces clairs entre termes, texte et tableaux lisibles, pas de distinction uniquement par couleur; schémas avec étiquettes et version textuelle.
- Lire les énoncés à voix haute, dicter ou saisir la règle au clavier, fournir des jetons non dangereux (objets de taille convenable et surveillance selon le contexte) ou papier quadrillé.
- Autoriser une explication en français oral, écrite ou via flèches annotées avec explicitation; évaluer **les mêmes** valeurs, le même processus et la même autonomie.
- Éviter de noter l'orthographe, la vitesse, la motricité fine, la familiarité avec une unité non enseignée ou la capacité à voir un code couleur.

## 11. Critères de sortie

1. `crit-1` : compléter correctement une suite et formuler une règle qui en prévoit la suite.
2. Vérifier explicitement au moins deux transitions, y compris celle autour d'une case masquée s'il y en a une.
3. Produire **deux preuves distinctes** (`q-010` et `q-011` ou versions équivalentes validées) en contexte différent, sans indice de stratégie ni correction durant l'essai, puis expliquer oralement/écritement la règle.
4. Montrer une autonomie de décision (choisir calcul, tableau ou représentation) et corriger une erreur typique sur un nouvel essai si nécessaire.
5. Décider selon `evaluation/GRILLE_MAITRISE.md` : acquis, à consolider ou non attesté; pas de réussite automatique sur une note globale unique.
6. **Rappel différé** après plusieurs jours : `9,13,17,__,__` → `21,25`, règle « partir de 9, ajouter 4 »; puis un contexte inédit pour tester le maintien de l'acquis. Ce rappel ne remplace pas les deux preuves.

## 12. Références pédagogiques et limites

- **Autorité consultée :** `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md` et `CHARTE_CONVERSION_QC.md` (lus dans le bundle source); contenu et exercices originaux.
- **Graphe :** `registry/GRAPHE_PEDAGOGIQUE_202.json` — aucun `requires` sortant, `recommends_before` vers `qc-pri-ma-002` sans blocage; pas de nouvelle arête proposée.
- **Sources probantes :** mention initiale EEF/IES/CAST dans la frame, **non retenue comme citation indépendante sans lecture de documents primaires**; voir `sources/REFERENCES_CONTENU.md`.
- **Correspondance Québec :** `authoring/ALIGNEMENT.md` original inchangé; nomenclature seulement, ni alignement détaillé au PFEQ ni homologation.
- **Limites :** aucune banque IA n'est certifiée par calcul seul; revoir les formulations, l'accessibilité réelle et les seuils de la grille avec un évaluateur humain avant toute publication. Les contrôles exécutés figurent dans `livraison/VALIDATION.md`.
