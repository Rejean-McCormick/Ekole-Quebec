# Validation et journal de modifications — `qc-pri-ma-011`

**Périmètre exclusif :** `kristals/qc-pri-ma-011/`. **Base :** frame pédagogique v1.2 de l'archive source `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`, à l'intérieur du dossier maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Les gouvernances v1.2 actives ont été lues; nom externe de l'archive non confondu avec la version du dossier maître.

## Modifications réellement livrées

- **2 remplacements complets :** `authoring/PARCOURS.md` (frontmatter YAML original conservé octet pour octet avant normalisation d'affichage; 12 sections enrichies) et `authoring/CONTRAT_PEDAGOGIQUE.json` (mêmes clés et valeurs invariantes, famille native enrichie de paramètres, aucun ID changé).
- **12 nouveaux fichiers :** six documents pédagogiques (`contenu/`), trois d'évaluation (`evaluation/`), une provenance (`sources/`), le manifeste et ce rapport (`livraison/`).
- **Banque :** 12 items, dont 4 fixes et 8 paramétriques à jeu fermé; 53 couples/admissibilités numériques soumis à vérification arithmétique, dont deux preuves finales situées (livres, billets).

## Contrôles réellement exécutés dans le script local

- 27 contrôles préassemblage, puis 29 vérifications de présence, JSON, chemins, manifeste et intégrité ZIP (**56 contrôles au total**, en complément des 53 variantes mathématiques); tout échec interrompt la livraison.
- Contrôle d'identité, titre, `obj-1`, `crit-1`, dépendances `requires qc-pri-ma-003` et `recommends_before qc-pri-ma-010` sur le graphe source; aucun lien nouveau ajouté.
- Comparaison exacte du frontmatter YAML d'origine et recensement des **12 sections**, conservation des champs et liens canoniques du contrat v1.2 et des identifiants de famille.
- Contrôle des **12 numéros uniques q-001…q-012**, des champs obligatoires et des niveaux/modes permis, des **2 contextes autonomes**, des 2 diagnostics, 3 guidages, 4 autonomies, 2 transferts.
- Vérification de 53 couples (règle fermée, contraintes de report et de zéro, valeurs correctes et copies fausses distinctes) avec contrôle inverse indépendant utilisant `int` Python; vérification des calculs numériques fixes cités dans les cours. Les textes expliquant le « premier pas faux » sont aussi explicites, mais **pas validés par un expert humain**.
- Le ZIP est soumis ensuite à des tests spécifiques : chemins autorisés, taille non nulle, JSON strict, manifeste, absence de parcours `..`, `testzip()` CRC. Le rapport final n'atteste de ces tests ZIP que si le programme a terminé sans exception et affiche leur succès.
- Vérification documentaire du traitement des droits (textes originaux et statut des licences à confirmer), accès oral/visuel/manipulable, sécurité fictive des scénarios et liens relatifs contrôlés.

## Non exécuté — revue humaine nécessaire

- **Aucun** essai auprès d'apprenants, aucune estimation empirique de difficulté, aucune étude psychométrique, aucun audit exhaustif d'accessibilité avec lecteurs d'écran ou dispositifs spécialisés.
- Aucune validation pédagogique humaine des formulations, des écarts de complexité ni des rubriques; il faut vérifier les consignes des copies fictives, le temps réel, l'intelligibilité de la correction et l'absence d'ambiguïté du « premier faux pas ».
- Aucun test d'intégration au LMS, au runtime ni au build v9; aucune publication, certification, homologation PFEQ, vérification juridique de licence ou qualification réseau.
- La revue humaine devra notamment confirmer que l'extension multiplication courte est adaptée au parcours assemblé et qu'une modalité orale conserve une trace exploitable du calcul.

## Propositions seulement (aucune base centrale modifiée)

1. Dans le registre/Framework lors d'une révision centrale éventuelle, définir un schéma formel pour `parametres.couples_autorises`, `selection` et les rubriques C1–C4; **proposition non appliquée**.
2. Outiller un banc de tests automatique inter-Kristals avec génération exhaustive pour les ensembles fermés, suivi des versions du pool et de la graine; **proposition non appliquée**.
3. Prévoir une projection de la modalité d'accessibilité et des deux preuves datées dans le LMS, hors canon; **proposition non appliquée**.

**Statut :** `controles_techniques_effectues_revue_humaine_requise` ; tous les items `a_revoir`. Aucun statut « certifié », « publié » ou « homologué ».
