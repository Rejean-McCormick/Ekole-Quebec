# Validation et journal de livraison — qc-pri-fr-013 · v1.2

**Objet :** delta fusionnable de rédaction pour le seul Kristal `qc-pri-fr-013` — « Classes de mots ».  
**Base :** archive source `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis` fournie dans `initbundle(1).zip`.  
**Statut documentaire :** `a_revoir` — le contrôle technique ne vaut ni certification linguistique, ni qualification institutionnelle, ni publication du canon.

## Provenance et décisions appliquées

- Lecture effective des trois textes de `governance/Norme_Pedagogique_Autonome_v1.2/` demandés, du graphe `registry/GRAPHE_PEDAGOGIQUE_202.json`, des quatre fichiers locaux `authoring` demandés, de `AGENTS.md` et de `kristal.workspace.json`.
- Aucun `requires`, `recommends_before` ni `reinforces` **sortant** depuis cet ID dans le graphe v1.2; les relations **entrantes** ne modifient pas ses préalables.
- Intégrité conservée : `qc-pri-fr-013`, « Classes de mots », `FR`, objectif `obj-1`, critère `crit-1`, les cinq notions, preuve attendue, préalables et famille `qc-pri-fr-013-ev-01`.
- Développement du `PARCOURS.md` sans perdre le frontmatter YAML ni l'ordre des 12 sections. Complément du contrat JSON en gardant l'organisation existante, ses familles et ses champs initiaux; le statut de rédaction est désormais « à revoir ».
- Aucun fichier du workspace global, du canon, de la gouvernance, du registre, du runtime, des docs existantes ou d'un autre Kristal inclus/modifié dans ce delta.

## Contenu livré

| Dossier | Livrables | Couverture |
|---|---|---|
| `authoring/` | 2 remplacements | parcours 12 sections, contrat v1.2 avec attributs d'évaluation supplémentaires |
| `contenu/` | 6 nouveaux documents | 5 notions, 3 exemples résolus, 4 contre-exemples, 2 diagnostics, 1 modelage, 3 guidés, 4 autonomes, 2 transferts, feedback et rappels J+2 / J+7 |
| `evaluation/` | 3 nouveaux documents | plan détaillé, 12 items fixes, grille non compensatoire à 2 contextes autonomes (A/B), 2 justifications ambiguës par preuve |
| `sources/` | 1 nouveau document | source interne, pages linguistiques consultées, raisonnements dérivés, droits et limites |
| `livraison/` | 2 nouveaux documents | manifeste des 14 fichiers, présente note de validation |

## Vérifications techniques réellement réalisées

Les contrôles sont menés sur les fichiers réellement produits et sur l'archive ZIP finale par un script Python local. **La validation doit être lue conjointement avec la sortie d'exécution correspondante; l'absence d'exécution réussie empêche toute revendication de succès.**

1. Présence et taille non nulle des **14 chemins exacts**, aucun fichier supplémentaire.
2. Parse `json` des trois JSON (contrat, banque, manifeste); parse YAML du frontmatter `PARCOURS.md` et comparaison des clés et valeurs initiales à la base source.
3. Conservation des **12 rubriques** dans le même ordre; objectif / preuve / identifiants / préalables / famille conformes à la source.
4. Présence des **13 attributs minimum** de la famille prévus par `GENERATEUR_ET_EXAMENS.md`; 12 items numérotés sans doublon avec tous les champs requis, corrigés structurés et rétroactions.
5. Contrôle lexical de toutes les étiquettes de mots visés dans leurs stimuli et correspondance 1:1 avec les repères élèves; vérification structurée des cinq classes dans chaque preuve et de deux justifications par preuve.
6. Vérification des références locales relatives `../...` trouvées dans les documents Markdown, contrôle de la situation du graphe source (aucune arête sortante).
7. Comparaison du manifeste aux 14 chemins canoniques exacts, puis inspection du ZIP : 14 entrées régulières seulement, première entrée sous `kristals/qc-pri-fr-013/`, aucune entrée absolue ou avec `..`, pas de racine englobante, contenu binaire égal aux fichiers sources, intégrité CRC.
8. Relecture rédactionnelle interne des exemples clés (*le*, *les*, *marche*, *porte*, *ferme*), consignes, niveaux, corrigés et propositions de remédiation. Cette relecture n'est **pas** un second correcteur indépendant ni un test sur élèves.

## Limites non résolues et revue humaine obligatoire

- **Validation humaine de contenu non réalisée :** faire revoir l'exactitude de chaque phrase, la terminologie de grammaire actuelle, les indices de justification et le caractère univoque des repères par une ou un spécialiste du français.
- **Épreuves non pilotées :** tester les deux tâches A/B auprès d'apprenants, calibrer le seuil indicatif de 10/12, la durée et l'équité des contexts, s'assurer que deux manifestations suffisent pour la décision voulue.
- **Accessibilité technique non testée en situation :** vérifier lecteur d'écran, synthèse vocale, description des repères, dictée littérale et interface LMS. Les options de conception sont proposées mais non qualifiées.
- **Droits :** textes originaux produits pour cette livraison; liens URL informatifs vers des sources publiques. Aucune illustration tierce ni citation longue reproduite. Pas d'audit juridique indépendant ni de validation des droits de diffusion dans une plateforme donnée.
- **Qualité automatisée limitée :** le parseur et le contrôle lexical attestent la structure, **pas** la justesse grammaticale exhaustive ni la qualité psychométrique. Aucun moteur de validation externe des réponses libres ou générateur paramétrique effectif.
- **Infrastructure non testée :** pas de build canonique v9, de validation par le Framework Kristal, de publication/activation ni de test d'import Moodle. Le bundle est uniquement un delta documentaire.
- **Aucune conformité scolaire officielle :** la discipline est nommée selon la charte Québec; aucune conformité détaillée ni homologation PFEQ revendiquée.

## Propositions de structure — non appliquées

1. Pour une version ultérieure du contrat commun, ajouter un schéma JSON versionné des objets `criteres` et `corrige_structure` afin de sécuriser leur interprétation par le LMS; aucun schéma central n'a été modifié.
2. Prévoir dans un registre global distinct un champ de **révision humaine du corrigé**, une date et un identifiant de réviseur; ne pas utiliser `validation_status: a_revoir` comme signal de publication.
3. Ajouter un mécanisme transversal d'accessibilité des repères (références explicites aux positions dans le texte source) avant tout générateur de variantes; aucune variante libre n'est livrée.

## Fusion dans le workspace existant

Depuis la racine décompressée `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, extraire **`qc-pri-fr-013_livraison_v1.2.zip`**. Les chemins internes commencent tous par `kristals/qc-pri-fr-013/` et se superposent à cette seule feuille, sans dossier `Frames_202_...` englobant. Vérifier les deux remplacements `authoring/` avant qualification; les autres 12 fichiers sont des ajouts.
