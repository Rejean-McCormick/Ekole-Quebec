# Validation technique et limites — `qc-pri-ilss-004`

**Statut de livraison :** rédaction complète, items et grille `a_revoir`; non homologué, non certifié. Rapport établi le 8 octobre 2026; contrôles documentaires et de fusion effectivement exécutés.

## Contrôles exécutés et réussis

- **516 assertions de préarchivage réussies** : structure exacte, 14 fichiers non vides, graphes requires/recommends, invariants YAML et JSON, 12 sections, dix items numérotés sans doublons, modes fixes, preuves d'autonomie dans deux contextes, rubriques et références.
- **Contrat natif :** toutes les clés racines et clés de famille existantes ont été préservées; l'objectif, la preuve, les concepts, l'identifiant de famille, le préalable strict `qc-pri-ilss-001` et l'ordre conseillé `qc-pri-ilss-003` restent inchangés.
- **Contrôle déterministe des corrigés :** pour chacun des dix stimulus fixes, les valeurs essentielles des réponses ont été recherchées dans le texte fourni (vérification de fragments littéraux, pas un essai psychométrique). Les deux preuves utilisent des documents différents et des cases/segments référencés.
- **Simulation de fusion du workspace complet :** 2 anciens fichiers `authoring/` remplacés, 12 fichiers ajoutés; **7355 fichiers maîtres protégés** sont préservés octet par octet sur la base de SHA-256. Aucun autre ID ni base centrale n'est compris dans le delta.
- **Droits et sécurité documentaire :** textes originaux et références déclarées; absence de documents scolaires réels ou de données personnelles, pictogrammes décrits en texte, aucun média tiers. Les limites de droits et d'accessibilité sont explicites.
- **Contrôle de l'archive finale :** 14 fichiers dans l'ordre du manifeste, premier chemin `kristals/qc-pri-ilss-004/authoring/PARCOURS.md`, aucune traversée de chemin, taille non nulle, CRC vérifié, trois JSON directement réanalysés après packaging.

## Limites et revue humaine nécessaires

- **Pédagogie ILSS :** relire la clarté des documents adaptés, la pertinence du lexique et l'inclusion des élèves aux expériences scolaires diverses.
- **Accessibilité :** examiner avec des utilisateurs les supports visuels, les consignes lues oralement, la communication assistée et la comparabilité des réponses.
- **Exactitude des corrigés et décisions :** les réponses sont vérifiables sur les documents fictifs; l'aptitude des grilles à produire des jugements stables entre évaluateurs n'est **pas** testée avec des élèves.
- **Protection :** aucun formulaire réel, consentement scolaire réel ou donnée identifiable collecté; confidentialité des traces à définir au déploiement.
- **Portée :** aucune équivalence au PFEQ, aucune validation institutionnelle, aucun test en contexte réel.

## Propositions sans changement de structure centrale

- Ajouter ultérieurement au schéma de banque des champs de contrôle d'accessibilité (mode de lecture du document, mode de réponse autorisé, indice directif intervenu), seulement après approbation du mainteneur.
- Définir une bibliothèque partagée de pictogrammes **légendés et licenciés** si des images sont nécessaires à l'avenir, avec texte alternatif vérifié; ce delta ne modifie aucun référentiel.
- Mettre en place une revue pédagogique des deux contextes et une procédure d'essai interévaluateurs avant qualification.
