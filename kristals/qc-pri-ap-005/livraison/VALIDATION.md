# VALIDATION DE LIVRAISON — `qc-pri-ap-005` (v1.2)

## Provenance, périmètre et état

- **Source effectivement consultée :** arborescence `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` incluse dans le ZIP de conversation `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`; les huit documents imposés ont été extraits et lus. L'archive `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` en fichier autonome n'était pas présente, mais son arborescence et ses métadonnées l'étaient.
- **Delta prévu :** 14 fichiers non vides sous `kristals/qc-pri-ap-005/` seulement; deux remplacements (`authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`), 12 nouveaux fichiers. Aucun objet canonique, registre, norme, autre Kristal, `kristal.workspace.json` ou `AGENTS.md` modifié.
- **Statut pédagogique :** rédaction complète au niveau prévu, **à revoir humainement**, non publiée, non homologuée, non certifiée; l'enrichissement ne change pas l'état de publication local du workspace.

## Contrôles techniques et de cohérence exécutés

Les contrôles ci-dessous sont des assertions Python exécutées localement sur les fichiers préparés, avec analyse YAML (`PyYAML`) et JSON (`json`). Une vérification technique n'est pas une étude de fidélité intercorrecteurs ou une validation didactique sur élèves.

1. **RÉUSSI** — Source cible et 8 références normatives/locales disponibles.
2. **RÉUSSI** — Source originale YAML parsable.
3. **RÉUSSI** — YAML final parsable et champs/valeurs originaux identiques.
4. **RÉUSSI** — PARCOURS a exactement 12 sections numérotées dans ordre.
5. **RÉUSSI** — PARCOURS sans placeholders rédactionnels.
6. **RÉUSSI** — Identité du titre et discipline à source.
7. **RÉUSSI** — Objectif observable immuable cohérent.
8. **RÉUSSI** — Critère de preuve immuable cohérent.
9. **RÉUSSI** — Trois concepts natifs exacts et dans l’original.
10. **RÉUSSI** — Liens préalables et conseillé conservés.
11. **RÉUSSI** — Liens sortants réellement attestés au registre.
12. **RÉUSSI** — Contrat préserve clés top-level natives.
13. **RÉUSSI** — Contrat conserve identifiants et famille native.
14. **RÉUSSI** — Contrat conserve les sous-champs natifs famille et generation.
15. **RÉUSSI** — Contrat 13 clés minimum générateur complètes.
16. **RÉUSSI** — Contrat rubrique possède 4 dimensions et 4 niveaux.
17. **RÉUSSI** — Banque format/identité et famille stricts.
18. **RÉUSSI** — Au moins 8 items et dix numéros consécutifs distincts.
19. **RÉUSSI** — Chaque item contient champs contractuels complets.
20. **RÉUSSI** — Chaque item est lié à obj-1/crit-1/famille.
21. **RÉUSSI** — Modes/seed/paramètres cohérents, statuts prudents.
22. **RÉUSSI** — 10 stimuli distincts, aucune consigne dupliquée.
23. **RÉUSSI** — Deux preuves indépendantes sur contextes distincts.
24. **RÉUSSI** — Corrigés critériés observables plutôt que réponse esthétisante.
25. **RÉUSSI** — Corrigés de maîtrise intègrent D1–D4 et autonomie.
26. **RÉUSSI** — 2 exemples commentés et 2 contre-exemples présents.
27. **RÉUSSI** — 2 diagnostics présents.
28. **RÉUSSI** — 3 exercices guidés indices dégressifs présents.
29. **RÉUSSI** — 4 exercices autonomes avec critères présents.
30. **RÉUSSI** — 2 transferts rédigés en contextes distincts.
31. **RÉUSSI** — Feedback ciblé, rappel différé et modalités accessibles.
32. **RÉUSSI** — Fichiers prose de plan, grille et droits non vides.
33. **RÉUSSI** — Droits tiers et statut de revue explicités.
34. **RÉUSSI** — Aucun ID Kristal tiers sauf liens autorisés.
35. **RÉUSSI** — Plan lie tout item à famille, obj-1 et crit-1.
36. **RÉUSSI** — Grille contient deux preuves, seuil, sécurité et remédiation.
37. **RÉUSSI** — Aucun fichier libre ou fichier d’un autre Kristal dans arborescence de production.
38. **RÉUSSI** — MANIFEST exact et statut non certifié.

## Contrôle ZIP exécuté lors du conditionnement

- Entrées stockées sans répertoires explicites : première entrée `kristals/qc-pri-ap-005/authoring/PARCOURS.md`.
- Test du nombre exact **14**, identité des chemins avec le manifeste, absence de doublons, de chemin absolu ou traversée `../`, fichiers non vides, intégrité CRC du ZIP et JSON reparsés après extraction en mémoire.
- Les nombres et résultats déclarés dans ce paragraphe ont été contrôlés par le script de conditionnement, et non évalués seulement par inspection visuelle.

## Contrôles éditoriaux menés, limites et revue humaine

**Revue rédactionnelle locale (non certification) :** l'objectif, la preuve, l'identité, les préalables et les liens ont été confrontés aux sources; les exemples de production ne sont jamais des solutions esthétiques obligatoires; les réponses des dix items sont des traces observables/critères, non un corrigé mathématique unique; aucune assertion sur une symbolique universelle des couleurs. Des matériaux non toxiques et des modalités de communication accessibles sont précisés. Aucun outil dangereux ni fichier média externe n'est distribué. Cette revue éditoriale et les tests de présence ne démontrent pas que l'évaluation est fidèle et équitable auprès de vrais élèves.

**Non réalisés :** test utilisateur/élèves, validation par un spécialiste des arts et de l'accessibilité, test intercorrecteurs des niveaux de la grille, validation psychométrique, audit approfondi des licences de toute illustration ajoutée ultérieurement, test d'intégration LMS, publication et audit PFEQ. Aucun cas réel de maîtrise ou de rappel différé n'a été observé. Les adaptations locales liées à la motricité et les politiques de confidentialité des créations doivent être confirmées par l'établissement.

**Revue humaine requise avant qualification :** (1) cohérence didactique et compréhension du vocabulaire, (2) impartialité de la grille et accord entre correcteurs sur des productions réelles, (3) pertinence des délais et des dix tâches, (4) sécurité des matériels et accès non discriminant, (5) droits/confidentialité en cas d'ajout de médias et de diffusion des productions, (6) validation des deux épreuves maîtresses et d'une variante de remplacement si remédiation.

## Propositions sans changement central effectué

- Proposer ultérieurement au mainteneur un schéma explicite pour `critere_id`, `representation`, `variabilite_permise`, `statut_preuve` et `contexte_maitrise` dans les items, sans modifier les registres ni générer des arêtes.
- Ajouter au niveau de l'application un journal protégé des preuves A/B et aides d'accès, distinct du contenu canonique; les deux preuves ne doivent pas être publiées automatiquement.
- Prévoir une procédure de création **révisée** d'une tâche alternative après remédiation; aucune génération IA libre n'est admise comme source de notation fiable.

## Fusion dans le workspace existant

Après extraction du ZIP maître et entrée dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, décompresser `qc-pri-ap-005_livraison_v1.2.zip` **à cet endroit**. Le chemin racine interne est `kristals/qc-pri-ap-005/` et seuls les deux fichiers d'auteur existants sont remplacés. Les douze autres sont des ajouts. Ne pas extraire dans un second dossier `Frames_.../`.
