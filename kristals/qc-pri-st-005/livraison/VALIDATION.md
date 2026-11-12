# Validation de livraison — qc-pri-st-005

**Base :** workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` depuis `initbundle(1).zip`.  
**Autorité :** gouvernance pédagogique v1.2; zéro intervention sur la norme, le registre, les fichiers canoniques ou un autre Kristal.  
**Livrable :** delta de 14 fichiers sous `kristals/qc-pri-st-005/`; 2 fichiers `authoring` remplacent entièrement les frames sources, 12 fichiers nouveaux.

## Contrôles effectivement réalisés

- **Test Python préalable (exécuté) :** 311 assertions de structure et de contenu terminées sans échec, avant emballage, comprenant les vérifications de présence des sources, conservation du YAML, 12 sections, objectif et preuve, champs v1.2 existants, famille, liens de graphe, identifiants des items, énumérations, métadonnées de génération et sécurité.
- **Banque :** 12 items, dont 6 fixes et 6 scénarios contrôlés; tous `validation_status=a_revoir`. Chaque item dispose d'un stimulus factuel figé, d'une table de réponses par code, de deux critères indépendants par échantillon, d'une rétroaction et de limites de variation.
- **Variantes encadrées :** 186 permutations d'ordre testées sur les graines des six scénarios (`seed` à `seed+30`), en vérifiant le même ensemble sans répétition; exemples `seed`, `seed+1`, `seed+2` comparés à l'algorithme. **Aucune génération IA libre; les propriétés et corrigés scientifiques restent figés.**
- **Corrigés :** correspondance contrôlée automatiquement entre tous les codes, observations des stimuli et critères cités dans le tableau de correction, sans reprise d'une donnée absente des fiches; ce test contrôle la cohérence textuelle, non la validité scientifique ultime.
- **Maîtrise :** `q-011` et `q-012` sur cinq codes chacun; corpus disjoints des dix autres items et l'un de l'autre, deux contextes distincts, indices d'état et de propriété par code; maîtrise non déduite d'une note unique.
- **Couverture :** deux diagnostics, trois exercices guidés à indices dégressifs, quatre pratiques autonomes, au moins deux exemples et deux contre-exemples, deux transferts, remédiations, rappel différé et accessibilité documentés.
- **Sources/droits :** sources externes consultées et attribuées; aucune illustration ni extrait substantiel repris, réutilisation OpenStax à examiner si prévue ultérieurement. Les scénarios sont des productions originales fictives.

## Tests ZIP complémentaires

**12 vérifications ZIP exécutées et réussies :** 14 entrées non vides, première entrée `kristals/qc-pri-st-005/authoring/PARCOURS.md`, tous chemins sous `kristals/qc-pri-st-005/`, pas de traversée (`../`) ni racine absolue, aucune entrée dans les dossiers interdits, intégrité CRC, JSON analysables, manifeste identique à la liste ZIP et comparaison octet pour octet avec les fichiers sur disque. Aucun essai pédagogique avec des élèves n’a été exécuté.

## Limites non résolues et revue humaine indispensable

1. **Révision scientifique :** un spécialiste vérifie la formulation des états, les cas limites, les propriétés comme la compressibilité, le statut des fiches fictives et la distinction entre un état et un matériau.
2. **Révision pédagogique et linguistique :** vérifier la lisibilité en français québécois, la durée de chaque épreuve, l'exigence de deux critères par fiche et le risque de surcharge cognitive; mener des essais avec des élèves.
3. **Évaluation :** validation humaine des corrections, de la grille de jugement et de l'interprétation des justifications alternatives; aucun test de fidélité intercorrecteurs réalisé.
4. **Accessibilité et sécurité :** audit avec utilisateurs et responsables du contexte local; les fiches textuelles évitent la manipulation réelle, mais aucune certification de sécurité ou accessibilité n'est revendiquée.
5. **Droits :** le contenu créé ici est original, mais aucun audit juridique approfondi n'a été effectué. Les documents tiers restent des sources de vérification; leur réutilisation est soumise aux licences applicables.
6. **Intégration :** test technique de chemins, non déploiement dans un LMS ni homologation par le système scolaire québécois.

## Propositions de structure — non appliquées au workspace

- Envisager un schéma explicite `criteres_independants` et un mécanisme de validation du corpus fermé des scénarios scientifiques; décision à l'échelle centrale uniquement.
- Prévoir un champ d'évaluation humaine des faits scientifiques et du risque des manipulations, distinct du contrôle syntaxique de JSON.
- Envisager un journal d'essais élèves anonymisé et une mesure d'accord entre évaluateurs avant toute qualification; ne pas les créer comme dossiers additionnels dans ce delta.

**Statut :** tests de cohérence internes réalisés; **revue humaine requise**, non publié, non homologué, non certifié.
