# Validation de livraison — `qc-pri-us-012`

**Statut :** matériel rédigé, tests techniques documentés ci-dessous au terme de leur exécution, validation pédagogique et historique humaine requise. Ne constitue pas une publication certifiée ni une homologation PFEQ.

## Règles de l’archive

Le ZIP contient seulement `kristals/qc-pri-us-012/` et exactement 14 fichiers : deux fichiers `authoring/` remplacés intégralement, 12 fichiers ajoutés. Le JSON des familles est enrichi sans changer les valeurs canoniques. Aucune modification du registre, de la gouvernance, du canon, des autres Kristals ni de `ALIGNEMENT.md` ou `BRIEF_REDACTION.md`.

## Contrôles effectivement réalisés

- **652 assertions documentaires pré-fusion réussies** : arborescence 14 fichiers, YAML valide (clés/valeurs canoniques conservées), douze sections, JSON du contrat, de la banque et du manifeste valides, liens du graphe, dix items distincts, corrigés et années des 9 cartes, provenance S1–S9, deux preuves autonomes aux thèmes et événements distincts, accessibilité et droits déclarés.
- **7324 assertions supplémentaires de fusion réussies**, dont vérification SHA-256 de **7320 fichiers existants protégés**, et simulation de **2 remplacements + 12 ajouts**, aucun autre contenu préexistant modifié. Le test a extrait l’archive source v1.2 dans un dossier temporaire et superposé exactement les 14 fichiers.
- **Qualité des corrigés** : chaque item cite les bonnes années en ordre croissant, les cartes fournies portent leur code source; les réponses et liens sont rédigés et contrôlés formellement. Le contrôle des causalités et interprétations reste soumis à la revue historique humaine. Pas de générateur aléatoire ni de « corrigé IA » libre.
- **Sources / droits** : vérification externe documentaire des sources institutionnelles et de la Nation crie, liste de provenance et limites; aucun extrait long, photo, musique ou licence tierce incorporés. Pas d’audit juridique formel.
- **ZIP final** : validation de taille, 14 chemins, JSON dans archive, correspondance du manifeste et test CRC complétés après empaquetage (résultat confirmé par le script de construction).

## Limites non résolues

- Corpus sélectif 1936–1977, et non récit exhaustif des sociétés québécoises du XXe siècle; la portée de la documentation de la Nation crie ne doit pas être généralisée à toutes les communautés.
- Les cartes-sources sont des synthèses postérieures avec références et ne valent pas témoignages contemporains; leurs liens doivent être relus par une personne compétente en histoire.
- Deux contextes de maîtrise ont un protocole interne et une grille non étalonnés, sans validation intercorrecteurs ni mise à l’essai réelle.
- Les supports de lecture, les obstacles linguistiques et les sensibilités culturelles doivent faire l’objet d’adaptations et d’une consultation en contexte éducatif.
- Aucun matériel externe sous licence (image, photo, document d’époque) livré; futurs ajouts nécessiteraient vérification des droits et du consentement.

## Revue humaine obligatoire avant qualification

1. Historien ou historienne : dates, nuance des interprétations, portée de la législation et relations entre les événements.
2. Ressources autochtones et didactiques : vérifier que la présentation de la convention de 1975 respecte les perspectives pertinentes; examiner les limites du corpus.
3. Enseignant et responsable de l’évaluation : clarté des consignes, juste charge documentaire, validité des deux preuves, cohérence et fiabilité de la rubrique.
4. Accessibilité et droit : équivalence des modalités orale/tactile/numérique, citations et usage futur des supports.

## Propositions de structure, sans modifier les fichiers centraux

- Normaliser dans une prochaine version un champ de type `document_source` (producteur, nature primaire/secondaire, date du fait, date de publication, URL et portée de l’interprétation).
- Prévoir dans la future banque une ontologie explicite de liens `chronologique`, `thematique_source`, `causal_documente` pour éviter d’assimiler ordre et cause.
- Ajouter un protocole de revue des perspectives et de la représentativité des sources sans créer de nouvelle dépendance au graphe.
