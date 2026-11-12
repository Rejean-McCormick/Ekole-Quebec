---
format: qc.learning-path/1.0
id: qc-pri-ma-015
titre: 'Nombres décimaux : représentations'
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Relier les écritures décimales aux décompositions en dixièmes et centièmes.
objectifs_secondaires: []
criteres_reussite:
- Représenter un même décimal par un dessin et une décomposition.
prealables_declares:
- qc-pri-ma-003
- qc-pri-ma-012
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-015-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-015`

**Discipline (appellation québécoise) :** Mathématique  
**Titre :** Nombres décimaux : représentations  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut de travail :** cours rédigé, items non qualifiés et revue humaine requise; l'en-tête YAML du blueprint est conservé à l'identique.

## 1. Intention et frontières

- `obj-1` — **Objectif observable immuable :** Relier les écritures décimales aux décompositions en dixièmes et centièmes.
- `crit-1` — **Preuve autonome immuable :** Représenter un même décimal par un dessin et une décomposition.
- L'élève lit, produit et justifie des nombres de 0,00 à 2,99 à deux chiffres décimaux au plus; il explicite l'unité et met en relation l'écriture à virgule, les dixièmes, les centièmes, un quadrillage et une droite graduée.
- Hors champ principal : calculs sur nombres décimaux, comparaison systématique de décimaux, arrondis, pourcentages et notation illimitée; `qc-pri-ma-016` et `qc-pri-ma-017` sont des successeurs du graphe, non du contenu à réécrire ici.
- Les deux préalables stricts restent `qc-pri-ma-003` (valeur de position) et `qc-pri-ma-012` (fraction-partage); un diagnostic positif peut prouver un acquis équivalent sans imposer leur consultation.

## 2. Notions et représentations

- **Unité :** un tout de référence, par exemple un carré entier de 10 × 10 cases ou une longueur entière de 1 mètre. Sans unité fixée, « 37 cases » ne donne pas une quantité décimale déterminée.
- **Décimal :** dans ce parcours, nombre écrivable avec une virgule et au plus deux chiffres décimaux, soit `N/100` avec `N` entier non négatif. Exemples : `0,7 = 0,70 = 70/100`, `1,26 = 126/100`. Le zéro terminal ne change pas la valeur.
- **Dixième :** une part égale parmi dix d'une unité (`1/10 = 10/100 = 0,1`). Sur une grille de 100 cases, une bande de 10 cases est un dixième.
- **Centième :** une part égale parmi cent d'une unité (`1/100 = 0,01`). Une case d'une grille de 100 cases est un centième.
- **Droite graduée :** ligne avec origine, unité de longueur constante et graduations régulières. Entre `0` et `1`, dix subdivisions égales marquent les dixièmes; chaque dixième peut être divisé en dix pour marquer les centièmes. Ne jamais déduire une valeur de distances non égales.
- Décomposition canonique : `N = 100u + 10d + c` en centièmes, avec `u = N // 100`, `d = (N % 100) // 10`, `c = N % 10`; valeur `u + d/10 + c/100`. Autres écritures équivalentes acceptées si elles sont justifiées (ex. `0,70 = 70/100 = 7/10`).
- **Progression concret → dessin → écriture :** bloc-unité et dix bandes de dix cases; quadrillage accessible à hachures et coordonnées; écriture `0,47 = 4/10 + 7/100`; droite de `0` à `1` placée à `47/100` de l'unité.
- **Exemple modèle A :** `0,36` = zéro unité, 3 dixièmes, 6 centièmes : colorier 3 bandes de 10 cases puis 6 cases distinctes; `30+6=36` cases sur 100, position 36/100 sur la droite.
- **Exemple modèle B :** `1,24` = une grille entière et 24 cases d'une deuxième; `1+2/10+4/100 = 124/100` ; sur la droite `1` à `2`, avancer de 24 centièmes après `1`.
- **Contre-exemple A :** une grille entière plus 24 cases ne vaut pas `0,24`, mais `1,24`.
- **Contre-exemple B :** « `0,5 = 5/100` » est faux : cinq dixièmes valent `50/100` et non cinq centièmes.
- Ressource détaillée et exemples dessinables : `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- Préalables du registre : `qc-pri-ma-003` et `qc-pri-ma-012`; aucun `recommends_before` ni `reinforces` pour cette feuille.
- `diag-1` — Dessiner une unité en dix parts égales : expliquer à quoi correspond `3/10`, puis montrer `30/100` sur grille de 100 cases. Attendu : 3 bandes ou 30 cases, même quantité.
- `diag-2` — Placer `0,4` sur une droite `0—1` partagée en dix parts égales; comparer par un dessin avec `0,04`. Attendu : 4e graduation sur 10 et quatre petites cases sur 100, **pas** la même grandeur.
- Examiner le regroupement en dizaines, les fractions de l'unité, la relation 10 centièmes = 1 dixième. Si les deux tâches sont expliquées sans guidage, le diagnostic peut attester des acquis équivalents même sans fréquentation documentée des préalables.
- Si échec : micro-remédiation sur l'unité partagée ou la position décimale; ne pas confondre absence de fichier historique et absence de compétence. Voir `contenu/02_DIAGNOSTIC.md`.

## 4. Enseignement guidé

- `teach-1` — Annoncer « Je peux montrer **le même nombre** par un quadrillage, une décomposition et sa place sur une droite. »
- Montrer une grille de 100 cases nommée « 1 unité ». Pour `0,36`, colorier trois bandes complètes puis six cases, prononcer « 3 dixièmes et 6 centièmes », écrire `3/10 + 6/100 = 36/100 = 0,36`.
- Modeler l'échange de dix cases individuelles contre une bande. Démontrer `0,30 = 0,3` sans ajouter d'unité fictive.
- Puis `1,24` avec deux grilles : tout le premier carré, deux bandes et quatre cases du second. Indiquer `1,24` sur une droite `1—2` correctement graduée.
- Vérifications fréquentes : « Où est le tout? », « Combien de cases pour un dixième? », « Pourquoi 0,4 et 0,04 ne se placent-ils pas pareil? ». Ne pas déclarer maîtrisé sur répétition orale seule.
- Déroulement rédigé dans `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- `guided-1` — Trois exercices à indices dégressifs : G1 `0,52` (grille préparée, rappel 10 cases = 1 dixième), G2 `0,07` (grille préparée, choix de l'unité à expliciter), G3 `1,40` (deux grilles vierges et droite, sans rappel immédiat).
- Pour chacun, produire dessin et décomposition; recevoir une question sur le premier changement de position ou de tout, pas seulement « faux ».
- Indices décroissants : G1 « 5 bandes puis 2 cases »; G2 « Quelle case représente 1/100 ? »; G3 uniquement « Que représente une grille entière ? » **si nécessaire**.
- Retirer les repères dès que l'élève organise lui-même les centièmes. Versions orales ou tactiles possibles avec une trace vérifiable.
- Corrigés détaillés : `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- `independent-1` — Quatre tâches A1–A4, données nouvelles : `0,68`, `1,05`, `0,90`, et « 2 unités, 3 dixièmes, 6 centièmes ». Pour chaque tâche, fournir un dessin de grille(s) et une décomposition numérique; A3 ou A4 inclut une droite graduée.
- Les aides ne sont pas données pendant la collecte de preuve. L'élève peut utiliser des grilles vierges, un outil accessible ou dicter ses choix de cases si le scripteur ne suggère pas les nombres.
- Critère : même quantité cohérente dans les deux représentations, unité stable et justification d'au moins un choix de dixième/centième.
- Deux preuves de maîtrise distinctes ne sont **pas** les exercices d'entraînement A1–A4 : M1 (motif de mosaïque à `1,26` unité) et M2 (ruban de `0,84 m`, longueur comme unité). Voir `contenu/05_PRATIQUE_AUTONOME.md` et `evaluation/PLAN_EVALUATION.md`.

## 7. Feedback et erreurs typiques

- Erreur « `0,8 = 8/100` » → demander de colorier huit bandes puis huit petites cases; compter `80` contre `8` cases. Essai de contrôle : `0,6`.
- Erreur « `0,05 = 5/10` » → rappeler qu'après la virgule le deuxième rang est celui des centièmes; montrer 5 cases sur 100 et 50 cases sur 100.
- Erreur de comptage/recouvrement d'une même case deux fois → utiliser des cases numérotées ou deux hachures distinctes sur bande et cases additionnelles; vérifier `10d+c`.
- Erreur de droite non proportionnelle → reprendre deux repères 0 et 1 séparés par dix segments égaux, subdiviser; ne pas positionner à l'œil sans échelle.
- Retour : identifier la première incohérence de valeur, faire reconstruire par la grille, obtenir une justification, puis transférer à un cas nouveau. Détails : `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Famille immuable :** `qc-pri-ma-015-ev-01`; objectif `obj-1`; critère `crit-1`; type préférentiel `paramétrique_controle`.
- Banque de 12 items : Q001–Q003 fixes d'ancrage, Q004–Q010 paramétriques à graines constantes et domaines de valeurs explicitement énumérés, Q011–Q012 scénarios contrôlés constituant les deux preuves finales indépendantes.
- Q011 : mosaïque à `1,26` unité — dessiner deux carrés de 100 cases, représenter une unité complète et 26 centièmes sur l'autre, écrire `1+2/10+6/100`.
- Q012 : ruban `0,84 m` — un segment-unité représentant `1 m` subdivisé en cent parts égales (ou grille correspondante); montrer 84 parts et écrire `8/10+4/100`; dessiner aussi ou documenter visuellement la partition.
- Définition de maîtrise : **deux manifestations satisfaisantes dans deux contextes**, avec production de dessin + décomposition et justification, sans indice de fond. La grille peut déclencher remédiation même si un total numérique serait élevé.
- Corrigés : calculs en centièmes entiers, vérifiés par un contrôle rationnel distinct; items demeurent `a_revoir` et exigent revue humaine et essai pédagogique. Consulter `evaluation/PLAN_EVALUATION.md`, `BANQUE_ITEMS.json`, `GRILLE_MAITRISE.md`.

## 9. Remédiation / enrichissement

- Si confusion entre dixième et centième, remplacer les symboles par une grille tactile : comparer 10 cases adjacentes et 1 seule case avant de recoder `0,1` et `0,01`.
- Si confusion sur partie entière, juxtaposer une grille complètement remplie avec une grille partielle; reprendre `1,02` puis `1,20`.
- Si fraction comprise mais droite échouée, travailler sur une bande de 100 unités de longueur égale, marquer chaque dixième et subdiviser une bande.
- Enrichissement sans modifier l'objectif : représenter `0,70`, `0,07`, `1,07` avec le même matériel; expliquer `0,30 = 0,3` par échange de dix centièmes contre un dixième.
- Transferts T1 mosaïque et T2 longueur de ruban, avec critères et réponses dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 10. Accessibilité

- Texte lisible et oralisation possible; grilles numérotées coordonnées `(rangée, colonne)` et contrastes par hachures ou symboles au lieu de dépendre des couleurs.
- Matériel : 100 jetons / 10 bandes, papier quadrillé, tableau tactile ou objets regroupés; droite avec marques régulières ou règle adaptée, supports manipulables fixés si besoin.
- Dessin peut être produit manuellement, par dictée des cases à une personne neutre ou avec interface de grille accessible. L'adulte retranscrit sans souffler la décomposition; on conserve l'autonomie mathématique.
- Autoriser plus de temps et une police adaptée; ne pas modifier l'unité ni fournir des indices conceptuels pendant la preuve sommative. Ne jamais attribuer une erreur de motricité fine à une méconnaissance des centièmes.

## 11. Critères de sortie

1. Montrer **le même décimal** par un dessin lisible avec unité spécifiée et par une décomposition exacte en unités, dixièmes et centièmes (`crit-1`).
2. Localiser ou expliquer au besoin sa position sur une droite régulièrement graduée et repérer pourquoi une représentation alternative est erronée.
3. Fournir **deux preuves indépendantes M1 et M2** dans des contextes distincts, dont une sans indices conceptuels (ici les deux sont sans indices); produire justification observable.
4. Selon la grille, atteindre au moins le niveau 2 sur chacun des critères essentiels pour chacune des deux preuves. Si ce n'est pas atteint, remédier à l'erreur précise puis recueillir de nouvelles preuves, jamais inférer une maîtrise sur moyenne ou âge.

## 12. Références pédagogiques et limites

- Sources internes consultées : normes v1.2 (contrat, générateur, charte), graphe, frame, alignement et brief. Traçabilité dans `sources/REFERENCES_CONTENU.md` (SHA-256 du fichier du workspace).
- Les énoncés arithmétiques, grilles et scénarios sont des constructions originales dérivées d'égalités rationnelles exactes. Aucun emprunt d'image, aucun dessin tiers.
- Le document `REFERENCES_EVIDENCE.md` du workspace liste EEF, IES/WWC et CAST comme repères de conception; ces liens externes ne sont pas présentés ici comme relus ou comme preuves directes de l'efficacité de cette feuille.
- Appellation « Mathématique » conservée selon la charte du Québec; aucune conformité PFEQ, année fixe, approbation ou code de cours officiel revendiqué.
- Révision humaine requise : précision didactique, lisibilité des supports tactiles, diversité des contextes, qualité des jugements d'évaluation et essai d'interface LMS. Aucun item qualifié de certifié ou publié.
