# Validation et journal de livraison — `qc-pri-eps-007`

**Lot :** delta v1.2 d'un seul Kristal, 14 fichiers, racine interne du ZIP `kristals/qc-pri-eps-007/`. **Statut de contenu** : rédigé, **en attente de revue humaine**; aucun cours publié, certifié ou homologué. La présente page décrit les vérifications automatisées effectuées par le script local final; si une étape ne peut être exécutée, son résultat est à corriger ici avant livraison.

## Origine et invariants contrôlés

Source : `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`, qui contient l'arborescence `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`; archive maîtresse autonome `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` **non fournie séparément**, mais les fichiers maîtres effectivement présents dans l'archive source ont été lus. `kristals/qc-pri-eps-007/authoring/PARCOURS.md` et `CONTRAT_PEDAGOGIQUE.json` d'origine servent de base aux remplacements complets. Consultez le [MANIFEST.json](MANIFEST.json) pour la liste exacte des fichiers.

| Élément | Valeur maintenue |
|---|---|
| ID, discipline, titre | `qc-pri-eps-007` · Éducation physique et à la santé · Stratégies d’action collective |
| `obj-1` | Choisir une stratégie collective simple puis l’adapter après observation. |
| `crit-1` | Expliquer un choix tactique et montrer un ajustement en jeu. |
| `requires` | `qc-pri-eps-006` (diagnostic équivalent autorisé) |
| `recommends_before` | aucun |
| `reinforces` | `qc-pri-fr-025` (aucun verrou) |
| famille / mode | `qc-pri-eps-007-ev-01` / `observation_ou_production` |

## Contrôles techniques réellement exécutés

Les contrôles et leurs résultats numériques sont consignés ci-dessous **par le script de contrôle**, et doivent correspondre à ses sorties :

- **PASS — 14/14** chemins attendus, distincts, fichiers non vides, aucun ajout interdit dans le lot préparé.
- **PASS — YAML** : frontmatter de `PARCOURS.md` parsé et **identique en clés et valeurs** au fichier v1.2 d’origine; **12/12 sections** ordonnées.
- **PASS — 3 JSON** (`CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json`, `MANIFEST.json`) parsables; champs natifs du contrat conservés, seuls statut éditorial et champs de famille enrichis, sans changer l'objectif, la preuve, les prérequis ni la famille.
- **PASS — cohérence avec le graphe** : ID, titre, discipline, objectif, preuve, `requires: qc-pri-eps-006`, `reinforces: qc-pri-fr-025`, aucun ordre conseillé.
- **PASS — 13 items** uniques et séquentiels : 2 diagnostics, 3 guidages, 4 autonomes, 2 transferts, 2 maîtrises distinctes (`q-012` collecte / `q-013` relais), avec consigne, stimulus, preuve attendue, critères et feedback non vides. **Contrôle statique**, non mise en situation.
- **PASS — 24 liens Markdown locaux** : chacun mène à un fichier inclus. Liens externes de références consignés après consultation documentaire.
- **PASS — accessibilité/sécurité/droits (présence documentaire seulement)** : mentions d'arrêt, adaptation et sécurité, provenance des productions originales, distinction des droits et limites. **Aucun audit matériel ou juridique réalisé**.
- **PASS — contrôle du ZIP après construction** : 14 entrées ordonnées selon le manifeste, première entrée `kristals/qc-pri-eps-007/authoring/PARCOURS.md`, racine correcte, pas de chemin absolu ni `../`, toutes non vides, concordance octet pour octet avec les fichiers préparés, test CRC de l'archive réussi.

**Portée** : les tests lexicaux et structurels ne valident pas scientifiquement la grille, ne démontrent pas l'efficacité des pratiques en classe et ne certifient pas les conditions matérielles de sécurité.

## Contrôles éditoriaux réalisés sur le dossier

- Progression diagnostique → modelage → guidage dégressif → quatre pratiques → deux transferts → deux preuves A/B → rappel différé, toutes explicitement rédigées.
- Treize tâches fixes avec énoncé, contexte, preuve observable attendue, critères, rétroaction, limites de variation et signaux de sécurité; aucune génération numérique ni formule mathématique impliquée.
- Les corrigés décrivent des **actions collectives observables** à deux tours, en acceptant plusieurs choix sûrs fonctionnellement équivalents : ils ne prétendent pas à une unique solution tactique.
- Aucune évaluation du corps, de la rapidité, d'un diagnostic, d'une opinion ni de l'accent; séparer barrières d'accès des échecs de stratégie.
- Les liens `qc-pri-eps-006` / `qc-pri-fr-025` sont des références **seulement**; aucune autre arborescence de Kristal n'est incluse.
- Sources internes consultées et deux sites publics identifiés; exemples et rubriques originaux, sans médias tiers intégrés. Licences externes non présumées.

## Limites et points exigeant une revue humaine

1. **EPS/sécurité** : inspection du terrain réel, risques individuels, niveau de supervision, compatibilité des objets, dispositions locales et protocole de pause/arrêt; aucune séance réelle exécutée ici.
2. **Accessibilité** : vérifier chaque équivalence entre trajet physique, poste fixe et plateau partagé, disponibilité réelle des aides, réception des signaux et acceptabilité des modalités sans rendre le critère impossible.
3. **Évaluation** : pilotage des deux tâches `q-012/q-013`, calibration interobservateurs, clarté des ancrages I1-I5, impacts du rôle des partenaires, équité des scénarios et du seuil proposé; tests en contexte non effectués.
4. **Droits et gestion** : valider la licence de diffusion du contenu original, la gestion des traces individuelles dans le LMS, les règles locales d'utilisation des supports et du matériel.
5. **Schéma et publication** : les deux fichiers authoring mis à jour préservent les champs initiaux; certains champs supplémentaires de famille n'ont pas de schéma JSON formel autonome connu dans l'archive. Contrôler l'interopérabilité du consommateur avant fusion; qualification/framework non lancé.

## Propositions de changements de structure (non appliquées)

- Proposer au mainteneur central un schéma JSON officiel v1.2+ pour distinguer `critere_id` de la preuve textuelle et normer les niveaux de rubrique de manière stable, **sans modifier maintenant la gouvernance**.
- Prévoir un champ formel de modalités d'accommodation préétablies et de conditions de suspension pour les évaluations pratiques; consigner les interventions de sécurité sans collecte de diagnostics personnels.
- Définir un format de trace pseudonymisée « observation avant / indice / décision / après » et une procédure de revue interobservateurs, en dehors du delta présent.

**Fusion** : depuis la racine du workspace maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, extraire le ZIP (ses entrées commencent directement par `kristals/qc-pri-eps-007/`). Ne pas extraire un dossier parent supplémentaire et ne pas remplacer les dossiers centraux.
