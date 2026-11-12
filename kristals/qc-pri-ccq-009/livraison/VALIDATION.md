# Validation du delta — `qc-pri-ccq-009`

**Statut** : contenus intégralement rédigés; banque et rubriques encore `a_revoir`; aucune validation en classe ou certification. Ce fichier est rempli avec les **tests effectivement exécutés** lors de l'archivage final.

## Périmètre contrôlé

- Un seul ID `qc-pri-ccq-009`, format delta enraciné dans `kristals/qc-pri-ccq-009/`.
- Deux remplacements exclusifs dans `authoring/`; douze nouveaux fichiers, sans toucher aux fichiers centraux ou voisins.
- Métadonnées v1.2 canoniques : objectif, preuve autonome, concepts, `requires: qc-pri-ccq-008`, ordre recommandé non bloquant `qc-pri-ccq-007`, renforcement non bloquant `qc-pri-fr-026`, famille `qc-pri-ccq-009-ev-01`.
- Deux preuves indépendantes de maîtrise : `q-009` (coin lecture, répartition) et `q-010` (classement de maquettes, exactitude de l'information).

## Contrôles techniques réellement exécutés

**508 assertions préarchivage exécutées avec succès** au moyen d'un script Python le 8 octobre 2026 : existence des 14 chemins, absence de fichiers vides, comparaisons des YAML et clés JSON sources, préservation du frontmatter original **à l'identique**, 12 sections, graphe lu dans l'archive maîtresse et liens `requires/recommends_before/reinforces`, conservation de la famille native et ajout de ses champs, 10 items distincts, champs obligatoires et références exactes, deux épreuves fixes indépendantes, rubriques, provenance et précautions d'accessibilité.

**Simulation de superposition :** comparaisons de l'inventaire des fichiers originaux du dossier `qc-pri-ccq-009` dans le ZIP maître; seules deux entrées existantes sont remplacées et douze sont ajoutées. Les fichiers protégés restent absents du delta. La lecture des fichiers originaux a été contrôlée sans modifier l'archive maîtresse.

**Cohérence des corrigés :** le contrôle documentaire a confronté deux options dans chaque cas de maîtrise (`3–3` / `4–2` pour six places et `publier provisoire` / `attendre demain` pour une fiche non vérifiée), les conséquences plausibles et les objections. Les contrôles automatisés vérifient leur présence et leurs liens; une revue humaine devra juger leur valeur argumentative réelle.

**Tests du ZIP final (après construction) :** entrée initiale sous la racine attendue, 14 fichiers exacts, entrées non vides et noms sûrs, manifeste identique, 3 JSON stricts décodables, contrôle CRC `testzip()`, absence de fichiers protégés ou d'autres Kristals (confirmés par le script de clôture).

## Contrôles de sens documentés

Les cas de maîtrise proposent des options explicites, avec des corrigés-types **A et B** tous deux recevables lorsqu'ils sont justifiés. La grille n'impose pas de conviction privée. La concordance de leurs faits et exemples est vérifiée textuellement, non confirmée par épreuve psychométrique.

## Limites non résolues

- Absence de mise à l'essai avec des élèves, de mesure d'accord entre évaluateurs et de validation d'un seuil suffisant par expertise CCQ.
- Besoins individuels d'accessibilité, maturité et contexte psychosocial à apprécier localement; protéger la confidentialité et offrir un mode individuel.
- Le contrat conserve les valeurs v1.2 ; les données de banque n'ont pas d'autorité pour modifier la gouvernance, le graphe ou les autres Kristals.
- Les références sont citées à la source; licences futures, éventuelles illustrations et diffusion restent soumises à revue.

## Revue humaine requise et propositions de structure (non exécutées)

1. **Expertise CCQ et biais** : analyser neutralité des deux options, richesse réelle des objections, durée et difficulté des scénarios pour l'âge choisi.
2. **Évaluation** : faire coter indépendamment les mêmes copies par plusieurs évaluateurs; discuter des divergences E1 à E5.
3. **Accessibilité** : valider un protocole commun de scribe neutre et de remise privée, sans réduire la tâche argumentative.
4. **Propositions sans modification du workspace central** : définir à l'avenir des champs partagés `faits_verrouilles`, `objections_acceptables`, `assistance_non_directive` et un corpus de scénarios révisés; soumettre au responsable du schéma plutôt qu'ajouter des clés au registre.
