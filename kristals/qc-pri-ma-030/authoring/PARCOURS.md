---
format: qc.learning-path/1.0
id: qc-pri-ma-030
titre: Collecter et organiser des données
discipline_code: MA
statut: en_rédaction
revision_contenu: 0.2.0
langue_contenu: fr-CA
resultat_principal: Collecter des données selon une question et produire un tableau fiable.
objectifs_secondaires: []
criteres_reussite:
- Construire un tableau sans omission à partir d’observations brutes.
prealables_declares: []
alignement_statut: à_vérifier
alignement_ref: ALIGNEMENT.md
familles_evaluation:
- qc-pri-ma-030-ev-01
provenance_statut: références_identifiées
auteur: role:architecture-pedagogique
reviseur: null
---


# Microparcours — `qc-pri-ma-030`

**Discipline (appellation québécoise) :** Mathématique  
**Intitulé éditorial :** Collecter et organiser des données  
**Gouvernance active :** `governance/Norme_Pedagogique_Autonome_v1.2/`  
**Statut :** développement pédagogique complet proposé; validation humaine encore requise, sans conformité officielle revendiquée.

## 1. Intention et frontières

- `obj-1` — **Résultat observable immuable :** Collecter des données selon une question et produire un tableau fiable.
- `crit-1` — **Preuve autonome immuable :** Construire un tableau sans omission à partir d’observations brutes.
- **Notions :** catégorie, relevé, effectif, tableau. On pose une question précise, on choisit une seule catégorie par observation et on compte toutes les observations admissibles exactement une fois.
- **Périmètre :** listes finies, petites collections, catégories exclusives et exhaustives définies par la question. Pas d'inférence statistique, de pourcentages, de graphiques complexes, ni de classification personnelle ambiguë.
- **Relations :** aucun préalable strict, aucun ordre conseillé ni renforcement sortant; le graphe possède des liens *entrants*, sans incidence sur les accès ni les fichiers livrés.

## 2. Notions et représentations

- **Question de collecte :** « Combien d'objets de chaque sorte ont été observés? » Son champ détermine ce qu'il faut relever.
- **Catégorie :** classe nommée d'observations selon un critère commun; pour cette tâche chaque observation appartient à une seule catégorie et toutes les observations admissibles trouvent une catégorie. Exemple : `rond` ou `carré`, jamais une catégorie `joli` non observable.
- **Relevé :** trace ordonnée des observations brutes au fur et à mesure; une marque de pointage correspond à une observation.
- **Effectif :** nombre entier d'observations d'une catégorie; la somme des effectifs est le nombre d'observations retenues.
- **Tableau d'effectifs :** colonnes « Catégorie » et « Effectif », une ligne par catégorie; le total peut figurer à la dernière ligne. Le pointage `||||` matérialise quatre observations (cinq peuvent être barrées par convention, explicitée au besoin).
- **Concret → schéma → notation :** déplacer un jeton par observation → cocher une case de relevé → inscrire les effectifs. L'ordre du relevé ne change pas les effectifs.
- **Exemple 1 :** crayons : rouge, bleu, rouge, vert, bleu, rouge, vert → rouge 3, bleu 2, vert 2, total 7. On recompte les 7 éléments.
- **Exemple 2 :** étiquettes : rond, carré, triangle, carré, rond, rond, triangle, carré → rond 3, carré 3, triangle 2, total 8.
- **Contre-exemple 1 :** rouge, rouge, bleu avec « rouge 1; bleu 1 » : la seconde occurrence rouge a été omise, total 2 au lieu de 3.
- **Contre-exemple 2 :** une même pomme classée simultanément sous « pomme » et « fruit rouge » : les catégories se recouvrent; double comptage possible. Corriger en adoptant uniquement « sorte de fruit » avec des modalités définies.

## 3. Préparation / diagnostic

