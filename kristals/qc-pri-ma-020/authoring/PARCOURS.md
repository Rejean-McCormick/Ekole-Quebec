---
format: qc.learning-path/1.0
id: qc-pri-ma-020
titre: Situations-problèmes multiplicatives
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Modéliser une situation multiplicative ou de partage et contrôler la solution.
objectifs_secondaires: []
criteres_reussite:
- Construire une représentation et résoudre un problème multiplicatif inédit.
prealables_declares:
- qc-pri-ma-008
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-020-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-020`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Situations-problèmes multiplicatives  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** contenu rédigé, calculs contrôlés, à revoir pédagogiquement; ni publié ni certifié.

## 1. Intention et frontières

- `obj-1` — **Résultat vérifiable :** Modéliser une situation multiplicative ou de partage et contrôler la solution.
- `crit-1` — **Preuve autonome inchangée :** Construire une représentation et résoudre un problème multiplicatif inédit.
- Un modèle relie **quantités, unités, opération et interprétation**. L'élève ne gagne pas la maîtrise par une réponse isolée, même juste.
- Quatre familles de problèmes : (a) groupes égaux et multiplication; (b) proportion simple à rapport constant entier; (c) partage équitable; (d) groupement avec ou sans reste. On n'enseigne pas ici des rapports fractionnaires complexes ni la division décimale.
- Chemin pédagogique : diagnostic → modelage en objets et dessins → équations → justifications → deux preuves sur situations inédites → rappels différés.

## 2. Notions et représentations

1. **Groupes égaux :** pour `g` groupes de `p` objets, total `T = g × p`, en précisant « objets par groupe ». Exemple : 5 plateaux de 4 muffins → 20 muffins. Des groupes de tailles différentes ne peuvent pas être traités comme `g × p` sans transformation justifiée.
2. **Proportion simple :** si chaque unité contient exactement `p` unités de l'autre grandeur, alors `T(g)=p × g`; le rapport `T/g=p` est constant lorsque `g>0`. Exemple : 3 crayons dans chaque étui, 7 étuis → 21 crayons; ce n'est pas une formule valable si le nombre de crayons par étui varie.
3. **Quotient :** pour `N` objets et `d>0` parts égales, le quotient entier `q = ⌊N/d⌋` est la quantité entière par part ou le nombre de groupes complets, selon la question.
4. **Reste :** Dans une division euclidienne, `r=N−dq`, avec `0≤r<d`. Il signifie des objets non placés en groupes complets; il faut dire ce qu'on en fait. 23 livrets en paquets de 5 → 4 paquets complets et 3 livrets; pour les transporter tous, il faut 5 paquets, dont un incomplet.
- **Traductions :** jetons/paquets → rectangles ou barres légendés → écriture numérique avec unités → vérification inverse (`g×p=T`, `dq+r=N`).
- Exemples résolus avec matériel et schémas : `contenu/01_NOTIONS_ET_EXEMPLES.md`. Le zéro et le cas `r=0` sont explicités; toute division par zéro est interdite.

## 3. Préparation / diagnostic

- **`requires` :** `qc-pri-ma-008`, sens et stratégies de la multiplication; acquittable par le diagnostic d'une compétence équivalente, sans lecture forcée du Kristal.
- **`recommends_before` non bloquant :** `qc-pri-ma-009` pour le langage des partages. Aucun renforcement/transfert requis dans le graphe.
- `diag-1` : « Quatre rangées de six jetons : calcule et dessine autrement. » Attendu : 24, quatre groupes identiques ou rectangle `4×6`; la deuxième représentation montre la compréhension.
- `diag-2` : « Répartis 17 jetons dans quatre enveloppes, autant que possible. » Attendu : 4 dans chacune et 1 restant; `4×4+1=17`. Pour ne pas pénaliser l'élève débutant, un essai concret est permis.
- Décision : si multiplication non comprise, reprendre avec `qc-pri-ma-008`; si partage incompris mais groupes corrects, poursuivre avec des jetons et référence facultative `qc-pri-ma-009`. Si les deux sont manifestement acquis, raccourcir le modelage et proposer l'autonomie.

## 4. Enseignement guidé

- `teach-1` : « 6 trousses de 4 crayons → combien de crayons? » Lire la quantité/unité, représenter six groupes de quatre, écrire `6×4=24 crayons`, contrôler en additionnant six fois 4.
- Deuxième modelage : « 26 cartes, pochettes de 6 : nombre de pochettes **complètes** ? » Dessiner quatre paquets de six et deux cartes isolées, puis `26=6×4+2`; contrôler `0≤2<6`. Si on demande des pochettes pour **toutes** les cartes, il en faut cinq, dont une incomplète : le sens de la question commande la réponse.
- Comparer multiplication « connaître la taille des groupes, trouver total » et division « connaître le total et la capacité, trouver les groupes ».
- Questions de contrôle oral : « Que signifie le 4 dans `6×4` ? », « Pourquoi les 2 cartes ne font-elles pas un paquet complet ? », « Est-ce que 4 pochettes suffisent pour tout ranger ? ». Exiger les unités.

## 5. Pratique accompagnée

- `guided-1` : 3 boîtes de 8 pastels, total? Indice complet : entourer trois paquets, légender 8 par paquet, choisir multiplication. `3×8=24 pastels`.
- `guided-2` : 5 dossiers de 7 pages, total? Indice réduit : dessiner seulement cinq barres égales puis écrire l'égalité. `5×7=35 pages`.
- `guided-3` : 29 perles réparties dans des sachets de 6; nombre de sachets complets et reste? Aucun dessin fourni; demander un schéma, `29=4×6+5`; quatre sachets complets, cinq perles seules. Pour emballer toutes les perles, un cinquième sachet est nécessaire. Voir `contenu/04_PRATIQUE_ACCOMPAGNEE.md` pour les interventions.

## 6. Pratique autonome

- `independent-1` : 4 boîtes de 9 cahiers → 36 cahiers, `4×9`; représentation en barres.
- `independent-2` : 32 badges divisés également en 8 équipes → 4 badges par équipe, `32÷8`.
- `independent-3` : 35 oranges à placer dans des sacs de 6 → 5 sacs pleins et 5 oranges; six sacs pour tout contenir.
- `independent-4` : 6 mètres de ruban à 3 fanions par mètre → 18 fanions; rapport constant « 3 fanions/mètre » et représentation par tableau.
- Chaque pratique demande un dessin/une manipulation décrite, une équation, une réponse avec unité et un contrôle inverse, sans indice; corrigés dans `contenu/05_PRATIQUE_AUTONOME.md`.

## 7. Feedback et erreurs typiques

- **Addition d'unités sans groupes :** « 4 groupes de 7 » → `4+7` : représenter 4 fois 7; tester si 11 paraît plausible comparé à quatre paquets de sept.
- **Reste impossible :** annoncer `29=6×3+11` comme quotient/reste final : `11≥6`; reformer un groupe et obtenir `29=6×4+5`.
- **Arrondi automatique :** dire cinq paquets **complets** pour 23 objets et capacité 5 : seulement quatre complets, trois objets restants; cinq récipients nécessaires pour tout contenir.
- **Mauvaise unité :** « 18 groupes » au lieu de « 18 objets » : souligner la grandeur demandée, puis relégender le schéma.
- **Fausse proportion :** extrapoler avec un rapport non constant; vérifier le nombre d'objets **par** unité avant multiplication.
- Feedback = citer d'abord le premier saut incorrect et demander une correction, puis un cas parallèle inédit; ne jamais accepter un « j'ai compris » sans trace.

## 8. Évaluation formative et preuves

- Famille inchangée : `qc-pri-ma-020-ev-01`, `obj-1` et `crit-1`.
- Banque : 12 items (`q-001` à `q-012`), dont six paramétriques par fonctions arithmétiques explicites, quatre fixes d'analyse et deux épreuves indépendantes (`q-011` et `q-012`) dans des contextes éloignés de l'enseignement.
- Tous exigent au moins une modélisation et une vérification; les réponses numériques seules ne suffisent pas pour la maîtrise.
- `q-011` : centre communautaire, 47 livrets à classer par piles de 6; un élève explique quotient, reste, et capacité totale. `q-012` : ferme pédagogique, paniers de pommes récoltées selon un rapport stable; tableau et multiplication.
- **Seuil interne** : deux preuves satisfaisantes dans deux contextes (au moins une totalement sans indice), exactitude des calculs, justification du modèle et contrôle inverse. Voir plan et grille. Aucun item « certifié » sans revue humaine.

## 9. Remédiation / enrichissement

- Groupes incertains : former avec jetons 2, puis 3 puis 5 groupes identiques; remplacer progressivement les objets par barres.
- Choix d'opération incorrect : masquer les nombres, annoter « nombre de groupes », « par groupe », « total recherché », puis seulement insérer les données.
- Reste non compris : manipuler `N=14`, `d=4`, reconstituer `3×4+2`; tester `r<d`; refaire avec `N=16` pour un reste zéro.
- Proportion douteuse : dresser un tableau des couples (1,3), (2,6), (4,12); comparer à (4,11) où le rapport diffère.
- Enrichissement : distinguer « contenants complètement remplis » et « contenants nécessaires pour tout transporter » sur des exemples où le reste est zéro ou non; comparer dessins et équations.
- Transferts : transport de matériel sportif et jardinage; corrigés documentés dans `contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 10. Accessibilité

