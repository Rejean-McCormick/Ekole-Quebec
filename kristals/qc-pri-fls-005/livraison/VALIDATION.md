# Validation et journal de livraison — `qc-pri-fls-005` (delta v1.2)

## 1. Périmètre réel

La livraison est un **delta de 14 fichiers** à extraire dans le dossier racine **déjà décompressé** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` : toutes les entrées portent le préfixe `kristals/qc-pri-fls-005/`. Le dossier d'archive supérieur n'est pas inclus. Les deux remplacements complets sont `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`; les douze autres fichiers sont nouveaux. Aucune modification des registres, de la gouvernance, des bases `canon/`, du runtime ou d'un autre Kristal n'a été livrée.

## 2. Contrôles techniques locaux exécutés

Les contrôles ont été effectués au moyen d'un script Python **hors ZIP** comparant l'archive à la base v1.2 extraite de l'archive source reçue. Les résultats ci-dessous désignent des vérifications automatiques de structure, de présence et de cohérence de métadonnées, pas des essais pédagogiques avec élèves.

- Vérification des huit fichiers sources consultés : gouvernance (3), graphe (1), documents d'authoring originaux (4).
- Analyse YAML du front matter : conservation des champs et valeurs canoniques de la base, excepté `revision_contenu` augmenté pour signaler l'enrichissement; ordre et présence des 12 sections.
- Analyse JSON stricte de `authoring/CONTRAT_PEDAGOGIQUE.json`, `evaluation/BANQUE_ITEMS.json` et `livraison/MANIFEST.json`; vérification des valeurs identitaires et des champs natifs conservés, extension de la famille selon le contrat du générateur.
- Vérification des liens : `qc-pri-fls-005` exige uniquement `qc-pri-fls-004` dans le graphe sortant; l'absence d'ordre conseillé est préservée; tous les items renvoient à `obj-1`, `crit-1` et `qc-pri-fls-005-ev-01`.
- Dix items distincts, IDs consécutifs `q-001` à `q-010`, consignes, stimuli, réponses/observables, critères, rétroactions et niveaux d'observation non vides; modes fixes contrôlés, seed et paramètres nuls par construction.
- Deux preuves finales distinctes `q-009`/`q-010`, chacune avec carte du partenaire, quatre critères T/C/R/P, conditions d'autonomie et contextes non identiques.
- Contrôles textuels ciblés sur 2 exemples, 2 contre-exemples, 2 diagnostics, 3 exercices guidés, 4 pratiques autonomes, 2 transferts, feedbacks, rappel différé, accessibilité, droits et consentement.
- Contrôle ZIP final : liste de 14 entrées égale à celle du manifeste, premier chemin adéquat, chemins non absolus et sans traversée (`../`), tailles non nulles, contenu identique aux fichiers livrés, intégrité CRC vérifiée par `ZipFile.testzip()`.

**Nature des contrôles :** vérifications automatiques et revue de cohérence éditoriale dans cette livraison; aucun jugement de certification. Les scénarios et réponses conditionnelles ont été relus pour détecter des divergences de contenu. Aucune simulation de conversations d'élèves ni calibration interjuges n'a été effectuée.

## 3. Limites non résolues et qualification

- **Revue humaine FLS requise :** intelligibilité des consignes pour des profils linguistiques variés, pertinence des questions possibles, adaptation à un groupe scolaire donné, absence de biais et clarté des cartes partenaires.
- **Étalonnage non exécuté :** aucun essai avec élèves, mesure de fidélité entre observateurs, validation de durée, étude psychométrique ou audit d'accessibilité avec usagers.
- **Droits :** scénarios originaux; aucun support tiers ou voix enregistrée intégrés. Les droits associés au workspace maîtresse et à toute diffusion ultérieure ne sont pas juridiquement vérifiés.
- **Données :** toute captation en classe doit suivre les règles de consentement et de conservation applicables; ici, aucun enregistrement de personne n'est livré.
- **Statut :** `a_revoir` pour chaque item; contenu rédigé pour fusion technique et **revue humaine**, non publié, non homologué, non certifié.

## 4. Modifications livrées et suggestions hors périmètre

- `PARCOURS.md` : enrichissement des 12 sections et de l'enseignement complet; valeurs identitaires YAML conservées; révision éditoriale portée de `0.2.0` à `0.3.0` sans prétention à une nouvelle version de norme.
- `CONTRAT_PEDAGOGIQUE.json` : champs originaux de base et de famille conservés; champs de génération/contrôle ajoutés; statut descriptif mis à jour en « rédigé à revoir ».
- Six documents pédagogiques, plan et banque d'évaluation, grille, provenance, manifeste et ce rapport créés sans toucher aux fichiers centraux.
- **Propositions seulement (non appliquées) :** (a) prévoir une propriété normalisée pour le type de support d'accessibilité effectivement employé pendant une épreuve; (b) un format de carte partenaire conditionnelle structuré et versionné; (c) un historique de jugements T/C/R/P anonymisé au niveau de la plateforme; (d) une procédure locale de revue humaine et de conservation du consentement. Ces idées exigeraient décision et versionnement centralisés.

## 5. Fusion demandée

Décompresser le workspace maître v1.2, entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis extraire `qc-pri-fls-005_livraison_v1.2.zip` **à cet endroit**, en acceptant le remplacement exclusif des deux fichiers d'authoring du Kristal cible. Le ZIP ne contient ni autre Kristal, ni base globale, ni arborescence `Frames_202_...` supplémentaire.
