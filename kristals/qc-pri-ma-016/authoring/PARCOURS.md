---
format: qc.learning-path/1.0
id: qc-pri-ma-016
titre: 'Nombres décimaux : comparaison et calculs'
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Comparer et calculer avec des décimaux en utilisant les valeurs de position.
objectifs_secondaires: []
criteres_reussite:
- Résoudre deux calculs décimaux et justifier la plausibilité des réponses.
prealables_declares:
- qc-pri-ma-015
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-016-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-016`

**Discipline (appellation québécoise) :** Mathématique  
**Titre :** Nombres décimaux : comparaison et calculs  
**Cadre :** conception pédagogique Kristal v1.2; pas de conformité ni d'homologation PFEQ revendiquée.  
**Statut de travail :** cours et items rédigés, calculs vérifiés localement; revue pédagogique humaine et qualification du moteur non effectuées. Le front matter canonique v1.2 est conservé à l'identique, y compris ses statuts initiaux.

## 1. Intention et frontières

- **Objectif `obj-1`, immuable :** Comparer et calculer avec des décimaux en utilisant les valeurs de position.
- **Preuve `crit-1`, immuable :** Résoudre deux calculs décimaux et justifier la plausibilité des réponses.
- **Actions observables :** comparer deux nombres, expliquer le rôle de l'unité, des dixièmes et des centièmes; aligner les virgules pour additionner ou soustraire; estimer avant de calculer; vérifier au moyen d'une opération inverse ou de bornes.
- **Étendue :** décimaux non négatifs à **au plus deux chiffres après la virgule**, valeurs en centièmes exacts; addition, soustraction à résultat non négatif, comparaison `=`, `<`, `>` et calculs en contexte d'une même unité. Le zéro, les zéros terminaux et les retenues/emprunts sont enseignés. Pas de calcul monétaire réel, pas d'arrondi flottant, pas de multiplication/division de décimaux, pas de nombres négatifs. L'étiquette « primaire québécois » n'est qu'une projection de présentation.
- **Lieux documentaires :** leçons `contenu/01_NOTIONS_ET_EXEMPLES.md` à `contenu/06_REMEDIATION_ET_TRANSFERT.md`; banque et décision en `evaluation/`.

## 2. Notions et représentations

1. **Décimal et valeur de position.** `4,07` = quatre unités, zéro dixième et sept centièmes = `407/100`. `4,7 = 4,70` parce que sept dixièmes correspondent à soixante-dix centièmes; `4,07` est plus petit que `4,7`. Utiliser un tableau unités | dixièmes | centièmes, une grille de cent cases ou une droite graduée.
2. **Comparer** : même unité, compléter les zéros de droite au besoin, comparer les unités, puis les dixièmes, puis les centièmes, **pas** la longueur de la partie écrite après la virgule. Ainsi `6,08 < 6,8 = 6,80`.
3. **Alignement des rangs** : placer unités sous unités, virgules sous virgules, dixièmes sous dixièmes, centièmes sous centièmes. Ajouter des zéros terminaux n'altère pas la valeur : `3,4 + 2,08 = 3,40 + 2,08 = 5,48`.
4. **Opérations** : additionner ou soustraire des unités semblables, effectuer les retenues et les échanges entre rangs; exemple `7,10 − 2,46 = 4,64` (10 centièmes ne suffisent pas : on échange une unité de rang approprié). Vérifier avec `4,64 + 2,46 = 7,10` et avec une estimation `7 − 2,5 ≈ 4,5`.
5. **Plausibilité** : avant ou après le calcul, choisir des bornes ou une estimation de grandeur adaptées (`4,20 + 1,30` est entre `5` et `6`, pas `55`) puis vérifier, si possible, avec une opération inverse. Les estimations n'ont pas besoin d'être exactement identiques si elles justifient réellement le résultat.

## 3. Préparation / diagnostic

- **Seul `requires` strict :** `qc-pri-ma-015` — Nombres décimaux : représentations. Si les tâches diagnostiques attestent une compréhension équivalente des valeurs de position, ce préalable est reconnu sans obligation de refaire le Kristal; sinon proposer un renforcement ciblé. Aucune relation `recommends_before` ni `reinforces` sortante.
- **D1 :** placer `2,36` et `2,6` dans un tableau des rangs et les comparer : `2,36 < 2,60`. Critère : sait que `6` dixièmes > `3` dixièmes.
- **D2 :** montrer `4,5 = 4,50` avec une grille et expliquer pourquoi `4,05` diffère : `4,05` est inférieur de `0,45`.
- **D3 (non bloquant, repérage de la procédure) :** estimer `3,20 + 1,45` et dire où vont les virgules : environ `4,5 à 5`, exact `4,65` si l'élève calcule. Un calcul incorrect ici ne disqualifie pas la compréhension des rangs; il oriente l'enseignement.
- Consigner les traces sans score unique de passage; voir `contenu/02_DIAGNOSTIC.md`.

## 4. Enseignement guidé

- **Modelage `teach-1` :** avec 3 unités, 4 dixièmes et 7 centièmes, représenter `3,47`; ajouter deux unités et huit dixièmes : convertir `2,8` en `2,80`, regrouper centièmes et dixièmes, obtenir `6,27` pour `3,47 + 2,80` (47+80 centièmes = 127 centièmes, soit 1 unité et 27 centièmes); contrôler `6,27 − 2,80 = 3,47`.
- **Modelage `teach-2` :** montrer `8,20 − 3,65 = 4,55` avec échanges (emprunt à l'unité pour retirer 65 centièmes après avoir enlevé 3 unités); vérifier `4,55 + 3,65 = 8,20`.
- **Modelage `teach-3` :** comparer `5,6` et `5,64` via `5,60 < 5,64`; expliquer que `5,6` n'est pas « plus grand parce qu'il a moins de chiffres ».
- Démontrer d'abord avec tableau de rangs et grille de centièmes, puis enlever le tableau. Demander à l'élève quel rang s'aligne avec le `8` de `2,8`. Les explications détaillées sont dans `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- **G1 :** `2,35 + 1,40 = 3,75` avec tableau prérempli (unités, dixièmes, centièmes) et contre-vérification par estimation.
- **G2 :** `6,00 − 2,78 = 3,22` avec seul rappel « ajoute un zéro terminal si utile »; demander de justifier l'échange à la soustraction.
- **G3 :** comparer `4,09`, `4,90` et calculer `4,09 + 0,81 = 4,90` sans tableau fourni; l'élève choisit une estimation et explique `4,09 < 4,90`.
- Retirer les indices à chaque tâche. Corriger d'abord le premier rang mal aligné, sans donner le total. Détails et indices dégressifs en `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- **A1 :** comparer `7,08` et `7,8`, justifier avec `7,80`.
- **A2 :** `4,56 + 2,70 = 7,26`, estimation environ `7,3`.
- **A3 :** `9,02 − 4,85 = 4,17`, contrôle `4,17 + 4,85 = 9,02`.
- **A4 :** deux rubans `1,75 m` et `2,40 m` sont mis bout à bout (`4,15 m`); on en coupe `0,65 m`, reste `3,50 m`. Justifier l'ordre de grandeur.
- Réponses, critères et modalités dans `contenu/05_PRATIQUE_AUTONOME.md`; aucune correction pendant la production autonome. Les **deux preuves distinctes** sont `q-009` (achat fictif) et `q-010` (distance parcourue), chacune demandant deux calculs et une justification indépendante.

