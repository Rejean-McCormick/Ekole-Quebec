# Validation technique et limites — qc-pri-st-018
**Base :** archive `initbundle(1).zip`, sous-racine `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. **Statut :** `controles_techniques_effectues_revue_humaine_requise`, pas de certification.

## Contrôles réellement exécutés avant le ZIP
**43 assertions nommées réussies**, dont **12 variantes de contexte effectivement parcourues** à corrigé verrouillé (4 items × 3 cas). Les contrôles d'exécution sont définis dans le script local de construction; seul le présent document de résultats est livré.

1. OK — 14 chemins de manifeste exacts et uniques.
2. OK — Identité et version du manifeste.
3. OK — 14 fichiers attendus (12 avant rapport final) non vides.
4. OK — Banque et contrat au format JSON strict.
5. OK — Identifiants fixes de la banque.
6. OK — 12 items sans doublon, numéro séquentiel.
7. OK — Champs obligatoires et rétroactions de chaque item.
8. OK — Chaque item lié à obj-1, crit-1 et à la famille.
9. OK — Modes fixés aux trois valeurs admises, statuts a_revoir.
10. OK — Deux preuves autonomes distinctes et fixes.
11. OK — Corrigés des deux preuves contiennent étapes clés.
12. OK — Aucune variation non contrôlée.
13. OK — Scénario 007 : graine, stimulus et exemple calculé.
14. OK — Scénario 007 variante 0 : corrigé invariant, situation unique.
15. OK — Scénario 007 variante 1 : corrigé invariant, situation unique.
16. OK — Scénario 007 variante 2 : corrigé invariant, situation unique.
17. OK — Scénario 008 : graine, stimulus et exemple calculé.
18. OK — Scénario 008 variante 0 : corrigé invariant, situation unique.
19. OK — Scénario 008 variante 1 : corrigé invariant, situation unique.
20. OK — Scénario 008 variante 2 : corrigé invariant, situation unique.
21. OK — Scénario 009 : graine, stimulus et exemple calculé.
22. OK — Scénario 009 variante 0 : corrigé invariant, situation unique.
23. OK — Scénario 009 variante 1 : corrigé invariant, situation unique.
24. OK — Scénario 009 variante 2 : corrigé invariant, situation unique.
25. OK — Scénario 010 : graine, stimulus et exemple calculé.
26. OK — Scénario 010 variante 0 : corrigé invariant, situation unique.
27. OK — Scénario 010 variante 1 : corrigé invariant, situation unique.
28. OK — Scénario 010 variante 2 : corrigé invariant, situation unique.
29. OK — Tous les champs originaux conservés à la racine du contrat.
30. OK — Famille originale et génération préservées (sous-ensemble sans mutation).
31. OK — Champs requis par gouvernance présents dans la famille.
32. OK — Aucun prérequis bloquant; ordre conseillé inchangé.
33. OK — Frontmatter YAML original préservé mot pour mot.
34. OK — 12 sections du parcours en place, ordonnées.
35. OK — Objectif/preuve exacts rappelés dans le parcours.
36. OK — 2 tâches diagnostiques, 3 exercices guidés, 4 autonomes, 2 transferts.
37. OK — 2 exemples et au moins 2 contre-exemples.
38. OK — Plan d’évaluation nomme chacun des 12 items.
39. OK — Liens locaux au sein des documents sont valides.
40. OK — Règles de sécurité/accessibilité/référence présentes.
41. OK — Droits et limites explicitement documentés.
42. OK — Références externes HTTPS et identifiées.
43. OK — Aucun autre Kristal dans les fichiers prévus.

## Vérification scientifique éditoriale (non automatique)
Les réponses des items ont été rédigées en se fondant sur les faits vérifiés des sources NHLBI, NIDDK et NIAMS. Les assertions précédentes vérifient la présence, la cohérence formelle et l'invariance des corrigés du corpus; **elles ne prouvent pas automatiquement la justesse scientifique d'une rubrique**, qui demeure à revoir par une personne qualifiée.

## Contrôles du ZIP et de la fusion
Contrôle final prévu puis exécuté après fabrication : compte et nom exacts des 14 entrées, préfixe exclusif `kristals/qc-pri-st-018/`, absence de chemins absolus, de `../` et de dossier enveloppant; JSON analysables; manifeste conforme au ZIP; CRC intégral. Aucune donnée de la gouvernance/du registre ni de Kristal voisin n'est incluse. Voir résultat imprimé par le script de vérification d'archive.

## Revue humaine encore requise
- Vérifier exactitude anatomique, nuances « mouvement / besoin vital », formulation et charge de lecture selon l'âge réel des élèves.
- Relire les 12 stimuli et rubriques, les réponses équivalentes possibles, les deux preuves autonomes, les biais et la durée; essai en classe avant usage sommatif.
- Vérifier la possibilité de répondre oralement, avec cartes tactiles, scripteur et aides neutres; documenter les modalités réellement utilisées.
- Vérifier les droits du workspace maître et les usages publics des contenus; aucune image/source tierce n'a été copiée dans le delta.
- Vérifier le comportement du moteur Kristal après **fusion réelle**, non simulée ici : aucune commande `check`, `build-v9`, `check-ai` ni qualification n'a été lancée.

## Propositions de structure **non appliquées**
1. Ajouter ultérieurement au schéma central une métadonnée `mode_reponse_accessible` pour les schémas oraux/tactiles.
2. Ajouter une option `corpus_controle` documentée dans le schéma d'examen pour verrouiller les variations de scénarios.
3. Ajouter un état `revue_scientifique_humaine` distinct des contrôles techniques.
Aucun fichier central n'est modifié. Aucun statut publié, homologué ou certifié n'est revendiqué.
