# Plan d’évaluation — qc-pri-ma-030

**Ancrage inchangé :** `obj-1` — Collecter des données selon une question et produire un tableau fiable.  
**Critère inchangé :** `crit-1` — Construire un tableau sans omission à partir d’observations brutes.  
**Famille inchangée :** `qc-pri-ma-030-ev-01` (`paramétrique_controle`).

## Table de correspondance (chaque item porte les trois références)

| Item | But/étape | Difficulté | Mode | Représentation | Attendu / couverture |
|---|---|---|---|---|---|
| q-001 | D1: symboles | initial | fixe | relevé textuel et tableau | catégories, relevé, effectifs, total, contrôle |
| q-002 | D2: déplacements | initial | fixe | liste numérotée et marques de pointage | catégories, relevé, effectifs, total, contrôle |
| q-003 | P3: motifs de rubans | intermediaire | parametrique | liste de motifs puis tableau | catégories, relevé, effectifs, total, contrôle |
| q-004 | P4: tailles de fiches | intermediaire | parametrique | fiches textuelles vers pointage | catégories, relevé, effectifs, total, contrôle |
| q-005 | P5: quatre formes | intermediaire | parametrique | quatre catégories et tableau | catégories, relevé, effectifs, total, contrôle |
| q-006 | P6: animaux sur cartons | transfert | parametrique | liste numérotée et tableau à quatre modalités | catégories, relevé, effectifs, total, contrôle |
| q-007 | P7: catégorie zéro | transfert | parametrique | catégorie à effectif zéro | catégories, relevé, effectifs, total, contrôle; catégorie à zéro |
| q-008 | P8: codes A/B/C | transfert | parametrique | codes abstraits puis seconde vérification | catégories, relevé, effectifs, total, contrôle |
| q-009 | F9: modalité absente | intermediaire | fixe | codes avec catégorie zéro | catégories, relevé, effectifs, total, contrôle |
| q-010 | T10: comptoir de billets | transfert | scenario_controle | relevé de billets, contrôle inverse | catégories, relevé, effectifs, total, contrôle |
| q-011 | M11: matériel sportif | transfert | scenario_controle | liste brute, tableau et contrôle autonome | catégories, relevé, effectifs, total, contrôle; preuve indépendante |
| q-012 | M12: véhicules fictifs | transfert | scenario_controle | observation fictive de véhicules et contrôle autonome | catégories, relevé, effectifs, total, contrôle; preuve indépendante |

## Modèles d’items et pondération

- Diagnostic : q-001, q-002; entrée formative, pas condition bloquante.
- Construction/variation : q-003 à q-008, paramétriques déterministes; q-009 vérifie le zéro, q-010 examine le transfert.
- Preuves de sortie : q-011 et q-012 dans deux contextes distincts. Elles exigent toutes les observations, catégories exactes, tableau complet et vérification indépendante. L’une au moins doit être réalisée sans aucune aide mathématique; idéalement les deux.
- Chaque item est rattaché explicitement à `obj-1`, `crit-1` et à la famille dans la banque JSON. On conserve les traces de processus pour différencier les erreurs.
- Pas de score global seul ni seuil en points : la grille juge séparément exhaustivité, affectation, effectifs, tableau, contrôle, autonomie et répétition dans deux contextes.

## Génération contrôlée P-030/1

- **Variables** : `seed` entier borné par item à `[seed_stable, seed_stable+99]`, `n`, catégories littérales définies par item, et `zero_last` booléen figé par item.
- **Domaines** : pour trois catégories, `n=10+(seed%5)` (10 à 14) ; pour quatre catégories actives, `n=13+(seed%5)` (13 à 17). Avec trois catégories actives et une catégorie forcée à zéro, `n=10+(seed%5)` (10 à 14).
- **Formule des effectifs** : poser `A` comme catégories actives, `m=|A|`. Pour `i=0..m-2` : `e_i=2+(floor(seed/(i+2)) mod 3)` ; `e_(m-1)=n−somme(e_i)`. La dernière catégorie, si inactive, vaut `0`. Les minima choisis rendent `e_(m-1)>=1` pour toutes les graines autorisées.
- **Construction reproductible du stimulus** : tourner `A` à gauche de `seed mod m` places; inverser l’ordre si la graine est impaire; parcourir cet ordre par tours `j=0..max(e)-1`, en émettant une occurrence d’une catégorie lorsque `j<e(catégorie)`. Numéroter les positions 1..n.
- **Solveur indépendant** : faire un comptage `Counter` sur toutes les occurrences émises, puis ajouter le zéro à la catégorie prévue; comparer chaque effectif, vérifier les catégories et le total. Ce solveur n’utilise pas les formules d’effectifs pour calculer le corrigé.
- **Corpus fixe** : aucune catégorie générée librement; les six listes de catégories, graines stables et trois exemples calculés par item sont présents dans `BANQUE_ITEMS.json`.
- **Restrictions** : pas de question fondée sur une caractéristique personnelle réelle; pas de changement de catégorie à la volée; pas de génération IA comme arbitre de corrigé.

## Variations autorisées et accessibilité

- Les six items paramétriques peuvent changer de graine dans le domaine documenté, mais l’instance présentée est une version figée et vérifiable de la banque. Dans q-011 et q-012 aucune variation de données ou de contexte n’est autorisée sans nouvelle revue.
- Les tableaux peuvent être dictés, tapés, construits à l’aide d’objets ou de grandes cases; les étiquettes restent textuelles même lorsqu’une aide visuelle est donnée. Un assistant peut déplacer des objets sur commande sans décider des effectifs.
- Le mot « observation » désigne un enregistrement fictif, pas une personne réelle. Éviter tout renseignement personnel ou matériel dangereux; une variante doit maintenir les mêmes contraintes mathématiques et le même degré de difficulté.

## Contrôle humain requis

La cohérence mathématique du générateur et des corrigés est soumise à tests dans `livraison/VALIDATION.md`. La clarté linguistique, les adaptations pour les besoins particuliers, le biais des exemples, l’ergonomie, la durée et les seuils de jugement nécessitent une revue d’enseignement. Aucun item n’est « certifié » ni officiellement homologué.
