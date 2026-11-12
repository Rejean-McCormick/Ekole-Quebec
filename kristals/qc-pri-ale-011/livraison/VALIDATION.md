# VALIDATION — `qc-pri-ale-011` — delta v1.2

## Source réellement disponible et périmètre

L'archive autonome nommée `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` n'était pas présente en fichier indépendant. L'arborescence **`Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`** était réellement contenue dans le ZIP de conversation `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip` et a permis de lire les huit fichiers sources exigés, le document de références de méthode ainsi que `sources/source-catalog.json`. Aucune métadonnée de remplacement n’a été inventée.

La livraison est **un delta uniquement** de 14 fichiers sous `kristals/qc-pri-ale-011/` : deux remplacements complets (`authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`), douze créations. Aucun fichier central ni voisin n'a été modifié ou empaqueté. Le front matter YAML et les attributs JSON v1.2 sont restés identiques; de nouveaux champs de famille ont été ajoutés sans effacer la structure native.

## Contrôles locaux effectivement exécutés

Assertions exécutées via Python avec parsing JSON natif et PyYAML; les corrigés de tâches ouvertes ont été comparés à leurs contraintes écrites, **mais pas évalués statistiquement**. Les contrôles techniques ne valent ni calibration intercorrecteurs ni essai élève.

1. **OK** — Les 8 fichiers normatifs/cibles requis sont disponibles.
2. **OK** — Source YAML parse.
3. **OK** — YAML final parse et champs source intégralement inchangés.
4. **OK** — 12 sections numérotées une fois et dans ordre.
5. **OK** — Identité/titre/discipline natifs.
6. **OK** — Objectif et preuve immuables (YAML & contrat).
7. **OK** — Quatre concepts exacts conservés.
8. **OK** — Requires et ordre conseillés exacts.
9. **OK** — Graphe sortant valide sans relation ajoutée.
10. **OK** — Contrat préserve strictement toutes les valeurs natives hors additions famille.
11. **OK** — Famille, objectif et format identiques.
12. **OK** — 13 attributs obligatoires de famille présents et valides.
13. **OK** — Rubrique de famille 4 dimensions et 4 niveaux descriptifs.
14. **OK** — Banque JSON format et identité exacts.
15. **OK** — 10 items numérotés sans doublon.
16. **OK** — Items tous complets et opérationnels.
17. **OK** — Items tous reliés à obj-1/crit-1/famille.
18. **OK** — Aucune génération libre, seed/mode/statut contrôlés.
19. **OK** — Consignes et stimuli non dupliqués.
20. **OK** — Deux épreuves indépendantes, contextes différents.
21. **OK** — Deux types distincts informatif/persuasif et lecteurs différents.
22. **OK** — Deux preuves scorées sur 4 critères D1-D4.
23. **OK** — Exemples de corrigés anglais avec deux paragraphes.
24. **OK** — Contenu 2 modèles commentés et 2 contre-exemples.
25. **OK** — Contenu 2 diagnostics et équivalence attestable.
26. **OK** — 3 exercices guidés et retrait documenté.
27. **OK** — 4 pratiques autonomes avec réponses/critères.
28. **OK** — 2 transferts contextuels et remédiation.
29. **OK** — 4 définitions et progression disciplinaires.
30. **OK** — Rappel différé et accommodations explicites.
31. **OK** — Plan relie explicitement tous les items.
32. **OK** — Grille décision non compensatoire avec 2 preuves.
33. **OK** — Références catégories vérifiées, dérivées, originales, licences.
34. **OK** — Aucun id externe non autorisé dans contenus produits.
35. **OK** — Pas de placeholder ni de faux certificat.
36. **OK** — Manifest contient exactement 14 chemins sous préfixe.

## Contrôles après constitution du delta et du ZIP

Les vérifications suivantes ont été réellement exécutées sur les 14 fichiers assemblés et sur les octets relus dans le ZIP avec `zipfile` (dont contrôle CRC `testzip`). Elles complètent les 36 assertions précédentes :

37. **OK** — Arborescence réelle : 14 fichiers, tous non vides et dans le périmètre autorisé.
38. **OK** — Premier chemin du ZIP au bon emplacement.
39. **OK** — ZIP de 14 fichiers exactement, sans dossier englobant.
40. **OK** — Chemins ZIP sans traversée `../`, chemin absolu ni antislash.
41. **OK** — Entrées ZIP non vides et test CRC sans erreur.
42. **OK** — Les trois JSON stockés dans le ZIP sont parsables et l’identité de la banque est correcte.
43. **OK** — Les 14 chemins du manifeste correspondent aux 14 entrées du ZIP dans leur ordre.

## Limites non résolues et revue humaine obligatoire

- **Non vérifié par essais humains :** adéquation à une cohorte, compréhension des énoncés, équité sociolinguistique, temps de passation, résultats d’élèves, stabilité intercorrecteurs de D1–D4, effets des modalités d’accessibilité sur la comparabilité. Grammaire et fluidité de l’anglais restent à relire par une personne compétente dans les deux langues.
- **Non vérifié par navigation externe :** état des liens EEF, IES/WWC, CAST et éventuels droits de tiers; aucun de leurs extraits n’est reproduit. Seule la présence des références dans le workspace source a été contrôlée.
- **Non exécuté :** tests d’intégration dans LMS/canon/runtime, migration réelle vers le workspace complet, essai de certification ou contrôle PFEQ. Aucune publication, homologation ou certification affirmée.
- **Décision de maîtrise :** suspendue à une correction humaine des deux productions autonomes dans deux contextes, pas au seul passage des tests techniques.

## Propositions de changement de structure — sans toucher aux fichiers centraux

1. Ajouter au schéma central (dans une révision future, après approbation) des champs optionnels de preuve `context_id`, `aides_contenu`, `modalite_acces`, `observations_dimensionnelles` et identifiants de correcteur, afin de distinguer indépendance et accommodations.
2. Documenter dans une évolution versionnée un contrat de double correction pour les tâches langagières ouvertes (comparaison de rubriques et désaccords).
3. Proposer un champ source vérifiable propre aux banques fixes (`scenario_version`, `rubric_version`), sans modifier aujourd'hui `registry/`, `governance/`, `canon/`, `runtime/` ni d'autres Kristals.

**Statut final :** `a_revoir` pour tous les items; tests locaux de cohérence et de conditionnement réussis, revue pédagogique humaine toujours obligatoire.