- **Préalables bloquants :** aucun. **Ordre conseillé :** aucun. Le diagnostic sert uniquement à calibrer l'enseignement.
- `diag-1` : 6 symboles lus ou montrés dans l'ordre (étoile, lune, étoile, soleil, lune, étoile). Construire le tableau étoile 3, lune 2, soleil 1; vérifier total 6.
- `diag-2` : 8 déplacements notés (vélo, marche, bus, marche, vélo, marche, bus, bus). Construire vélo 2, marche 3, bus 3; vérifier total 8 et expliquer comment éviter l'oubli.
- **Interprétation :** si les catégories et le total sont exacts et le contrôle indépendant est explicité, proposer un défi sans forcer une leçon déjà maîtrisée. Sinon intervenir sur le premier maillon déficient : champ de la question, catégorie, pointage, somme ou lecture du tableau.

## 4. Enseignement guidé

- `teach-1` : afficher les 7 crayons de l'exemple 1. Poser « Combien de crayons de chaque couleur? » et énoncer les catégories avant de compter.
- Modeler le relevé numéroté : toucher l'élément 1, déposer un jeton dans la case « rouge », marquer un trait, poursuivre sans sauter d'indice; ne jamais compter le même indice deux fois.
- Transformer les traits en effectifs 3, 2, 2, écrire le tableau, puis vérifier **autrement** : parcourir les positions 7 à 1 et cocher chaque observation exactement une fois. Constater 3 + 2 + 2 = 7.
- Montrer l'erreur « rouge 2 » : comparer le tableau aux positions brutes 1, 3, 6; corriger le relevé, pas seulement le nombre final.
- **Contrôle de compréhension :** pourquoi les catégories doivent-elles être distinctes? Pourquoi le total doit-il être 7? Voir `contenu/03_ENSEIGNEMENT_GUIDE.md`.

## 5. Pratique accompagnée

- `guided-1` : six boutons gris, noir, gris, blanc, noir, gris. Avec toutes les catégories affichées, réaliser le pointage (gris 3, noir 2, blanc 1), total 6.
- `guided-2` : neuf coquillages étiquetés rond, pointu, rond, plat, pointu, rond, plat, pointu, pointu. Retirer les cases préremplies : rond 3, pointu 4, plat 2, total 9.
- `guided-3` : dix jetons carré, triangle, rond, rond, triangle, carré, rond, triangle, carré, rond. Sans modèle de tableau : carré 3, triangle 3, rond 4, total 10.
- **Indices dégressifs :** indices de position et catégories → seulement question « Que reste-t-il à vérifier? » → aucun indice. Feedback après un essai, sur l'erreur observable initiale, jamais sur la personne.

## 6. Pratique autonome

- `independent-1` : quatre jeux de données nouveaux, avec catégories fixes, 7 à 12 observations, à résoudre sans indices. Ils sont explicités et corrigés dans `contenu/05_PRATIQUE_AUTONOME.md`.
- Exiger une question de collecte, un relevé (traits, coches ou classement), le tableau, un total et un contrôle sans simplement recopier les mêmes traits.
- Autoriser production orale dictée, manipulation de jetons, gros caractères ou saisie adaptée, mais pas d'aide sur la classification ou les effectifs.
- Préparer deux preuves **non utilisées dans les exemples** : inventaire sportif (15 enregistrements; trois catégories) et passage de véhicules fictifs (16 enregistrements; quatre catégories).

## 7. Feedback et erreurs typiques

- **Omission :** le total est inférieur au nombre de lignes; faire correspondre chaque ligne brute à une seule coche numérotée, puis recompter.
- **Double comptage :** deux catégories partagent une observation; afficher une règle de catégories mutuellement exclusives et reclasser.
- **Confusion étiquette/effectif :** dans « rond 4 », 4 est le nombre de ronds et non le nom de la catégorie; présenter les deux colonnes avec en-têtes.
- **Catégorie manquante / zéro :** une catégorie déclarée qui ne figure pas dans les observations conserve la ligne d'effectif 0.
- **Somme incorrecte :** recomposer le total avec des jetons et comparer au nombre d'enregistrements, sans introduire de nouveaux enregistrements.
- Après correction, faire un nouvel essai sur données différentes pour contrôler le transfert.

