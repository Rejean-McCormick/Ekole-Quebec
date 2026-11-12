---
format: qc.learning-path/1.0
id: qc-pri-ma-012
titre: 'Fractions : représentations et sens'
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Représenter une fraction comme partie d’un tout ou d’une collection.
objectifs_secondaires: []
criteres_reussite:
- Produire trois représentations correctes d’une même fraction simple.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-012-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-012`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Fractions : représentations et sens  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**État éditorial :** cours et banque rédigés, à revoir et à éprouver avant toute qualification; le YAML v1.2 est conservé, dont son statut administratif `en_rédaction`.

## 1. Intention et frontières

- **`obj-1` — objectif observable INCHANGÉ :** Représenter une fraction comme partie d’un tout ou d’une collection.
- **`crit-1` — preuve de maîtrise INCHANGÉE :** Produire trois représentations correctes d’une même fraction simple.
- Noyau : **tout**, **parts égales**, **numérateur**, **dénominateur**; fractions propres simples `a/b` avec `0 < a < b`, `b` entier positif; exemples et activités majoritairement avec `b ∈ {2,3,4,5,6,8}`.
- Trois représentations à produire d'une même fraction : **surface partagée en aires égales**, **bande segmentée en longueurs égales**, **collection d'objets discrets sélectionnés**. Le nombre d'objets de la collection peut être un multiple du dénominateur si ce regroupement est justifié.
- Ni calcul d'opérations sur les fractions, ni comparaison formelle, ni équivalence généralisée ne sont évalués. On peut utiliser `a×m` objets sur `b×m` pour représenter la même part du tout sans exiger de simplification algébrique.
- **Aucun `requires` entrant, aucun `recommends_before`, aucun `reinforces` sortant** pour ce Kristal, selon les relations du registre. Les références d'autres Kristals *vers* celui-ci ne sont pas des préalables à ce cours.

## 2. Notions et représentations

1. **Tout (unité de référence)** : ce que l'on a décidé de compter comme un entier — une tarte complète de taille définie, une bande complète ou l'ensemble complet de jetons. Dire « trois jetons colorés » n'indique pas une fraction si le total du groupe n'est pas établi.
2. **Parts égales** : les subdivisions d'un tout continu doivent avoir **la même aire** pour un modèle d'aire, ou **la même longueur** pour une bande; leurs formes peuvent différer. Pour une collection d'objets équivalents dans l'activité, on compte chaque objet une fois et on connaît l'effectif total; il n'est pas nécessaire de ranger les objets dans des groupes de taille égale avant de compter, mais les groupes représentatifs utilisés pour modéliser `1/b` doivent avoir la même taille.
3. **Dénominateur `b`** : nombre de parts égales constituant le tout de référence; pour une collection découpée en `b` groupes égaux, c'est le nombre de groupes, pas nécessairement le nombre d'objets individuels.
4. **Numérateur `a`** : nombre de ces parts ou groupes sélectionnés; l'écriture `a/b` relie les deux nombres à **la même unité**.
5. **Invariant de contrôle** : préciser le tout → montrer l'égalité des parts → montrer `b` parts → repérer `a` parts → écrire `a/b` → justifier. Si la collection a `b×m` objets et `a×m` sélectionnés, chaque groupe comporte `m` objets.

**Exemple original résolu A.** Une feuille rectangulaire est divisée en quatre bandes d'aire égale. Trois bandes sont coloriées : `3/4`. Une bande de 4 segments de longueur égale, dont 3 mis en évidence, et une collection de 8 jetons de même statut dont 6 cochés représentent aussi `3/4` : `8 = 4×2`, `6 = 3×2`.

**Exemple original résolu B.** Sur 12 étiquettes identiques du même ensemble, 4 sont marquées. Grouper en trois groupes de quatre; un groupe marqué sur trois = `1/3`. Un rectangle partagé en trois aires égales et une bande de trois longueurs égales, chacun avec une part coloriée, conviennent. Le tout reste les **12 étiquettes**, pas les 4 marquées.

**Contre-exemple 1.** Une surface en quatre régions visiblement d'aires différentes, dont deux coloriées, ne représente pas `2/4` au seul motif « deux sur quatre ». Corriger en quatre aires égales.

**Contre-exemple 2.** 3 billes choisies dans une boîte de 10 ne représentent pas `3/5` : le tout est de 10, donc `3/10`. Pour faire `3/5`, choisir 6 billes de 10, soit trois groupes de deux sur cinq.

Tout le développement et les représentations textuelles accessibles : [01_NOTIONS_ET_EXEMPLES.md](../contenu/01_NOTIONS_ET_EXEMPLES.md).

## 3. Préparation / diagnostic

**Zéro préalable bloquant.** `diag-1` (3 à 5 min) : montrer `■■□` comme trois cases de même aire, deux remplies. Demander : « Quel est le tout? Combien de parts égales? Quelle fraction est remplie? » Solution : un rectangle de trois cases; `2/3`; `2` numérateur, `3` dénominateur. `diag-2` (4 min) : 2 jetons marqués sur 8 jetons d'une même collection; représenter cette part par une bande de quatre parts égales. Résultat : `2/8 = 1/4` dans cette situation, bande avec une section sur quatre; l'élève doit expliciter pourquoi le regroupement 2-par-2 est possible. Ne pas imposer l'algorithme d'équivalence.

**Interprétation :** réussite autonome des deux tâches avec unité, égalité et justification → raccourcir le modelage, proposer une tâche de transfert. Une erreur d'unité → reprise avec collection; une erreur d'égalité → comparer aires/longueurs; confusion de l'ordre de `a/b` → reconstruire trois cas concrets. Le diagnostic n'est **pas** une preuve suffisante de maîtrise à lui seul. Matériel et corrections : [02_DIAGNOSTIC.md](../contenu/02_DIAGNOSTIC.md).

## 4. Enseignement guidé

**`teach-1` :** annoncer exactement `obj-1`, puis penser à voix haute : « Quel est le tout? » Utiliser un rectangle de 5 cases égales dont 2 coloriées, une bande de 5 segments égaux dont 2 marqués, puis 10 boutons en cinq paires dont 4 marqués. Insister : deux paires sur cinq = quatre boutons sur dix = `2/5` du tout. À chaque transition, énoncer le rôle de `a=2` et `b=5`; ne jamais substituer « pièces égales » à « aires égales » pour un dessin de surfaces.

**Contrôles en cours de modelage :** « Pourquoi `2/10` serait faux pour les 10 boutons? » (Il y a 4 boutons choisis, donc 4 sur 10; les **deux groupes sur cinq** donnent `2/5`.) « Si je change la largeur d'une case du rectangle, que dois-je vérifier? » (Égalité des aires). Démonstrations et phrases d'enseignant : [03_ENSEIGNEMENT_GUIDE.md](../contenu/03_ENSEIGNEMENT_GUIDE.md).

## 5. Pratique accompagnée

**`guided-1` (indices décroissants)** :
1. `1/2` : un rectangle de 2 parts et 6 jetons, guidage explicite « entoure le tout; groupes de 3 »; réponse 1 part d'aire sur 2 et 3 jetons sur 6.
2. `2/3` : rectangle/bande de trois cases égales et neuf jetons; indice conditionnel « combien de groupes égaux? »; réponse 2 sur 3 et 6 sur 9.
3. `3/4` : demander une bande de 4 unités et une collection de 12 avec indice disponible **après** un essai; réponse 3 segments sur 4, 9 objets sur 12.

Critères : tout nommé, parts effectivement égales, correspondance `a/b`, justification de la collection; réponse erronée traitée par comparaison avec le premier modèle valide, sans fournir le résultat immédiatement. Détails : [04_PRATIQUE_ACCOMPAGNEE.md](../contenu/04_PRATIQUE_ACCOMPAGNEE.md).

## 6. Pratique autonome

**`independent-1` :** quatre tâches nouvelles sans rétroaction immédiate : représenter `2/5` avec surface/bande/collection de 15, interpréter `3/6` d'une collection de 12, corriger un partage non égal, résoudre la part de 3 objets sur 12. Chaque réponse inclut l'énoncé du tout et la justification. **Il ne suffit pas de recopier trois fois le même dessin.** Voir [05_PRATIQUE_AUTONOME.md](../contenu/05_PRATIQUE_AUTONOME.md).

Les deux preuves de maîtrise, séparées et plus exigeantes, sont **q-009** (aménagement d'un jardin; `2/5` ou variation contrôlée) et **q-010** (distribution de matériel; `3/4` ou variation contrôlée); chacune demande les trois modes, sans indice ni accès au corrigé. Elles mobilisent deux contextes effectivement distincts. Les traces de réponses sont stockées par l'environnement d'apprentissage, jamais dans le canon.

## 7. Feedback et erreurs typiques

- **Référence absente :** « De quels objets le groupe entier se compose-t-il? Entoure-le d'abord. » Nouvelle collection de 9 et 3 marqués à représenter = `1/3`.
- **Partitions inégales :** « Le nombre de régions ne garantit pas l'égalité d'aire. Superpose ou mesure des unités. » Nouvelle bande de 4 segments égaux, 1 choisi = `1/4`.
- **Numérateur/dénominateur inversés :** « Compte toutes les parts égales d'abord; compte celles prises ensuite. » 2 cases sur 5 = `2/5`, pas `5/2`.
- **Collection mal groupée :** « Pour `2/3` sur 12 objets, fabrique trois groupes **de quatre**; entoure deux groupes. » Résultat 8 objets sélectionnés, non 2.
- **Deux touts différents comparés sans précision :** « `1/2` de 4 et `1/2` de 10 sont la même fraction mais pas le même nombre d'objets. » Recommencer avec unités explicites.

Demander correction *et* essai neuf. Table diagnostique et parcours de reprise : [06_REMEDIATION_ET_TRANSFERT.md](../contenu/06_REMEDIATION_ET_TRANSFERT.md).

## 8. Évaluation formative et preuves

- **Famille conservée** `qc-pri-ma-012-ev-01` ; `objectif_ref: obj-1` ; `critere_ref: crit-1`.
- **Mode de prédilection** : `paramétrique_controle` via **catalogues bornés, seed stable et solution dérivée déterministement**, sans génération libre. Dix items `q-001` à `q-010` : analyse, construction, diagnostic d'erreur et deux preuves intégratrices.
- **Attendu pour chaque preuve intégratrice** : 3 modèles réellement distincts, fraction unique, tout repéré, parts égales dans les modèles continus, regroupement discret correct et justification. Deux productions indépendantes réussies sur contextes différents, sans indices; aucune note isolée ne suffit.
- **Notation** : grille à niveaux par dimensions plutôt que score unique. Éléments susceptibles de varier fixés dans [PLAN_EVALUATION.md](../evaluation/PLAN_EVALUATION.md) et la [BANQUE_ITEMS.json](../evaluation/BANQUE_ITEMS.json); décision dans [GRILLE_MAITRISE.md](../evaluation/GRILLE_MAITRISE.md).

## 9. Remédiation / enrichissement

- Difficulté à choisir le **tout** : délimiter physiquement une collection entière avant de choisir les objets.
- Parts **non égales** : utiliser une bande pliée en parts de mêmes longueurs; pour des surfaces, un quadrillage de cases de mêmes aires.
- Rôle **numérateur/dénominateur** : décrire `b` comme « en combien de parts égales » et `a` comme « combien sélectionnées », puis alterner dictée et schéma.
- **Collection** : faire des groupes de même nombre d'objets, puis montrer pourquoi `a×m` sur `b×m` représente `a/b`; refaire avec un `m` différent.
- **Enrichissement** : remplacer une disposition 1×4 par 2×2 carrés d'aires égales; expliquer pourquoi formes/aspects visuels variables peuvent préserver la part, sans ajouter d'objectif de calcul formel.
- **Transferts** : contexte d'un jardin (aire) et contexte de matériel (collection); [06_REMEDIATION_ET_TRANSFERT.md](../contenu/06_REMEDIATION_ET_TRANSFERT.md).

## 10. Accessibilité

- Schémas ASCII toujours expliqués en mots (« 3 cases sur 5 »), sans coder la solution **uniquement** par la couleur; proposer motifs, relief ou jetons tactiles.
- Impression en grand, quadrillage et objets manipulables; consigne lue à voix haute sans résoudre le raisonnement; réponse à l'oral, par pointeur ou en manipulation si la justification est observable et transcrite.
- Ne pas dépendre de découpage fin, acuité chromatique ou dextérité. Dessin remplacé par disposition de bandes et jetons si les trois modèles demeurent distinguables.
- Temps ajustable, consignes segmentées avant l'épreuve; **aucun indice conceptuel durant** les deux preuves d'autonomie. Si aide conceptuelle donnée, marquer « accompagnée » et recommencer plus tard avec une variante approuvée.
- Aucune collecte de données personnelles nécessaire, objets fictifs; pas de décision de valeur d'une personne selon le résultat.

## 11. Critères de sortie

1. `crit-1` strict : **Produire trois représentations correctes d’une même fraction simple.** À chaque preuve : surface, bande et collection du même `a/b`, tout explicite et parts égales assurées.
2. Réussite démontrée **deux fois** dans des contextes distincts (jardin et distribution de matériel, ou variantes validées) et **sans indice conceptuel**; aucune erreur conceptuelle sur l'unité, `a/b` et le partage.
3. Nommer `a` et `b`, justifier la collection si le nombre d'objets n'est pas égal à `b` et expliquer pourquoi trois modèles représentent le même rapport.
4. Si l'une des preuves échoue, enseigner le maillon défaillant, puis réévaluer avec une variante *non déjà travaillée*; ne pas compenser par une moyenne.
5. **Rappel différé** : 48 h–7 j après la dernière réussite, proposer `1/4` d'une affiche quadrillée et 3 sur 12 jetons; demander un troisième modèle en bande. Un oubli entraîne une consolidation/revérification, pas une annulation automatique des traces antérieures.

## 12. Références pédagogiques et limites

- **Sources internes vérifiées** : contrat de gouvernance v1.2, génération d'examens, charte et graphe; sources scientifiques externes et réserves documentées dans [REFERENCES_CONTENU.md](../sources/REFERENCES_CONTENU.md).
- **Correspondance Québec** : [ALIGNEMENT.md](ALIGNEMENT.md), conservé tel quel et **non livré**. La nomenclature « Mathématique » n'implique **aucune conformité PFEQ**; code de matière officiel : `null`.
- **Originalité** : exemples, contre-exemples, exercices, tableaux et grilles sont créés ici; aucun média tiers incorporé.
- **Limites** : les 10 items ont des corrigés numériques testés mais ne sont ni étalonnés, ni essayés auprès d'élèves, ni revus humainement; mode d'évaluation paramétrique simulé sur catalogues fermés, pas solveur externe ni génération IA libre. Aucune qualification canonique/publication dans cette livraison. Voir [VALIDATION.md](../livraison/VALIDATION.md).
