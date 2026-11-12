---
format: qc.learning-path/1.0
id: qc-pri-ma-028
titre: Aire et unités d’aire
discipline_code: MA
statut: redaction_complete_revue_requise
revision_contenu: 0.3.0
langue_contenu: fr-CA
resultat_principal: Mesurer ou calculer une aire en unités carrées adaptées.
objectifs_secondaires: []
criteres_reussite:
- Déterminer l’aire de figures quadrillées et expliquer la méthode.
prealables_declares:
- qc-pri-ma-023
- qc-pri-ma-025
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-028-ev-01
provenance_statut: references_documentees_et_contenu_original
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-028`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Aire et unités d’aire  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**État :** parcours et items rédigés, vérification mathématique automatisée effectuée; revue pédagogique humaine encore requise, non homologué au PFEQ.

## 1. Intention et frontières

- **`obj-1` (immuable) :** Mesurer ou calculer une aire en unités carrées adaptées.
- **`crit-1` (preuve immuable) :** Déterminer l’aire de figures quadrillées et expliquer la méthode.
- **Notions :** surface, quadrillage, unité carrée; compter sans double comptage, décomposer et choisir une unité.
- **Frontière :** figures quadrillées en cases entières et rectangles sur quadrillage uniforme, éventuellement composés; aucune formule avancée, aucun calcul d’aire pour contours irréguliers non quadrillés ni conversion d’unités non fondée sur une échelle.
- L’aire mesure une **surface intérieure couverte**, pas la longueur de son contour. Les proportions d’un dessin ne garantissent pas son échelle; une unité doit être précisée.

## 2. Notions et représentations

| Terme | Définition opérationnelle | Critère pour se contrôler |
|---|---|---|
| Surface | Partie plane occupée par une figure; l’**aire** est la mesure de l’étendue de cette surface. | On compte les cases *à l’intérieur*, non les bords. |
| Quadrillage | Réseau de lignes formant des cases; ici toutes les cases sont des carrés de même dimension. | Une case entière vaut **1 unité carrée du quadrillage**. |
| Unité carrée | Aire d’un carré dont le côté a la longueur d’une unité choisie. | Carré de côté 1 cm → 1 cm²; sans mesure de côté : écrire « unités carrées » (u²), jamais inventer cm². |

**Notation des figures textuelles :** `#` = case carrée entièrement occupée; `.` = case vide, chaque ligne est une rangée, le nombre de caractères par ligne est constant. Une figure peut être décomposée en rangées ou rectangles **disjoints**. Dans un rectangle de `l` colonnes × `h` rangées, `A = l × h × aire_d_une_case`; vérifier par addition répétée. Côté d’une case de 2 cm → aire d’une case = 2 × 2 = 4 cm², pas 2 cm².

**Exemple résolu E1, panneau :** `#### / #### / ####` (3 rangées de 4 cases) → `4+4+4=12 u² = 3×4 u²`. Si chaque case mesure 1 cm × 1 cm, `12 cm²`.

**Exemple résolu E2, figure en L :** `###. / #... / #...` → `3+1+1=5 u²`; également `3×1 + 1×2 = 5 u²`, en évitant de compter le coin deux fois.

**Contre-exemple C1 :** annoncer `14 cm` comme aire d’une figure de 3 × 4 cases de côté 1 cm, après comptage du contour (`2×(3+4)=14 cm`) est incorrect; l’aire est **12 cm²**.

**Contre-exemple C2 :** dire qu’un quadrillage de six cases de **côté 2 cm** a une aire de `6 cm²` est incorrect : `6×(2×2)=24 cm²`. Si aucune dimension physique de case n’est donnée, on peut seulement dire **6 u²**.

## 3. Préparation / diagnostic

