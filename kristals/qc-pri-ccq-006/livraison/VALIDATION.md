# Validation et journal de livraison — `qc-pri-ccq-006`

**Base :** archive `initbundle(1).zip`, dossier maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. **Cible :** `qc-pri-ccq-006_livraison_v1.2.zip`. **Statut :** `a_revoir` ; aucune homologation, certification ou publication déclarée.

## Travail livré

- Remplacement intégral de `authoring/PARCOURS.md` en conservant front matter YAML et les 12 rubriques numérotées; enrichissement du contrat JSON par ajout des champs minimaux de la famille d'évaluation.
- Six fiches pédagogiques et douze items à documents fictifs intégralement rédigés, chacun avec consigne, stimulus, réponse/critères et feedback. Deux preuves distinctes : bibliothèque (`q-011`) et jardin communautaire (`q-012`).
- Plan, grille et déclaration de provenance. Aucun document intime ni média tiers.

## Tests réellement exécutés

Le script local `_qa_ccq006.py` (non inclus dans le ZIP) a été exécuté sur les fichiers produits : **50/50 contrôles de préparation réussis** : filetree, YAML et 12 rubriques, champs v1.2 préservés, JSON analysés, familles, numérotation unique, corrigés, scénario contrôlé seed 6006, deux preuves, sécurité et manifeste. Après emballage, **8/8 contrôles de l’archive réussis** : premier chemin, 14 fichiers exacts, racine unique, tailles, absence de traversal, concordance octet à octet, CRC et JSON archivés. **Total : 58/58 contrôles techniques réussis.** Ce contrôle n’est ni un essai en classe ni une revue culturelle humaine.

## Limites non résolues et révision humaine

- Révision culturelle et pédagogique humaine non réalisée; difficulté et durée des items non expérimentées avec des élèves.
- Le barème 0–2 par dimension et les seuils de deux preuves sont des paramètres internes à éprouver, non une étude de fidélité intercorrecteurs.
- Les lieux fictifs ne constituent pas des sources historiques sur une population réelle; l'évaluation mesure la lecture de documents et la capacité à décrire sans jugement.
- Aucun audit détaillé de conformité PFEQ ni vérification de diffusion sur LMS; aucune donnée d'élève recueillie.

**Limite de lien héritée :** le champ original `referentiel_technique` pointe vers `gouvernance/...`, mais le répertoire source se nomme `governance/...`. Ce champ a été conservé intact conformément au mandat. Une rectification éventuelle relève du contrôle central du schéma v1.2.

## Proposition hors périmètre (aucune base centrale modifiée)

Envisager au niveau gouvernance une nomenclature partagée des dimensions « exactitude / contexte / neutralité / limites » et une politique de conservation des traces anonymisées des deux preuves. Cette proposition n'est **pas** une modification du schéma v1.2.

## Fusion

Extraire les **14 fichiers** à la racine du dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Les chemins internes commencent directement par `kristals/qc-pri-ccq-006/`. Ne remplacer aucun fichier sous `governance/`, `registry/`, `docs/`, `state/`, `runtime/`, `canon/` ou un autre Kristal.
