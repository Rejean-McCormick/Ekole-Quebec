# Rapport de validation effectivement réalisée — `qc-pri-als-002` v1.2

**Archive livrée :** `qc-pri-als-002_livraison_v1.2.zip`. **Base inspectée :** archive source nommée `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`, dont le workspace interne `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` est une **frame v1.2**. **Objet exclusif :** `qc-pri-als-002` — *Reconnaître et utiliser le vocabulaire quotidien*, Anglais, langue seconde. **Qualification :** contenu produit pour **revue humaine**, ni cours publié ni examen certifié.

## Contrôles exécutés par le script de construction

- Lecture effective du contrat pédagogique v1.2, du générateur/examens v1.2, de la charte de conversion, du graphe et des quatre fichiers locaux de la frame. Le graphe ne déclare **aucun `requires` partant** de `qc-pri-als-002`. Les liens **entrants** n'imposent pas de préalable à cette feuille.
- **YAML de la frame originale strictement identique** après remplacement du corps de `PARCOURS.md`; exactement **12 sections numérotées**, dans l'ordre, avec `obj-1`, `crit-1`, l'objectif et la preuve immuables. Contexte, notions, trois exercices guidés, quatre autonomes, deux diagnostics, deux transferts, feedback et rappel différé vérifiés par recherches structurées.
- **Contrat JSON** : champs préexistants conservés, valeurs identitaires, concepts, liens, famille, mode, rubriques natives et génération préexistante préservés; tous les champs supplémentaires `GENERATEUR_ET_EXAMENS.md` inclus dans la famille. `statut` et `review_status` de famille changés pour refléter le contenu produit **à revoir**.
- **12 items JSON uniques** `q-001` à `q-012`, avec énoncé, stimulus, réponse/grille, rétroaction, difficulté, `obj-1`, `crit-1`, famille `qc-pri-als-002-ev-01` et statut `a_revoir`. Deux preuves distinctes `q-009` et `q-010`, chacune dans une situation différente, portant sur **trois noms anglais distincts** en **deux tours de l'élève** sans indices lexicaux; deux variantes bornées par preuve et sans tirage aléatoire (`seed: null`).
- **Corrigés contrôlés textuellement** : pour chacun des 12 items, les mots cibles attendus figurent effectivement dans la réponse publiée; pour les deux preuves, les 3 noms des scénarios par défaut et ceux des variantes figurent dans leurs corrigés respectifs et sont distincts. **Il s'agit de contrôles de présence et cohérence lexicale**, non d'un test automatique d'acceptabilité linguistique universelle, d'un solveur, d'un enregistrement oral ou d'un essai en classe.
- Vérifications documentaires : au moins deux exemples résolus et deux contre-exemples, deux diagnostics, trois pratiques guidées à indices dégressifs, quatre tâches autonomes, deux transferts, remédiations ciblées, modalités d'accessibilité, scènes fictives et provenance/droits déclarés. Les liens relatifs de `PARCOURS.md` vers les fichiers prévus ou `ALIGNEMENT.md` ont été résolus par inventaire.

## Contrôle technique final de l'archive (exécuté automatiquement après sa fabrication)

- **14 fichiers strictement**, tous non vides, chacun sous la racine interne `kristals/qc-pri-als-002/`; premier chemin directement sous cette racine. Aucun dossier englobant `Frames_202_.../`, `lot/`, `livraison/` global ni autre Kristal; aucune entrée absolue ou contenant `../`.
- Liste du manifeste **égale à l'inventaire du ZIP**, ordre conforme au filetree; JSON de `CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json` et `MANIFEST.json` parsables en JSON strict; vérification **CRC du ZIP**, pas de fichiers vides.
- **Simulation de fusion par comparaison des chemins** à ceux du workspace v1.2 présent dans l'archive maîtresse : **2 remplacements** (`authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`) et **12 ajouts**. Aucun fichier `ALIGNEMENT.md`, `AGENTS.md`, `kristal.workspace.json`, `docs/`, `canon/`, `state/`, `runtime/`, `registry/`, `governance/` ou autre ID inclus. **Ce test ne remplace pas une fusion ou un déploiement effectif.**

## Limites non résolues — revue humaine obligatoire

1. **Anglais et contenu :** vérifier par une personne qualifiée les dialogues, leur naturel pour différentes variétés d'anglais, le seuil de 3 mots distincts, l'équilibre des contextes et les reformulations acceptables. Ce contrôle n'a pas été réalisé par un expert externe.
2. **Évaluation :** valider les rubriques L/C/T/I, former les évaluateurs, mesurer l'accord intercorrecteurs, contrôler le niveau de difficulté, la culture, l'équité, la durée et administrer un essai auprès d'apprenants; **aucun élève ni correcteur humain n'a été testé**.
3. **Accessibilité :** relire avec personnes concernées et adapter si besoin les descriptions, canaux écrits, CAA, audition, motricité et scénarios; **pas d'essai utilisateur**.
4. **Droits :** toutes les scènes et textes sont de rédaction originale dans ce delta; aucun média externe incorporé. **Aucun audit légal externe, vérification intégrale de droits ou contrôle automatisé de similarité effectué**.
5. **Sécurité et vie privée :** scénarios fictifs, pas de consommation ni données réelles nécessaires; les procédures de stockage/suppression d'observations doivent être définies au déploiement.
6. **Vérification technique intégrée :** JSON, schémas vérifiés par assertions structurelles locales et non par un validateur officiel Framework ou une intégration LMS. Les revendications de conformité PFEQ, homologation, publication ou certification sont **exclues**.

## Journal des modifications et propositions sans action centrale

- **Modifiés/remplacés :** `authoring/PARCOURS.md` (YAML original conservé octet pour octet) et `authoring/CONTRAT_PEDAGOGIQUE.json` (forme native conservée, champs de famille complétés).
- **Ajoutés :** six leçons sous `contenu/`, trois fichiers `evaluation/`, un fichier `sources/` et deux fichiers `livraison/`.
- **Propositions non appliquées** au centre : définir un validateur partagé de la banque 1.0, une liste contrôlée des statuts de qualification (`a_revoir`, `revue_humaine_terminee`, etc.) et un registre de vérification de l'équité/accord intercorrecteurs. **Aucun registre, graphe ni schéma central modifié.**

**Consigne de fusion :** décompresser la frame maîtresse v1.2, entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis extraire ce ZIP à cet emplacement. Pas de dossier parent additionnel.
