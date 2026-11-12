# Validation et journal de livraison — `qc-pri-da-006` v1.2

**Nature du livrable :** delta fusionnable d'un seul Kristal (deux remplacements complets `authoring/`, douze ajouts). **Statut :** contrôles techniques effectués, **validation humaine et essai pédagogique requis**; ni cours terminé, ni examen certifié, ni homologation québécoise.

## Provenance et périmètre

- Le ZIP autonome nommé `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` ne figure pas séparément parmi les fichiers montés. **La même arborescence source** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` est présente dans l'archive jointe `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`. C'est **cette version effectivement accessible** qui a été utilisée, sans recréer ses métadonnées.
- Sources lues : les trois documents actifs `governance/Norme_Pedagogique_Autonome_v1.2/` demandés, les relations du graphe `registry/GRAPHE_PEDAGOGIQUE_202.json`, le `PARCOURS.md` original et le `CONTRAT_PEDAGOGIQUE.json` original, `ALIGNEMENT.md` et `BRIEF_REDACTION.md` de `qc-pri-da-006`.
- Uniquement `kristals/qc-pri-da-006/` est livré. Les fichiers interdits, les répertoires `governance/`, `registry/`, `docs/`, `canon/`, `state/`, `runtime/` et les autres Kristals ne sont pas empaquetés ni modifiés.

## Contrôles réellement exécutés

**Prévalidation automatisée (270 contrôles, tous réussis sur les fichiers livrés et les sources natives de référence) :**

1. Parsage JSON de `CONTRAT_PEDAGOGIQUE.json` et `BANQUE_ITEMS.json`, format et identifiants, conservation des champs et valeurs originales (hors statuts éditoriaux actualisés), existence des treize champs minimum de la famille d'évaluation.
2. Parsage YAML du front matter de `PARCOURS.md`; maintien de toutes ses clés natives et de leur identité; exactement 12 sections numérotées.
3. Comparaison avec le graphe source : seul `qc-pri-da-002` en `requires`, `qc-pri-da-003` en `recommends_before` non bloquant. Objectif, preuve, discipline, notions et famille conservés.
4. Contrôle des six contenus : au moins 2 exemples résolus, 2 contre-exemples, D1/D2, G1–G3 à guidage dégressif, P1–P4 et 2 transferts (bibliothèque/marée). Recherche des passages de sécurité, d'accessibilité, de feedback, de rappel différé, de provenance et de droits.
5. Banque de **8 items uniques et ordonnés** `q-001` à `q-008`, mode `fixe`, `seed=null`, `parametres=null`, réponses observables développées, rubriques, autonomie, rétroactions, statuts `a_revoir` et liens complets `obj-1`/`crit-1`/`qc-pri-da-006-ev-01`.
6. Deux contextes terminaux distincts `q-007` (bibliothèque) et `q-008` (marée), plan d'évaluation couvrant les 8 items, grille fixant les deux preuves et vérification des références internes explicites. Inspection des conditions d'accès sûr et des limitations sur les droits.

**Limite importante :** les contrôles 4 et 6 constatent la présence et la cohérence structurale des dispositions, non leur efficacité sur des élèves. Les scénarios d'observation des corrigés ont été relus pour des contradictions de comptes/durées, puis ajustés pendant la rédaction. Ce contrôle éditorial **n'est pas** une passation réelle ni une validation interjuges.

**Contrôles finaux de l'archive :** un script distinct a vérifié avant remise exactement 14 fichiers, toutes les entrées non vides sous `kristals/qc-pri-da-006/`, première entrée autorisée, aucune racine d'archive englobante, aucun chemin absolu ou `../`, aucun fichier interdit, unicité et conformité du manifeste, parsage des trois JSON, structure de fichier non corrompue (test CRC). Les résultats de la dernière exécution figurent dans le journal technique local de génération; l'intégrité de l’archive est vérifiée après sa création.

## Limites non résolues et revue humaine obligatoire

- Aucune épreuve en classe, aucune observation de véritables élèves, aucune fiabilité inter-évaluateurs, aucun essai des adaptations par des personnes concernées ou professionnel·les de danse adaptée; les seuils 3/4 et les descriptifs sont **des choix pédagogiques internes** qui demandent ajustement.
- Revoir sécurité de l'espace et des mouvements selon l'âge, l'environnement réel et les besoins exprimés; ceci n'est pas une évaluation médicale ou ergonomique individualisée.
- Revoir la lisibilité des partitions, la durée du protocole, les supports multimodaux réellement fournis par le LMS, l'équité culturelle des métaphores de danse et la compatibilité des modes de capture sans vidéo obligatoire.
- Les partitions et exemples ont été rédigés originellement sans musique externe intégrée; aucune garantie juridique exhaustive de non-similarité avec toutes les œuvres existantes ni de politique locale de captation n'a été obtenue. Consentement et règles institutionnelles de conservation restent à vérifier.
- Les huit items sont marqués **`a_revoir`**; ils ne sont ni certifiés ni diffusables comme examen sommatif sans contrôle humain et essai. Aucun corrigé automatique ne remplace la grille d'observation.

## Anomalie héritée et propositions de structure, non appliquées

- Le champ natif `referentiel_technique` de `authoring/CONTRAT_PEDAGOGIQUE.json` pointe vers `gouvernance/Norme_Pedagogique_Autonome_v1.2` alors que le dossier source s'appelle **`governance/Norme_Pedagogique_Autonome_v1.2`**. La valeur native a été **conservée telle quelle** pour éviter de modifier une métadonnée canonique sans migration autorisée; soumettre une proposition de correction versionnée aux responsables du workspace.
- Proposer dans une future évolution centrale du schéma des champs normalisés pour l'`essai_numero`, la `modalite_accessible`, la `preuve_contexte`, les `observations_avant_apres` et une `validation_humaine` datée. Ici, ces informations figurent dans les rubriques et fiches, **sans** intervention sur le schéma central.
- Les statuts du contrat local ont été mis à jour pour représenter l'état réel de rédaction; les identifiants, relations, objectifs, concepts, type de famille, champs sources et front matter v1.2 sont préservés.

## Fusion attendue

Extraire l'archive maîtresse v1.2, entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` puis y extraire `qc-pri-da-006_livraison_v1.2.zip`. Les chemins de ce delta commencent directement par `kristals/qc-pri-da-006/`; seuls `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json` écrasent des fichiers sources existants.
