# VALIDATION DE LIVRAISON — `qc-pri-fls-003`

## État

**Livraison technique à revoir sur le plan scientifique et pédagogique.** Aucun examen n’est certifié, aucun Kristal n’est publié/activé et aucune conformité au PFEQ n’est revendiquée.

## Source et modifications

- Source : `initbundle(1).zip`, workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, fichiers locaux du Kristal et trois documents de gouvernance v1.2.
- Deux remplacements complets : `authoring/PARCOURS.md` (en-tête YAML préservé, 12 sections développées) et `authoring/CONTRAT_PEDAGOGIQUE.json` (champs v1.2 conservés, contrat de famille enrichi).
- Douze ajouts : six fichiers `contenu/`, trois `evaluation/`, références `sources/` et deux documents `livraison/`.
- Le contenu original de `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `docs/`, `canon/`, `registry/`, `governance/` et autres Kristals n’a pas été modifié ni empaqueté.

## Contrôles automatisés réellement exécutés avant l’assemblage

- PASS — Identité et famille origine
- PASS — Métadonnées du contrat préservées
- PASS — Champs familles v1.2 préservés
- PASS — Champs gouvernance famille
- PASS — Graphe sans préalable sortant
- PASS — Objectif et critère inchangés
- PASS — YAML parses et champs préservés
- PASS — 12 sections dans bon ordre
- PASS — 10 items
- PASS — Numérotation unique 001–010
- PASS — Lien obj/critere/famille dans chaque item
- PASS — Champs obligatoires et critères non vides
- PASS — Modes autorisés
- PASS — Aucune certification des items
- PASS — Deux contextes distincts de maîtrise
- PASS — Modèles et production autonome dans les deux preuves
- PASS — Contraintes de scénarios A/B avec seed
- PASS — Sélection reproductible et correction ancrée
- PASS — Les quatre variantes ont corrigé complet
- PASS — Deux diagnostics identifiés
- PASS — Trois exercices guidés
- PASS — Quatre autonomes
- PASS — Deux transferts
- PASS — Références distinguées et droits notés
- PASS — Accessibilité oral et accent
- PASS — JSON parses
- PASS — Manifeste 14 entrées sans doublon
- PASS — Aucun fichier autre Kristal
- PASS — Nom contenu provenance pas norme incluse

## Contrôles sur l’archive

**27 tests d’archive exécutés et réussis** sur le ZIP assemblé (puis réexécutés après mise à jour du présent rapport) :

- PASS Archive réouverte
- PASS Exactement 14 chemins
- PASS Premier chemin au bon préfixe
- PASS Tous les chemins préfixés du Kristal
- PASS Aucune entrée absolue ou traversée
- PASS Aucun dossier englobant ni répertoire additionnel
- PASS Chacun des 14 fichiers non vide
- PASS CRC interne ZIP vérifié
- PASS MANIFEST id/racine/base version
- PASS Manifeste égale ensemble des chemins
- PASS Trois JSON stricts lisibles
- PASS YAML natif conservé
- PASS 12 sections numérotées sans réordonnancement
- PASS Contrat d’origine champs scalaires inchangés
- PASS Famille originale entièrement conservée
- PASS Identité et absence de préalables v1.2
- PASS 13 propriétés de gouvernance présentes
- PASS Format, ID, famille de banque
- PASS 10 items numérotés uniques
- PASS Tous items liés à objet, critère, famille
- PASS Deux preuves finales à contextes distincts
- PASS Quatre variantes et exemples déterministes vérifiés
- PASS Tous items à revoir et corrigés/rubriques présents
- PASS Aucun autre Kristal ni fichier central livré
- PASS Références et droit explicitement traités
- PASS Liste ZIP stable et premier est PARCOURS
- PASS Pas de fichiers libres

## Limites non résolues et revue humaine obligatoire

- **Pas d’audio fourni** : les scripts demandent une lecture à voix haute compétente; la justesse des modèles effectivement prononcés n’a pas été mesurée. Aucune audition ou capacité de parole d’un enfant n’a été testée.
- Les contrastes et transcriptions /pul/, /bul/, /pɛ̃/, /bɛ̃/ et les groupes syllabiques doivent être relus par un spécialiste des variétés du français québécois; leur pertinence est proposée, non certifiée.
- Aucune épreuve sur des élèves réels, aucun accord entre correcteurs, aucun bilan d’équité d'accent, aucune adaptation clinique ni essai d’utilisabilité n’ont été exécutés.
- Les réponses orales étant ouvertes, les corrigés sont **grilles et réponses exemplaires**; l’évaluation n’est pas déterminée par simple comparaison de texte et aucune IA ne certifie l’intelligibilité.
- Références externes décrites comme consultées; pas de reprise d’audio, d’image de tiers ni de citation textuelle protégée dans les activités.

## Propositions hors livraison, sans changer la base

1. Prévoir ultérieurement une bibliothèque de modèles audio enregistrés avec autorisations, variantes naturelles et contrôle d’intelligibilité (travail central séparé).
2. Ajouter au moteur une grille structurée de double observation orale et un statut « preuve non observable avec cette modalité » plutôt que de transformer l’écrit en preuve orale.
3. Envisager un champ central de suivi d’adaptations individuelles et de contrôle des biais linguistiques sans stocker de données personnelles dans le contenu pédagogique.

Aucune de ces propositions ne modifie le registre, le canon ou la gouvernance dans ce ZIP.
