# Journal de validation et limites — `qc-pri-ma-032`

**Statut :** `controle_technique_passe_revue_humaine_requise`. Delta du workspace v1.2, non publié, non homologué et non certifié. Les épreuves n'ont pas été essayées avec des élèves.

## Contrôles effectivement exécutés (script local reproductible `_verify_ma032.py`)

1. **Structure :** exactement **14 fichiers ciblés**, non vides, aucun fichier hors liste (réussi).
2. **Identité et parcours :** front matter YAML vérifié (PyYAML), tous les champs d'origine conservés sauf statut et révision de contenu mis à jour; identifiant, titre, discipline, objectif, preuve, absence de préalables et famille immuables; **12 titres de section et ordre intacts** (réussi).
3. **Contrat :** JSON analysé, familles et champs v1.2 conservés; 13 champs minimum du contrat d'examens présents; statut `a_revoir` (réussi).
4. **Workspace maître :** présence des huit documents canoniques/gouvernance demandés; graphe vérifié, aucune arête entrante/sortante pour cet ID; comparaison des chemins : **2 remplacements** sous authoring et **12 ajouts** seulement (réussi).
5. **Items :** JSON analysé; 12 IDs uniques ordonnés, 8 modes `parametrique` + 4 `fixe`, tous liés à `obj-1`, `crit-1`, `qc-pri-ma-032-ev-01`; questions, réponses, critères, feedback et statuts présents; deux contextes de preuve signalés (réussi).
6. **Mathématiques paramétriques :** recomptage indépendant des issues par prédicats explicites sur **43 combinaisons** de huit domaines finis, comparé à la fonction de solution; **16 exemples seedés** vérifiés (stimulus, variables, comptes et texte du corrigé); aucune IA libre (réussi).
7. **Items fixes :** contrôle arithmétique indépendant des chances (9/10; 5/7 contre 2/7; 4/6 contre 2/6; angles de 270°, 30° et 330° sur 360°) (réussi).
8. **Cohérence textuelle :** 12 items référencés dans le plan, liens internes vers les fichiers du delta et lien autorisé vers ALIGNEMENT existant; contrôles textuels statiques de la provenance, des droits, de l'accessibilité et du rappel différé (réussi, **ne remplace pas** une revue d'accessibilité humaine).
9. **Manifeste :** JSON analysé; liste exacte des 14 chemins et racine `kristals/qc-pri-ma-032/` sans traversée ni espace global (réussi).
10. **Archive ZIP :** liste des 14 entrées, premier chemin dans la bonne racine, lecture intégrale et test CRC, parsing des JSON internes, identité des fichiers avec le dossier préparé (réussi).
11. **Simulation de fusion :** décompression de la source originale du dossier du Kristal et superposition du delta dans un dossier temporaire, vérification des 2 remplacements et 12 ajouts, contrôle des fichiers protégés inchangés (réussi).

## Limites non résolues / revue humaine nécessaire

- La **clarté du mot « probable »** (convention de majorité explicite) et des critères de justification doit être évaluée par une personne enseignante; ne pas confondre définition pédagogique choisie et usage universel du langage.
- Le générateur est reproductible mais ses règles de reconnaissance des **justifications en langage naturel** ne sont pas certifiées automatiquement. Une revue des rubriques, des accommodations et des variantes de réponse équivalentes est nécessaire.
- Les seeds peuvent produire une **même instance pour plusieurs seeds** si les domaines sont petits : déterminisme garanti, pas unicité garantie. Diversifier les tuples pour les deux preuves autonomes si un futur générateur les utilise.
- Aucun essai réel avec des élèves, aucune vérification LMS, aucune étude empirique des biais ou de l'adaptation visuelle/tactile; des validations humaines restent nécessaires avant déploiement.
- Les droits sont documentés comme productions originales et absence d'éléments tiers copiés; contrôle de rédaction, **pas** opinion juridique ni examen exhaustif de similitudes.

## Éléments de structure éventuellement à proposer (NON appliqués)

- Ajouter au futur schéma central un champ `hypothese_equiprobabilite` ou `definition_locale_de_probable` pour éviter les comparaisons non fondées.
- Ajouter un champ central `accessibility_review_status`, distinct de la validation des calculs.
- Outiller la conservation des preuves avec contexte et niveau d'aide, sans écriture dans `canon/` ni les registres centraux.

## Périmètre exact de la livraison

Seulement `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json` remplacés; les douze autres chemins du manifeste ajoutés. Aucun `AGENTS.md`, `kristal.workspace.json`, `ALIGNEMENT.md`, fichier canon, dossier `docs/`, `runtime/`, `state/`, `registry/` ou `governance/` inclus ou modifié. Extraire le ZIP directement à l'intérieur de `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` du workspace maître.