## 8. Évaluation formative et preuves

- **Famille :** `qc-pri-ma-030-ev-01` ; `objectif_ref: obj-1` ; `critere_ref: crit-1`.
- **Banque :** 12 items : deux d'ancrage fixe, six paramétriques déterministes, deux exercices de transfert, deux preuves autonomes en contextes distincts. Les variantes sont bornées par un générateur défini et testé; les items ne sont pas certifiés.
- **Critères :** catégorie pertinente et exclusive, exhaustivité du relevé, effectifs exacts, tableau lisible, somme égale à la taille du relevé, contrôle par seconde méthode et autonomie.
- **Maîtrise :** réussir les deux preuves indépendantes, dont une en autonomie complète, avec toutes les observations correctement affectées et un contrôle démontré; aucune note unique ne suffit.
- **Traces d'évaluation :** tableau et relevé uniquement dans l'instance d'enseignement, pas dans le canon.

## 9. Remédiation / enrichissement

- Revenir à une collection matérielle de 4 à 6 jetons si le relevé est fragile, faire une case par observation, puis retirer le support.
- Pour une catégorie ambiguë, reformuler la question et montrer un tri non superposé; pour un total erroné, recouper par ordre inverse ou lots.
- Pour une erreur de zéro, prévoir une colonne connue mais non observée (effectif 0).
- **Enrichissement :** permuter l'ordre d'un même relevé et constater que le tableau reste invariant; tester un tableau contradictoire et expliquer la correction; aucun prérequis additionnel.

## 10. Accessibilité

- Présenter chaque observation en texte accessible et, si nécessaire, en pictogramme contrasté avec étiquette textuelle; ne pas coder une catégorie uniquement par couleur.
- Autoriser pointage de jetons, réponse vocale transcrite, tableau à gros caractères, clavier et outils de lecture, sans fournir les effectifs.
- Si la motricité du traçage pose problème, l'élève peut annoncer chaque affectation et dicter les cases remplies; recueillir la démarche avec consentement et selon les règles locales.
- Activités avec objets fictifs neutres; ne pas recueillir de données personnelles réelles sur les élèves.

## 11. Critères de sortie

1. Produire pour `crit-1` un tableau complet en réponse à `obj-1`, sans ligne brute omise ou affectée deux fois.
2. Affecter chaque observation à exactement une catégorie, indiquer les effectifs exacts et vérifier que la somme équivaut au nombre d'observations admissibles.
3. Réussir **deux productions distinctes** (q-011 inventaire sportif et q-012 véhicules fictifs), l'une au moins entièrement sans indice, et expliquer son contrôle autrement.
4. Si un des contextes révèle une lacune, documenter la dimension et refaire une tâche neuve après remédiation, plutôt que convertir un résultat isolé en certification.
5. **Rappel différé** après environ une semaine (choix didactique non imposé) : nouvelle séquence brève de huit symboles à classer, sans modèle; comparer la stabilité et réactiver le pointage au besoin.

## 12. Références pédagogiques et limites

- **Sources internes vérifiées dans l'archive :** contrat pédagogique v1.2, générateur et examens, charte de conversion, graphe 202, frame original et alignement. Voir `sources/REFERENCES_CONTENU.md`.
- **Dérivations mathématiques :** si les catégories forment une partition d'un relevé fini, la somme des effectifs vaut le nombre d'observations retenues; vérifier également observation par observation.
- **Créations originales :** toutes les listes fictives, exemples, questions, rétroactions, algorithmes d'items et rubriques de ce delta; aucune citation externe ni droit tiers présumé.
- **Limites :** revue pédagogique humaine, vérification de l'accessibilité en situation, essais auprès d'apprenants et validation locale avant publication; aucune approbation ou conformité PFEQ revendiquée.
