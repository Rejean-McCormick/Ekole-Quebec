---
format: qc.learning-path/1.0
id: qc-pri-ma-024
titre: Droites, angles et symétrie
discipline_code: MA
statut: rédaction_complète_revue_humaine_requise
revision_contenu: 0.3.0
langue_contenu: fr-CA
resultat_principal: Identifier et construire des angles, des droites et des symétries simples.
objectifs_secondaires: []
criteres_reussite:
- Compléter une figure symétrique puis justifier la transformation.
prealables_declares:
- qc-pri-ma-023
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-024-ev-01
provenance_statut: documentation_et_exercices_originaux
auteur: role:architecture-pedagogique
reviseur: null
---
# Microparcours — `qc-pri-ma-024`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Droites, angles et symétrie  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** dossier d'enseignement et évaluations rédigés, corrigés testés automatiquement; revue humaine nécessaire avant qualification.

## 1. Intention et frontières

- **`obj-1` (immuable) :** Identifier et construire des angles, des droites et des symétries simples.
- **`crit-1` (preuve immuable) :** Compléter une figure symétrique puis justifier la transformation.
- Notions : **angle, parallélisme, perpendicularité, symétrie axiale**. Des points sur quadrillage de pas 1 servent de modèles mesurables; les coordonnées `(x;y)` identifient colonne et rangée. Une droite s'étend infiniment, mais on peut la représenter par un segment tracé.
- Domaine : droites parallèles ou perpendiculaires dans un plan, angle droit/aigu/obtus, réflexion par rapport à un axe horizontal ou vertical; constructions simples sur quadrillage et justification par distances perpendiculaires. Pas de symétrie centrale, de transformations composées ni de calcul trigonométrique.
- L'élève n'est pas sanctionné pour une qualité de trait liée à sa motricité si ses points, positions et relations sont corrects.

## 2. Notions et représentations

1. **Angle :** deux demi-droites de même origine forment un angle; l'origine est le sommet. Une ouverture de 90° est droite, moins de 90° aiguë, entre 90° et 180° obtuse. Une rotation de toute la figure ne change pas l'ouverture.
2. **Parallélisme :** deux droites distinctes d'un même plan qui ne se rencontrent jamais; sur grille, deux verticales `x=2` et `x=5` en sont un exemple. Deux segments qui n'ont pas de point commun ne prouvent pas, à eux seuls, le parallélisme de leurs droites porteuses.
3. **Perpendicularité :** deux droites qui se croisent à angle droit (90°). Une horizontale `y=4` et une verticale `x=6` sont perpendiculaires, même si leur intersection se situe au-delà des segments dessinés.
4. **Symétrie axiale :** réflexion dans une droite, l'axe; un point et son image se trouvent à distance égale de l'axe, sur une perpendiculaire à cet axe et de part et d'autre, sauf si le point est sur l'axe, auquel cas il reste fixe. Pour `x=6` : `(x;y) → (12−x;y)`; pour `y=6` : `(x;y) → (x;12−y)`.
5. Représentations : **matériel** (miroir manipulable ou feuille pliée), **schéma** (quadrillage avec axe, points et segments), **notation** (`A(2;3)`, `A′(10;3)`). Tout miroir/pliage est une aide exploratoire; seule la construction sur grille et sa justification établissent l'exactitude.

## 3. Préparation / diagnostic

- **Préalable strict `requires` : `qc-pri-ma-023`**, figures planes et propriétés. Le diagnostic peut attester l'équivalent et éviter de refaire automatiquement ce cours. Aucun `recommends_before`, aucun `reinforces` sortant. Les références n'autorisent aucune copie inter-Kristals.
- `diag-1` : identifier sommet et ouverture d'un angle dessiné par deux segments partant de `(2;2)`, l'un vers `(6;2)` et l'autre vers `(2;5)`; réponse : sommet `(2;2)`, 90°.
- `diag-2` : compléter sur axe vertical `x=6` le point `P(4;3)` et justifier; réponse : `P′(8;3)` puisque les distances horizontales à l'axe valent deux carreaux, à hauteur identique. Une figure plane simple à reconnaître permet aussi de constater le préalable.
- **Décision :** si les figures et leurs côtés/sommets sont compris, enseigner directement la géométrie cible. Sinon offrir une courte reprise sur points, segments et polygones sans créer une nouvelle dépendance bloquante.

## 4. Enseignement guidé

