---
format: qc.learning-path/1.0
id: qc-pri-ma-003
titre: Valeur de position et regroupements
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Décomposer et recomposer des nombres grâce aux valeurs de position.
objectifs_secondaires: []
criteres_reussite:
- Décomposer un nombre de deux façons puis effectuer un regroupement inverse.
prealables_declares:
- qc-pri-ma-002
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-003-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---
# Microparcours — `qc-pri-ma-003`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Valeur de position et regroupements  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** contenu pédagogique rédigé et corrigés testés localement; qualification humaine et publication non effectuées. Les métadonnées YAML v1.2 sont conservées à l'identique.

## 1. Intention et frontières

- `obj-1` — **Résultat vérifiable :** Décomposer et recomposer des nombres grâce aux valeurs de position.
- `crit-1` — **Production autonome qui atteste l’acquis :** Décomposer un nombre de deux façons puis effectuer un regroupement inverse.
- Notions : **unités**, **dizaines**, **centaines**, **base dix**. Domaine de travail : nombres naturels de **100 à 999** pour le cœur du parcours; cas limite **100** et **zéro dans une position** inclus. Les regroupements ne changent jamais la quantité totale.
- Ce Kristal ne valide pas automatiquement la compétence par l'âge ou l'année. `qc-pri-ma-002` est le préalable strict, ou son équivalent attesté par diagnostic; aucune autre arête n'est ajoutée.
- **Annonce à l'élève :** « Tu vas écrire une même quantité de deux façons, échanger 10 unités contre 1 dizaine (ou 10 dizaines contre 1 centaine), puis faire l'échange inverse pour retrouver ta première écriture. »

## 2. Notions et représentations

- **Unité (U) :** objet isolé compté pour 1. Dans 243, le 3 représente 3 unités.
- **Dizaine (D) :** groupe de 10 unités; une dizaine vaut 10, donc 4 D valent 40.
- **Centaine (C) :** groupe de 10 dizaines, soit 100 unités; 2 C valent 200.
- **Base dix :** valeur d'un chiffre multipliée par 1, 10 ou 100 selon sa position, avec échange réversible de 10 unités d'un rang contre 1 du rang immédiatement supérieur. Le chiffre 0 signifie qu'il n'y a aucun groupe à ce rang dans l'écriture canonique, non que ce rang n'existe pas.
- **Même quantité, groupements différents :** 243 = 2 C + 4 D + 3 U = 2 C + 3 D + 13 U. En échangeant 10 U de la deuxième écriture pour 1 D, retrouver 2 C + 4 D + 3 U. Une écriture dégroupée peut comporter plus de 9 unités ou dizaines; les chiffres de l'écriture canonique restent entre 0 et 9.
- **Trois représentations successives :** matériel (plaques de cent, bandes de dix, jetons); schéma textuel `[C][C] | [D]×4 | [U]×3` avec légende accessible; notation `200 + 40 + 3 = 243`. Le schéma est un code, pas une image indispensable.
- **Exemple 1 :** 354 = 3 C + 5 D + 4 U = 2 C + 15 D + 4 U; retour : 10 D -> 1 C.
- **Exemple 2 :** 208 = 2 C + 0 D + 8 U = 1 C + 10 D + 8 U; retour : 10 D -> 1 C.
- **Contre-exemple 1 :** `3 C + 6 D + 12 U = 362` est faux : 300 + 60 + 12 = 372. Il faut écrire `3 C + 6 D + 12 U = 372`, puis `3 C + 7 D + 2 U`.
- **Contre-exemple 2 :** `4 C + 0 D + 5 U = 450` est faux : c'est **405**, car 0 dizaine vaut 0.
- Démonstrations étendues et droits : [01_NOTIONS_ET_EXEMPLES.md](../contenu/01_NOTIONS_ET_EXEMPLES.md).

## 3. Préparation / diagnostic

- **Préalable `requires` unique :** `qc-pri-ma-002` (lire, écrire et comparer des nombres naturels). Aucun `recommends_before` ni `reinforces` sortant de ce Kristal; les liens entrants du graphe ne deviennent pas ses nouveaux préalables.
- `diag-1` : montrer 236; faire **lire/écrire** « deux cent trente-six », puis demander 2 C + 3 D + 6 U = ? et pourquoi le 3 vaut 30, non 3.
- `diag-2` : montrer `1 C + 12 D + 4 U`; demander la valeur **224** et une forme avec moins de 10 dizaines : `2 C + 2 D + 4 U`.
- **Décision d'accès :** si lecture/écriture des nombres et justification de leurs positions sont observables sur `diag-1`, compétence équivalente au préalable attestée localement même sans parcours `qc-pri-ma-002`; si non, remédier à la lecture/écriture en référant à cet ID avant l'échange avancé. Une erreur de regroupement sur `diag-2` n'empêche pas l'entrée dans l'enseignement de ce Kristal.
- **Collecter** réponses, justification orale/écrite et aide fournie; ne pas appeler le diagnostic « preuve de maîtrise ».
- Détails et corrigés : [02_DIAGNOSTIC.md](../contenu/02_DIAGNOSTIC.md).

