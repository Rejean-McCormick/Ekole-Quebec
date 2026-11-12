# Rapport de validation — qc-pri-eps-008 · delta v1.2

**Statut :** `controles_techniques_locaux_effectues_revue_humaine_requise`. **Périmètre :** le dossier `kristals/qc-pri-eps-008/`, deux fichiers authoring remplacés, douze fichiers ajoutés; aucun autre workspace, gouvernance, registre ou canon modifié. Référentiel de base lu dans l'archive jointe `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`, qui contient le dossier maître nommé `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` : les fichiers v1.2 ont été lus **dans ce dossier exact**, et non inventés. Date du contrôle local : 2026-10-09.

## Contrôles techniques réellement exécutés

- **40 assertions locales exécutées avec succès** par `build_and_test.py` (script de contrôle non livré) : liste et cardinalité 14; UTF-8 non vide; chemins sûrs; 3 JSON parsables; manifeste; métadonnées invariantes YAML et contrat v1.2; 12 sections dans l'ordre; cohérence du titre, de l'objectif, de `obj-1` et `crit-1`; aucune exigence de prérequis; champ famille `qc-pri-eps-008-ev-01`; champs de gouvernance; 12 ID d'items numérotés sans doublons; réponses/critères/feedback non vides; banque en mode fixe et `a_revoir`; deux preuves distinctes; diagnostics, pratiques, transferts; références, droits, liens vers fichiers sources du maître et absence de chemins hors-périmètre.
- **Contrôle des réponses de scénarios :** révision rédactionnelle des 12 énoncés face à leurs réponses proposées, comparaison des dangers et actions, contrôle programmatique des deux risques et recours adulte pour les preuves A/B. Ce contrôle **ne constitue ni un solveur externe ni une revue humaine indépendante**. Aucun corrigé mathématique ni paramétrage numérique requis pour des scénarios fixes de sécurité.
- **Liens :** les références `ALIGNEMENT.md`, `BRIEF_REDACTION.md` et le graphe existent dans la base source (pas dans le delta, conformément au mandat). Les autres fichiers liés sont dans la liste de livraison.
- **Provenance :** quatre pages publiques consultées, identifiées par URL; les descriptions et scénarios demeurent originaux. Aucune image, donnée d'élève, document tiers ou matériel à licence reproduit dans l'archive.

## Limites non résolues et revue humaine nécessaire

1. **Risque réel :** validation de la sécurité d'un milieu donné, adéquation du matériel et des procédures d'urgence de l'école, supervision et adaptations par un responsable qualifié.
2. **Contenu scientifique :** revue du choix des mots par professionnel de l'EPS, et protocole de gestion des commotions dans le contexte local; les élèves ne pratiquent pas de premiers soins à partir de ce cours.
3. **Évaluation :** revue des 12 items et de leurs rubriques, essai avec élèves, accord inter-évaluateurs, biais de lecture/language et pertinence des deux niveaux de preuves. Statut `a_revoir` maintenu; aucune certification.
4. **Accessibilité et droits :** adaptations à éprouver auprès des utilisateurs réels; les scénarios sont textuels originaux mais aucune expertise juridique ni test d'assistance technique (lecteur d'écran/LMS) exécuté.
5. **Intégration Framework/canon :** aucun `check`, `build-v9`, `check-ai`, publication, activation, homologation/PFEQ, ni déploiement en environnement cible exécuté. La fusion structurelle du ZIP sera contrôlée séparément à la création du fichier.

## Propositions de changements de structure (NON appliquées)

- Ajouter ultérieurement dans l'application LMS une représentation explicite des **indices de contenu** (pour exclure de la maîtrise une réponse soufflée) et des **aménagements d'accès** (autorisés).
- Ajouter un contrôle central versionné pour les variantes de scénarios approuvées et un journal des deux preuves distinctes. **Aucun registre ou contrat global modifié ici.**
- Ajouter un examen de sécurité/accessibilité humain comme étape formelle de qualification avant toute publication.

**Règle de fusion :** extraire le delta à l'intérieur de `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` : seules les deux entrées authoring de `qc-pri-eps-008` se superposent; les douze autres sont nouvelles. Aucun autre chemin du maître ne doit être écrasé.
