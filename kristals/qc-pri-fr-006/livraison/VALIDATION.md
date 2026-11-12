# Journal de livraison et validation — `qc-pri-fr-006` v1.2

**Statut :** rédaction terminée et contrôles techniques exécutés par le script de validation après création; tous les items restent `a_revoir`. Aucun qualificatif « certifié », « homologué » ou « publié » sans procédure supplémentaire.

## Périmètre

- Le ZIP contient uniquement **14 fichiers** sous `kristals/qc-pri-fr-006/` : deux fichiers `authoring/` complets remplacés et douze nouveaux documents.
- **Fichiers protégés exclus** : `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, tous les `docs/`, `canon/`, `state/`, `runtime/`, registres et gouvernance, ainsi que tout autre Kristal.
- Métadonnées YAML v1.2 et champs identitaires du contrat JSON natif conservés; arête `requires` vers `qc-pri-fr-005` maintenue sans créer d'autre lien.

## Contrôles automatisés effectivement réalisés

Le script `verify.py` (outil de production non inclus dans le ZIP) exécute les contrôles suivants; il stoppe la production sur échec :

1. Lecture des huit sources internes requises (normes, charte, graphe et quatre fichiers authoring), objectif, preuve, concepts, famille, préalable et ordre d'origine vérifiés.
2. Analyse du YAML du parcours et présence des **12 sections** numérotées; comparaison du frontmatter original (identique, hormis aucun changement), parcours non tronqué.
3. `json.loads` des trois JSON et préservation des clés canoniques et de la famille du contrat enrichi; tous les champs minimum de `GENERATEUR_ET_EXAMENS.md` présents.
4. Dix items fixes complets `q-001` à `q-010`, identifiants uniques, `obj-1`, `crit-1`, famille exacte, difficulté et statut corrects; consignes, stimuli, corrigés, critères et feedback non vides.
5. Épreuves A/B inédites `q-009` (musée) et `q-010` (jardin), chacune demandant deux inférences réellement différentes et deux indices distincts. Cohérence des citations attendues avec leur stimulus contrôlée par correspondance exacte de chaînes.
6. Documents couvrant au moins deux diagnostics, deux exemples et contre-exemples, trois tâches guidées, quatre autonomes, deux transferts, remédiations, accessibilité, droits et rappel différé.
7. L'intégrité CRC et la liste exacte des quatorze chemins dans le ZIP (pas de traversée `../`, ni préfixe du workspace maître) ont été vérifiées; manifeste intégré comparé aux entrées.
8. Superposition simulée avec le dossier source du Kristal : seuls deux chemins authoring sont des remplacements, douze sont nouveaux, tous les autres chemins sont inchangés.

## Limites honnêtes

- **Revue humaine des inférences recevables à accomplir** : les corrigés sont des ancrages argumentés, pas un ensemble exhaustif de toutes les hypothèses acceptables. La vérification de chaînes n'établit pas à elle seule la validité linguistique de chaque interprétation.
- Aucun test sur des élèves, aucun accord intercorrecteurs, aucune validation du temps, de la difficulté ou de la qualité didactique en contexte réel.
- Aucun audit de licence exhaustif des noms et liens bibliographiques; les textes de la banque sont rédigés spécifiquement, sans reproduction de contenus tiers.
- L'usage d'une lecture médiée doit être noté : l'inférence peut être évaluée, **pas** le décodage de façon équivalente. Adaptations à faire approuver localement.
- Aucune projection au Framework canonique v9, aucun alignement détaillé ni conformité PFEQ testés.

## Propositions de structure non appliquées

- Définir centralement un champ optionnel `evidence_anchor` (indices textuels exacts, explication, variantes acceptables) et un type `response_mode` distinguant lecture autonome, lecture médiée et réponse orale/écrite.
- Prévoir une revue humaine obligatoire des inférences alternatives et un protocole de calibration intercorrecteurs avant publication.

**Aucune base centrale ni aucun autre ID modifié.**
