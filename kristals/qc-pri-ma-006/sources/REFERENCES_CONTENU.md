# Références, vérifications et provenance — qc-pri-ma-006

## A. Sources locales effectivement lues (vérifiées dans l'archive fournie)

L'archive fournie `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip` contient le dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` et les fichiers ci-dessous. Leur présence et leur texte ont été consultés localement; cela n'est **pas** une vérification indépendante de validité scientifique ou d'homologation.

- `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` : autonomie pédagogique du système, deux preuves contextuelles, distinction du graphe, statut de validation.
- `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` : champs minimum des familles, génération déterministe et revue des corrigés.
- `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` : discipline « Mathématique » et absence de prétention PFEQ.
- `governance/Norme_Pedagogique_Autonome_v1.2/REFERENCES_EVIDENCE.md` : répertoire interne de références IES/WWC, EEF, CAST, UNESCO; **pages externes non ouvertes ou vérifiées** pour ce travail.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` : arêtes `qc-pri-ma-006 -> qc-pri-ma-002` (`requires`), `qc-pri-ma-006 -> qc-pri-ma-003` (`recommends_before`). Leurs statuts sont des décisions internes, pas des relations empiriquement universelles.
- `kristals/qc-pri-ma-006/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` : objectifs, notions, critère, famille et forme du YAML/JSON sources préservés.
- `kristals/qc-pri-ma-006/kristal.workspace.json` : identité locale consultée **sans modification ni inclusion** dans l'archive delta.

## B. Raisonnements dérivés (à partir de définitions et d'arithmétique exacte)

- `14 + 9 = 23`, `38 + 27 = 65`, `26 + 17 = 43`, `24 + 18 = 42`, `37 + 25 = 62`, et les autres résultats sont des conséquences de l'addition entière et de la décomposition (`b = x + y`), non des citations externes.
- Les bornes des générateurs (`q-006`, `q-009`), la sélection par `seed % N`, les filtres et les validations arithmétiques sont **des choix de design originaux**, non issus du programme québécois.
- La séparation entre réunion de groupes disjoints et augmentation d'un état est une explicitation mathématique de ces situations; aucun résultat de recherche extérieur n'a été prétendu pour cette distinction.

## C. Productions originales de ce delta

Tous les énoncés, contextes fictifs (atelier, tracé, trousse, bibliothèque, potager), descriptions de schémas, parcours enseigné, corrections, exercices, grilles, feedbacks et algorithmes de paramétrage de ce delta sont rédigés ici pour `qc-pri-ma-006`. Aucun visuel, image ou extrait textuel tiers n'est réutilisé. Les libellés immuables du mandat et les métadonnées locales proviennent du workspace source.

## D. Droits, limites et emploi

- Pas de reprise d'illustrations, de sujets d'examens tiers ou de contenus sous licence inconnue dans les nouvelles leçons; **cela ne constitue pas un avis juridique sur les droits de l'archive maîtresse**.
- Les URL et organismes listés par la gouvernance sont des pistes bibliographiques internes, pas des sources externes vérifiées par cette livraison. Ne pas transformer des références secondaires en preuve d'un alignement ministériel.
- Une **revue humaine des faits, des droits, de l'accessibilité et du niveau** est requise avant distribution; la réussite des tests locaux n'est pas une certification.