## 7. Feedback et erreurs typiques

- `3,4 + 2,08 = 2,42` (chiffres alignés à droite sans tenir compte des virgules) : aligner les **rangs**, réécrire `3,40 + 2,08 = 5,48`, expliquer pourquoi les deux unités s'ajoutent aux trois unités.
- `7,1 − 2,46 = 5,35` (échanges défectueux) : dessiner 7 unités et 10 centièmes, échanger 1 unité contre 100 centièmes, effectuer `7,10 − 2,46 = 4,64`, vérifier en additionnant.
- `5,9 < 5,12` parce que `9 < 12` comme entiers : utiliser `5,90 > 5,12`; comparer les dixièmes d'abord.
- Résultat numérique correct, explication « ça a l'air bon » : demander des bornes chiffrées ou une opération inverse, puis refaire sans indice sur un autre contexte.
- `contenu/06_REMEDIATION_ET_TRANSFERT.md` donne retours et essais ciblés.

## 8. Évaluation formative et preuves

- **Famille immuable :** `qc-pri-ma-016-ev-01`; `objectif_ref: obj-1`; `critere_ref: crit-1`; mode privilégié `paramétrique_controle`.
- Banque de **12 items** `q-001` à `q-012`, fixes et six familles d'instances paramétriques contrôlées; pour chacune, algorithme arithmétique en centièmes, seed stable, bornes, contraintes, variantes calculées, correction et justification exigée.
- **Preuve P1 (`q-009`, marché fictif)** : somme de deux prix puis monnaie rendue sur 10,00 $, avec calculs, unités et plausibilité.
- **Preuve P2 (`q-010`, marche fictive)** : somme de deux étapes puis distance restante sur 8,00 km, avec calculs, unités et plausibilité; contexte distinct et sans indices.
- Pas de décision de maîtrise à partir d'une note unique : deux productions autonomes satisfaisantes, observées avec une grille, dans des contextes différents; voir `evaluation/PLAN_EVALUATION.md` et `evaluation/GRILLE_MAITRISE.md`.
- Les items demeurent `a_revoir`; revue humaine nécessaire.

