# Validation technique — `qc-pri-us-008`

**Statut :** rédaction terminée; évaluation humaine, revue de perspectives historiques, essais pédagogiques et acceptation institutionnelle requis. Ni certification ni homologation ni alignement PFEQ affirmé.

## Périmètre exact du delta

Deux remplacements `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`, douze ajouts strictement locaux. Le ZIP n'inclut ni `ALIGNEMENT.md`, ni `BRIEF_REDACTION.md`, ni `AGENTS.md`, ni `kristal.workspace.json`, ni fichier `registry/`, `governance/`, `canon/`, `state/`, `runtime/`, `docs/`, ni autre Kristal.

## Tests exécutés

- **318 assertions préarchivage exécutées et réussies** dans un script Python, couvrant identifiants, sources, frontmatter YAML (identique à celui de la source), invariants JSON, notices H1–H9, rubriques, dix items et leurs réponses, 2 preuves distinctes, droits et accessibilité documentaire.
- **JSON validés** par décodage strict : `authoring/CONTRAT_PEDAGOGIQUE.json`, `evaluation/BANQUE_ITEMS.json`, `livraison/MANIFEST.json`. Frontmatter v1.2 parsé par YAML, 12 sections détectées en ordre.
- **Graphe contrôlé** dans l’archive maîtresse : `requires` = `qc-pri-us-001`; recommandations non bloquantes = `qc-pri-us-002` et `qc-pri-us-005`.
- **Plan et corrigés** : 10 IDs séquentiels uniques, rubriques explicites et deux chronologies distinctes A/B; contrôle automatisé des années et associations clés, complété par la consultation des sources institutionnelles. Cette dernière ne remplace pas la relecture d’un historien.
- **Chemins de fusion** : exactement deux remplacements autorisés et douze ajouts dans le Kristal, comparés aux chemins de l’archive maître. Une simulation matérielle du workspace complet et un contrôle CRC du ZIP sont effectués en fin de validation et consignés dans la sortie du vérificateur.
- **Provenance / droits / accessibilité** : notice H1–H9 rédigée de manière originale, aucune image ni fac-similé tiers embarqué, modalités orales/écrites/tactiles et protection des perspectives autochtones explicitées. Ces contrôles sont documentaires seulement.

## Limites et vérifications humaines indispensables

- Relecture par spécialiste de l'histoire de la Nouvelle-France et des perspectives autochtones pour vérifier dates, dénominations, causalité et absence d'anachronisme.
- Vérifier les adaptations pédagogiques (oral, scribe, police et mode de réponse), la lisibilité selon l'âge et l'équité des critères dans des situations réelles.
- Tester la fidélité intercorrecteurs sur les deux tâches distinctes, et contrôler la compréhension du périmètre du recensement de 1666.
- Aucune expérimentation avec élèves, aucun test de performance LMS ou essai d'un moteur de génération réalisé ici; toutes les banques demeurent `a_revoir`.
- Les sources externes ont été consultées, les notices sont des paraphrases originales; une revue des droits est nécessaire si des reproductions ou images sont ajoutées.

## Propositions de changement de structure (non appliquées)

1. Standardiser dans un prochain schéma central la distinction « fait / interprétation / limite » et `source_page_ref` par jalon.
2. Ajouter une liste centrale de corpus fermés approuvés, avec suivi de versions et historique de revue humaine avant substitutions.
3. Normaliser les adaptations non directives et la décision à deux preuves indépendantes, sans modifier le registre dans ce delta.
