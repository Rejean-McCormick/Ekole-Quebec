# Rapport de validation réelle — `qc-pri-eps-001`

**Base consultée :** ZIP maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` (fourni sous le nom de montage `initbundle(1).zip`). Seuls les 14 chemins listés par le manifeste sont remis; `AGENTS.md`, `kristal.workspace.json`, `authoring/ALIGNEMENT.md`, `registry/`, `governance/` et les autres Kristals ne sont ni écrasés ni inclus.

**État du livrable :** cours et évaluation rédigés, **contrôle technique effectué**, revue pédagogique/éthique de terrain indispensable. `validation_status = a_revoir` pour chaque item; aucune certification, homologation PFEQ ni publication déclarée.

## Vérifications réellement exécutées

1. Lecture et parsing du contrat source et du graphe; concordance `qc-pri-eps-001`, `obj-1`, `crit-1`, `qc-pri-eps-001-ev-01`, titre et appellation; aucune dépendance strictement bloquante.
2. YAML de front-matter du `PARCOURS.md` repris sans modification; parsing avec PyYAML; 12 rubriques numérotées, remplies.
3. Contrat JSON enrichi sans effacer ni changer ses anciens champs/familles; présence des 13 champs du générateur d'examens.
4. Banque JSON strictement parsable, 12 items uniques et ordonnés, chaque item avec tâche, réponse / grille, rétroaction et statut `a_revoir`, lien `obj-1`/`crit-1`/famille.
5. Deux contextes de maîtrise séparés (`q-011`, `q-012`) et variantes contrôlées; 800 instances de graines testées avec algorithme de sélection et corrigé couplé.
6. Nombre minimal d'activités et descriptions d'accessibilité et de sécurité vérifiés par inspection et assertions textuelles; **pas** de vérification clinique ni de test en classe.
7. Références externes consultées et listées; illustrations, photographies, musiques et autres assets tiers **absents**. Les contenus créés sont déclarés originaux, sans audit juridique exhaustif.
8. ZIP vérifié après création : 14 fichiers strictement conformes au manifeste, non vides, ordre et préfixe, aucun chemin absolu ou parent, intégrité CRC, JSON relus depuis le ZIP.
9. Simulation de fusion sur espace temporaire avec des fichiers protégés témoins : seuls les deux fichiers authoring prévus sont superposés, rien hors du périmètre n'est changé.

## Contrôles de conception non équivalents à une validation humaine

- Les rubriques de performance décrivent gestes, repères, sécurité et autonomie, jamais force, amplitude comparative, apparence, vitesse ni capacités physiques brutes.
- Un mouvement volontaire observable demeure requis; aménagement moteur et communication alternative doivent être vérifiés individuellement par l'équipe responsable.
- Une absence de geste dans un montage inaccessible est **non interprétable**, pas une « erreur » ou un diagnostic; les activités demandant une supervision humaine ne peuvent être testées physiquement par le script.

## Limites non résolues et relectures obligatoires

- Essai auprès de plusieurs élèves avec configurations de mobilité et de communication variées; ajustement de l'admissibilité des gestes, de la sécurité du mobilier et de la clarté des instructions.
- Étude de l'accord entre observateurs sur les quatre dimensions; cohérence de l'accommodation des repères de latéralité; protection effective des traces pédagogiques.
- Validation scientifique des formulations simplifiées et révision éditoriale francophone / EPS avant usage sommative.
- Confirmation des droits et consignes de réutilisation lors de l'intégration; ici, seulement des descriptions textuelles et des liens cités, pas de fichiers médias tiers.

## Propositions de changement (sans modification des bases centrales)

- Étudier, lors d'une version centralisée future, l'ajout d'un champ structuré `amenagements_accessibles` au registre d'items pour documenter la comparabilité des preuves.
- Étudier un champ `non_interpretable` distinct du niveau 0 dans un moteur LMS afin d'éviter de traiter une barrière d'accès comme un échec pédagogique.
- Ne modifier **aucun** graphe, schéma, norme, dossier canon, runtime ou workspace d'un autre ID dans ce delta.
