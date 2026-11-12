# Plan d'évaluation — `qc-pri-us-003-ev-01`

**Identité et périmètre :** `qc-pri-us-003`, `obj-1` — « Caractériser un territoire par ses ressources et les usages humains observables. »; `crit-1` — « Produire une carte annotée reliant ressources et activités. » Aucun préalable `requires`; `qc-pri-us-002` est un ordre conseillé non bloquant.

**Cible :** relief, climat (et distinction avec la météo), ressources, occupation; décrire un territoire **d'après une source située/datée**, construire une carte avec légende et justifier les relations. Scénarios uniquement **fictionnels, datés éditorialement du 8 octobre 2026**, non relevés publics ni témoignages historiques.

## Matrice d'alignement, difficulté et représentations

| Item | Objectif | Critère | Famille | Difficulté | Représentation et compétence observée |
|---|---|---|---|---|---|
| q-001 | obj-1 | crit-1 | qc-pri-us-003-ev-01 | initial | fiche / position relief et occupation |
| q-002 | obj-1 | crit-1 | qc-pri-us-003-ev-01 | initial | fiche climatique / distinguer météorologie |
| q-003 | obj-1 | crit-1 | qc-pri-us-003-ev-01 | initial | lecture critique / fait et hypothèse |
| q-004 | obj-1 | crit-1 | qc-pri-us-003-ev-01 | intermediaire | carte 3×3 / ressources et activités |
| q-005 | obj-1 | crit-1 | qc-pri-us-003-ev-01 | intermediaire | correction de carte / localisation et limites |
| q-006 | obj-1 | crit-1 | qc-pri-us-003-ev-01 | intermediaire | carte / annotations et sources |
| q-007 | obj-1 | crit-1 | qc-pri-us-003-ev-01 | transfert | **Preuve 1** : carte rurale Val-des-Saules |
| q-008 | obj-1 | crit-1 | qc-pri-us-003-ev-01 | transfert | **Preuve 2** : carte littorale Port-aux-Roches |
| q-009 | obj-1 | crit-1 | qc-pri-us-003-ev-01 | transfert | territoire forestier / variante de ressources |
| q-010 | obj-1 | crit-1 | qc-pri-us-003-ev-01 | transfert | territoire urbain / perspective temporelle et limites |

Tous ces liens sont également présents dans chaque objet JSON (`objectif_id`, `critere_id`, `family_id`). Les tâches courtes vérifient des composantes; **seuls q-007 et q-008** fournissent les deux productions intégrées nécessaires à la décision.

## Corpus contrôlé et diversité

- Modes : `fixe` pour réponses à source immuable; `scenario_controle` pour cartes à fiche fermée. Aucun item paramétrique numérique ni algorithme probabiliste; pas de génération IA libre.
- Les fiches fictives, coordonnées, dates éditoriales, usages **attestés dans les données** et limites sont inclus dans chaque `stimulus` JSON. Toute variante modifiant ces faits demande un nouveau scénario, des solutions recalculées manuellement et une revue.
- `seed` contractuelle stable `1203003` documente la version du catalogue; aucun tirage n'est exécuté. Les IDs de scénario des deux preuves sont verrouillés (`maitrise-val-des-saules` et `maitrise-port-aux-roches`) afin d'éviter deux variantes quasi-identiques.
- Variation autorisée : taille, mode tactile, transcription orale, symboles équivalents, ordre d'énonciation et reformulations correctes. Interdite : changement de cases, d'activités, de climat, de source, de contexte de la maîtrise ou invention d'une justification.

## Administration, barème et maîtrise

- Fournir une grille de 3 colonnes × 3 rangées, N↑. Sources accessibles sur la feuille; 15–25 minutes par carte selon le besoin, temps adaptable. Aucun accès au corrigé, aucune réponse positionnelle soufflée.
- Grille : localisation et signes, qualité des liens ressource/activité, preuves et limites, communication cartographique. Chaque critère niveau 0–3; **niveau ≥ 2 dans les quatre dimensions sur chacun des deux contextes**, autonomie consignée et absence d'affirmation factuelle inventée persistante. Aucun score total unique ne décide de la maîtrise.
- Garder la production ou une transcription fidèle, consigner aides/adaptations, analyser erreurs et reprendre une micro-compétence; une preuve réévaluée doit utiliser un **troisième dossier inédit**, pas le corrigé mémorisé.

## Couverture et protection

- Relief : q-001, 004, 006, 007, 008, 009. Climat : q-002, 005, 007, 008, 010. Ressources/occupations : q-001, 003–010. Sources/limites : q-003, 005, 007–010.
- Aucune adresse privée, photo d'enfant, localisation personnelle ou jugement sur un groupe; scénarios fictifs neutres, sans revendication sur les peuples autochtones. Les espaces ne sont pas présumés vacants ni librement exploitables.
- Accès : cartes en tableau texte ou quadrillage braille/tactile, symboles + mots (non couleur seule), police large, lecture des fiches, dictée de légende, temps adapté. Cote le raisonnement et la position, pas la calligraphie ou l'orthographe.
- Revue humaine encore nécessaire (faits, lecture, biais, niveau de difficulté, confort de l'outil). Aucun examen homologué/certifié.
