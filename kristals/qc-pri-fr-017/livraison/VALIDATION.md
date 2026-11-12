# Validation et journal de livraison — qc-pri-fr-017

**Statut :** `a_revoir` (delta rédigé et soumis à contrôles locaux; ni publication, ni homologation, ni certification). **Base :** workspace v1.2 fourni à l'intérieur de `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip` sous le dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`.

## Fichiers lus avant production

- Les trois normes actives exigées (`CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`) dans `governance/Norme_Pedagogique_Autonome_v1.2/`.
- `registry/GRAPHE_PEDAGOGIQUE_202.json` pour les deux arêtes sortantes de `qc-pri-fr-017`.
- Quatre fichiers d'authoring source : `PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`.
- Deux pages publiques OQLF sur repérage du sujet et coordination par *et*; les URL sont consignées dans `sources/REFERENCES_CONTENU.md`.

## Journal des changements, périmètre exclusif

- **Remplacement intégral** de `authoring/PARCOURS.md` : front matter v1.2 conservé dans ses clés/identités/relations, révision de contenu à `0.3.0`, douze sections complètes, diagnostic, modelage, indices dégressifs, pratique, remédiation, rappel différé, accessibilité et seuil autonome.
- **Remplacement intégral** de `authoring/CONTRAT_PEDAGOGIQUE.json` : structure native, famille et tous champs v1.2 d'origine conservés; paramètres minimaux de gouvernance ajoutés au même objet de famille; `seed` nul parce que banque fixe, statut `a_revoir`.
- **Nouveaux** : six fichiers de leçon dans `contenu/`, trois fichiers d'évaluation, références/provenance, ce journal et manifeste.
- **Aucun changement** à `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `docs/`, `canon/`, `state/`, `runtime/`, `registry/`, `governance/`, autres Kristals ou fichiers globaux.

## Contrôles effectivement exécutés

1. **PASSÉ** — lecture de l'archive source et présence des huit références exigées; identité, famille, `requires` et `recommends_before` comparés au graphe.
2. **PASSÉ** — validation JSON stricte du contrat, de la banque et du manifeste; champs de famille obligatoires; anciennes clés et valeurs d'origine préservées; front matter YAML décodable, mêmes clés sources et douze sections conservées.
3. **PASSÉ** — dix items numérotés de q-001 à q-010 sans doublons, chacun relié à `obj-1`, `crit-1` et `qc-pri-fr-017-ev-01`; dix corrigés structurés présents et formes du verbe des **20 phrases** comparées aux flexions indépendamment calculées à partir des infinitifs du corpus fixé.
4. **PASSÉ** — deux manifestations A/B distinctes, chacune de six phrases différentes, chacune avec sujet, personne, nombre, forme et justification; absence de variation non spécifiée; aucune réponse tirée librement.
5. **PASSÉ** — contrôles statiques d'accessibilité et droits : accès écrit obligatoire aux désinences, modalités alternatives documentées, absence d'images ou médias tiers, attribution OQLF avec liens de source vérifiés; revue juridique/humaine **non** effectuée.
6. **PASSÉ** — intégrité du ZIP : **exactement 14 fichiers non vides**, aucun fichier global, préfixe `kristals/qc-pri-fr-017/` dès la première entrée, aucune entrée absolue ou `../`, manifeste égal à la liste exacte et chemin d'extraction compatible avec le workspace existant.
7. **PASSÉ** — liens de référence vers `qc-pri-fr-014` et `qc-pri-fr-013` présents dans le graphe; chemins des documents locaux référencés compatibles avec le workspace source et/ou le delta.

**Portée des tests :** vérifications statiques et algorithmiques locales uniquement; la validation d'une justification ouverte reste un jugement humain fondé sur la grille, et les pages externes ne sont pas archivées dans le livrable.

## Limites et points nécessitant revue humaine

- Leçons et items **à relire** par une personne compétente en linguistique/didactique du français et à tester avec des apprenants; ni validation psychométrique ni calibration de difficulté n'ont été réalisées.
- Confirmer la pertinence didactique de la mise au seuil **six accords expliqués sur six**, deux fois, et la charge d'écriture pour l'âge ou le parcours auquel le module sera projeté; ceci demeure une **proposition de seuil interne**, pas un standard ministériel.
- Vérifier la faisabilité et l'équité des aménagements d'accès (transcription des réponses, lisibilité, durée, consignes) avec les outils réels du LMS.
- Les droits du workspace source et les règles éditoriales de publication du dépôt maître n'ont pas fait l'objet d'un audit externe; les exemples nouveaux sont originaux et les URL sont attribuées sans reproduction de contenu tiers.
- Un contrôle de schéma applicatif/framework réel et un test de fusion en production n'ont **pas** été exécutés; le ZIP a été contrôlé statiquement et l'extraction décrite, mais pas déployé dans un LMS.

## Propositions structurelles futures (non appliquées)

1. Définir officiellement, dans une prochaine version du contrat, un **schéma JSON** des champs supplémentaires de famille et un champ `critere_id` stable sur chaque item.
2. Prévoir dans le LMS un journal de passation distinguant aides d'accès et aides cognitives, contextes A/B et dates, **hors** des fichiers canoniques.
3. Prévoir un processus versionné de nouveaux dossiers de six phrases, validés en amont et non générés sans contrôle.

**Fusion ciblée :** extraire l'archive `qc-pri-fr-017_livraison_v1.2.zip` depuis l'intérieur de `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Les chemins du ZIP commencent immédiatement par `kristals/qc-pri-fr-017/` (aucun dossier englobant, aucun registre/norme livré).