- **Préalables `requires` stricts :** `qc-pri-ma-023` (figures planes et propriétés), `qc-pri-ma-025` (longueurs, masses et capacités). Compétence équivalente attestée par diagnostic = accès possible sans lecture imposée de ces Kristals. Aucun `recommends_before` ni `reinforces` sortant.
- **D1 — reconnaître une case carrée et l’unité :** « Dessine un carré sur un quadrillage régulier; si son côté vaut 1 cm, quelle aire compte une seule case ? » Réponse : `1 cm²`, explication `1 cm × 1 cm`. Observer reconnaissance du carré et de la longueur comme donnée distincte de l’aire.
- **D2 — lire une figure :** `##. / ###` ; demander l’aire en unités carrées et deux méthodes. Réponse : `2+3=5 u²`, ou rectangle 3×2 (=6) moins une case (=5). Un côté de case n’est pas fourni : ne pas écrire cm².
- **Décision :** D1 et D2 réussis avec explication → passer directement au guidage court ou à la pratique autonome; difficulté à reconnaître les figures → référence `qc-pri-ma-023`; confusion longueur/aire → renvoi `qc-pri-ma-025`. Jamais de blocage automatique si équivalence démontrée.

## 4. Enseignement guidé

- **`teach-1` — objectif explicite :** Mesurer ou calculer une aire en unités carrées adaptées.
- **Modelage concret :** poser 12 carrés identiques sans chevauchement pour recouvrir exactement un rectangle de trois rangées de quatre carrés; déplacer les pièces ne change pas le nombre de cases couvertes.
- **Modelage schématique :** tracer `#### / #### / ####`, pointer une rangée et écrire `4+4+4=12`.
- **Modelage symbolique :** `3×4=12 u²`; si les cases ont 1 cm de côté, `12 cm²`. Faire justifier la multiplication par les rangées réellement visibles.
- **Modelage composé :** `#### / #### / ##..` → `4+4+2=10 u²` ou `2×4+2=10 u²`. Chaque carré est compté une fois.
- **Contrôle :** « Pourquoi 4+4+2 ne vaut-il pas 12 ? » : la dernière rangée n’a que deux cases. « Pourquoi ne pas écrire cm² ici ? » : côté non spécifié.

## 5. Pratique accompagnée

- **G1, indices forts :** `### / ###` ; l’adulte montre les rangées et place une case témoin. Écrire `3+3=6 u²`, puis laisser l’élève refaire sans pointage.
- **G2, indices moyens :** `#### / ##.. / ##..` ; donner seulement « Compte par rangées OU par rectangles disjoints ». Solution `4+2+2=8 u²`, ou `2×3+2=8 u²`. Retirer ensuite le rappel des stratégies.
- **G3, indices minimaux :** `### / #.. / ###` ; proposer « Trouve l’aire et prouve ton résultat de deux façons ». Solution `3+1+3=7 u²`; aussi rectangle de 3×3 moins 2 cases = 7. Aucun indice pendant la seconde tentative.
- **Feedback** : faire préciser à quelle rangée le comptage diffère, demander une vérification addition/multiplication, puis reprendre avec un nouveau dessin; détaillé dans `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- **A1 :** rectangle 5×2, cases non graduées → `10 u²`, deux rangées de cinq.
- **A2 :** `###. / ##.. / .#..` → `3+2+1=6 u²`.
- **A3 :** rectangle 3×2, cases de côté 2 cm → `6×4=24 cm²`.
- **A4 :** rectangle 4×3 avec un trou de deux cases centrales distinctes → `12−2=10 u²`, jamais compter les vides.
- Chaque essai autonome comporte : réponse, unité, justification et contrôle avec une seconde stratégie; aucun indice sur le dénombrement pendant la réponse. Situations et corrigés développés dans `contenu/05_PRATIQUE_AUTONOME.md`.

## 7. Feedback et erreurs typiques

| Erreur observable | Détection | Réponse pédagogique et nouvel essai |
|---|---|---|
| Compter le contour | L’élève pointe les côtés, pas les cases. | « Que couvre-t-on ? » Colorier les cases pleines; refaire avec 2×5. |
| Double compter un angle d’un L | Somme des deux rectangles recouvrants. | Cercler l’intersection; découper en rectangles disjoints, puis recompter. |
| Compter les trous comme occupés | Aire égale au rectangle englobant. | Mettre un X sur les vides; utiliser `A_rectangle − A_vides`. |
| Écrire cm² sans connaître le côté de case | Unité physique inventée. | Garder `u²`, puis convertir seulement si dimension connue. |
| Prendre 2 cm pour 2 cm² | Aire d’une case confondue avec longueur du côté. | Dessiner le carré 2×2 de carrés de 1 cm²; constater 4 cm². |

## 8. Évaluation formative et preuves