1. Concret : montrer une droite en prolongeant mentalement un bord droit, puis vérifier un angle droit avec le coin d'une feuille; comparer deux rails parallèles à deux droites qui se croisent.
2. Schéma : placer l'axe vertical `x=6`, puis `A(3;2)`, `B(4;5)`, `C(2;4)`; tracer des segments `AB`, `BC`, `CA`.
3. Modeler la réflexion **sommet par sommet** : `A′(9;2)`, `B′(8;5)`, `C′(10;4)`. Pour A, mesurer `6−3=3` à gauche puis `9−6=3` à droite; refaire pour B et C; relier A′B′C′ dans l'ordre.
4. Symbolique : `(x;y)→(12−x;y)`; constater que l'abscisse change et l'ordonnée reste identique. Vérification par repli, puis par arithmétique indépendante (milieu des segments `AA′`, etc., à `x=6`).
5. Contrôle de compréhension : demander pourquoi une translation de trois carreaux à droite **ne constitue pas** cette symétrie pour tous les sommets.

## 5. Pratique accompagnée

- **G1, soutien fort :** compléter `D(2;3)` par rapport à `x=6`, marques des six carreaux déjà tracées; réponse `D′(10;3)`, deux distances 4. Retirer les marques après correction.
- **G2, soutien moyen :** compléter `E(4;2)`, `F(4;5)` par rapport à `x=6`, axe et quadrillage visibles mais distances non indiquées; réponse `E′(8;2)`, `F′(8;5)`; les segments verticaux correspondants sont parallèles.
- **G3, soutien faible :** symétriser `G(1;3)`, `H(3;4)`, `I(4;2)` par rapport à `y=6` sans aide de procédure; réponse `(1;9)`, `(3;8)`, `(4;10)`. Donner l'indice « compare les distances perpendiculaires » seulement lors d'une remédiation ultérieure.
- Après chaque essai, expliquer la **première erreur** (mauvais axe, mauvais sens ou distance) et faire reconstruire avec d'autres coordonnées, pas recopier le corrigé.

## 6. Pratique autonome

- **A1 :** classer les paires `x=2` / `x=5` (parallèles), `x=3` / `y=4` (perpendiculaires), `y=1` / `y=7` (parallèles); donner la propriété justificative.
- **A2 :** sur axe `x=6`, réfléchir `M(4;5)`, `N(2;3)` → `M′(8;5)`, `N′(10;3)`; dessiner et expliquer distances 2 et 4.
- **A3 :** sur axe `y=6`, réfléchir les sommets `U(2;2)`, `V(5;2)`, `W(5;4)` → `(2;10)`, `(5;10)`, `(5;8)`; tracer les deux triangles.
- **A4 :** corriger la fausse réponse `P(3;5)→P′(9;4)` pour axe `x=6` : la bonne image est `(9;5)`, même ordonnée et distances horizontales égales (3).
- Ces réponses sont détaillées dans `contenu/05_PRATIQUE_AUTONOME.md`; aucune reprise d'un exemple identique comme preuve finale.

## 7. Feedback et erreurs typiques

| Erreur observable | Feedback descriptif | Reprise vérifiable |
|---|---|---|
| Compter le long de l'axe plutôt que perpendiculairement | « L'écart doit traverser l'axe à 90°. » | Pour `x=6`, garder `y` inchangé; contrôler distance gauche/droite. |
| Confondre translation et réflexion | « Les points ne sont pas tous déplacés dans le même sens : les positions de part et d'autre s'inversent. » | Tracer trois paires perpendiculaires à l'axe; calculer leurs milieux. |
| Voir deux petits segments séparés comme forcément parallèles | « Prolonge les droites porteuses : se couperaient-elles ? » | Comparer verticales, horizontales et droites sécantes. |
| Tenir compte de l'orientation du dessin pour nommer l'angle | « Mesure l'ouverture, pas l'inclinaison des côtés sur la feuille. » | Tourner la feuille et utiliser un gabarit d'angle droit. |
| Inverser un axe horizontal et vertical | « Sur `y=6`, c'est l'ordonnée qui change. » | Tracer les segments point-image et vérifier qu'ils sont verticaux. |

## 8. Évaluation formative et preuves

