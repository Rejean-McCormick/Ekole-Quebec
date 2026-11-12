---
format: qc.learning-path/1.0
id: qc-pri-ma-032
titre: Probabilités et événements aléatoires
discipline_code: MA
statut: en_révision_pédagogique
revision_contenu: 0.3.0
langue_contenu: fr-CA
resultat_principal: Décrire des événements en termes de possibilité et de chance relative.
objectifs_secondaires: []
criteres_reussite:
- Classer des événements et expliquer les conditions du classement.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-032-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-032`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Probabilités et événements aléatoires  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** contenu développé, soumis à revue pédagogique humaine; ni publié ni certifié.

## 1. Intention et frontières

- **`obj-1` — objectif observable IMMUTABLE :** Décrire des événements en termes de possibilité et de chance relative.
- **`crit-1` — preuve autonome IMMUTABLE :** Classer des événements et expliquer les conditions du classement.
- **Concepts :** certain, impossible, probable, hasard; vocabulaire de soutien : possible, plus/moins/aussi probable et issue.
- **Frontière :** toutes les comparaisons numériques sont faites à l'intérieur d'une expérience décrite, avec des issues élémentaires équiprobables explicitées (jetons identiques, secteurs égaux, cartes indiscernables). Sans ces hypothèses, comparer les simples nombres d'issues ne suffit pas.
- **Convention d'enseignement :** ici, quand « probable » est opposé à « peu probable », un événement a plus d'une chance sur deux (strictement plus de la moitié des issues équiprobables). Si une chance sur deux, dire « aussi probable que son contraire ». « Certain » = toutes les issues; « impossible » = aucune; « possible » = au moins une. Une forte probabilité inférieure à 1 n'est pas une certitude.
- **Hors cible :** déduire le prochain résultat d'un tirage, inférer des chances à partir de préférences, apprendre la notation formelle de probabilité comme préalable, prédire avec certitude un événement aléatoire.

## 2. Notions et représentations

- **Hasard :** incertitude du résultat particulier avant une expérience aléatoire; les conditions permettent néanmoins d'étudier les issues possibles.
- **Certain :** événement qui se réalise quelle que soit l'issue admissible (toutes les issues favorables; `n/N=1`).
- **Impossible :** événement qui ne peut survenir parmi les issues admissibles (aucune favorable; `n/N=0`).
- **Probable :** dans les exercices à issues équiprobables, événement strictement majoritaire (`n > N/2`); son opposé est alors moins probable, sans être nécessairement impossible.
- **Possible mais non certain :** `0 < n < N`. « Aussi probable » si deux événements disjoints ou contraires ont le même nombre d'issues favorables sous équiprobabilité.
- **Représentation graduée :** pochette réelle de jetons dénombrables → tableau « couleur/effectif » ou schéma de cases textuellement étiquetées → comparaison `favorables/total` (notation facultative, jamais obstacle à la preuve orale).
- **Exemple repère :** 5 jetons verts et 2 blancs, tirage d'un jeton après mélange : vert `5/7`, blanc `2/7`, jaune `0/7`, vert ou blanc `7/7`. Vert probable, blanc possible mais moins probable, jaune impossible, vert ou blanc certain.
- **Contre-exemple :** « Vert est certain parce qu'il y en a beaucoup » est faux : deux blancs restent possibles. Voir `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- **Préalables bloquants (`requires`) :** aucun (`[]`). **Ordre conseillé :** aucun (`[]`). **Renforcement/transfert répertorié :** aucun (`[]`).
- **`diag-1` :** boîte transparente de 4 cubes rouges et aucun bleu; un cube est pris au hasard. Classer « rouge » et « bleu »; expliquer par les cubes présents. Attendu : rouge certain, bleu impossible.
- **`diag-2` :** 3 cartes « étoile » et 1 « rond » de même taille, mélangées; en tirer une. Quel symbole a le plus de chances? Un rond est-il impossible? Attendu : étoile plus probable (3 contre 1), rond possible (1 carte).
- **Équivalence :** si les deux diagnostics sont justes, justifiés sans aide et transposés à un schéma, autoriser une évaluation nouvelle sans refaire toute la leçon. Sinon pratiquer le maillon manquant. Oral, pointage ou manipulation sont admis avec observation enregistrée.

