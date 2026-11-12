---
format: qc.learning-path/1.0
id: qc-pri-ma-019
titre: Situations-problèmes additives
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Modéliser et résoudre une situation additive en distinguant les données utiles.
objectifs_secondaires: []
criteres_reussite:
- Résoudre deux problèmes verbaux nouveaux et expliquer les opérations.
prealables_declares:
- qc-pri-ma-006
- qc-pri-ma-007
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-019-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---

# Microparcours — `qc-pri-ma-019`

**Discipline :** Mathématique (appellation québécoise). **Titre :** Situations-problèmes additives. **État :** contenu rédigé en v1.2, à réviser humainement avant diffusion. **Autorité :** contrat pédagogique interne v1.2. Les données numériques et histoires de ce module sont inventées.

## 1. Intention et frontières

- `obj-1` — **Objectif observable immuable :** Modéliser et résoudre une situation additive en distinguant les données utiles.
- `crit-1` — **Preuve autonome immuable :** Résoudre deux problèmes verbaux nouveaux et expliquer les opérations.
- L'élève identifie *ce qu'on cherche*, repère les relations entre quantités, construit un schéma, choisit addition et/ou soustraction, calcule, explique et vérifie unités et plausibilité.
- Étendue : problèmes additifs à nombres naturels non négatifs; au plus deux étapes pour la synthèse; pas de multiplication nécessaire ni de nombres négatifs. Une donnée superflue fait partie de la tâche, sans piège linguistique injuste.
- Une opération correcte isolée n'atteste pas la capacité à modéliser un énoncé. Aucune équivalence officielle au PFEQ n'est revendiquée.

## 2. Notions et représentations

- **Schéma :** représentation organisée des relations; par exemple « 34 départ + 18 entrées = ? total », ou barre « total 52 | 34 connus | ? manquants ». Un dessin décoratif de 52 objets n'indique pas nécessairement la relation.
- **Inconnue :** quantité recherchée, notée `?` ou `x`; sa position peut être initiale, intermédiaire ou finale. `? + 13 = 40` implique `40 − 13 = 27`, et non `40 + 13`.
- **Addition :** somme de quantités compatibles lorsqu'on les réunit ou pour retrouver l'état initial après un retrait : `27 + 13 = 40`.
- **Soustraction :** différence/complément ou quantité restante : `40 − 13 = 27`; elle peut résoudre un énoncé où apparaît le mot « plus ».
- **Concret → schéma → notation :** déplacer 14 jetons et 9 jetons; dessiner deux segments de 14 et 9; écrire `14 + 9 = 23 objets`. Barrer les données hors problème, pas les quantités utiles.
- **Exemple résolu A :** 46 cartes, puis 17 reçues, 3 enveloppes sur la table. Chercher les cartes : `46 + 17 = 63` cartes; « 3 enveloppes » est inutile. Schéma `[46][17] → [?]`.
- **Exemple résolu B :** 71 graines au départ; 24 utilisées, 5 étiquettes. Reste `71 − 24 = 47` graines; 5 étiquettes inutiles. Schéma `[? reste][24 utilisées]=[71 départ]`.
- **Contre-exemple A :** `46 + 17 + 3 = 66` additionne des enveloppes aux cartes : unités et lien incorrects.
- **Contre-exemple B :** « il reste 47, on en a retiré 24, donc il y en avait 47 − 24 = 23 » inverse la relation; départ `47 + 24 = 71`.
- Développement détaillé et vérification inverse : `contenu/01_NOTIONS_ET_EXEMPLES.md`.

## 3. Préparation / diagnostic