- Famille **`qc-pri-ma-024-ev-01`**, objectif `obj-1`, critère `crit-1`, mode préféré **`paramétrique_controle`**. Banque de **10 items** (4 fixes + 6 paramétriques déterministes). Contraintes calculées, seed fixe, correcteurs et cas d'essai décrits dans `evaluation/BANQUE_ITEMS.json`.
- **Preuve A `q-009`** : compléter un **motif triangulaire pour un panneau sur un quadrillage** par rapport à l'axe vertical `x=6`; justifier les trois paires de points et tracer la figure obtenue.
- **Preuve B `q-010`** : compléter une **ligne brisée de décoration** par rapport à l'axe horizontal `y=6`; recommencer de façon autonome, expliquer distances, perpendiculaires et la conservation de l'ordre des sommets.
- Les deux performances doivent être **distinctes, autonomes et suffisantes selon la grille**; l’autonomie fait l’objet d’un critère propre; pas de moyenne globale compensant une justification absente. Un diagnostic satisfaisant peut attester le préalable, pas remplacer les deux preuves finales.

## 9. Remédiation / enrichissement

1. Erreur de coordonnées : repérer colonne x et rangée y avec deux bandes ou pointeurs, puis reconstruire deux nouveaux points.
2. Axe mal identifié : fixer un repère `x=6` ou `y=6` et souligner la coordonnée qui **reste** constante sur la transformation.
3. Distances incorrectes : utiliser matériel déplaçable ou repli avant la formule; recommencer sur nouveau cas; retirer progressivement ces aides.
4. Absence d'argument : gabarit « axe…, distance…, coordonnée inchangée…, donc image… » à l'entraînement, puis retirer le gabarit à l'évaluation.
5. **Rappel différé :** séance suivante, redessiner un point-image sans modèle; quelques séances plus tard, compléter une petite figure selon l'autre orientation d'axe; noter persistance et réentraîner la seule dimension déficiente.

## 10. Accessibilité

- Dessins contrastés avec axe **étiqueté** `x=6` ou `y=6`, points nommés et repères lisibles; ne pas compter uniquement sur la couleur. Texte de description des coordonnées en complément de la grille visuelle, support tactile/relief si disponible.
- Autoriser règle, papier quadrillé agrandi, manipulables, prise de coordonnées dictée, clavier ou technologie d'assistance. L'adulte peut tracer fidèlement des points **dictés** sans fournir leur emplacement ni la démarche; documenter ce soutien.
- Les justifications peuvent être orales, tapées ou dictées, avec les mêmes relations géométriques. Éviter petites cases non lisibles ou exigence de traçage fin lorsque l'objectif est la relation spatiale.
- Pas de collecte d'image ou de données sensibles requise; prudence élémentaire avec règle/compas/outil de pliage, sans objets coupants.

## 11. Critères de sortie

1. Sur **deux contextes différents**, identifier l'axe, construire tous les points images exacts et les relier dans l'ordre imposé.
2. Justifier pour chaque sommet vérifié : segment point-image **perpendiculaire** à l'axe, distances **égales**, milieu situé sur l'axe; angle droit mentionné ou montré correctement.
3. Justification autonome sans indices sur les coordonnées et aucune erreur essentielle non corrigée; adaptations d'accès non directives autorisées.
4. Si une seule preuve est suffisante, ne pas inférer la maîtrise d'une note globale; appliquer la remédiation ciblée et refaire une tâche distincte.

## 12. Références pédagogiques et limites

- Sources primaires internes lues : contrat pédagogique v1.2, générateur et examens, charte de conversion, graphe 202, parcours et contrat de ce Kristal, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`.
- Référence géométrique vérifiée : **Math Is Fun**, « Reflection », `https://www.mathsisfun.com/geometry/reflection.html` (distances égales mesurées perpendiculairement à l'axe). Les représentations et exercices de cette livraison sont originaux et ne reproduisent pas ses illustrations.
- Référence d'accessibilité vérifiée : **CAST**, *UDL Guidelines v3.0*, options d'expression et de communication, `https://udlguidelines.cast.org/action-expression/expression-communication/`.
- Les règles de coordonnées pour axes `x=6`, `y=6` sont des déductions mathématiques, les scénarios, barèmes et jeux paramétriques des créations de ce dossier. Voir `sources/REFERENCES_CONTENU.md`.
- Aucun essai avec apprenants, aucune certification/validation psychométrique; revue pédagogique humaine et tests terrain encore requis. La nomenclature du Québec est conservée, sans homologation PFEQ revendiquée.
