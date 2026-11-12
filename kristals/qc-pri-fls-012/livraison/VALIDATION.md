# Rapport de validation locale — livraison `qc-pri-fls-012` v1.2

## Périmètre, autorité et étiquette de qualité

- **Périmètre exclusif :** `qc-pri-fls-012` — « Réaliser des projets de communication en français »; discipline « Français, langue seconde »; vague 3.
- **Source de départ effectivement présente :** dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` contenu dans l'archive fournie `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`. Le **nom du ZIP conteneur** indique v1.1, mais les fichiers utilisés portent bien la gouvernance et les métadonnées de la **frame v1.2**. Aucune frame n'a été réinventée.
- **Statut de la livraison :** contenus rédigés, contrôles structurels locaux effectués, **revue pédagogique humaine et mise à l'essai nécessaires**. Banque et famille à `a_revoir`. Aucun statut certifié, homologué, approuvé ou publié.
- **Champs d'identité inchangés :** ID, titre, discipline FLS, `obj-1`, `crit-1`, texte exact de l'objectif et de la preuve, `requires: qc-pri-fls-005`, `recommends_before: qc-pri-fls-009`, `reinforces: qc-pri-ccq-008`, famille `qc-pri-fls-012-ev-01`; pas d'alignement détaillé PFEQ.

## Fichiers livrés et opérations

1. `authoring/PARCOURS.md` — 12 sections remplies; frontmatter YAML original reproduit octet par octet et conservé `en_rédaction` jusqu'à validation humaine.
2. `authoring/CONTRAT_PEDAGOGIQUE.json` — valeurs et champs natifs préservés, famille enrichie des clés demandées par la gouvernance (variables de scénario fermées, contraintes, rubriques, source, seed nul et statut à revoir).
3. `contenu/01_NOTIONS_ET_EXEMPLES.md` — trois notions définies, 2 exemples résolus et 4 contre-exemples commentés.
4. `contenu/02_DIAGNOSTIC.md` — 3 tâches avec corrigés et décision conditionnelle de maîtrise équivalente du prérequis.
5. `contenu/03_ENSEIGNEMENT_GUIDE.md` — 2 démonstrations (invitation, demande), contrôles de compréhension et modelage oral/écrit.
6. `contenu/04_PRATIQUE_ACCOMPAGNEE.md` — 3 exercices à indices dégressifs, modèles possibles et rétroactions ciblées.
7. `contenu/05_PRATIQUE_AUTONOME.md` — 4 situations différentes, critères et réponses possibles.
8. `contenu/06_REMEDIATION_ET_TRANSFERT.md` — remédiations ciblées, 2 transferts distincts et rappels différés.
9. `evaluation/PLAN_EVALUATION.md` — matrice explicite de 12 items vers `obj-1`, `crit-1` et la famille; accessibilité et contrôle des variantes réelles.
10. `evaluation/BANQUE_ITEMS.json` — 12 items : 10 tâches formatives fixes + 2 preuves authentiques encadrées de type `scenario_controle`, sans génération aléatoire et avec observation écrite/orale.
11. `evaluation/GRILLE_MAITRISE.md` — 6 dimensions, 4 niveaux descriptifs, contrôle de 2 contextes et règle de maîtrise non compensatoire.
12. `sources/REFERENCES_CONTENU.md` — références internes consultées, références externes seulement signalées, productions originales, droits et limites.
13. `livraison/MANIFEST.json` — liste exhaustive des 14 chemins, format, version, racine et statut.
14. `livraison/VALIDATION.md` — présent rapport.

## Tests réellement exécutés

**Méthode :** scripts locaux de lecture/validation JSON/YAML et inspection des fichiers source, contrôles de texte structurés, comparaison des champs v1.2, vérifications de faits dans les dix corrigés fixes, et tests des entrées ZIP/CRC. **Les assertions automatiques sont des contrôles techniques et de cohérence, pas une preuve de justesse pédagogique ou de qualité linguistique.**

- **Préemballage : 504 assertions réussies** sur les 13 fichiers disponibles à cette étape et le ZIP source. Parmi elles : preservation récursive des 57 éléments originaux du contrat; identité YAML et 12 sections; 12 identifiants uniques et ordonnés; champs/états de tous les items; corrigés fixes confrontés à 24 valeurs ou termes clés; présence de la matrice complète; deux rôles distincts de maîtrise, deux modalités, scénarios bornés, provenance et graphe d'origine vérifiés. Une comparaison de chaînes initialement trop stricte a été adaptée pour tenir compte de formulations françaises équivalentes; un corrigé a été précisé (item 002 : « deux boîtes »), puis la batterie a été **réexécutée avec succès**.
- **Emballage et fusion technique :** seconde passe de validation effectuée **après** création du ZIP : arborescence exacte et unique de 14 entrées sans dossier englobant; préfixe et premier chemin corrects; aucune entrée absolue ou `../`; fichiers non vides; identités et JSON parsables depuis l'archive; comparaison binaire ZIP ↔ fichiers source; lecture CRC ZIP; compatibilité des chemins avec la racine du workspace v1.2. Les tests de fusion portent sur la **superposition des chemins** et la préservation de la frame, pas sur une exécution de moteur ou un déploiement.
- **Test d'accessibilité documentaire :** présence contrôlée de solutions adaptées (texte lisible, supports oraux/visuels, communication assistée, jugement sur intelligibilité plutôt que l'accent) et de règles de confidentialité. L'accessibilité auprès d'élèves réels **n'a pas été testée**.

## Validations humaines nécessaires

- Vérifier l'adéquation des énoncés, la charge langagière et la qualité des rubriques avec un enseignement de français langue seconde; vérifier le caractère non discriminatoire des choix de supports et critères, et effectuer un essai en classe.
- Pour les preuves A/B, confirmer **localement** les faits authentiques, la disponibilité du destinataire, les conditions de remise, le contexte réel, l'absence de données privées, les modalités d'accès; observer en direct deux productions **écrites et présentées oralement**. En absence d'un contexte, reporter l'évaluation au lieu d'inventer un « réel » fictif.
- Examiner les droits/licences institutionnels sur les documents du workspace et les modalités de conservation des traces (ne pas enregistrer des données d'enfants dans le dépôt canonique).
- Qualifier les évaluations, clarifier les seuils après essai interjuges et procéder aux contrôles techniques propres au Framework/LMS de destination. Aucun test d'intégration Framework, de publication, de qualité par des enseignantes/enseignants ni d'alignement PFEQ n'a été réalisé.

## Propositions de changement de structure — **aucune modification appliquée**

1. Au besoin, soumettre au responsable du registre **une proposition versionnée** d'ajout d'un pointeur facultatif vers les fiches de faits locaux datés, qui resteraient dans le LMS, hors du canon.
2. Proposer un champ de trace séparant observation orale et produit écrit, et une marque « situation réelle vérifiée », sans changement rétroactif des identifiants ou familles.
3. Ne modifier aucun `registry/`, `governance/`, `canon/`, `state/`, `runtime/`, `AGENTS.md`, `ALIGNEMENT.md`, `kristal.workspace.json` ou workspace voisin.

**Bilan :** delta fusionnable sur la frame v1.2, non qualifié pour publication sans revue, essais et validation humaine des preuves authentiques.
