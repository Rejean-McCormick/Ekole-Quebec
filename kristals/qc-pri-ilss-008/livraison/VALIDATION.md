# Rapport de validation de livraison — `qc-pri-ilss-008`

**Statut :** `controles_techniques_executes_revue_pedagogique_humaine_requise` — aucun statut « publié », « homologué » ou « certifié ».

## Travail effectivement réalisé

- Consultation dans le ZIP source de la gouvernance v1.2, du graphe, du parcours et du contrat d'origine, des fichiers `ALIGNEMENT.md` et `BRIEF_REDACTION.md`.
- Préservation **identique** du frontmatter YAML canonique et des 12 sections numérotées, remplacées par une rédaction complète sans modifier les champs/ID établis.
- Conservation de la structure de famille `qc.education-assessment-blueprint/1.2` et de ses champs natifs, avec ajout des paramètres exigés par le générateur.
- Production de 6 documents de contenu, de 12 items d'évaluation fixe et d'une grille à deux preuves distinctes.

## Contrôles automatisés **exécutés**

- **Réussi :** YAML original conservé à l’octet près; 12 sections numérotées consécutives; identité, notions et préalables.
- **Réussi :** Contrat JSON conservant tous les champs v1.2, génération native et famille complète.
- **Réussi :** Graphe source : les deux requires stricts, aucun lien conseillé ou transfert.
- **Réussi :** 12 items JSON stricts, IDs uniques ordonnés, 12 stimuli distincts, modalités fixe, rubriques complètes.
- **Réussi :** Contrôles numériques déterministes de 4 exemples et assertions de concordance stimulus/corrigé.
- **Réussi :** Couverture mécanique : 2 exemples, 2 contre-exemples, 2 diagnostics, 3 guidées, 4 autonomes, 2 transferts, rappel.
- **Réussi :** Références : liens au workspace source, préalables déclarés et ressources de la famille présents.
- **Réussi :** Sécurité/accessibilité : gardes-fous explicites; pas de média tiers embarqué; provenance déclarée.
- **Réussi :** Manifeste : base 1.2, format, ID, racine et liste ordonnée des 14 chemins.
- **Réussi :** 14 fichiers non vides, aucun fichier étranger ou chemin dangereux; 3 JSON parsables.

## Vérifications manuelles de conception, distinctes de tests automatisés

- **Corrigés :** seuls les faits numériques, associations citées et calculs déterministes simples font l'objet d'assertions; les exemples de textes sont des productions recevables et non des réponses uniques. Une correction critériée humaine demeure indispensable.
- **Deux contextes :** `q-011` est un compte rendu scientifique fictif de feuilles (3 puis 5); `q-012` est une communication mathématique fictive sur des emprunts (8, 11, 9). La maîtrise n'est pas attestée tant que deux textes d'élève autonomes n'ont pas été observés.
- **Droits :** les textes et données ont été rédigés pour ce Kristal; aucun média tiers n'est empaqueté. Aucun audit juridique externe n'a été mené.
- **Accessibilité :** garde-fous écrits (oral de compréhension, clavier, langues de planification, tableaux linéarisés, critères sur sens et organisation). Aucun test de lecteur d'écran ou test élève réalisé.

## Limites et revue humaine obligatoire

1. Faire relire par une personne experte en ILSS et en évaluation de l'écriture les tâches, contre-exemples, rubriques et seuils C1–C4; vérifier l'équité pour les élèves plurilingues sans inférence sur l'origine familiale.
2. Essayer les tâches auprès d'élèves avec modalités d'accès variées; examiner si les deux preuves sont suffisamment indépendantes et si les consignes n'entraînent pas une surcharge de lecture.
3. Tester l'import dans le vrai workspace / LMS, la lisibilité du français et la conversion des tableaux accessibles. Aucune intégration sur une instance active n'a été faite.
4. Examiner si les textes témoins excluent involontairement des formulations correctes; calibrer les jugements entre correcteurs. Ne pas qualifier les items de « certifiés ».
5. Réexaminer les droits si des sources tierces, des images ou des textes externes sont ajoutés après fusion.

## Suggestions de changements structurels **non effectués**

- Dans une future évolution versionnée de la gouvernance, normaliser `preuve_maitrise` (contexte, conditions d'autonomie, trace de soutien), établir un protocole de calibration de la grille et ajouter des contrôles LMS pour la traçabilité des adaptations. Aucun fichier central ni aucun autre Kristal n'est inclus ou modifié.
