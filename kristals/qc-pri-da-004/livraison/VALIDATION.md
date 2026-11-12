# Journal de validation — `qc-pri-da-004` (livraison v1.2)

**Objet livré** : delta local de 14 fichiers sous `kristals/qc-pri-da-004/`, destiné à être extrait depuis la racine **interne** du workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. **Statut** : `a_revoir` (ni publié, ni homologué, ni certifié).

## Sources examinées et étendue du travail

- Source effectivement disponible : `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`, contenant le dossier maître **v1.2** sous `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`.
- Lus : `governance/Norme_Pedagogique_Autonome_v1.2/{CONTRAT_PEDAGOGIQUE_V1.2,GENERATEUR_ET_EXAMENS,CHARTE_CONVERSION_QC}.md`, graphe central, `authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`, `authoring/ALIGNEMENT.md` et `authoring/BRIEF_REDACTION.md` du Kristal concerné; `REFERENCES_EVIDENCE.md` consulté.
- Le YAML original et ses champs ont été préservés **à l'identique** dans `PARCOURS.md`. Le contrat JSON conserve les propriétés et identifiants v1.2 existants, avec des paramètres supplémentaires **dans la famille d'évaluation d'origine**; seuls deux statuts textuels deviennent des descriptions de la rédaction en cours.
- Identité et graphe : `obj-1`, `crit-1`, preuve et famille `qc-pri-da-004-ev-01` inchangés; `requires` = `qc-pri-da-003`, recommandation non bloquante = aucune, `reinforces` = `qc-pri-mu-002`. Le diagnostic permet de faire valoir un acquis équivalent.

## Contrôles exécutés par le script de livraison

1. Lecture et analyse du JSON du graphe et du contrat v1.2; vérification des arêtes sortantes `requires` / `reinforces` et du contrat originel.
2. Parsing du front matter YAML d'origine puis comparaison intégrale au front matter livré; présence des **12 sections numérotées** dans l'ordre exact, ainsi que de l'objectif, de la preuve et des relations attendus.
3. Préflight du contrat JSON : conservation des champs et identifiants préexistants, famille d'évaluation unique et présence des treize propriétés requises par `GENERATEUR_ET_EXAMENS.md`.
4. Préflight du contenu : présence d'au moins **2 exemples résolus, 2 contre-exemples, 2 diagnostics, 3 exercices guidés, 4 pratiques autonomes, 2 transferts** (présence structurelle des sections ciblées).
5. Banque JSON : **10 items** distincts, identifiants séquentiels `q-001`–`q-010`, champs communs renseignés, liens `obj-1` / `crit-1` / `qc-pri-da-004-ev-01`, modes dans l'ensemble autorisé, tous `a_revoir`; aucun paramétrage aléatoire ni seed prétendument calculée.
6. Vérification structurelle des deux preuves indépendantes : **`q-009` horloge (temps) et `q-010` archipel (espace)**, consignes différentes, rubriques A–D et conditions d'autonomie. Les corrigés sont **rubriques descriptives et productions possibles**, pas des réponses numériques déterministes. Une validation scientifique/terrain de ces rubriques n'est pas accomplie.
7. Préflight de la liste exacte du manifeste : **14 chemins relatifs complets**, aucune ressource externe embarquée. Le script de construction vérifie ensuite le contenu réel du ZIP, l'absence d'échappement de répertoire, sa CRC et la cohérence entre manifeste et entrées.
8. Revue rédactionnelle préliminaire des droits et de l'accès : absence de fichiers média et de chorégraphies tierces reproduites; consignes textuelles originales; modalités assise/debout/assistée, absence de mouvements dangereux imposés et possibilité de refuser une captation. **Ce contrôle du texte ne remplace pas un audit de licences ou un essai d'accessibilité effectif.**

## Points qui ne sont PAS validés

- **Revue humaine disciplinaire** des concepts, scénarios, exemples, grilles et seuils 0–3; essai par un enseignant de danse avec un groupe d'élèves; durée réelle; stabilité interévaluateurs; biais d'interprétation.
- Sécurité et accessibilité **en situation réelle**, notamment avec outils d'assistance ou interprète volontaire. Aucune évaluation de santé individuelle ou de locaux n'a été faite.
- Qualification de publication/Framework, `check`/`build-v9`/`check-ai`, projection LMS ou traitement du canon; aucune commande de ce type n'a été exécutée. Aucun alignement détaillé au PFEQ n'est revendiqué.
- Contrôle automatisé de la justesse artistique d'une production libre (impossible à garantir par simple génération textuelle). Les exemples sont plausibles à la lecture mais non certifiés sans revue et observation.
- Droit à diffuser les créations ultérieures des élèves : autorisations et politique locale à examiner; la livraison n'inclut ni musique, ni photo, ni vidéo.

## Propositions non appliquées aux structures centrales

- Ajouter ultérieurement au LMS un enregistrement **non canonique** des quatre dimensions A–D, du soutien fourni et des deux contextes, sans données sensibles ni vidéo par défaut.
- Soumettre à la gouvernance une convention de métadonnées de variation contrôlée, de traçabilité de l'accessibilité et d'une troisième preuve équivalente en cas de reprise.
- **Aucun changement** proposé ne modifie dans ce ZIP `registry/`, `governance/`, `canon/`, `docs/`, `state/`, `runtime/`, `AGENTS.md`, `ALIGNEMENT.md` ni les dossiers voisins.
