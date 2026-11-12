---
format: qc.learning-path/1.0
id: qc-pri-ma-021
titre: Positions, déplacements et repérage
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Décrire un trajet ou une position au moyen de repères spatiaux stables.
objectifs_secondaires: []
criteres_reussite:
- Donner puis suivre un parcours spatial précis sans ambiguïté.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-021-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-021`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Positions, déplacements et repérage  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** contenu de cours proposé et instrumenté; revue humaine et qualification Framework requises. Les métadonnées du frontmatter v1.2 sont conservées, notamment `en_rédaction`, `alignement_statut: à_vérifier` et `revision_contenu: 0.2.0` (version initiale du blueprint, non homologation du texte).

## 1. Intention et frontières

- `obj-1` — **Résultat vérifiable immuable :** Décrire un trajet ou une position au moyen de repères spatiaux stables.
- `crit-1` — **Preuve autonome immuable :** Donner puis suivre un parcours spatial précis sans ambiguïté.
- Notions : **orientation**, **coordonnées simples**, **déplacement**, avec référence à un même repère.
- Une position seule (point final) ne prouve pas la capacité à communiquer *un parcours*. Il faut énoncer le départ, le cadre orienté, l'ordre des étapes et permettre à une autre personne de reproduire toutes les positions successives.
- Pas de préalables inter-Kristals; âge et niveau scolaire ne sont pas des critères de maîtrise. Le repérage porte ici sur une grille finie, pas sur des angles, GPS, systèmes de latitude, ou la programmation avancée.

## 2. Notions et représentations

- **Cadre commun :** grille carrée 6 × 6 de **points** repérés `x=1…6` (colonnes vers l'est), `y=1…6` (rangées vers le nord). Le nord est **en haut**; est à droite, sud en bas, ouest à gauche. Position notée `(x ; y)` : colonne d'abord, rangée ensuite; origine de comptage `(1 ; 1)` au sud-ouest. Les cases intérieures ne sont pas les points : chaque déplacement d'une unité rejoint le point voisin.
- **Orientation :** sens stable des quatre directions fixé par les flèches de la grille, **indépendant** de l'endroit où regarde une personne. `E`, `O`, `N`, `S` sont des noms de direction, non des ordres relatifs du type « tourne à gauche ».
- **Coordonnées simples :** paire ordonnée `(x ; y)` d'entiers de 1 à 6. `(2 ; 5)` ≠ `(5 ; 2)`; nommer un point sans convention d'axes est ambigu.
- **Déplacement :** `E1` augmente x de 1; `O1` diminue x de 1; `N1` augmente y de 1; `S1` diminue y de 1. `E3` = trois pas **successifs** `E1`, pas un saut diagonal. Les déplacements diagonaux et hors grille sont exclus.
- **Parcours complet :** `(départ ; repère ; commandes ordonnées ; trace des positions ; arrivée)`. Par exemple, `(2 ; 2) → E2 → N1` traverse `(3 ; 2)`, `(4 ; 2)`, `(4 ; 3)`. L'arrivée seule ne suffit pas, car plusieurs trajets peuvent y mener.
- **Trois supports équivalents :** pion sur quadrillage, liste de points reliés, suite de commandes en notation. Voir `contenu/01_NOTIONS_ET_EXEMPLES.md` pour deux modèles et des contre-exemples contrôlés.

## 3. Préparation / diagnostic

- Aucun `requires`, aucun `recommends_before` sortant, aucun `reinforces` sortant dans le cadre de ce Kristal; ne pas créer de verrou caché.
- **`diag-1` :** montrer un point `(3 ; 2)` puis demander ses coordonnées, puis faire expliquer comment le retrouver sur une grille vierge orientée identiquement. Critère : colonne avant rangée et axes fixes.
- **`diag-2` :** depuis `(2 ; 3)`, faire suivre `E2, N1` et noter chaque étape : `(3 ; 3)`, `(4 ; 3)`, `(4 ; 4)`. Demander si `N1, E2` donne le même **parcours** (non, malgré la même arrivée).
- Décision : si les deux tâches sont correctement justifiées, passer rapidement à une tâche autonome complexe; si erreur, enseigner la notion ciblée. Une réussite de diagnostic ne suffit pas à déclarer une maîtrise générale : deux preuves indépendantes demeurent exigées.

## 4. Enseignement guidé

- `teach-1` : établir et faire verbaliser la flèche du nord, les valeurs des axes et la convention `(colonne ; rangée)` sur une grille tactile/papier ou verbalement décrite.
- **Modelage concret :** pion au point `(2 ; 2)`; exécuter `E2, N1`, arrêter le pion à **chaque point** et décrire l'effet sur x ou y; contrôler que toutes les positions sont dans 1…6.
- **Schéma :** dessiner ou énumérer `(2 ; 2) → (3 ; 2) → (4 ; 2) → (4 ; 3)`. **Notation :** `E2, N1` et arrivée `(4 ; 3)`.
- **Contre-modèle :** `E2, N1` et `N1, E2` ont la même arrivée mais pas les mêmes points intermédiaires; ne pas confondre destination et parcours.
- **Contrôle verbal :** « Si je fais `O1`, quelle coordonnée change ? Et si je change l'orientation affichée du nord ? » Attendu : x diminue; un nouveau cadre doit être annoncé avant de réinterpréter les commandes.

## 5. Pratique accompagnée

- `guided-1` — Depuis `(1 ; 2)`, suivre `E2, N1`; **indice fort** : montrer axes et poser le premier pion `(2 ; 2)`; trace attendue `(1 ; 2),(2 ; 2),(3 ; 2),(3 ; 3)`.
- `guided-2` — Depuis `(4 ; 4)`, suivre `S2, O1`; **indice léger** : « note x puis y après chaque pas »; trace `(4 ; 4),(4 ; 3),(4 ; 2),(3 ; 2)`.
- `guided-3` — Depuis `(2 ; 5)`, rédiger puis exécuter le plus court trajet passant par `(5 ; 5)` avant `(5 ; 3)`; **sans indice initial**, à l'erreur « garde l'étape obligatoire ». Solution `E3, S2`; trace `(2 ; 5),(3 ; 5),(4 ; 5),(5 ; 5),(5 ; 4),(5 ; 3)`.
- Le soutien décroît de modelage partagé à simple vérification. Reprendre une nouvelle variante en cas d'aide substantielle; ne pas créditer comme preuve autonome.

## 6. Pratique autonome

- `independent-1` : quatre activités différentes dans `contenu/05_PRATIQUE_AUTONOME.md`, toutes avec résultats/grilles : lire un plan, exécuter une route, critiquer une route et en composer une.
- **Preuve A, bibliothèque :** sur une grille 6 × 6, partir de `(1 ; 2)` et atteindre `(4 ; 4)` par le comptoir `(4 ; 2)` en **5 pas exactement**; donner les commandes et les suivre point par point, sans indice. Solution minimale `E3, N2`.
- **Preuve B, robot de jardin :** départ `(2 ; 5)`, arrivée `(5 ; 5)`; points interdits `(3 ; 5),(4 ; 5),(3 ; 4),(4 ; 4),(3 ; 6),(4 ; 6)`; donner et suivre une route valide de **7 pas exactement**, sans indice. Solution `S2, E3, N2`.
- Changer de contexte et de modalité (plan de lieux vs planification de robot), pas les notions ni le seuil; conserver la trace de chaque prestation hors canon dans le LMS. Aucune correction au cours de la prestation.

## 7. Feedback et erreurs typiques

- **Inversion x/y :** demander « quelle colonne puis quelle rangée ? » et reprendre le point `(2 ; 5)` vs `(5 ; 2)`.
- **Direction relative « gauche/droite » :** pointer la flèche nord fixe, puis substituer `E/O` aux mouvements relatifs.
- **Saut non découpé :** arrêter le pion à chaque point sur un `E3`; un chemin doit rester sur la grille à chaque pas, pas seulement à l'arrivée.
- **Arrivée juste, chemin erroné :** comparer les listes successives de positions; réparer la première divergence avant de refaire une autre route.
- **Obstacle/hors grille :** barrer le point illégal, arrêter à la dernière position valide et recommencer avec une étape correcte. Ne pas conserver une note de maîtrise pour un trajet réparé avec aide.

## 8. Évaluation formative et preuves

- Famille invariante `qc-pri-ma-021-ev-01` ; `obj-1` ; `crit-1` ; mode familial `paramétrique_controle`.
- Banque de **11 items** : fixes, paramétriques à choix fermé et scénarios contrôlés. Les paramètres appartiennent à une table finie de cas avec seed entier et vérification des traces; aucune improvisation par IA lors de l'exécution.
- Les items 001–009 sont des observations formatives; 010 et 011 sont les deux preuves dans des contextes différents. Les items de composition exigent **donner** (communiquer un parcours) puis **suivre** (tracer/faire suivre) avec report exact des points visités.
- Succès de chaque preuve : départ/cadre/commandes sans ambiguïté, chaque pas légal, passage par point requis ou contournement d'obstacle, arrivée visée, trace reproductible et autonomie sans indices. Décision combinée fondée sur les **deux preuves**, jamais un pourcentage unique.
- Voir `evaluation/PLAN_EVALUATION.md`, `BANQUE_ITEMS.json`, `GRILLE_MAITRISE.md`. Statut des items : `a_revoir` jusqu'à validation humaine.

## 9. Remédiation / enrichissement

- Confusion axe : deux étiquettes « colonnes x / rangées y », puis retrait des étiquettes.
- Confusion de direction : rose des vents fixe, comparaison de déplacements `E1` vs `O1`.
- Séquençage : matérialiser chaque pas, puis rapprocher trace et commandes à l'oral; enfin transférer sur grille non annotée.
- Obstacle/bord : inspecter chaque nœud intermédiaire et non seulement l'arrivée; vérifier les quatre points voisins possibles.
- Enrichissement : expliquer pourquoi plusieurs chemins rejoignent le même point, pourquoi l'ordre compte, et comparer des chemins minimums avec ou sans zones interdites.
- **Rappel différé** à J+2 et J+7, sur versions inédites avec conventions annoncées; ce sont des reprises diagnostiques, non de nouvelles preuves automatiques.

## 10. Accessibilité

- Énoncer textuellement la grille et les repères; proposer grille agrandie à contraste suffisant, pion contrasté/tactile, coordonnées lues à voix haute ou braille selon besoins.
- Autoriser texte, schéma, matériel déplacé par l'élève ou instructions dictées à un scribe neutre; ne pas donner l'orientation, la route ni les corrections à la place de l'élève.
- Éviter l'exigence de déplacement physique réel; préférer plateau ou simulation sans risque. Les obstacles ne représentent que des points interdits sur un dessin fictif.
- Lors d'une adaptation, conserver : repère stable, séquence exacte, contraintes et absence d'indices mathématiques pour la maîtrise.

## 11. Critères de sortie

1. Exécuter et **communiquer** une suite de pas reproductible avec départ, nord fixe, conventions des coordonnées et trace des points intermédiaires.
2. Respecter les contraintes de grille, d'ordre, de passage et d'obstacles, puis expliciter pourquoi une route respecte ces conditions.
3. Réussir `q-010` et `q-011` à deux occasions sans indices, en contextes bibliothèque et robot; accepter une adaptation de modalité neutre.
4. Une erreur critique ou aide sur l'une des preuves => remédiation ciblée et **nouvelle** preuve analogue, sans déclarer la maîtrise sur la seule autre réussite.
5. Organiser un rappel différé J+2 et J+7 après la décision pour vérifier maintien/transfert sans modifier rétrospectivement les traces.

## 12. Références pédagogiques et limites

- Autorités de conception **internes consultées** : `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`, et métadonnées de ce workspace.
- Grille, définitions opérationnelles, exemples, tâches et cas paramétriques : **production originale** explicitée dans `sources/REFERENCES_CONTENU.md`. Validité arithmétique susceptible d'être contrôlée par calculs entiers; pertinence pédagogique soumise à revue.
- `ALIGNEMENT.md` reste inchangé : appellation québécoise conservée, aucune conformité, homologation, approbation PFEQ ni code officiel inventé.
- `AGENTS.md`, `kristal.workspace.json`, canon et registres restent inchangés. Aucun acte de build-v9, publication, activation ou validation auprès d'élèves n'est réalisé par ce delta.
