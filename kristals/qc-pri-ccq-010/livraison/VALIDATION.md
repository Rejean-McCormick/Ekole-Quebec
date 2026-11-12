# Validation du delta — `qc-pri-ccq-010` (v1.2)

## Nature du livrable

- **Archive visée :** `qc-pri-ccq-010_livraison_v1.2.zip`.
- **Périmètre :** exactement 14 fichiers sous `kristals/qc-pri-ccq-010/`; 2 remplacements complets (`authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`) et 12 ajouts.
- **Statut de contenu :** rédigé et **à revoir**. Aucune certification, homologation, publication ou reconnaissance de conformité PFEQ revendiquée.

## Vérifications automatisées effectivement exécutées — 8 octobre 2026

- **194 assertions automatisées réussies** dans le script de contrôle local `qa_ccq010.py` (hors ZIP), lors du passage initial complet après correction de deux hypothèses de test et d'un rappel différé manquant.
- **Métadonnées :** YAML parsé et conservé champ pour champ depuis le `PARCOURS.md` maître; 12 sections numérotées 1 à 12; identifiants, texte exact de l'objectif et de la preuve, type, famille et paramètres préexistants vérifiés depuis le `CONTRAT_PEDAGOGIQUE.json` source.
- **Évaluations :** trois JSON parsés (contrat, banque, manifeste), 12 items uniques `q-001` à `q-012`, objectifs `obj-1`, critère `crit-1`, famille `qc-pri-ccq-010-ev-01`, statut `a_revoir`, présence de corrigés et critères, difficultés, deux contextes de preuve autonomes distincts et absence de génération incontrôlée.
- **Présence des contenus :** six fichiers substantiels; au moins deux diagnostics, trois exercices guidés, quatre pratiques autonomes, deux transferts, exemples, contre-exemples et remédiations; présence des sections sur l'accessibilité et des références de protection.
- **Fusion :** intégrité ZIP/CRC, exactement 14 chemins autorisés non vides, premier chemin et racine `kristals/qc-pri-ccq-010/`, absence de traversée et dossier englobant, manifeste correspondant exactement au contenu; simulation d'extraction sur une copie isolée du Kristal source : **2 remplacements + 12 ajouts**, et **34 autres fichiers d'origine non modifiés**.
- **Limite du test :** les vérifications automatisées contrôlent structure, cohérence et présence des corrigés, **pas leur qualité validée auprès d'enfants**, ni une homologation, ni les résultats d'une revue experte. Les liens externes consultés ont été vérifiés en recherche web, mais la maintenance future des URL n'est pas testée.

## Revue humaine obligatoire (non effectuée par les scripts)

1. **Protection et sensibilité :** revue spécialisée en pédagogie adaptée aux enfants et en protection des mineurs (vignettes fictives, absence de blâme, gestion des confidences, sécurité en ligne, soins).
2. **Âge :** l'architecture v1.2 ne fixe aucune année unique; vérifier vocabulaire, lecture, maturité, supports et progression selon la projection réelle.
3. **Institutions :** confirmer les coordonnées d'aide, les procédures de signalement, les règles du personnel et la confidentialité LMS; le guide n'est pas une politique de protection.
4. **Équité :** tester les réponses alternatives, les barrières de langue/communication et la variété des adultes protecteurs; ne pas inférer la situation familiale réelle.
5. **Épreuves :** essai avec observation par personnel formé avant usage officiel; tous les items sont `a_revoir`.
6. **Droits :** textes originaux et références liées seulement; revoir les droits si ajout de médias ou réemploi hors du projet.

## Propositions de structure (aucune appliquée)

- Ajouter au schéma v1.3, si validé centralement, un champ `safeguarding_review` et une version explicite du protocole institutionnel de signalement.
- Prévoir un registre d'options d'accessibilité pour les évaluations CCQ, distinct des traces de réponses et sans recueil d'informations intimes.
- Prévoir un corpus fermé de vignettes validées par tranche d'âge au niveau central; aucun tirage libre génératif.

**Les registres, la gouvernance, les dossiers canoniques, `AGENTS.md`, `kristal.workspace.json` et les autres Kristals restent inchangés.**
