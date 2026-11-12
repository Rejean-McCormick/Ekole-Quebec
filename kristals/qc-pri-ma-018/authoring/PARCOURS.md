---
format: qc.learning-path/1.0
id: qc-pri-ma-018
titre: Relations et égalités numériques
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.3.0
langue_contenu: fr-CA
resultat_principal: Établir et expliquer des égalités ou relations numériques correctes.
objectifs_secondaires: []
criteres_reussite:
- Compléter des égalités ouvertes en explicitant la relation choisie.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-018-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---
# Microparcours — `qc-pri-ma-018`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Relations et égalités numériques  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** contenu rédigé en v1.2; revue pédagogique humaine et essais apprenants requis avant toute qualification.  
**Identifiants intangibles :** `obj-1`, `crit-1`, `qc-pri-ma-018-ev-01`.

## 1. Intention et frontières

- `obj-1` — **Résultat vérifiable :** Établir et expliquer des égalités ou relations numériques correctes.
- `crit-1` — **Production autonome qui atteste l’acquis :** Compléter des égalités ouvertes en explicitant la relation choisie.
- **Notions :** égalité, inconnue, compensation, relation.
- Une égalité est vraie si ses deux expressions représentent le même nombre. « = » signifie « a la même valeur que », pas « écris la réponse ».
- Une inconnue (□, puis éventuellement une lettre) est le nombre à déterminer; sa position peut changer.
- Une relation numérique explicite comment deux valeurs, écritures ou changements sont liés.
- La compensation préserve une somme lorsqu’on augmente un terme d'une certaine quantité et diminue l’autre terme de la même quantité. Une opération effectuée sur les deux membres d'une égalité préserve aussi l'égalité, mais c'est une règle de maintien de l'égalité distincte de la compensation interne à une somme.
- **Frontière :** nombres entiers non négatifs, additions/soustractions exactes, une seule inconnue et une solution unique; pas d'algèbre formelle, d'équations à solutions multiples ni de générateurs libres.
- Le fait d'appartenir à une année du primaire ne prouve pas cette maîtrise.

## 2. Notions et représentations

- **Matériel :** deux plateaux de jetons, un par membre; ajouter/retirer des jetons ou réorganiser une collection sans la changer.
- **Schéma :** deux barres de même longueur, partitionnées en segments qui totalisent pareillement; chaque segment porte une valeur ou `?`.
- **Notation :** `13 + 9 = 15 + □` : le total de gauche est 22, donc □ = 7; relation : 13→15 (+2) et 9→7 (−2). Vérification : 22 = 22.
- **Exemple 2 :** `□ + 6 = 11 + 8` ; côté droit 19; □ = 13; vérification 13 + 6 = 19.
- **Contre-exemple 1 :** `10 + 4 = 14 + 4` est faux (14 ≠ 18), malgré la répétition du signe `+`.
- **Contre-exemple 2 :** `12 + 7 = 14 + 9` n'est pas une compensation : les deux termes ont augmenté; 19 ≠ 23.
- Employer les écritures équivalentes seulement après la vérification des quantités. Des exemples complets figurent dans `../contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- **Préalables stricts `requires` :** aucun; **ordre conseillé :** aucun; **renforcement/transfert référencés :** aucun, conformément au graphe v1.2.
- `diag-1` — Sans indice, compléter `6 + 5 = 8 + □`, puis expliquer avec jetons/barres ou calcul. Solution 3 : 11 = 11.
- `diag-2` — Décider si `9 + 4 = 7 + 6` est vraie et l'expliquer d'une autre manière. Oui : 13 = 13; +2 dans un terme correspond à −2 dans l'autre.
- **Décision :** deux réponses exactes avec justification intelligible et vérification autonome → accès direct à des applications et preuves; sinon, module adapté, jamais verrou d'accès à cause d’un ID absent. Consigner séparément exactitude, interprétation de `=` et justification. Voir `../contenu/02_DIAGNOSTIC.md`.

## 4. Enseignement guidé

- `teach-1` — Afficher : `14 + 8 = 16 + □` avec deux collections de 22 jetons; demander ce que veut dire `=`.
- Modéliser la barre gauche [14][8], la droite [16][?]. Les 16 dépassent 14 de 2; il faut 2 de moins dans l'autre groupe : □ = 6.
- Contrôler : `14 + 8 = 22`, `16 + 6 = 22`; comparer la stratégie par calcul du total (22 − 16 = 6) et par compensation (+2/−2).
- Faire une seconde démonstration à position inversée : `□ + 9 = 12 + 7` donne □ = 10 car 19 − 9 = 10.
- **Question de compréhension :** « Si le membre de droite est plus grand, peut-on dire que le signe = est quand même vrai? » Non; les valeurs doivent coïncider.
- Déroulement détaillé dans `../contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- `guided-1` — Trois essais avec indices décroissants (énoncé, indices, réponse et rétroaction dans `../contenu/04_PRATIQUE_ACCOMPAGNEE.md`).
- Essai 1, matériel + barres + question : `8 + 7 = 10 + □` → 5; dire « +2 / −2 ».
- Essai 2, barres facultatives et rappel minimal : `□ + 4 = 9 + 6` → 11; vérifier 15 = 15.
- Essai 3, aucun indice initial : `23 − □ = 17` → 6; vérifier 23 − 6 = 17. Si erreur, révéler un indice seulement après tentative.
- Feedback : pointer le premier changement incorrect (signe, total, inconnue), demander une vérification numérique, puis refaire sur nombres nouveaux.

## 6. Pratique autonome