## 4. Enseignement guidé

- `teach-1` — **Objectif immuable :** Décomposer et recomposer des nombres grâce aux valeurs de position.
- Dire avec **132** : « 1 C + 3 D + 2 U vaut 100 + 30 + 2. Je défais une dizaine en 10 unités; j'obtiens 1 C + 2 D + 12 U = 132. Je vérifie 100 + 20 + 12 = 132. Maintenant je regroupe ces 10 unités en 1 dizaine et je retrouve la première forme. »
- Montrer parallèlement 1 plaque, 3 bandes, 2 jetons; transformer une bande en 10 jetons; puis afficher le schéma annoté; enfin remplacer le matériel par la notation seule. Toujours énoncer la conservation de la valeur.
- **Arrêt compréhension :** « Dans 132, combien d'unités le 2 représente-t-il? Combien le 3 représente-t-il? Dans `1 C + 2 D + 12 U`, quel regroupement inverse ramène à 3 D? » (2 unités; 30 unités; 10 U -> 1 D.)
- Comparer l'erreur `1 C + 2 D + 12 U = 122` et recalculer 100 + 20 + 12 = **132**.
- Le texte pas à pas : [03_ENSEIGNEMENT_GUIDE.md](../contenu/03_ENSEIGNEMENT_GUIDE.md).

## 5. Pratique accompagnée

