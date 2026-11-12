# Rapport de validation — qc-pri-ale-007 — livraison v1.2

**Périmètre :** un seul Kristal, `qc-pri-ale-007`; delta de 14 fichiers sous `kristals/qc-pri-ale-007/`. **État :** `a_revoir`, non publié, non homologué, non certifié.

## Origine et invariants vérifiés

- Lu dans l'archive maîtresse : contrat v1.2, générateur/examens, charte de conversion, graphe, `PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`.
- Conservé : ID `qc-pri-ale-007`, titre « Apprécier la littérature de langue anglaise », discipline ALE, objectif `obj-1`, preuve `crit-1`, concepts `theme / narrative choice / textual evidence`, famille `qc-pri-ale-007-ev-01`, prérequis strict `qc-pri-ale-004`, aucun ordre conseillé ni autre lien.
- `PARCOURS.md` : mêmes clés YAML et mêmes valeurs canoniques; seule `revision_contenu` passe de `0.2.0` à `0.3.0` pour refléter le texte livré. Les 12 sections restent numérotées dans l'ordre.
- `CONTRAT_PEDAGOGIQUE.json` : anciens champs et anciennes valeurs préservés; ajouts non destructifs des champs du générateur dans la famille unique.

## Tests réellement exécutés par script avant emballage

- 47 assertions de préparation réussies : métadonnées, graphe, dix IDs uniques, JSON, familles, prérequis, dix stimulis fixes, contextes distincts, références de lignes dans les bornes, supports pédagogiques et sécurité des chemins.
- Test de limite **automatisable seulement** : les numéros de ligne repérés dans les corrigés sont dans les bornes des œuvres. Cela ne prouve pas, à lui seul, la justesse de chaque interprétation.
- Les textes sont des créations originales du présent livrable; les recommandations externes sont référencées, et non reproduites. Aucun contrôle de droits externe exhaustif n'a été mené.

## Contrôles de ZIP consignés après construction

Voir ci-dessous l'attestation produite par la routine de contrôle de l'archive; celle-ci teste la liste exacte des 14 entrées, la racine, les octets non vides, les JSON relus, le manifeste et le CRC. **Le journal terminal** constitue la trace d'exécution.

## Couverture du contenu

- Notions : thème, procédé narratif/poétique, preuve textuelle, différence résumé/appréciation; 2 démonstrations détaillées et 4 contre-exemples.
- Diagnostic : 2 textes et décisions d'appui; pratiques : 3 guidées à indices dégressifs, 4 autonomes, 2 transferts distincts.
- Évaluation : 10 tâches avec réponses exemplaires et rubriques (8 formatives, 2 preuves sur récit et poème). Toutes `a_revoir`, aucune variante paramétrique non contrôlée.
- Maîtrise : deux preuves autonomes de genres et contextes différents avec niveaux C1–C4 documentés; pas de décision sur une note unique.

## Limites non résolues et revue humaine obligatoire

1. Faire relire l'anglais des quinze textes originaux, les nuances de thème et les corrigés par un professionnel anglophone compétent en littératie du primaire. Les interprétations fournies ne sont **pas** des réponses exclusives.
2. Vérifier l'adéquation du niveau de vocabulaire, la durée, l'accès aux textes avec lecteurs d'écran et l'équité linguistique auprès du public cible. Aucun essai d'administration avec élèves n'a été mené.
3. Calibrer les quatre dimensions de la grille entre au moins deux évaluateurs sur des exemples réels; aucune mesure d'accord interjuges n'a été produite.
4. Examiner les droits et modalités de publication selon les politiques du projet; aucune expertise juridique n'a été menée.
5. Vérifier en intégration la résolution des références relatives dans le LMS; **aucun test de LMS/framework externe** n'a été effectué.
6. Ne pas utiliser une génération IA libre pour approuver des changements d'items; les stimuli demeurent fixes, et une variante exigerait une revue humaine et une nouvelle version.

## Propositions de structure (non appliquées)

- Centraliser éventuellement un identifiant stable de chaque passage littéraire et ses numéros de lignes pour éviter les divergences entre correction et stimulus.
- Documenter dans un adaptateur LMS le niveau d'étayage réel, les transcriptions et les niveaux de chaque preuve sans introduire ces données dans le canon.
- Ajouter plus tard un jeu de calibration humaine des rubriques et des versions de textes accessibles; **aucun fichier de gouvernance, canon, runtime, state, registry ou autre Kristal n'a été modifié ici**.