- **Famille :** `qc-pri-ma-028-ev-01`; `obj-1`; `crit-1`; type natif **`paramétrique_controle`**.
- **Banque :** dix items `qc-pri-ma-028-q-001` à `-q-010`, dont paramètres entiers contrôlés par une table finie, une graine stable et `index = seed modulo N`. Les instances affichées, les résultats et tous les cas permis sont validés indépendamment au moment de la fabrication.
- **Maîtrise A :** `q-009`, planche rectangulaire d’une exposition, quadrillage de côté 1 cm → création d’un calcul **et** d’un regroupement par rangées, sans indices.
- **Maîtrise B :** `q-010`, jardinière quadrillée avec partie manquante, cases unitaires non métrées → compter par bandes disjointes ou rectangle moins trous, sans indices. Autre contexte et autre type de figure.
- **Maîtrise :** deux performances distinctes, exactes, avec unités justes et démarche explicite. Aucun total de points unique ne compense une réponse erronée dans l’une des deux preuves; `evaluation/GRILLE_MAITRISE.md` détaille décision/remédiation.
- **Statut :** toutes les questions restent `a_revoir`, sans certification ni homologation.

## 9. Remédiation / enrichissement

- Revenir au pavage de carrés identiques pour une confusion de surface, au coloriage du seul intérieur pour une confusion de périmètre, à la grille de cases 2×2 pour un côté de 2 cm, et au trait de séparation pour une somme double.
- Enrichissement sans nouveau préalable : figures de même aire mais de formes différentes; par exemple 2×6 et 3×4 occupent toutes deux `12 u²` avec des contours différents.
- **Transferts** : carreaux d’un tapis scolaire (quadrillage uniforme) et jardin partagé (forme composée) avec contraintes explicites; travaux du même Kristal uniquement.
- **Rappel différé** : à la séance suivante, mesurer sans aide `### / ### / #..` → `7 u²`; après quelques séances, un carré de côté 2 cm au milieu d’un pavage → `4 cm²` par case. Ce rappel ne remplace pas les deux preuves.

## 10. Accessibilité

- Figures fournies en grands caractères monospaces avec légende `#` / `.`, quadrillages épais ou relief tactile; alternatives en carrés manipulables identiques, description orale de chaque rangée, affichage numérique agrandissable.
- Réponses par écrit, pointage, dictée à un scribe non directif ou oral enregistré **uniquement avec consentement**; évaluer le calcul de l’aire, non la dextérité du tracé.
- Garantir même information géométrique, mêmes unités et mêmes critères dans chaque modalité; donner temps ajusté et aucun indice de solution pendant les deux épreuves.
- Ne pas supposer que la taille visuelle d’un dessin fixe la dimension réelle des cases. Vérifier le contraste et l’absence de confusion entre symbole `.` et case remplie.

## 11. Critères de sortie

1. Identifier correctement les cases occupées, y compris celles de figures composées et de figures avec trous.
2. Calculer exactement l’aire; produire une réponse dans **la bonne unité** (`u²`, `cm²` ou autre unité carrée explicitement donnée).
3. Expliquer une démarche vérifiable (somme des rangées, rectangles **sans chevauchement**, ou rectangle englobant moins les cases vides).
4. Produire **deux preuves autonomes** exactes dans les contextes différents A=`q-009` et B=`q-010`; si une seule est suffisante, remédier puis réévaluer avec cas parallèle vérifié.

## 12. Références pédagogiques et limites

- **Sources effectivement lues :** `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`, graphe 202, parcours/contrat/alignement/brief sources de `qc-pri-ma-028`.
- **Connaissances dérivées et vérifiées :** aire de cases entières par addition; `A_rectangle = colonnes × rangées × aire_case`; addition des ensembles disjoints; soustraction des trous intérieurs; conversion carré de côté 2 cm = 4 cm².
- **Créations originales :** dessins textuels, leçons, exemples, consignes, situations d’évaluation, cas paramétriques et rubriques. Provenance et droits dans `sources/REFERENCES_CONTENU.md`.
- **Limites :** cas volontairement bornés; revue humaine requise pour les aménagements, formulations, difficulté et usage sommatif; aucune correspondance détaillée au PFEQ ni validation de terrain revendiquée.
