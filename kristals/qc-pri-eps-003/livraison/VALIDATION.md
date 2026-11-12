# Rapport de validation — qc-pri-eps-003, livraison v1.2

## Périmètre du delta
14 fichiers attendus sous `kristals/qc-pri-eps-003/` : deux fichiers existants remplacés sans suppression de champs canoniques; douze fichiers nouveaux (6 contenus, 3 évaluations, 1 source, 2 livraison). Aucun autre fichier du workspace n'est dans le delta. Statut : **contrôle technique à confirmer par script**, revue humaine nécessaire; n'est ni une certification, ni une homologation au PFEQ.

## Contrôles exécutés et résultats
**44 contrôles locaux exécutés et réussis avant empaquetage** : conservation du YAML et des champs JSON natifs, invariants pédagogiques et graphe, 12 sections, 10 items uniques, mapping `obj-1`/`crit-1`/qc-pri-eps-003-ev-01, deux contextes de maîtrise, quatre catalogues A/B avec **16 sélections reproductibles** contrôlées, remédiations et séquences d'exercices, ressources, droits, sécurité, accessibilité et liens. La vérification est **structurelle et par inspection de rubriques**; aucune performance d'enfant n'a été observée ni simulée.

```text
- 14 entries precisely: RÉUSSI
- No files outside declared set: RÉUSSI
- All nonempty: RÉUSSI
- All filenames safe: RÉUSSI
- Manifest fixed identity: RÉUSSI
- YAML frontmatter parse: RÉUSSI
- YAML canonical fields preserved: RÉUSSI
- 12 numbered section headings once: RÉUSSI
- Objective immutable: RÉUSSI
- Identity and family YAML: RÉUSSI
- Existing contract keys preserved: RÉUSSI
- Original contract top-level values preserved: RÉUSSI
- Original family values preserved: RÉUSSI
- One family exact: RÉUSSI
- Every government-required family field: RÉUSSI
- Immutable prerequisites, order and proof: RÉUSSI
- Family review status honest: RÉUSSI
- Graph exact outgoing reference: RÉUSSI
- Graph no requires incoming from self: RÉUSSI
- Graph inbound not converted to prerequisite: RÉUSSI
- Bank schema identity: RÉUSSI
- 10 distinct contiguous IDs: RÉUSSI
- Item required fields populated: RÉUSSI
- Each item maps objective, criterion, family: RÉUSSI
- No certified items, valid modes: RÉUSSI
- Physical observation represented: RÉUSSI
- Two separate final mastery contexts: RÉUSSI
- Six fixed four catalog scenarios: RÉUSSI
- Catalog variants deterministic and fully corrected: RÉUSSI
- 16 deterministic selections alternate as intended: RÉUSSI
- Scenario variation not random AI: RÉUSSI
- Diagnostic at least 2: RÉUSSI
- Guided exercises 3: RÉUSSI
- Autonomous exercises 4: RÉUSSI
- Transfer tasks 2: RÉUSSI
- At least two examples / two counterexamples: RÉUSSI
- Rubric four dimensions and two contexts: RÉUSSI
- Plan covers each ID and rubric: RÉUSSI
- No score on morphotype: RÉUSSI
- Rights/source declarations: RÉUSSI
- Accessibility and supervision in each exercise file: RÉUSSI
- All local referenced files exist: RÉUSSI
- No off-scope paths in manifest: RÉUSSI
- All files UTF8 decodable: RÉUSSI
```

**Contrôles ZIP exécutés :** 9 contrôles réussis :
- exact 14 files: RÉUSSI
- first path with required prefix: RÉUSSI
- only allowed nested paths: RÉUSSI
- nonempty and CRC ZIP: RÉUSSI
- 3 JSON files parse: RÉUSSI
- manifest exactly equals ZIP entries: RÉUSSI
- two master replacements match intended source identity: RÉUSSI
- only target workspace packaged: RÉUSSI
- no nonempty ZIP directory entry: RÉUSSI

En toute rigueur, l’archive a été réemballée avec le rapport ci-dessus; l’intégrité ZIP et le contenu exact ont été vérifiés à nouveau après cette écriture.

## Risques et limites connus
- Aucun essai d'observation en milieu réel ni mesure de fiabilité interjuges; seuils et grilles à réviser par une personne qualifiée en EPS et en adaptation scolaire.
- Chaque scénario est préparé pour être sûr **sur papier**; espace réel, matériel, aides et conditions individuelles ne peuvent être validés hors établissement.
- Les éléments de sécurité cités d'OPHEA viennent d'Ontario, non d'une autorité québécoise. Le responsable applique les règles locales en vigueur.
- Les variations A/B sont intégralement rédigées; pas de génération IA libre, pas d'items certifiés.

## Revue humaine requise
Éducateur EPS : pertinence et progressivité; spécialiste d'accessibilité ou personnel responsable : équivalence des gestes adaptés; responsable des lieux : risques concrets/plan d'urgence; réviseur francophone : clarté pour l'âge ciblé; évaluateurs indépendants : concordance des critères et robustesse des deux preuves.

## Propositions de changements structurels (NON APPLIQUÉES)
1. Ajouter dans le schéma central futur un champ facultatif `intervention_de_securite` distinct des indices pédagogiques et un état `non_evaluable` pour ne jamais pénaliser un arrêt protecteur.
2. Définir un champ `adaptation_approuvee`/`responsable` dans la trace LMS (pas dans le canon) tout en préservant données de santé et identité confidentielles.
3. Ajouter un mécanisme de revue interjuges pour les rubriques d'observation; **aucune modification** du registre ou du contrat central effectuée ici.
