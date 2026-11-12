# Validation effectivement exécutée — `qc-pri-st-008`

**Source utilisée :** `/mnt/data/initbundle(1).zip` contenant le workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` (le ZIP source n’est pas livré).

## Tests d’identité, contenu et banque, exécutés le 2026-10-08

Résultats contrôlés automatiquement par `test_pack_st008.py` :

- **PASS** — YAML parse et conservation exacte du bloc YAML.
- **PASS** — Métadonnées objectives immuables.
- **PASS** — Familles d’origine conservées.
- **PASS** — Clés racines du contrat préservées et valeurs non famille inchangées.
- **PASS** — Clés de famille natives préservées, autres valeurs natives inchangées.
- **PASS** — 13 paramètres du générateur présents.
- **PASS** — Pré-requis / ordre conseillé.
- **PASS** — Identité, concepts, familles YAML.
- **PASS** — Graphe : sortie conseillée non bloquante.
- **PASS** — 12 sections pédagogiques numérotées.
- **PASS** — Connaissances, diagnostic, rappel différé, adaptation explicités.
- **PASS** — ≥ 2 exemples commentés et ≥ 2 contre-exemples.
- **PASS** — ≥ 2 tâches diagnostiques.
- **PASS** — ≥ 3 activités guidées progressives.
- **PASS** — ≥ 4 pratiques autonomes corrigées.
- **PASS** — 2 tâches de transfert et rappel différé.
- **PASS** — Format de banque, identités, famille.
- **PASS** — 10 items complets, 10 ID uniques.
- **PASS** — Champs du format obligatoires et énoncés non vides.
- **PASS** — Références d’items obj-1, crit-1, famille figées.
- **PASS** — Modes, difficultés, statuts admis.
- **PASS** — 6 scénarios contrôlés et 4 fixes.
- **PASS** — 12 variantes deterministes à seed et réponse fixes.
- **PASS** — 12 variantes de stimulus distinctes.
- **PASS** — 4 items fixes sans seed/variables.
- **PASS** — Deux contextes de maîtrise autonomes distincts.
- **PASS** — 10 lignes du plan lient obj-1, crit-1 et family_id.
- **PASS** — Grille 4 axes, 3 niveaux et 2 preuves.
- **PASS** — Sources vérifiées vs original séparés et aucun média incorporé.
- **PASS** — Références relatives ../ entre fichiers existantes.
- **PASS** — Sécurité / accessibilité dans parcours et évaluation.
- **PASS** — Manifeste strict des 14 chemins.
- **PASS** — 2 seuls remplacements et 12 fichiers neufs.

**Résultat de cette phase : 33/33 contrôles réussis; 12 variantes résolues par correspondance exacte catalogue/seed/réponse (ce test ne constitue PAS un solveur scientifique indépendant).**

## Vérification éditoriale (différente des tests automatiques)

- Les contenus décrivent uniquement des situations contrôlées sur papier, distinguent observations et explications modélisées, et ne prétendent pas que l’énergie est créée ou disparaît. Les exemples de type pile→lampe, vent→moulinet et photovoltaïque ont été confrontés aux principes exposés par EIA/DOE (sources détaillées dans `../sources/REFERENCES_CONTENU.md`).
- Les textes d’items et corrigés ont été relus dans le cadre de cette production; aucune validation externe ni essai sur élèves. Il subsiste un jugement de contenu scientifique humain à effectuer pour les variantes et des décisions de cotation à calibrer.

## Contrôles du ZIP fusionnable

Le ZIP est construit en ne prenant que les 14 fichiers du manifeste et avec la racine interne `kristals/qc-pri-st-008/`. Vérifications exécutées après empaquetage : voir la liste ci-dessous.

- **PASS** — 14 entrées ZIP exactement, toutes non vides, pas de dossiers englobants ni entrée isolée.
- **PASS** — premier chemin sous `kristals/qc-pri-st-008/`; aucun autre Kristal, aucune traversée `../` ni chemin absolu.
- **PASS** — intégrité CRC/testzip de chaque entrée; les octets empaquetés sont identiques aux fichiers rédigés.
- **PASS** — les trois JSON sont parsables depuis leurs octets dans l’archive; le manifeste y liste les 14 chemins exactement.

## Limites ouvertes, revue humaine et décisions

1. **À revoir humainement :** exactitude physique et simplifications (pile et stockage chimique, dynamo, moteur et rendement, frontière des systèmes), équité des contextes, niveau de langue, accessibilité effective et durée de passation.
2. **Non réalisé :** essai en classe, calibration entre correcteurs, contrôle institutionnel de licences externes, intégration LMS ou compilation de canon v9, vérification d’homologation PFEQ. Aucune qualification « publié », « homologué » ou « certifié » n’est revendiquée.
3. **Proposition de structure (non appliquée) :** ajouter ultérieurement au standard un champ explicite `frontiere_du_systeme` et un attribut `nature_preuve = observee|inference` pour les items scientifiques; nécessite décision versionnée centrale, **aucun fichier global modifié**.
4. **Portée de la fusion :** seuls `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json` remplacent des fichiers préexistants; 12 autres sont ajoutés. Ne fusionner qu’à la racine du workspace v1.2; ne modifier ni `governance/`, `registry/`, `AGENTS.md`, `ALIGNEMENT.md`, `docs/`, `canon/`, `runtime/`, `state/` ni d’autres Kristals.
