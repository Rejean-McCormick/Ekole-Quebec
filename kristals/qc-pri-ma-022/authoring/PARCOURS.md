---
format: qc.learning-path/1.0
id: qc-pri-ma-022
titre: Solides et représentations spatiales
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Reconnaître et décrire des solides grâce à leurs éléments constitutifs.
objectifs_secondaires: []
criteres_reussite:
- Associer une description à un solide et justifier à l’aide de ses propriétés.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-022-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-022`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Solides et représentations spatiales  
**Autorité interne :** `governance/Norme_Pedagogique_Autonome_v1.2/` (non déposée dans cette livraison)  
**Statut :** contenu rédigé et contrôlé techniquement, révision humaine requise avant qualification.

## 1. Intention et frontières

- `obj-1` — **Objectif observable immuable :** Reconnaître et décrire des solides grâce à leurs éléments constitutifs.
- `crit-1` — **Preuve autonome immuable :** Associer une description à un solide et justifier à l’aide de ses propriétés.
- **Notions :** face, arête, sommet, patrons. Enseigner les propriétés sur les polyèdres convexes suivants : cube, pavé droit non cubique, prisme droit à base triangulaire, pyramide à base carrée, tétraèdre.
- **Frontières épistémiques :** ne pas transférer arbitrairement la définition de face polygonale à une surface courbe; éviter de promettre qu'un nombre F/A/S identifiera toujours un solide unique. Le carré étant un rectangle, le cube est un pavé droit particulier.
- **Portée administrative :** ID Kristal interne; pas de déclaration d'homologation, d'équivalence au PFEQ ou de programme scolaire officiel.

## 2. Notions et représentations

**Définitions exploitables :**

1. **Face :** région polygonale plane délimitant un polyèdre. Un carré entier du cube est une face; la diagonale dessinée à l'intérieur n'en est pas une arête.
2. **Arête :** segment commun à deux faces du polyèdre; compter une seule fois chaque segment malgré ses deux faces voisines.
3. **Sommet :** point où se rejoignent au moins trois arêtes; le point milieu d'une arête n'est pas un sommet.
4. **Patron :** assemblage de faces dans le plan pouvant être replié sans lacune ni chevauchement pour former le polyèdre.

**Tableau contrôlable :** cube : F6/A12/S8 (6 carrés); pavé droit non cubique : F6/A12/S8 (6 rectangles, certains non carrés); prisme droit triangulaire : F5/A9/S6 (2 triangles et 3 rectangles); pyramide à base carrée : F5/A8/S5 (1 carré et 4 triangles); tétraèdre : F4/A6/S4 (4 triangles).

**Exemple résolu 1 :** deux triangles opposés et trois rectangles conduisent au prisme droit triangulaire : 5 faces; arêtes 3+3+3=9; sommets 3+3=6. Ce n'est pas une pyramide, qui n'a pas deux bases triangulaires.

**Exemple résolu 2 :** une base carrée, quatre triangles convergents : pyramide à base carrée, F=1+4=5, A=4+4=8, S=4+1=5. Le mot « pointe » ne suffit pas seul; la forme de la base discrimine.

**Contre-exemple 1 :** « cinq faces implique une pyramide » est faux, car le prisme triangulaire en a cinq. **Contre-exemple 2 :** six carrés en rectangle plein 2 × 3 ne forment pas un patron de cube; le pliage des faces impose des orientations incompatibles.

**Représentations :** maquette tangible → tracé schématique décrit en texte → tableau (F/A/S) et justifications. Une maquette, sa description neutre et son dessin doivent être concordants. Voir `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- **Prérequis stricts `requires` :** aucun. **Ordre recommandé non bloquant :** `qc-pri-ma-021`. Aucune référence de renforcement déclarée.
- `diag-1` : sur un cube, repérer face/arête/sommet, trouver F6/A12/S8 et exclure une diagonale intérieure de face; correction /4.
- `diag-2` : opposer « deux triangles et trois rectangles » et « un carré, quatre triangles vers une pointe »; identifier les deux solides et justifier par une propriété différenciante de chacun; correction /4.
- **Décision :** si 7–8/8 avec justifications fiables, permettre un itinéraire abrégé, mais obtenir quand même deux manifestations autonomes ultérieures; si 4–6, guider; si 0–3, manipuler et réenseigner les termes. Aucun accès n'est bloqué par le suivi de `qc-pri-ma-021`.
- **Mode d'accès :** textes lus intégralement à voix haute, éléments tactiles, ou copie agrandie, sans livrer l'indice de solution.

