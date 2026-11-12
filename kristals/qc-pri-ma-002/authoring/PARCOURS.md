---
format: qc.learning-path/1.0
id: qc-pri-ma-002
titre: Lire, écrire et comparer des nombres naturels
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Lire, écrire, ordonner et comparer des nombres naturels dans un champ adapté.
objectifs_secondaires: []
criteres_reussite:
- Placer et comparer des nombres en expliquant le critère de comparaison.
prealables_declares:
- qc-pri-ma-001
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-002-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-002`

**Discipline :** Mathématique. **Titre :** Lire, écrire et comparer des nombres naturels. **Vague :** 1. **Source :** workspace enrichi v1.2. **Statut :** contenu rédigé, revue humaine encore requise. Métadonnées YAML natives préservées; aucune revendication de conformité PFEQ.

## 1. Intention et frontières

- `obj-1` **IMMUTABLE :** Lire, écrire, ordonner et comparer des nombres naturels dans un champ adapté.
- `crit-1` **IMMUTABLE :** Placer et comparer des nombres en expliquant le critère de comparaison.
- **Notions :** numération, ordre, symbole, comparaison. Champ concret principal 0 à 9 999, étendu au besoin à un champ plus petit sur diagnostic; aucun nombre négatif ni virgule décimale dans ce module.
- L'objectif porte sur lecture/écriture de nombres, mise en ordre et **justification des comparaisons**, pas sur le calcul d'opérations. Des matériels de base dix peuvent être manipulés ou décrits.

## 2. Notions et représentations

- **Numération décimale de position :** dix unités constituent une dizaine, dix dizaines une centaine, dix centaines un millier. Dans 4 072 : 4 milliers, 0 centaines, 7 dizaines, 2 unités, soit `4 000 + 70 + 2`. Le chiffre zéro garde une place même lorsque sa contribution vaut 0.
- **Ordre :** pour deux naturels, celui placé plus à gauche sur une droite graduée croissante est le plus petit. On peut classer plusieurs nombres par ordre croissant ou décroissant.
- **Symboles :** `0`–`9` sont des chiffres; `1 205` est une écriture numérique; `<`, `>` et `=` expriment une relation vraie. La pointe de `<` est du côté du plus petit nombre.
- **Comparaison :** déterminer la relation entre deux naturels; d'abord comparer les nombres de chiffres significatifs, puis les chiffres du rang le plus élevé vers les unités, jusqu'à la première différence; égalité si tous identiques.
- **Représentations :** collections regroupées, tableau M/C/D/U, décomposition additive, droite numérique (graduations précises), écriture symbolique et écriture en mots. Voir `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- `requires` strict : **`qc-pri-ma-001`** (dénombrer et représenter des collections). Le **diagnostic d'équivalence** peut valider l'acquis et dispenser du parcours préalable, sans modifier le graphe.
- `recommends_before` : aucun; `reinforces` : aucun. Liens entrants du graphe descriptifs seulement.
- **Diagnostic D1 :** représenter 236 par 2 centaines, 3 dizaines, 6 unités et l'écrire; corriger la confusion chiffre/valeur.
- **Diagnostic D2 :** classer 508, 580, 805 et justifier en indiquant le premier rang différent. Diagnostic d'aptitude et de maîtrise antérieure, avec décisions explicitement décrites dans `contenu/02_DIAGNOSTIC.md`.

## 4. Enseignement guidé

- Modelage E1 : 3 406 = 3 000 + 400 + 0 + 6, puis distinguer 3 406 de 3 460 (dizaines 0 contre 6); 3 406 < 3 460.
- Modelage E2 : sur droite 1 200 → 1 300, placer 1 240 et 1 270 à des graduations de dix; `1 240 < 1 270`. Montrer pourquoi une droite non graduée ne permet pas un placement exact.
- Expliciter : annoncer le rang dominant, repérer la première différence et vérifier que le symbole et la position concordent. Faire reformuler sans mémoriser « le plus grand chiffre n'importe où ».
- Contre-exemples et verbalisation pas à pas dans `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- **G1** : comparer 2 405 / 2 450 avec un tableau M/C/D/U prérempli; rétroaction sur le rang des dizaines (indices complets).
- **G2** : classer 906, 960, 609 et identifier la centaine dominante; seul un rappel de procédure demeure.
- **G3** : placer 1 010, 1 040, 1 090 entre 1 000 et 1 100 sur une droite à pas de dix et expliquer la position; aucun indice de fond initial. Les indices sont retirés progressivement.
- Détails, mesures et corrigés `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- **A1** écrire 5 063 à partir du tableau de position; **A2** comparer 4 608 et 4 680; **A3** placer 740, 770, 790 sur une droite graduée de 700 à 800 par pas de 10; **A4** classer 2 901, 2 109, 2 910, 2 190.
- Réponses et critères détaillés : `contenu/05_PRATIQUE_AUTONOME.md`. Réponse orale, pointage accessible ou saisie assistée acceptable lorsque les nombres et la justification restent observables.
- Présenter de nouveaux nombres sans indice; conserver la trace du rang de comparaison, pas uniquement le bon symbole.

