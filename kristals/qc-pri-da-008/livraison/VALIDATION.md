# Validation de livraison — `qc-pri-da-008`

**Statut :** banque rédigée, items `a_revoir`; aucune certification ni homologation. Le présent rapport doit mentionner exclusivement des tests réellement exécutés sur le ZIP final et leurs limites.

## Périmètre de la livraison

Le delta contient **exactement 14 fichiers** sous `kristals/qc-pri-da-008/` : deux fichiers `authoring/` remplacent les versions initiales et douze nouveaux fichiers sont ajoutés. Aucun dossier parent, document global ou autre Kristal n’est inclus. Les parties immuables sont l’objectif exact, la preuve, les notions, le préalable `qc-pri-da-007`, les identifiants v1.2 et les liens du graphe; le frontmatter est conservé littéralement.

## Tests techniques effectivement exécutés

- **7842 assertions préarchivage réussies** dans `verify_da008.py` : fichiers, 12 sections, invariants YAML/JSON, natifs du contrat et de sa génération, dix items uniques complets, liens de famille, deux contextes d’évaluation, sécurité, accessibilité, droits et références.
- **YAML** du `PARCOURS.md` conservé **textuellement à l’identique** dans son frontmatter; 12 sections renseignées. **Trois JSON** décodés avec succès.
- **Simulation d’une fusion intégrale du workspace source** par extraction des fichiers originaux, superposition physique des 14 fichiers puis comparaison SHA-256 de chaque fichier protégé : **2 remplacements exacts, 12 ajouts, aucun fichier hors cible modifié**. Nombre de fichiers protégés inchangés : **7320**.
- **Qualité de corrigés testée structurellement** : dix items avec tâche, stimulus déterminé, réponse, critères et feedback; les deux preuves 009 et 010 ont des stimuli temporels distincts et une grille détaillée. La justesse de toutes les interprétations possibles et la fiabilité d’usage restent à revoir par un humain.
- **Sources/droits** : présence et traçabilité des trois types de provenance et absence de média tiers dans le paquet; aucune expertise juridique ou expérience pratique effectuée.
- **Contrôle ZIP effectué après création** : CRC, 14 chemins, protection anti-traversée, manifeste strict, trois JSON internes et comparaison des 14 contenus aux fichiers produits (voir la vérification de sortie).

## Contrôle pédagogique restant / revue humaine

1. **Danse** : exactitude du vocabulaire descriptif de mouvement, interprétations possibles, absence de réduction à une performance corporelle.
2. **Évaluation** : valeur diagnostique des deux premières tâches, correction des dix items, comparabilité des niveaux, qualité et fidélité intercorrecteurs de la grille R1–R5; vérifier qu’A et B sont bien distincts en situation réelle.
3. **Accessibilité** : lecture orale à débit choisi, transcription fidèle des cartes, usages de moyens de communication; ajustement local pour besoins particuliers, sans donner le contenu de la réponse.
4. **Éthique et droits** : valider tout futur ajout d’image ou vidéo et les éventuels consentements; le dossier actuel ne contient que des descriptions originales.
5. **Décision** : aucune décision sommative automatique; deux preuves indépendantes et un jugement humain sont requis, sans promesse de conformité PFEQ.

## Propositions de changement structurel (aucune modification centrale)

- Proposer au responsable du schéma une propriété facultative `stimulus_reading_protocol` pour documenter la neutralité de la lecture à voix haute, sans altérer la banque actuelle.
- Proposer une propriété contrôlée `evidence_observation_refs` pour relier un constat aux temps du stimulus, et un outil de calibration de correcteurs avant toute épreuve sommative.
- Laisser `registry/`, `governance/`, `canon/`, `state/`, `runtime/` et `authoring/ALIGNEMENT.md` complètement intacts.