- `independent-1` — Quatre tâches nouvelles, sans aide pendant l'essai; traces : résultat, démarche et substitution.
- `A1 : 21 + 6 = 24 + □` → 3; `A2 : □ + 8 = 13 + 7` → 12;
- `A3 : 30 − □ = 18` → 12; `A4 : 17 + 9 = □ + 11` → 15.
- Exiger pour chacune une relation explicitée : compensation, différence ou égalité des deux totaux. Calculatrice non requise; elle n'est pas une preuve de justification.
- Fournir oral/écrit/dessin comme moyens équivalents. Corrigés et critères complets : `../contenu/05_PRATIQUE_AUTONOME.md`.

## 7. Feedback et erreurs typiques

- `error-1` — Lire `=` comme ordre de calcul → comparer deux membres avec jetons. Par exemple `4 + 6 = 5 + □` représente 10 de chaque côté, donc □ = 5.
- `error-2` — Augmenter les deux termes en prétendant compenser → reprendre `12 + 7 = 14 + □` : □ = 5 (−2), non 9.
- `error-3` — Traiter `□` comme un zéro ou croire qu'il est toujours à droite → substituer et vérifier l'égalité dans les deux orientations.
- `error-4` — Inverser le sens d'une soustraction → résoudre `20 − □ = 14` par « de 14 à 20 il manque 6 », pas 34.
- `error-5` — Résultat correct sans relation explicitée → demander une phrase ou un schéma liant les changements et une vérification indépendante. Protocoles dans `../contenu/06_REMEDIATION_ET_TRANSFERT.md`.

## 8. Évaluation formative et preuves

- **Famille :** `qc-pri-ma-018-ev-01`; `objectif_ref: obj-1`; `critere_ref: crit-1`; **type :** `paramétrique_controle`.
- Banque : **10 items** dont cinq gabarits paramétriques déterministes à solution unique; cinq cas fixes/scénarios contrôlés; identifiants `q-001` à `q-010`.
- **Preuve 1 (`q-007`) :** plateaux de jetons. **Preuve 2 (`q-008`) :** récolte d'un jardin collectif. Contextes distincts, sans indices ni corrigés visibles à l'élève.
- Pour chaque preuve : nombre exact + relation justifiée + vérification des deux membres; ne pas inférer la maîtrise d’une seule note totale.
- Seeds, domaines, algorithmes et contrôle arithmétique documentés dans `../evaluation/BANQUE_ITEMS.json` et `../evaluation/PLAN_EVALUATION.md`.
- Les items restent `a_revoir` tant qu'une revue humaine et un essai auprès d'apprenants n'ont pas été réalisés.

## 9. Remédiation / enrichissement

- Remédiation ciblée par erreur : sens de l'égalité (deux collections), inconnue (case vide mobile), compensation (+k/−k), inversion de soustraction (droite graduée).
- Après intervention, proposer une tâche de structure identique avec valeurs neuves; ne pas simplement redonner la correction.
- **Transfert T1 :** organisation de crayons (`18 + □ = 14 + 11` → 7); **T2 :** emprunts de livres (`□ + 6 = 17 + 4` → 15). Ces données sont fictives et originales.
- Enrichissement : produire deux égalités vraies différentes de même valeur et en expliquer les transformations sans symbole algébrique avancé. Aucun lien `reinforces` absent ne doit être inventé.

## 10. Accessibilité

- Consignes courtes, une équation par ligne, contrastes lisibles, symbole □ explicité oralement, texte alternatif pour tout schéma, langage simple en français du Québec.
- Autoriser jetons, barre tactile, droite graduée, réponse orale transcrite ou écrite; ne pas donner d’indice dans les deux preuves de maîtrise.
- Évaluer le raisonnement numérique, jamais la vitesse, la calligraphie, l'aisance orale ou le contexte culturel; éviter de dépendre d’une illustration en couleur.
- Aucun achat de matériel requis; des marques dessinées sur papier remplacent les jetons.

## 11. Critères de sortie

1. Réaliser `crit-1` de façon autonome : **Compléter des égalités ouvertes en explicitant la relation choisie.**
2. Deux manifestations **séparées** et satisfaisantes dans des contextes différents (`q-007`, `q-008`), dont au moins une sans dispositif d'aide aux calculs; sans indice conceptuel sur aucune des deux.
3. Dans chaque preuve : valeur exacte, justification correcte de la relation, substitution/contrôle des deux côtés. Une démonstration par matériel ou schéma est admise.
4. Si une dimension n'est pas démontrée, suivre la branche de remédiation et collecter une **nouvelle** preuve comparable; ne pas compenser une relation non expliquée par le score d'items simples.
5. Programmer un rappel différé vers J+2 à J+4 et J+10 à J+14, par exemple `7 + 6 = 9 + □` (4) puis `□ + 5 = 8 + 9` (12); ne pas transformer cet exemple de calendrier en prérequis.

## 12. Références pédagogiques et limites

- **Sources internes consultées** : `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`, graphe central, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` et contrat source de cette feuille; liste détaillée et classement dans `../sources/REFERENCES_CONTENU.md`.
- **Dérivations mathématiques** : propriétés élémentaires des entiers non négatifs, vérifiées par calcul exact et tests de domaines; les exercices, contextes et corrections sont des productions originales.
- **Correspondance Québec** : appellation « Mathématique » seulement, sans revendication d'alignement PFEQ. `ALIGNEMENT.md` n'a pas été modifié.
- **Code officiel de cours** : aucun attribué; ID interne uniquement.
- **Qualification non acquise** : revue humaine d'adéquation au public cible, essais d'accessibilité sur dispositifs, expérimentation des items, intégration LMS et exécution du Framework/Kristal v9 non effectuées dans cette livraison.