## 7. Feedback et erreurs typiques

- **E1** : « 4 072 = 4 702 » → les places centaines/dizaines sont inversées; utiliser M/C/D/U.
- **E2** : « 925 > 1 003 parce que 9 > 1 » → le nombre de positions significatives prime : 1 003 a 4 chiffres et 925 en a 3.
- **E3** : « 3 406 > 3 460 parce que 6 > 0 » → comparer de gauche à droite et s'arrêter à la première différence (dizaines).
- **E4** : droite non étalonnée → tracer les graduations régulières et vérifier l'écart.
- Rétroactions ciblées, nouvelles tentatives : `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Famille inchangée :** `qc-pri-ma-002-ev-01` ; liens `obj-1` et `crit-1` ; type natif `paramétrique_controle`. Banque de 10 items : 7 paramétriques déterministes et 3 fixes, dont deux **preuves autonomes**.
- **Preuve 1 (`q-009`)** : classer et placer quatre étiquettes de livres sur une droite croissante; établir et expliquer une comparaison.
- **Preuve 2 (`q-010`)** : ordonner quatre codes d'inventaire, relier l'un d'eux au tableau M/C/D/U et justifier une comparaison sur une fiche différente.
- **Grille :** exactitude de l'ordre/placement, relation symbolique, explication par la valeur de position et autonomie; chacune des deux preuves doit réussir séparément. Voir `evaluation/PLAN_EVALUATION.md` et `evaluation/GRILLE_MAITRISE.md`.
- **Paramètres contrôlés :** seeds entières 0…8 999, formules entières déterministes par famille; exemples recalculés et cas limites exhaustivement testés par script. Aucune IA libre ne tranche la validité d'un corrigé.

## 9. Remédiation / enrichissement

- Si difficultés de numération : revenir aux regroupements d'objets et décomposition M/C/D/U; test nouveau 3 020 = 3 000 + 20.
- Si erreurs de rang : masquer de droite à gauche pour faire ressortir le premier rang différent, puis retirer le masque.
- Si symboles inversés : dire la relation complète (« 860 est plus petit que 906 ») et vérifier la pointe du symbole.
- **Enrichissement** : zéro au milieu, franchissement d'une centaine (1 999 / 2 000), égalité et quatre nombres sur une droite. Aucun ajout d'un nouveau préalable.

## 10. Accessibilité

- Lire la consigne à voix haute, donner tableau en gros caractères ou tactile, manipulables de base dix, droite numérique à relief, braille/mathématiques ou technologie d'assistance.
- Ne pas remplacer le raisonnement par une aide qui révèle le bon ordre; consigner toutes les aides de fond. Possibilité de dicter les nombres et d'expliquer oralement; vérifier que la lecture/écriture numérique reste attestée par une modalité accessible équivalente.
- Pas de condition d'âge, de rapidité d'exécution ou de matériel coûteux. Stimuli fictifs; aucune information personnelle collectée.

## 11. Critères de sortie

1. Diagnostiquer ou attester l'acquis équivalent à `qc-pri-ma-001` pour satisfaire la condition `requires`, sans blocage inutile.
2. Dans deux contextes nouveaux, classer **quatre** nombres naturels et les placer dans un ordre cohérent ou sur une ligne graduée; établir une comparaison symbolique vraie et expliquer **le premier rang différent ou la longueur de l'écriture**.
3. Pour `q-009` **ET** `q-010` : exactitude complète des nombres/ordre, explication pertinente et autonomie. Remédiation de la dimension déficiente puis réépreuve nouvelle si preuve insuffisante; **aucune note unique ne conclut**.
4. Rappel différé à J+2–3 : 3 090 / 3 900; à J+10–14 : droite graduée autour de 2 000 et comparaison nouvelle. Rappel formatif, pas preuve unique.

## 12. Références pédagogiques et limites

- **Source maîtresse interne vérifiée :** trois normes v1.2, graphe 202, `authoring` v1.2, alignement et brief. Aucun fichier central modifié.
- **Repère externe consulté** : Alloprof, *Les nombres* (primaire), pour la numération, la comparaison et la droite; non comme autorité de conformité PFEQ. Toutes les tâches et formules sont des créations originales pour ce Kristal.
- **Validation :** le calcul des variantes est contrôlé par un script et les JSON sont parsables; absence de révision humaine et d'essai en classe. Le projet conserve le statut `a_revoir`.
- Détails : `sources/REFERENCES_CONTENU.md` et `livraison/VALIDATION.md`. Aucune certification, homologation ni année scolaire normative assignée.
