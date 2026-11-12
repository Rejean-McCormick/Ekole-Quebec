# Validation et journal de livraison — `qc-pri-st-011` (delta v1.2)

## Périmètre strict et identité

**Kristal traité exclusivement :** `qc-pri-st-011` — « Objets techniques, mécanismes et fonctions », discipline « Science et technologie », vague 0. **Source :** workspace v1.2 imbriqué dans l'archive de spécification fournie. L'archive finale est un **delta fusionnable de 14 fichiers**, pas une nouvelle racine de projet. Les fichiers de gouvernance, registre, canon, runtime, state, docs, `AGENTS.md`, `kristal.workspace.json` et `authoring/ALIGNEMENT.md` ne sont pas inclus ni modifiés.

**Objectif inchangé** : `obj-1`, « Identifier la fonction d’éléments d’un objet technique usuel. »  
**Preuve inchangée** : `crit-1`, « Annoter un objet démontable ou documenté et expliquer ses fonctions. »  
**Aucun requires**; seul `qc-pri-st-001` reste conseillé/non bloquant. Famille unique `qc-pri-st-011-ev-01`.

## Livrables et modifications

- `authoring/PARCOURS.md` : 12 sections réellement rédigées, frontmatter YAML d'origine conservé avec mise à jour du seul statut éditorial et de la révision; enseignement, diagnostic, feedback, rappel différé, sécurité, maîtrise.
- `authoring/CONTRAT_PEDAGOGIQUE.json` : champs et structure v1.2 initiaux conservés; famille enrichie des 13 champs minimum de la norme, paramètres d'un **corpus fermé**, rubriques, seeds de traçabilité et statut `a_revoir`.
- `contenu/01..06` : 4 définitions, 2 exemples résolus, 2 contre-exemples, 2 tâches diagnostiques, 3 exercices accompagnés avec indices dégressifs, 4 pratiques autonomes, 2 transferts contextualisés, remédiations ciblées et rappel différé.
- `evaluation/PLAN_EVALUATION.md`, `BANQUE_ITEMS.json`, `GRILLE_MAITRISE.md` : 10 items distincts (8 fixes + 2 scénarios contrôlés), réponses/rubriques, données A et B fermées, double preuve non compensatoire, variations interdites/admises.
- `sources/REFERENCES_CONTENU.md` : faits documentaires, raisonnements dérivés, descriptions originales et limites des droits.
- `livraison/MANIFEST.json` et ce journal : liste explicite des 14 chemins et résultat des validations.

## Contrôles techniques effectivement effectués

Des tests automatisés locaux ont été exécutés sur le dossier de livraison, sur les champs canoniques originaux et sur le **fichier ZIP final**. Résultats observés après exécution du script de contrôle :

- **Structure / sécurité ZIP :** exactement 14 entrées de fichiers non vides; 14 chemins du manifeste identiques à ceux du ZIP, uniquement sous `kristals/qc-pri-st-011/`; première entrée correcte; ni `../`, ni chemin absolu, ni dossier englobant, ni autre ID, ni fichier interdit. Contrôle de CRC du ZIP passé.
- **JSON :** les trois JSON (`authoring/CONTRAT_PEDAGOGIQUE.json`, `evaluation/BANQUE_ITEMS.json`, `livraison/MANIFEST.json`) parsables strictement, identifiants cohérents, aucune collision d'item_id (10 uniques, numérotés 001–010).
- **Contrat :** champs natifs v1.2 conservés; valeurs invariantes vérifiées contre les originaux; `requires=[]`, conseil `qc-pri-st-001`, liens de famille inchangés; complétude des champs minima de famille.
- **Parcours :** frontmatter décodable en YAML; mêmes clés canoniques; 12 sections numérotées 1 à 12; présence de la preuve, du critère, de la séquence diagnostic/enseignement/pratique/feedback/évaluation/remédiation/accessibilité.
- **Évaluation :** chaque item possède mode, stimulus, consigne, réponse, critères, feedback, difficulté, `seed`, `parametres`, `validation_status=a_revoir`, `obj-1`, `crit-1`, identifiant de famille. Deux scénarios de maîtrise distincts A/boîte et B/chariot sont présents, non aléatoires, avec une clé de corpus et une seed fixe. Vérification croisée textuelle des éléments, actions et limites avec les corrigés des deux fiches; aucune formule numérique à résoudre.
- **Droits et accessibilité (contrôle documentaire uniquement) :** toutes les fiches textuelles ont une description utilisable sans image et des modalités alternatives de réponse; aucune image ou matériau tiers incorporé; références et limites déclarées; scénarios documentaires sans manipulation dangereuse. Ce contrôle ne constitue **pas** un audit de licence externe ni un test d'utilisabilité par élèves.

## Limites non résolues / décisions humaines indispensables

1. **Revue scientifique** de toutes les simplifications de mécanismes, notamment ressort de pince, glissières, charnière, filets et roues. Ce sont des **fiches pédagogiques fictives contrôlées**, pas des notices de fabricants ni une vérification expérimentale de produits réels.
2. **Revue des réponses ouvertes** et étalonnage de la grille par au moins un spécialiste de l'enseignement; vérifier les réponses équivalentes, les formulations acceptables et les erreurs disqualifiantes. Aucun essai d'élève ni accord intercorrecteurs n'a été effectué.
3. **Revue d'accessibilité / sécurité** des supports réellement présentés; approuver les documents en lecture adaptée et toute éventuelle maquette. Aucun test d'accès avec lecteur d'écran réel ni essai matériel n'a été exécuté.
4. **Vérification des licences** si des médias supplémentaires sont ajoutés dans le futur. Aucune illustration externe n'est fournie dans cette archive.
5. **Qualification technique Framework/production :** non effectuée; aucun `check`, `build-v9`, `check-ai`, publication, activation ou modification canonique n'est présumé; aucune homologation ou conformité PFEQ revendiquée.

## Propositions non appliquées (évolution centralisée seulement)

- Le registre central pourrait prévoir un **statut distinct « texte rédigé, banque à réviser »** afin d'éviter la confusion entre structure livrée et validation pédagogique; **aucun registre modifié**.
- Le système d'évaluation pourrait ajouter une validation de corpus fermé par empreinte du document source et un journal des variantes textuelles permises; **aucune extension du schéma imposée** dans cette livraison.
- Le LMS pourrait séparer preuves autonomes A/B des entraînements et enregistrer adaptations d'accessibilité / autonomie; **aucune base centrale modifiée**.

**État de livraison :** prêt pour revue et fusion contrôlée; **non publié, non certifié, non homologué**.
