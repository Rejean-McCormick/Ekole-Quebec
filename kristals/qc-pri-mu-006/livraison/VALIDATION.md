# Validation de livraison — `qc-pri-mu-006` (v1.2)

## Périmètre effectivement contrôlé

Le script de fabrication a exécuté les tests automatiques suivants sur les 14 fichiers destinés à l'archive (et de nouveau sur les entrées du ZIP final) :

1. Lecture réelle de la gouvernance v1.2, du graphe, du parcours original, du contrat source, de l'alignement et du brief dans le ZIP source contenant le workspace v1.2; vérification de l'identité, de l'objectif et des relations dans le graphe.
2. Conservation de **tous les champs YAML d'origine**, dans le même ordre et avec les mêmes valeurs; présence et unicité des 12 titres de sections numérotés; conservation des champs JSON et propriétés des objets originaux, enrichissement sans suppression.
3. Cohérence des chaînes immuables, liens `requires` et `recommends_before`, type de famille, `obj-1` et `crit-1`; aucune référence à un autre Kristal hors liens pédagogiques autorisés.
4. Validité des deux JSON de production et du manifeste; dix items distincts et numérotés `q-001` à `q-010`, avec champs contractuels et modes fixes `seed`/`parametres` nuls; deux contextes de maîtrise séparés q-009 et q-010.
5. Relecture par règles de cohérence des modèles d'attaque `X` et silence `.`, quatre positions par segment, couverture des quatre notions, trois activités guidées, quatre autonomes, deux diagnostics et deux transferts.
6. Contrôle des termes de sécurité, d'accessibilité, des droits, du statut `a_revoir` et de la distinction entre corrigé ouvert critérié et réponse verrouillée pour les cellules prédéfinies.
7. Création et réouverture du ZIP : **exactement 14 fichiers non vides** et tous sous `kristals/qc-pri-mu-006/` à la racine, aucun dossier englobant, aucune entrée absolue ni `../`, premier chemin conforme, CRC intègres, manifeste identique aux entrées.

## Limites qui demeurent (non validées automatiquement)

- Une validation automatisée ne prouve **ni** la qualité artistique, **ni** la facilité réelle d'écoute ou d'exécution, **ni** la fiabilité interévaluateurs de la grille. Aucune audition humaine d'élèves ni essai en classe n'a été réalisée.
- Les réponses ouvertes n'admettent pas de correction unique : la grille a été conçue, mais non calibrée par plusieurs correcteurs. Aucun générateur aléatoire ni solveur de performance musicale n'a été employé.
- Aucun audio réel n'étant livré, aucune mesure acoustique, test de décibels, contrôle d'un périphérique ou essai de dispositif d'accessibilité n'a été effectué.
- Aucune certification, homologation ni alignement détaillé au PFEQ ne sont revendiqués. Le contenu, les grilles et la banque sont encore à revoir humainement.

## Revue humaine obligatoire avant qualification

- Spécialiste en musique primaire : faisabilité des 12 pulsations, distinction audible de variation/contraste, cohérence des exemples et temps nécessaire.
- Personne experte en accessibilité : faisabilité des adaptations visuelles, auditives, tactiles et techniques, sécurité sonore, maintien de l'autonomie créative.
- Évaluateurs indépendants : test à blanc de q-009 et q-010 et accord interjuge sur R, O, M, I, D; vérification que les scénarios ne favorisent pas une culture ou une physiologie particulière.
- Responsable des droits/confidentialité : autorisations si des enregistrements, voix, samples ou œuvres tierces sont ajoutés ensuite.

## Propositions non exécutées sur la structure centrale

1. Éventuellement normaliser `family_id`, `seed=null` et la représentation des rubriques par schéma JSON public stable; seule la famille de ce Kristal est enrichie ici.
2. Éventuellement ajouter un champ runtime de **modalité d'accessibilité** distinct du niveau de soutien artistique, pour éviter de confondre assistance technique et guidage cognitif.
3. Éventuellement associer à chaque tâche les emplacements de traces dans le LMS; aucune création dans `runtime/`, `state/`, `registry/`, `canon/` ou `governance/` n'est effectuée.

## Résultat des contrôles exécutés

**Bilan avant fermeture de l’archive :** 106 contrôles programmatiques réussis sur le contenu et le manifeste, incluant les contrôles unitaires des 10 items. Les vérifications d’intégrité du ZIP sont exécutées après écriture et répétées sur l’archive fermée. Aucune audition humaine n’est comptée comme test.
