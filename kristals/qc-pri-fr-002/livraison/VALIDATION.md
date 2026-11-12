# Validation exécutée — `qc-pri-fr-002` v1.2

**Statut : rédaction complète, contrôles techniques exécutés, revue humaine requise.** Aucun item certifié et aucune conformité PFEQ revendiquée.

## Contrôles réalisés sur la livraison

- **341 assertions préarchivage réussies** dans `verify.py`, comprenant : existence et lecture des sources, comparaison du graphe et de la source contractuelle, frontmatter YAML conservé, 12 sections, 10 items sans doublon et leurs clés/réponses/critères, famille, manifestes et liens.
- Deux preuves autonomes `q-009` et `q-010` distinctes, **24 unités** au total, toutes distinctes et revérifiées par **un deuxième décodeur indépendant** du générateur de la banque. Quatre sous-ensembles séparés (3 syllabes lecture + 3 mots lecture + 3 syllabes écriture + 3 mots écriture) dans chaque preuve.
- Exactitude technique des corrigés : 24 comparaisons graphèmes→transcriptions phonémiques réussies dans le corpus fermé; cette vérification du code n'est **pas** une validation audio, psychométrique ou d'usage chez les élèves.
- Conformité attendue du delta : seulement deux remplacements préexistants (`authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`) et 12 fichiers nouveaux; aucun autre fichier maître ciblé.
- Intégrité ZIP, CRC, liste exacte des 14 chemins, tailles non nulles et concordance avec le manifeste **testées après écriture du ZIP par le même vérificateur**. Toute anomalie fait échouer le script.

## Contrôles éditoriaux documentaires et limites non résolues

- Le diagnostic oral distingue le préalable `qc-pri-fr-001` du décodage/encodage. Le lexique phonémique réduit l'ambiguïté des graphies, sans promettre l'unicité orthographique du français hors de la banque.
- Accessibilité : lecture à grande taille, dictée orale réservée à l'adulte, aides motrices non directives, variantes phonétiques du français québécois. La modalité équivalente en cas de difficulté auditive ou articulatoire nécessite une décision humaine spécialisée.
- **Revue humaine indispensable** : vérifier la prononciation locale et les ambiguïtés orthographiques, le rythme d'administration, l'équilibre des mots, la sécurité acoustique et la fiabilité intercorrecteurs. Aucune séance réelle ni enregistrement audio n'a été réalisé.
- Provenance/droits : sources OQLF/EEF référencées sans reprendre leurs illustrations ou banques; les droits de redistribution du workspace maître ne sont pas attestés indépendamment.

## Propositions de structure non appliquées

- Proposer un champ standard `stimulus_visibility` distinguant « réservé à l'adulte pour dictée » et « visible à l'apprenant pour lecture »; proposer un champ optionnel de variantes phonétiques acceptées.
- Ajouter ultérieurement un protocole d'enregistrement de corrections contextualisées, sans modifier `governance/`, `registry/`, `canon/`, les workspaces voisins ou les liens du graphe.