## 4. Enseignement guidé

- **`teach-1` :** annoncer « Je décris ce qui peut ou ne peut pas sortir et j'explique lequel a plus de chances ». Montrer 3 jetons « A » et 1 « B » identiques, sauf l'étiquette.
- **Concret :** compter 4 jetons; chaque jeton a la même chance d'être tiré si mélange adéquat et tirage à l'aveugle.
- **Schéma :** `A | A | A | B`; entourer les 3 « A » et la case « B »; demander si « B » reste réalisable.
- **Symbolique facultatif :** A a 3 issues sur 4; B en a 1 sur 4; A plus probable, aucun des deux n'est certain, C impossible et « A ou B » certain.
- **Modelage verbal :** « Je connais toutes les possibilités; je compare les cas favorables; je classe; je justifie avec les conditions ». Ne pas interpréter un tirage isolé comme démonstration de chance relative.
- **Contrôle :** « Est-ce que 3 sur 4 rend A certain? Explique en nommant l'autre issue ». Réponse : non, B peut encore sortir.
- **Référence :** `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- **`guided-1` (appuis complets) :** 2 blancs et 2 noirs : classer blanc, rouge, blanc ou noir; cases dessinées et rappel « compte les possibles ». Attendu : blanc possible et aussi probable que noir; rouge impossible; blanc ou noir certain.
- **`guided-2` (indice léger) :** roue de 6 secteurs égaux `P,P,P,P,O,O` : comparer P/O, dire si O impossible; enseignant demande seulement « Que comptes-tu? ». Attendu : P plus probable (4/6 contre 2/6), O possible.
- **`guided-3` (indice retiré) :** 5 billets numérotés 1 à 5 : classer nombre supérieur à 5, nombre de 1 à 5, nombre pair; expliquer. Attendu : impossible, certain, possible (2/5) mais moins probable que impair (3/5).
- **Retrait progressif :** schéma + questions → question stratégique unique → aucune aide avant réponse. Marquer le recours à l'indice; ne pas compter comme preuve autonome.
- **Remédiation sur place :** si confusion, reconstruire la liste des issues et vérifier si l'événement en couvre aucune, certaines ou toutes. Voir `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- **`independent-1` :** quatre tâches inédites, avec contextes de boutons, cartes, roue et bibliothèque, dans `contenu/05_PRATIQUE_AUTONOME.md`.
- **Production :** classement exact **et** conditions énoncées (composition complète, chances égales, effectifs/secteurs concernés); comparer des chances relatives quand la consigne l'exige.
- **Situation de preuve :** sans indice relatif à la réponse, nouvel ensemble d'objets, réponse orale enregistrée/transcrite, écrite ou tableau pointé puis justifié. Les aides d'accès (lecture d'une consigne, grossissement, objets tactiles étiquetés) restent possibles.
- **Trace :** uniquement dans la plateforme de suivi pédagogique; aucune donnée d'élève inscrite dans un fichier canonique.

## 7. Feedback et erreurs typiques

- **`error-1` — probable vs certain :** « 4 bleus et 1 rouge ⇒ bleu certain » : faire pointer le rouge encore accessible.
- **`error-2` — improbable vs impossible :** « 1 jaune parmi 8 ⇒ impossible » : relever l'issue jaune existante; distinguer rareté et impossibilité.
- **`error-3` — un tirage vs chance :** « J'ai tiré rouge une fois, donc rouge est le plus probable » : revenir à la composition **avant** le tirage.
- **`error-4` — dénombrement biaisé :** comparer 3 rouges vs 2 bleus dans des jetons de tailles différentes sans condition de tirage : expliciter/contrôler l'équiprobabilité avant de compter.
- **`error-5` — égalité ignorée :** 3 blancs, 3 noirs ≠ « blanc probable » au sens de majorité; dire « chances égales ».
- **Feedback :** faire repérer la première hypothèse fautive, corriger avec représentation, puis vérifier sur des nombres changés; voir `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Famille immuable :** `qc-pri-ma-032-ev-01`, `objectif_ref: obj-1`, `critere_ref: crit-1`; mode privilégié `paramétrique_controle`.
- **Banque :** 12 items utilisables : 8 paramétriques déterministes avec domaine et seed, 4 fixes; toutes les instanciations mathématiques ont des corrigés à contrôler par tests.
- **Deux preuves autonomes distinctes :** `qc-pri-ma-032-q-010` (jetons dans un sac de classe) et `qc-pri-ma-032-q-011` (roue de jeu à secteurs égaux), avec classement et raison, sans indices.
- **Critères :** exactitude des classes, énoncé des conditions, comparaison justifiée de chances, transfert sans indice. Deux manifestations suffisantes et cohérentes dans deux contextes différents requises; aucun score unique ne suffit.
- **Statut :** items `a_revoir` jusqu'à validation humaine. Voir `evaluation/PLAN_EVALUATION.md`, `BANQUE_ITEMS.json`, `GRILLE_MAITRISE.md`.

## 9. Remédiation / enrichissement

- **Certain/impossible :** une boîte contenant seulement 3 verts; tester « vert » et « bleu » avant de passer à des mélanges.
- **Possible/plus probable :** 4 rouges + 1 noir, puis 1 rouge + 4 noirs; comparer les cases, sans tirer, pour observer le renversement.
- **Chances égales :** 2 étiquettes X + 2 étiquettes Y, puis 3 + 3; expliciter égalité sans en déduire certitude.
- **Préjugé du résultat précédent :** répéter mentalement une expérience *avec remise* : chaque nouveau tirage retrouve la même composition; vérifier par le modèle, pas par série de tirages.
- **Enrichissement :** discuter pourquoi une roue à secteurs **inégaux** ne peut se comparer seulement en comptant les secteurs.
- **Transferts :** billets de bibliothèque et choix d'une case dans une application fictive, `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 10. Accessibilité

- Représenter chaque issue par une **lettre, un nom et un effectif**; couleur jamais seule source de sens. Décrire toutes les cases oralement; fournir gros caractères et objets tactiles comparables.
- Autoriser réponse orale, dictée à un adulte, tableau accessible ou choix de cartes de classement + justification; même exigence de raisonner sur les possibilités.
- S'assurer que les objets sont identiques au toucher si l'expérience suppose l'équiprobabilité; autrement utiliser un tableau théorique explicite et ne pas simuler un hasard biaisé.
- Aucun exercice n'exige de divulgation personnelle, de pari, d'argent réel ou de résultat d'une expérience risquée.

## 11. Critères de sortie

1. `crit-1` : Classer des événements et expliquer les conditions du classement.
2. Distinguer sans hésitation **aucun/tous/quelques** cas favorables, puis **majorité/égalité/minorité** si chances égales.
3. Réaliser deux démonstrations cohérentes, sur sac et roue (ou équivalents contrôlés), dont au moins une entièrement autonome, avec conditions observables et explication correcte.
4. Faire une courte tâche de rappel différé à J+7 sur un contexte nouveau : classer sans support initial, puis comparer à sa propre explication antérieure. En cas d'instabilité, reprendre seulement le concept en cause.
5. Décision consignée avec grille et preuves; pas de certification automatique sur score.

## 12. Références pédagogiques et limites

- **Autorité interne :** `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` et `GENERATEUR_ET_EXAMENS.md`, lus dans le bundle; `CHARTE_CONVERSION_QC.md` uniquement pour l'appellation.
- **Sources et statut de vérification :** `sources/REFERENCES_CONTENU.md`. Les explications, tâches et cas sont des productions originales; les propriétés mathématiques sont dérivées du dénombrement d'issues équiprobables.
- **Présentation Québec :** `authoring/ALIGNEMENT.md` maintenu tel quel dans l'archive maîtresse; aucune revendication de conformité au PFEQ, d'homologation ni de code administratif.
- **Validation encore requise :** revue d'enseignant, test d'utilisabilité et d'accessibilité avec le public cible, intégration sur plateforme LMS; statut `a_revoir`.
