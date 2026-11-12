# Validation et note de fusion — `qc-pri-da-003` (v1.2)

**Statut :** validation technique exécutée; **revue humaine pédagogique et sécuritaire exigée avant qualification**. Aucun examen certifié, aucun alignement officiel PFEQ revendiqué. Document de delta, non de publication.

## Contrôles réellement exécutés

Un script local a effectué **33 contrôles préalables** (résultats tous positifs) et une seconde passe de validation ZIP :

- [x] YAML valide et frontmatter conservé.
- [x] Métadonnées YAML d’origine identiques.
- [x] Identité/titre/discipline/objectif/concept source.
- [x] Préalable et famille YAML conservés.
- [x] 12 sections numérotées sans rupture.
- [x] JSON du contrat valide.
- [x] Identifiants et champs source complets conservés.
- [x] Structure de famille native et valeurs inchangées.
- [x] Tous les champs gouvernance de famille présents.
- [x] Objectif/preuve/type/famille immuables.
- [x] Préalable strict unique sans ordre/renforcement sortant dans contrat.
- [x] Relations sortantes réconciliées au graphe.
- [x] JSON de banque valide et famille exacte.
- [x] 12 items distincts numérotés sans trous.
- [x] Champs communs complets pour chaque item.
- [x] Chaque item lié à obj-1, crit-1 et family.
- [x] Modes fixes sans variabilité aléatoire.
- [x] Items complets et corrigés observables.
- [x] Statut a_revoir et difficultés contractuelles.
- [x] Phases 2 diagnostics, 3 accompagnés, 4 autonomes, 1 transfert, 2 preuves.
- [x] Preuves dans deux contextes distincts et non interchangeables.
- [x] Plan relie explicitement tous les items.
- [x] Grille : E1–E5 et deux preuves sans note compensatoire.
- [x] Contenu : deux exemples et deux contre-exemples.
- [x] Contenu : au moins deux diagnostics.
- [x] Contenu : 3 guidés dégressifs.
- [x] Contenu : quatre autonomes distincts.
- [x] Contenu : deux transferts explicites.
- [x] Droits et provenance déclarés.
- [x] Accessibilité/sécurité clairement documentées.
- [x] Manifest exact et conforme.
- [x] Liens autorisés vérifiés dans source.
- [x] Liens internes vers les contenus livrés valides.

**Validation après empaquetage :** ouverture et intégrité CRC du ZIP, correspondance exacte aux 14 chemins du manifeste et à l’ordre attendu, absence de chemin absolu ou de traversée, lecture de tous les JSON, relecture du YAML et simulation d'extraction sous une racine de workspace fictive. Ces contrôles sont exécutés par le même script de finalisation et leurs résultats sont affichés sur la console d'exécution.

## Portée et limites non résolues

- Le nombre d'items, leurs rubriques et la présence de corrigés par **preuves observables** sont testés automatiquement. Leur **pertinence artistique**, leur équilibre de difficulté et la concordance réelle entre observateurs ne peuvent pas être démontrés par ces tests.
- L'absence de média tiers est inspectable dans les 14 textes/JSON et aucun média n'est inclus; aucun audit de droits sur des supports ajoutés plus tard n'a été mené.
- Les consignes de sécurité et adaptations sont relues **textuellement**, non expérimentées avec des élèves; l'adéquation ergonomique réelle et les besoins d'accès personnels demandent un contrôle humain.
- Les sources effectivement consultées sont les fichiers de gouvernance et d'authoring du ZIP existant. Aucune validation empirique extérieure ni calibration psychométrique n'a été effectuée.
- Pas de test de déploiement Moodle/LMS, pas de séance menée avec élèves, pas de captation ou d'autorisation de captation testée.
- Le statut des 12 items demeure `a_revoir`; un commentaire de validation automatique ne remplace pas la qualification pédagogique.

## Revue humaine nécessaire

1. Expertise en danse, motricité inclusive et sécurité de l'espace, y compris interprétations assises et aides stables.
2. Essai des deux scènes de preuve auprès d'apprenants volontaires, contrôle de compréhension et de durée.
3. Calibration interobservateurs de E1–E5 et de la décision à partir de **deux** productions indépendantes; éviter biais de goût esthétique.
4. Revue de langage fr-CA, d'accessibilité des consignes et de confidentialité des traces.
5. Contrôle des droits de toute musique, image ou vidéo **éventuellement ajoutée** lors d'une publication ultérieure.

## Propositions de changement de structure — non appliquées

- Envisager dans une **future** version du schéma central un tableau de preuves avec `preuve_id`, `contexte`, `modalite`, `soutiens_autorises` et `indices_observes` (sans stockage de données personnelles dans le contenu canonique).
- Ajouter au validateur commun un contrôle de conservation récursive des champs de famille v1.2 et des rubriques arts, ainsi qu'un test d'extraction non régressive par workspace.
- Ajouter un champ optionnel de revue humaine distinct de `validation_status` pour documenter les tests en situation et l'accord interobservateurs.

## Fusion (aucune modification au registre ni à la gouvernance)

1. Décompresser la version maîtresse v1.2.
2. Se placer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`.
3. Extraire `qc-pri-da-003_livraison_v1.2.zip` **à cet emplacement**; le premier dossier interne doit être `kristals/`.
4. Les deux fichiers `authoring/` remplacent ceux du Kristal concerné; les 12 autres sont ajoutés. Ne pas écraser `ALIGNEMENT.md`, `AGENTS.md`, `kristal.workspace.json`, `registry/`, `governance/` ou un autre Kristal.