- `guided-1` — **G1 (indice détaillé) :** 264; écrire 2 C + 6 D + 4 U, échanger 1 D pour 10 U, obtenir 2 C + 5 D + 14 U, puis refaire 10 U -> 1 D. Indice : barrer une bande et dessiner 10 points.
- **G2 (indice limité) :** 317; écrire 3 C + 1 D + 7 U, chercher une deuxième forme en échangeant 1 C contre 10 D : 2 C + 11 D + 7 U; retourner 10 D -> 1 C. Indice seulement : « Quel lot de dix peux-tu défaire? »
- **G3 (sans indice d'emblée) :** 580; deux formes 5 C + 8 D + 0 U et 4 C + 18 D + 0 U; retour 10 D -> 1 C. En cas d'échec, présenter le choix entre une plaque de 100 et dix bandes, puis retirer à nouveau l'appui.
- Après toute erreur : demander d'abord la valeur numérique de chaque terme, puis le premier échange qui ne conserve pas la valeur; fournir le corrigé **après** essai de correction.
- Voir [04_PRATIQUE_ACCOMPAGNEE.md](../contenu/04_PRATIQUE_ACCOMPAGNEE.md).

## 6. Pratique autonome

- `independent-1` — **P1 :** 426, décomposer deux fois et inverser 1 D -> 10 U. Solution : `4 C + 2 D + 6 U = 4 C + 1 D + 16 U`; inverse 10 U -> 1 D.
- **P2 :** 709, décomposer deux fois et inverser 1 C -> 10 D. Solution : `7 C + 0 D + 9 U = 6 C + 10 D + 9 U`; inverse 10 D -> 1 C.
- **P3 :** 192, décomposer deux fois et inverser 1 D -> 10 U. Solution : `1 C + 9 D + 2 U = 1 C + 8 D + 12 U`; inverse 10 U -> 1 D.
- **P4 :** 600, décomposer deux fois et inverser 1 C -> 10 D. Solution : `6 C + 0 D + 0 U = 5 C + 10 D + 0 U`; inverse 10 D -> 1 C.
- **Modalité :** aucune amorce algorithmique durant l'essai, mais tableaux de position vierges et matériel manipulable autorisés si leur usage est indiqué; conserver les deux écritures, l'échange inverse et une phrase ou des flèches expliquant l'équivalence.
- **Nouveaux contextes de maîtrise** (pas des répétitions de ces nombres) : bibliothèque à 486 livres et atelier de mosaïque à 257 pièces, items `q-007` et `q-008`, sans indices, à deux moments distincts.
- [05_PRATIQUE_AUTONOME.md](../contenu/05_PRATIQUE_AUTONOME.md) et [PLAN_EVALUATION.md](../evaluation/PLAN_EVALUATION.md).

## 7. Feedback et erreurs typiques

- `error-1` : transformer 1 dizaine en **1** unité. Dire : « Une bande en contient 10; dessine les dix points, puis recompte 100 H + 10 D + U. »
- `error-2` : confondre le chiffre et la valeur (`4` dizaines = 4). Faire la comparaison `4 D = 40 U` et recalculer les deux côtés.
- `error-3` : ignorer un zéro intérieur, `405` lu 450. Inscrire C=4, D=0, U=5, puis comparer 405 à 450.
- `error-4` : échanger 10 D -> 1 C tout en **gardant** les 10 D. Barrer physiquement les groupes utilisés; exiger conservation de la somme.
- `error-5` : proposer une deuxième écriture identique ou omettre l'échange inverse. Faire nommer l'échange avant la seconde ligne, puis flécher l'opération inverse.
- Toujours montrer le premier maillon incorrect et refaire un **cas différent** avant de recontrôler l'autonomie.

## 8. Évaluation formative et preuves

- **Famille unique :** `qc-pri-ma-003-ev-01`, `objectif_ref: obj-1`, `critere_ref: crit-1`; génération privilégiée `paramétrique_controle`, instanciée de manière déterministe; item fixe/scénario contrôlé permis pour garantir la diversité.
- **Trace minimale par item :** forme canonique (avec zéros); seconde décomposition numériquement équivalente issue d'un vrai échange; regroupement inverse explicite; vérification des deux totaux.
- **Deux preuves distinctes obligatoires :** `qc-pri-ma-003-q-007` (bibliothèque; centaine ↔ dizaines) et `qc-pri-ma-003-q-008` (mosaïque; dizaine ↔ unités), nouvelles données, aucun indice, occasions séparées; matériel neutre accepté si trace individuelle autonome.
- **Règle de décision :** chacune des deux preuves satisfait les quatre critères de [GRILLE_MAITRISE.md](../evaluation/GRILLE_MAITRISE.md), dont invariance de la quantité, échange + inverse et explication; un score global ne compense pas une erreur conceptuelle.
- **Banque :** 10 items verrouillés ou paramétrés par formules reproductibles; exemples contrôlés par tests locaux, statut `a_revoir` jusqu'à revue humaine.

## 9. Remédiation / enrichissement

- Si confusion U/D, reconstruire 10 jetons en une bande, puis écrire 10 U = 1 D; essai nouveau sur 153, puis retirer la bande.
- Si confusion D/C, échanger 10 bandes pour 1 plaque, puis calculer 10 × 10 = 100; nouveau 406.
- Si valeur non conservée, remplir le tableau « avant / après / somme » et signaler le premier terme modifié incorrectement.
- Si zéros difficiles, examiner 305, 500 et 709, avec colonnes C-D-U; zéro n'est pas une consigne de supprimer le rang.
- Si transfert difficile, raconter autrement l'histoire en conservant la même relation mathématique; ensuite transférer à une nouvelle quantité et à une autre modalité.
- **Enrichissement :** faire trouver trois décompositions de 348 (`3C4D8U`, `2C14D8U`, `3C3D18U`) et expliquer les deux inverses séparés; ne pas créer de nouvel objectif.
- [06_REMEDIATION_ET_TRANSFERT.md](../contenu/06_REMEDIATION_ET_TRANSFERT.md).

## 10. Accessibilité

- Offrir une version textuelle entièrement suffisante de chaque schéma; ne transmettre aucune information uniquement par couleur, image, son ou mouvement.
- Paroles, écriture, pointage d'un tableau, blocs physiques ou représentation tactile sont des modalités admissibles. Évaluer la **valeur**, les **échanges** et la **justification**, pas la vitesse d'écriture, l'orthographe ou la motricité.
- Lire une consigne à voix haute, permettre une transcription dictée ou agrandir les symboles; documenter l'aide. Pour une **preuve autonome**, ne pas donner d'indice sur les calculs ni choisir l'échange pour l'élève.
- Ne pas exiger internet, écran, marque de matériel ni communication de données personnelles.

## 11. Critères de sortie

1. Réaliser `crit-1` complètement sur **deux contextes distincts** : deux décompositions exactes du même nombre, regroupement inverse rétablissant la première, justification de la conservation.
2. Montrer autonomie sans indice mathématique sur les deux preuves; noter si la consigne a été lue, si le support est utilisé et si une erreur est auto-corrigée spontanément.
3. Interpréter correctement unités, dizaines, centaines, y compris un zéro de position ou un groupement non canonique.
4. Si une preuve échoue, localiser l'erreur et pratiquer un nouvel item; reporter la décision de maîtrise en attendant deux **nouvelles** preuves autonomes; ne pas conclure sur une seule note.
5. Revoir à **J+2 et J+7** (rappel différé, calendrier proposé et non imposé) : à J+2, transformer `2C3D5U` en `2C2D15U` et inverser; à J+7, `4C0D8U` en `3C10D8U` et inverser. Enregistrer exactitude et reprise éventuelle, sans ajouter de verrou au graphe.

## 12. Références pédagogiques et limites

- **Sources effectivement consultées dans l'archive :** `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`, `GRAPHE_PEDAGOGIQUE_202.json`, `authoring/ALIGNEMENT.md`, `authoring/BRIEF_REDACTION.md` et la famille JSON v1.2; traçabilité en [REFERENCES_CONTENU.md](../sources/REFERENCES_CONTENU.md).
- **Design pédagogique :** principes de modelage, entraînement et rappel empruntés à la gouvernance interne qui cite EEF, IES/WWC, CAST; **aucune consultation indépendante ni validation empirique de ces sites** n'est revendiquée.
- **Charte Québec :** discipline « Mathématique » uniquement; aucune conformité PFEQ, aucune homologation, aucun code officiel (valeur administrative : `null`).
- **Statut éditorial :** productions originales, exemples arithmétiques contrôlés localement; revue professionnelle des consignes, droits des adaptations, pilote utilisateur, contrôle LMS/Framework et publication non réalisés. Voir [VALIDATION.md](../livraison/VALIDATION.md).
