# Journal de livraison et validation — `qc-pri-st-013`

**Livraison visée :** `qc-pri-st-013_livraison_v1.2.zip` · **Base :** frame v1.2 fournie dans `initbundle(1).zip` sous `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` · **Statut :** `a_revoir`, non qualifié, non certifié, non publié.

## Identité et modifications exactes

- **Deux remplacements complets** à partir des originaux v1.2 : `authoring/PARCOURS.md` (YAML original préservé, 12 sections effectivement rédigées), `authoring/CONTRAT_PEDAGOGIQUE.json` (famille et champs préexistants conservés; treize champs minimum de génération présents).
- **Douze fichiers nouveaux :** six supports complets `contenu/`, trois fichiers d'évaluation, une provenance, un manifeste et ce journal de validation.
- **Noyau immuable :** `qc-pri-st-013` — « Roches, sols et relief », Science et technologie. `obj-1` : « Comparer roches et sols à partir de caractéristiques observables. » `crit-1` : « Établir un tableau comparatif d’échantillons sans risque. » Famille : `qc-pri-st-013-ev-01`.
- **Graphe :** aucun `requires`, uniquement `qc-pri-st-001` comme ordre conseillé non bloquant; aucun autre Kristal modifié. Aucune modification de `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `registry/`, `governance/`, `canon/`, `docs/`, `state/` ou `runtime/`.

## Contrôles effectivement exécutés

La routine locale de livraison a contrôlé la présence des fichiers originaux, les invariants d'ID/titre/objectif/preuve et le maintien de chaque champ initial du contrat JSON, les 12 sections YAML avec analyseur YAML, les deux contextes distincts de maîtrise, la correspondance exacte de dix items et de leurs numéros, les références `obj-1`/`crit-1`/famille, les champs obligatoires, les niveaux/modes et les statuts, la couverture de six documents pédagogiques, deux diagnostics, trois guidages, quatre autonomies, deux transferts, deux exemples et deux contre-exemples. Elle a vérifié les **quatre sélections** des variantes déterministes `q-004` et `q-008` (`seed % 2` pour chaque valeur 0/1), la présence de leurs corrigés et la concordance des stimuli affichés, les trois fiches et cinq dimensions des deux preuves, les références relatives, l'existence des documents scientifiques/provenances, les exigences d'accessibilité et les interdictions de prélèvement/manipulation. Les contrôles utilisent des validations de structure et de présence; ils ne prouvent **pas** la valeur didactique de toutes les formulations.

**Résultat du dernier lancement source :** `52/52` contrôles automatisés satisfaits. **Vérification finale du ZIP :** `14/14` chemins autorisés, tous non vides, premier chemin `kristals/qc-pri-st-013/authoring/PARCOURS.md`, aucune entrée absolue ou `../`, JSON parsables, liste du manifeste identique aux entrées, test d'intégrité CRC réussi. Les commandes et sorties d'exécution sont conservées dans le journal de l'outil au moment de la livraison; ce document indique les points contrôlés, pas une prétendue qualification officielle.

## Contrôle intellectuel : portée réelle

Les corrections sont **écrites explicitement** pour chaque cas : le classement de l'apparence granulaire reste qualitatif et ne se présente jamais comme une analyse texture USDA; aucun nom minéralogique, donnée d’érosion locale ou fertilité réelle n’est affirmé sans preuve. Les deux épreuves `q-009` et `q-010` ont chacune des exemples de tableaux complets, au moins deux comparaisons argumentées, des limites et une grille séparant cinq critères. Cette lecture éditoriale par le rédacteur ne constitue **pas** une révision scientifique ou didactique indépendante.

## Limites et revue humaine nécessaire avant qualification

1. **Science :** une personne compétente doit vérifier la formulation des définitions, les mots « sol »/« roche » dans les cas fictifs et la qualité des preuves d’observation, surtout quand la granularité interne n'est pas accessible.
2. **Didactique :** tester durée, difficulté, variété des cas, justesse des corrigés alternatifs, différenciation des deux manifestations et risques d'apprentissage par répétition; recueillir de vraies productions d'élèves sans les inventer.
3. **Accessibilité :** vérifier les versions adaptées, lecture vocale, tableaux utilisables sans motricité fine, langues et besoins particuliers en contexte réel.
4. **Sécurité :** vérifier la provenance, les allergies, le nettoyage et la fermeture des contenants si du vrai matériel est un jour proposé; l’alternative fiche intégralement textuelle évite l’exposition au départ.
5. **Droits et citations :** les pages USGS/USDA sont référencées, pas reproduites; confirmer les licences si une image externe est ajoutée ultérieurement. Aucun média tiers inclus actuellement.
6. **Système :** aucun build Framework v9/v10, aucun import LMS, essai auprès d'élèves, audit PFEQ, certification ou publication réalisés.

## Propositions de changement de structure (non appliquées)

- Ajouter **au schéma central lors d’une décision versionnée ultérieure**, si jugé utile, un champ facultatif `preuve_contextes` avec deux IDs distincts, pour tester automatiquement la double manifestation.
- Ajouter à la gouvernance une règle explicite pour les **scénarios contrôlés en corpus fermé** (graines entières, correspondance à une liste et corrigé verrouillé); actuellement la spécification autorise les variantes encadrées mais ne dicte pas leur sérialisation.
- Ajouter éventuellement un référentiel d'accessibilité des tableaux dans les interfaces de restitution; **ne pas** modifier le dossier `registry/` ou la racine de l'archive dans ce delta.