## 9. Remédiation / enrichissement

- Problème de valeur de position : construire `1,04`, `1,4`, `1,40` sur 100 cases; expliquer `1,04 < 1,40 = 1,4` et refaire D2.
- Problème d'alignement : tableau unités | dixièmes | centièmes, déposer chiffres puis refaire `2,50 + 0,35 = 2,85`.
- Problème de regroupement : échanges de dixièmes/centièmes avec cartes de valeur, puis `5,00 − 1,76 = 3,24` vérifié par `3,24 + 1,76 = 5,00`.
- Problème de plausibilité : encadrer chaque terme et le résultat entre entiers, puis valider une opération inverse sans calculatrice.
- Enrichissement : trouver deux méthodes pour `6,75 − 2,30`, comparer des solutions équivalentes ou justifier une vérification par somme complémentaire. Deux transferts supplémentaires dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 10. Accessibilité

- Énoncés lisibles avec virgule décimale et unités, tableau à grands caractères, grille tactile ou jetons, lecture orale et réponses par écrit, dictée à scribe neutre ou description orale de la disposition des rangs; ne pas dépendre d'une couleur ou d'une motricité précise.
- Le scribe/transcripteur écrit sans interpréter ni guider la procédure; pendant les preuves, **aucune aide au choix des opérations ou aux résultats**. Les aménagements gardent identiques comparaison, calcul exact et justification.
- Les scénarios sont fictifs, sans dépendance aux dépenses personnelles de l'élève. Unités explicites, temps flexible, examen des obstacles de lecture. Aucun diagnostic médical ou donnée personnelle exigé.

## 11. Critères de sortie

1. Comparer et représenter des nombres à deux décimales, y compris des zéros de remplissage et des cas `=`; expliquer les rangs utilisés.
2. Sur **P1 (`q-009`)** et **P2 (`q-010`)**, réaliser **deux calculs décimaux exacts par contexte**, maintenir les unités et justifier pourquoi chaque résultat est plausible (estimation chiffrée, borne ou opération inverse expliquée).
3. Sur chaque preuve autonome, satisfaire toutes les dimensions essentielles de la grille (alignement/sens, exactitude, plausibilité, autonomie), sans aide conceptuelle. Traces recueillies séparément et contextes non enseignés mot à mot.
4. Si la seconde preuve échoue, ne pas inférer la maîtrise : cibler l'erreur et demander une nouvelle preuve dans un autre contexte; enregistrer la décision dans le LMS, jamais dans le canon.
5. **Rappel différé** : deux à sept jours plus tard, comparer `3,09` et `3,9`, puis vérifier `5,20 − 1,45 = 3,75`; fournir feedback si un rang est mal lu, et reprogrammer si nécessaire.

## 12. Références pédagogiques et limites

- **Autorité interne vérifiée dans l'archive :** `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`, graphe et frame originale; provenance détaillée dans `sources/REFERENCES_CONTENU.md`.
- **Arithmétique :** écritures à deux décimales et règles de calcul sont dérivées de la numération en base dix; exemples, figures textuelles, scénarios et banque sont originaux. Corrigés recalculés indépendamment en entiers de centièmes et en `Decimal`.
- **Charte Québec :** uniquement appellation Mathématique et niveaux/cycles de présentation éventuels. `ALIGNEMENT.md` est inchangé; aucune conformité, homologation ou année de cours imposée.
- **Limites :** pas de test élève, pas d'essai d'import LMS, pas de revue humaine sur accessibilité ou biais, pas de certification. Tous les items restent `a_revoir`; une validation humaine doit précéder toute publication.
