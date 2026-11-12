# Rapport de validation — `qc-pri-fr-008` / v1.2

**Statut de livraison :** delta techniquement contrôlé, contenu et items **à revoir** par une personne qualifiée. Ne pas utiliser « certifié », « homologué » ou « publié ».

## Contrôles réellement exécutés
- **251 assertions préarchivage exécutées et réussies** par `validate.py` : présence des huit sources v1.2, conservation du frontmatter YAML source, 12 sections dans l’ordre, JSON strict, champs d’authoring v1.2 conservés, objective/proof et prérequis exacts, graphe `requires(qc-pri-fr-008,qc-pri-fr-005)`, famille `qc-pri-fr-008-ev-01` et champs complets.
- Banque de **10 items** fixes contrôlés (`q-001` à `q-010`) avec consignes, récits, corrigés et critères rédigés, sans doublons ni génération aléatoire. Deux preuves différentes sont réservées (`q-009` bibliothèque; `q-010` belvédère).
- Vérification **structurelle** des corrigés, rubriques, marqueurs d’accessibilité et des liens internes; la relecture éditoriale des intrigues est effectuée par rapport à leurs seuls textes originaux, **sans** test auprès d’élèves.
- Vérifications finale du ZIP (réalisées à la fin du même script, avec interruption sur échec) : **14 fichiers non vides exactement**, chemin racine `kristals/qc-pri-fr-008/`, noms manifestes concordants, aucune traversée `../`, JSON décodables, CRC correct, aucune entrée hors périmètre.
- Simulation de fusion par superposition du delta au dossier Kristal v1.2 existant : deux fichiers d’authoring remplacés, 12 ajoutés, et fichiers protégés préservés par comparaison SHA-256. Aucun workspace central ou autre ID inclus dans l’archive.

## Limites non résolues et points de revue humaine
1. Faire relire les dix récits et les justifications causales par une personne experte du français québécois et de l’enseignement de la lecture. Une formulation équivalente doit rester admissible; distinguer cause attestée et inférence plausible.
2. Vérifier la compréhension réelle des consignes et la durée d’administration chez des élèves de niveaux variés, puis réaliser une analyse d'accord entre correcteurs sur les quatre dimensions.
3. Tester les modalités d’accessibilité : lecture neutre, production à l’oral/dictée, schéma manipulable et soutien au décodage sans souffler les liens de causalité.
4. Vérifier les droits si le propriétaire redistribue le workspace au-delà de sa licence; les récits sont créés dans ce delta, les métadonnées conservées proviennent de l’archive maître fournie. Aucun livre, image ou contenu extérieur reproduit.
5. Aucun examen certifié, test LMS, essai empirique, analyse psychométrique, ni alignement détaillé au PFEQ n’a été effectué.

## Propositions de structure — non appliquées
- Considérer à l’échelle du programme un champ facultatif `evidence_quote` pour chaque flèche causale, plus une annotation `chronologie_vs_causalite`, avec schéma versionné seulement après revue collective.
- Définir une procédure commune de validation intercorrecteurs et de conservation des deux productions hors du canon. Aucun registre, gouvernance, document d’alignement ni dossier d’un autre Kristal n’est modifié.