## 4. Enseignement guidé

- `teach-1` : annoncer explicitement l'objectif. Observer une boîte 2 × 3 × 5 (pavé non cubique) : 6 faces rectangulaires, 12 arêtes, 8 sommets; montrer pourquoi un triple numérique ne distingue pas le cube d'un pavé non cubique.
- Modéliser une pyramide carrée : une face carrée + quatre triangulaires, 8 arêtes et 5 sommets; comparer au prisme triangulaire qui a aussi cinq faces, mais 9 arêtes et 6 sommets.
- Construire le patron d'un cube en croix (4 carrés en bande, rabats haut/bas du deuxième); le comparer à un bloc 2 × 3 impropre au pliage.
- **Vérification formative :** « pourquoi la diagonale intérieure n'est-elle pas une arête? » (pas une frontière de deux faces), puis « quel indice distingue les deux solides à cinq faces? » (forme des faces et A/S).
- Verbaliser chaque étape avant de demander l'identification à l'élève; présenter au choix concret, schéma textuel, notation F/A/S.

## 5. Pratique accompagnée

- `guided-1`, aide forte : 1 carré + 4 triangles vers une pointe → pyramide à base carrée; surligner la base, montrer la pointe, décomposer A=4+4; retirer progressivement.
- `guided-2`, indice bref : boîte rectangulaire avec une face 2 × 5 et F6/A12/S8 → pavé droit non cubique; seul indice : « un cube a des faces carrées ». Exiger une justification et noter l'insuffisance des seuls nombres.
- `guided-3`, sans indice initial : comparer patron de cube en croix et bloc de six carrés 2 × 3. N'offrir une maquette de pliage qu'après l'essai; valider l'argument « ne se replie pas sans chevauchement ».
- **Rétroaction :** désigner précisément la première confusion (forme de base, frontière de faces, double décompte, patron), demander à l'élève de corriger, puis de réussir sur un *nouveau* solide.
- Voir `contenu/04_PRATIQUE_ACCOMPAGNEE.md` pour stimuli, indices gradués et solutions.

## 6. Pratique autonome

- `independent-1` : prisme droit triangulaire à partir de deux triangles et de trois rectangles, avec F/A/S=5/9/6 et deux justifications.
- `independent-2` : tétraèdre à quatre faces triangulaires, F/A/S=4/6/4, distingué de la pyramide carrée.
- `independent-3` : pavé droit non cubique (au moins une face 2 × 4), F/A/S=6/12/8 communs au cube; établir une propriété discriminante.
- `independent-4` : identifier parmi une croix de six carrés et un rectangle 2 × 3 le patron pouvant former un cube, argumenter par le pliage.
- **Consigne générale :** sans indices, avec description ou maquette neuve, nom du solide + décomptes pertinents + deux propriétés. Corrigés disponibles après remise dans `contenu/05_PRATIQUE_AUTONOME.md`. Trace enregistrée par le système d'apprentissage, non par la couche canonique.

## 7. Feedback et erreurs typiques

- **Double comptage** des segments : une arête appartient à deux faces mais compte une fois; recompter 9 arêtes sur un prisme triangulaire.
- **Diagonale prise pour une arête :** elle n'est pas commune à deux faces; vérifier un cube annoté.
- **Sommet confondu avec un point du dessin :** seuls les coins structuraux, par exemple les 5 de la pyramide carrée, comptent.
- **F=5 considéré comme suffisant :** opposer pyramide carrée F5/A8/S5 et prisme triangulaire F5/A9/S6.
- **Cube déduit de 6/12/8 :** comparer une face de 2 × 4 à un carré; cube et pavé non cubique ont les mêmes comptes.
- **Patron validé par simple nombre de faces :** tester une croix de cube contre 2 × 3; le second arrangement ne se replie pas correctement.
- Demander justification révisée + second cas équivalent, sans recycler mot pour mot la réponse modèle. Guide dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Famille immutable :** `qc-pri-ma-022-ev-01`. **Objets :** `obj-1` et `crit-1`.
- **Mode préféré :** `paramétrique_controle` : sélection de cas dans des corpus finis documentés, modulo sur seeds entières et corrigés tabulés/testés; pas de génération d'énoncés par IA sans contrôle.
- **Banque :** 12 items, dont items paramétriques `q-007`, `q-008`, `q-009` avec variables, contraintes, algorithmes, graines et échantillons vérifiables; tous `validation_status: a_revoir`.
- **Deux preuves autonomes obligatoires :** `q-011` (scénographie d'un musée : prisme triangulaire) et `q-012` (fabrication d'un objet-lumière : pyramide carrée), dans deux séances/contextes différents sans feedback intercalaire révélant la solution de l'autre épreuve.
- **Critères :** choix correct sur description, au moins deux propriétés pertinentes dont une discriminante, compte F/A/S vérifiable, correspondance schéma/patron quand demandé; grille descriptive à 4 niveaux. Les deux preuves sont observées séparément : jamais de maîtrise conclue sur une moyenne unique.
- **Document de référence :** `evaluation/PLAN_EVALUATION.md`, `evaluation/BANQUE_ITEMS.json`, `evaluation/GRILLE_MAITRISE.md`.