- Texte court à lire à haute voix, pictogrammes originaux ou matériel manipulable; schémas de groupes aussi décrits verbalement. Pas de couleur comme seul porteur d'information.
- Autoriser une trace orale enregistrée, un schéma tactile, des jetons ou une notation écrite pour montrer la **même** relation et le même contrôle numérique.
- Police lisible, unités explicites, temps prolongé si utile; aucune information personnelle demandée. La lecture du texte peut être aidée sans résoudre l'opération.
- Les items paramétriques n'utilisent que des entiers bornés et des contextes quotidiens ne supposant ni coût d'achat ni familiarité culturelle spécifique.

## 11. Critères de sortie

- `crit-1` : Construire une représentation et résoudre un problème multiplicatif inédit.
- Dans **deux contextes différents**, l'élève identifie les quantités et unités, choisit un schéma et une opération correspondant à la situation, calcule exactement, interprète le quotient et le reste s'il y en a, puis vérifie par une égalité inverse ou un test de vraisemblance fort.
- Deux réussites indépendantes sont nécessaires; une copie corrigée après indice est formative et ne vaut pas preuve autonome.
- Si une dimension échoue, proposer une remédiation ciblée et deux nouveaux contextes de reprise; ne pas qualifier l'élève à partir d'une note globale unique.

## 12. Références pédagogiques et limites

- Gouvernance consultée : `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md` dans `governance/Norme_Pedagogique_Autonome_v1.2/`; graphe central v1.2 et fichiers d'auteur de ce Kristal.
- Les lois arithmétiques et les résultats calculés sont vérifiables par arithmétique élémentaire; les problèmes, schémas textuels, réponses et grilles de cette livraison sont des productions originales. Documentation des sources : `sources/REFERENCES_CONTENU.md`.
- La nomenclature « Mathématique » est une projection québécoise et **ne signifie pas** homologation, conformité détaillée au PFEQ ou certification officielle.
- Rappel différé proposé : à J+2, demander « 4 groupes de 6 » avec dessin et calcul; à J+7, demander « 31 objets par groupes de 5, complets et nécessaires »; à J+21, poser un autre rapport simple, sans reproduire la démonstration.
- La qualification finale exige une relecture professionnelle du niveau, des items, des modalités d'accessibilité et des essais auprès d'apprenants; aucune intégration LMS n'a été exécutée.