- **Préalables `requires` :** `qc-pri-ma-006` (sens de l'addition), `qc-pri-ma-007` (sens de la soustraction). Aucun `recommends_before` ni `reinforces` pour ce Kristal.
- Deux essais courts sans aide d'opération : D1 « 18 billes et 7 gagnées; 2 boîtes; combien de billes ? » (25; 2 boîtes inutiles); D2 « 29 figurines après en avoir donné 8; combien avant ? » (37; addition inverse). L'élève indique l'inconnue, une représentation et l'opération. Voir `contenu/02_DIAGNOSTIC.md`.
- Vérifier indépendamment calcul élémentaire et relation de l'énoncé; si le calcul est fragile, offrir jetons/droite graduée et revoir le préalable concerné. Un diagnostic équivalent réussi peut satisfaire les conditions d'entrée sans parcours formel antérieur. Les critères détaillés sont dans le diagnostic.

## 4. Enseignement guidé

- **`teach-1` :** enseigner la boucle « question → quantités utiles et unités → relation/schéma → opération → calcul → réponse vérifiée ».
- Modelage A : « 58 images, 16 offertes à un ami, 4 albums; combien reste-t-il d'images ? » Représenter 58 comme barre totale, séparer 16 et `?`, écrire `58 − 16 = 42 images`. Vérification : `42 + 16 = 58`.
- Modelage B (inconnue initiale) : « après l'ajout de 19 fiches il y en a 64; 3 chemises; combien avant ? » Dessiner `[?][19] = 64` puis `64 − 19 = 45 fiches`; ne pas additionner 3 chemises.
- Dire explicitement pourquoi les nombres inutiles ne comptent pas et pourquoi la position de l'inconnue prime sur un mot-clé. Contre-exemple commenté : « ajouté » n'impose pas l'addition si la quantité de départ est cherchée.
- Contrôle de compréhension : l'élève explique pourquoi une même égalité peut se lire `45 + 19 = 64` et `64 − 19 = 45`.
- Séquence détaillée : `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- **`guided-1` :** G1 (avec schéma offert) : 36 + 14 = 50 autocollants; 2 pochettes inutiles. G2 (indice « quelle est l'inconnue ? ») : 62 − 27 = 35 feuilles, 4 classeurs inutiles. G3 (sans aide initiale) : `? − 18 = 47`, donc `47 + 18 = 65` objets au départ, 3 paniers inutiles.
- Réduire progressivement l'aide : flèches et barres → question ciblée → relecture autonome. Ne révéler le résultat qu'après tentative justifiée.
- Enseignant : noter si l'erreur vient de la relation, du filtrage, du calcul, de l'unité ou de la vérification. Exercices et corrigés : `contenu/04_PRATIQUE_ACCOMPAGNEE.md`.

## 6. Pratique autonome

- **`independent-1` :** P1 `25 + 38 = 63`; P2 `90 − 34 = 56`; P3 départ `52 + 17 = 69`; P4 `44 + 27 − 18 = 53`. Toutes les situations incluent une donnée non pertinente clairement identifiable; détaillées dans `contenu/05_PRATIQUE_AUTONOME.md`.
- Sans indices de sélection de l'opération ni rétroaction pendant l'essai; matériel de représentation accessible si utilisé sans aide sur la décision. Demander une phrase indiquant pourquoi la donnée écartée est inutile.
- Pour la preuve `crit-1`, deux problèmes **nouveaux et distincts** : `q-010` (centre de prêt de livres) et `q-011` (jardin communautaire), administrés sans indication d'opération, réponses et justifications conservées localement dans le LMS; voir grille.

## 7. Feedback et erreurs typiques

- **Mélange des unités :** « 3 boîtes » ajoutées aux 46 cartes → « Quels nombres décrivent des cartes ? » → refaire barres séparées.
- **Automatisme des mots-clés :** « a reçu » → addition irréfléchie → faire entourer l'inconnue et écrire `départ + reçu = final` avant de calculer.
- **Inversion de quantité initiale :** `47 − 24` au lieu de `47 + 24` → restituer 24 jetons retirés et tester l'équation.
- **Calcul seul :** résultat sans explication → exiger schéma ou égalité interprétée et phrase de justification.
- **Deux étapes :** une seule opération → reformuler ce qui se passe *avant* puis *après*. Donner un nouvel exercice isomorphe, pas le même corrigé recopié.

## 8. Évaluation formative et preuves

- `family_id: qc-pri-ma-019-ev-01`; `objectif_ref: obj-1`; `critere_ref: crit-1`; mode de référence : `paramétrique_controle`.
- Douze items `q-001` à `q-012` : cinq ancrages fixes, trois items paramétriques bornés, un problème fixe en deux étapes, deux preuves de transfert sans aide et une analyse d'erreur. Détails : `evaluation/PLAN_EVALUATION.md` et `evaluation/BANQUE_ITEMS.json`.
- Les variantes paramétriques sont une liste finie de cas vérifiés : choix par `index = seed mod 4`; trois familles numériques, quatre cas chacune; aucune génération libre. Énoncé, corrigé et contrôles décrits dans la banque et le plan.
- Pour maîtriser : réussir `q-010` **et** `q-011` dans deux contextes distincts et justifier les opérations sans intervention sur le choix des nombres ou des opérations. Si une preuve échoue, remédier et recueillir une nouvelle preuve équivalente.

## 9. Remédiation / enrichissement

- Remédiation par erreur observée : relation → barres `départ / changement / final`; filtrage → tableau quantité/unité/utile; calcul → décomposition additive, recomposition; deux étapes → chronologie en deux lignes.
- Enrichissement : comparer deux schémas pour la même égalité, fabriquer un problème à donnée superflue puis expliquer comment le résoudre, varier la position de l'inconnue (sans introduire des négatifs).
- Deux transferts distincts et rétroactions cibles : `contenu/06_REMEDIATION_ET_TRANSFERT.md`. Aucun nouveau lien de graphe.

## 10. Accessibilité

- Proposer lecture orale fidèle, police lisible, espacement, schémas textuels accessibles et jetons/tactiles. Décrire les schémas en mots : « le tout de 58 est séparé en 16 et ? »; ne jamais dépendre d'une couleur.
- Autoriser dictée orale, écriture, clavier ou schéma explicité; évaluer relation, unités, calcul et justification, non l'aisance graphique ou la vitesse de lecture. Ne pas mettre en évidence les nombres utiles au moment de la preuve autonome.
- Réduire au besoin la charge de transcription, pas les données pertinentes ni le niveau de raisonnement; proposer pause et temps supplémentaire. Contextes fictifs ne demandant aucune expérience personnelle.

## 11. Critères de sortie

- Produire les deux tâches verbales nouvelles `q-010` et `q-011` **sans indice**; identifier question, quantités pertinentes, inconnue, schéma ou relation, calcul exact avec unité, et justification des opérations.
- Au moins deux contextes : un problème de changement avec résultat final inconnu; un problème avec quantité initiale inconnue suivi d'un retrait. Chaque contexte satisfait indépendamment la rubrique définie dans `evaluation/GRILLE_MAITRISE.md`.
- Ne pas accorder maîtrise sur une note unique ni sur les seules variantes d'entraînement; en cas d'échec ciblé, enregistrer une non-maîtrise temporaire et obtenir une nouvelle preuve après remédiation.
- Rappel différé proposé 2 à 4 jours puis 2 semaines : nouvelle variante additive et explication de la donnée inutile; le rappel entretient la maîtrise mais ne remplace pas les deux preuves.

## 12. Références pédagogiques et limites

- Norme active et contraintes de production : `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, charte d'appellations québécoises; `authoring/ALIGNEMENT.md` demeure non modifié.
- Pratiques inspirées du recueil interne `governance/Norme_Pedagogique_Autonome_v1.2/REFERENCES_EVIDENCE.md` (exemples guidés, feedback, accessibilité). Les exercices, valeurs, contextes et textes sont des créations originales, sans prétention de résultat empirique ni citation textuelle externe.
- Voir `sources/REFERENCES_CONTENU.md` pour distinguer références effectivement lues, raisonnements arithmétiques vérifiés et créations. Pas de licence externe revendiquée.
- Limites : contenu/banque au statut `a_revoir`, revue humaine de la clarté, du niveau, de l'accessibilité effective, du biais contextuel et des modalités d'administration requise. Pas d'homologation PFEQ ni de qualification automatique.