## 9. Remédiation / enrichissement

- **Erreur de terme :** maquette à grands reliefs; marquer face, arête, sommet, puis reporter sur un second polyèdre.
- **Erreur de comptage :** lister chaque face/segment/coin une fois; comparer au patron; tester le théorème de contrôle F+S=A+2 seulement pour ces polyèdres convexes, sans en faire un raccourci de reconnaissance.
- **Erreur de patron :** replier une représentation papier de la croix; comparer à la disposition 2 × 3; expliquer pourquoi le nombre de carrés est insuffisant.
- **Enrichissement :** décrire un autre patron valide de cube en le testant physiquement ou par un logiciel validant les orientations; ne pas conclure sur un dessin non testé. Transferts d'entraînement : colis triangulaire et toit de kiosque (`contenu/06_REMEDIATION_ET_TRANSFERT.md`).
- **Rappel espacé :** +2–3 jours (termes), +7–10 jours (prisme/pyramide), +3–4 semaines (patron et raisonnement), sans modèle sous les yeux.

## 10. Accessibilité

- Multimodalités équivalentes : description écrite lue à voix haute, objets réels en carton/textures, pièces à arêtes en relief, schéma agrandi à contraste suffisant, restitution orale enregistrée et transcrite.
- Ne jamais évaluer la précision du découpage, la dextérité, la rapidité motrice, la perception de couleur ou la capacité de dessiner en perspective : ces aptitudes ne sont pas l'objectif.
- Pour les patrons, permettre le pliage d'une copie pré-découpée ou une démonstration commentée; recueillir les mêmes raisons géométriques. Ne pas confondre aide physique neutre et indication de la réponse.
- Sécurité : aucun objet coupant requis; s'il y a ciseaux, supervision adaptée; protection des données dans le LMS, pas d'information d'élève dans le ZIP.

## 11. Critères de sortie

- **`crit-1` immuable :** Associer une description à un solide et justifier à l’aide de ses propriétés.
- **Preuve A (`q-011`) :** musée, solide choisi, propriété des deux bases et décompte exact, choix correct de patron. **Preuve B (`q-012`) :** luminaire, base carrée + quatre triangles, décompte exact, description du patron.
- **Maîtrise interne proposée :** sur **chacune** des deux preuves, identification exacte, au moins deux arguments justes dont un discriminant, F/A/S exacts et argument de patron correct; sans aide sur le raisonnement. Une tâche manquée ou justifiée au hasard déclenche une reprise ciblée et une nouvelle preuve distincte.
- **Décision :** « maîtrise attestée localement » seulement après deux manifestations autonomes cohérentes; sinon « en consolidation » ou « données insuffisantes ». Revue humaine des grilles avant publication.

## 12. Références pédagogiques et limites

- **Documents internes effectivement consultés :** `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`; `registry/GRAPHE_PEDAGOGIQUE_202.json`; `authoring/ALIGNEMENT.md`, `BRIEF_REDACTION.md`, versions d'origine de `PARCOURS.md` et `CONTRAT_PEDAGOGIQUE.json`.
- **Autorité des exemples :** raisonnement géométrique mathématiquement reproductible (comptage des faces/segments/sommets) et créations inédites; voir `sources/REFERENCES_CONTENU.md` pour distinction entre matériau lu, démonstration dérivée et textes originaux.
- **Limites :** matériel cartonné à essayer avec des élèves, lecture de l'accessibilité et contrôle humain des textes et rubriques requis. Tests automatisés des JSON, des triplets et du ZIP ne constituent ni qualification institutionnelle ni validation psychométrique.
- **Correspondance Québec :** `authoring/ALIGNEMENT.md` laissé inchangé. Aucune attribution à une année scolaire, homologation ou conformité PFEQ revendiquée.
