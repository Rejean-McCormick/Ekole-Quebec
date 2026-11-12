# Validation — livraison `qc-pri-eps-012` v1.2

**Livrable :** delta strict des 14 chemins de `livraison/MANIFEST.json`. **Source :** dossier du workspace `qc-pri-eps-012` et gouvernance/registre directement lus dans le ZIP source. **Statut :** contrôle technique local; contenu **à revoir** par une personne qualifiée.

## Contrôles prévus et résultats

Le contrôle automatique final est exécuté **après la construction des fichiers**. Son rapport exact figure ci-dessous et doit coïncider avec l'état réel de l'archive :

- **PASS** — graphe lu : requires eps-009, recommends_before eps-010 et aucun autre lien sortant.
- **PASS** — 14 fichiers exacts et non vides dans la staging area.
- **PASS** — YAML natif intégralement conservé et 12 sections 1 à 12 présentes.
- **PASS** — 3 JSON stricts lisibles et manifeste à 14 chemins exactement.
- **PASS** — métadonnées immuables, champs historiques famille et 13 champs gouvernance présents.
- **PASS** — 10 items distincts, identifiants 001–010 sans doublons, champs et réponses complètes.
- **PASS** — deux preuves A/B dans deux activités différentes et grille à niveaux 0–3.
- **PASS** — couverture des notions, diagnostics, guidages, pratiques, transferts et plan 10 items.
- **PASS** — présence explicite des garde-fous EPS/accessibilité/droits et statut non certifié.
- **PASS** — chemins internes normalisés, confinement au seul Kristal, aucune base centrale.

- **Tests complémentaires sans donnée réelle :** revue textuelle ponctuelle des dix réponses modèles et des critères, cohérence logique des deux preuves et des décisions d’arrêt; **aucun essai sur participants, aucune simulation de motricité réelle et aucun calcul arithmétique requis pour ces items qualitatifs.**
- **ZIP final :** la vérification de l’empaquetage figure dans le contrôle indépendant du même script après création de l’archive; aucune preuve d’intégration dans un workspace maître n’est revendiquée.

## Vérifications rédactionnelles effectuées

- Objectif immuable `obj-1`, preuve `crit-1`, titre, discipline EPS, famille `qc-pri-eps-012-ev-01`, préalable `requires qc-pri-eps-009` et ordre non bloquant `qc-pri-eps-010` préservés des sources locales; **aucun autre lien de graphe ajouté**.
- Contenu : quatre notions définies; deux exemples entièrement commentés et deux contre-exemples; deux diagnostics; trois exercices accompagnés à aides dégressives; quatre tâches autonomes; deux transferts dans des cadres distincts; erreurs typiques et interventions.
- Banques : réponses témoins et **rubriques descriptives** plutôt que verdicts sur la performance motrice; les deux épreuves q009 (manipulation contrôlée) et q010 (enchaînement adapté) constituent deux manifestations distinctes de `crit-1`.
- Sécurité : surveillance par adulte, matériel/trajectoires adaptés, droit d'arrêt et de report, aucune exigence de vitesse/force, aucun score morphologique ou de capacité, aucune donnée de santé; aides motrices/communication distinctes des aides cognitives.
- Droits et provenance : corpus et cas fictifs rédigés originalement dans cette livraison; fichiers sources internes identifiés; aucune reproduction de document externe ou de média protégé. Cela **ne remplace pas** une vérification juridique ni un audit de similarité indépendant.

## Points restant à vérifier humainement

1. Personne formée en EPS : faisabilité et sécurité des propositions selon lieu, encadrement et besoins d'accessibilité; vérifier la conduite à tenir locale si la pratique doit être suspendue.
2. Personne enseignante/réviseuse : lisibilité pour l'âge effectif choisi en assemblage, progressivité des indices, pertinence du traitement de l'effort et de la subjectivité.
3. Réviseuses et réviseurs de l'évaluation : interprétation interévaluateurs des cinq dimensions et du seuil niveau 2, biais éventuels liés à la langue, l'aide à la communication ou à la motricité.
4. Intégration : chemin d'extraction dans workspace maître, compatibilité réelle avec adaptateur LMS/Framework, validations d'exécution en salle et avec technologies d'assistance (non exécutées).

## Limites et propositions sans modification des bases centrales

- **Non testé :** mise en œuvre physique, essais réels avec élèves, protocole local de sécurité, revue médicale, qualification officielle, intégration runtime et contrôle de droits par juriste; aucune attestation inventée.
- **Proposition de schéma (à faire approuver centralement, non appliquée) :** ajouter aux contrats v1.2 un champ optionnel `preuve_en_attente_pour_securite` distinct d'un score faible, et un champ `aide_cognitive_vs_physique` de preuve.
- **Proposition de collecte (non appliquée) :** stocker au niveau session du LMS les deux preuves et la nature des aides, jamais dans `canon/` ni dans le manifeste. Aucun changement de `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `docs/`, `canon/`, `state/`, `runtime/`, `registry/` ou `governance/`.

**Qualification finale :** delta prêt à soumettre à revue, non publié, non homologué et non certifié.
