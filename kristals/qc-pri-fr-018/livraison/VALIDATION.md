# Validation technique — `qc-pri-fr-018` — 8 octobre 2026

## Résultat et portée
**Statut :** rédaction achevée; contrôles techniques réalisés; **revue humaine requise**. Cette livraison n'est pas une publication ni une certification. Comparaison effectuée contre le dossier source v1.2 de `initbundle(1).zip`, pas contre une autre édition du workspace.

## Contrôles exécutés avec résultat
- Source : gouvernance (3 textes), graphe et 4 fichiers `authoring/` lus; relation **`requires` → `qc-pri-fr-013`** vérifiée, aucun autre verrou.
- Objectif observable et preuve de maîtrise : chaînes **identiques** aux métadonnées canoniques v1.2; famille `qc-pri-fr-018-ev-01` inchangée.
- Frontmatter YAML de `PARCOURS.md` : **conservé intégralement**; les 12 rubriques numérotées sont développées.
- Contrat JSON : tous les champs natifs v1.2 et de la famille préservés; champs minimaux de `GENERATEUR_ET_EXAMENS.md` présents; famille unique.
- Banque : **12 items uniques** q-001 à q-012, chacun référant `obj-1`, `crit-1` et `qc-pri-fr-018-ev-01`, réponses et rétroactions non vides; modes techniques **fixes**, sans génération IA libre.
- **22 formes écrites** attendues recomputées par un générateur local de flexion régulière en -er et retrouvées dans leurs corrigés; corpus limité aux verbes sans alternance orthographique. Le contrôle automatique ne remplace pas une revue linguistique humaine.
- Deux manifestations de maîtrise distinctes q-011 (club) et q-012 (jardin) avec trois complétions et deux productions chacune, justifications et conditions d'autonomie explicites.
- Accessibilité/sécurité : contrôle documentaire de la présence de lecture des consignes, clavier, transcription fidèle sans suggestion de désinence; aucune donnée personnelle ni exercice à risque requis. **Aucun essai utilisateur réalisé.**
- Sources/droits : attribution explicite des pages OQLF et distinction productions originales / raisonnements dérivés; aucun droit de reproduction tiers affirmé.
- Archive : exactement 14 chemins sous `kristals/qc-pri-fr-018/`, aucun chemin absolu, parent `..`, autre Kristal, registre, gouvernance ou fichier protégé; fichiers non vides, JSON/YAML parsables, liste du manifeste exacte, CRC ZIP vérifié.
- Simulation de fusion : extraction des 14 entrées par superposition logique des chemins à partir du workspace source; **2 remplacements** (`authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`) et **12 ajouts**, aucun autre chemin traité.

## Limites non résolues
- Revue par spécialiste de langue française du Québec **non exécutée**; le corpus, les seuils et la lisibilité des consignes sont une proposition interne.
- Essai en classe, vérification de temps de passation, accord entre correcteurs et efficacité des aides accessibles **non exécutés**.
- Sources linguistiques consultées publiquement; aucune licence d'illustration ou droit dérivé revendiqué; aucun audit juridique externe effectué.
- Les fichiers centraux, canoniques et de l'architecture v9 ne sont ni inclus ni modifiés; les commandes internes `check`, `build-v9` et `check-ai` ne sont **pas exécutées** dans cette livraison autonome.
- La revue de compatibilité complète avec les adaptateurs LMS et la publication sont hors périmètre.

## Revue humaine demandée
1. Vérifier justesse grammaticale, naturalité en français québécois et difficulté adaptée à chaque parcours de projection.
2. Tester deux preuves dans des conditions d'autonomie et d'accessibilité réelles; observer la fiabilité de la transcription fidèle.
3. Calibrer la grille entre correcteurs et examiner si une preuve alternative est nécessaire selon les apprenants.

## Propositions **sans modification** de structure
- Ajouter ultérieurement un champ transversal optionnel `corpus_formes_etudiees` aux registres de contenu pour identifier officiellement les temps ciblés; n'a pas été introduit hors de ce delta.
- Ajouter une procédure centralisée de validation des graphies orthographiques et du niveau d'aide autorisé pour les items de langue; ne modifier aucun registre depuis ce travail local.

## Commande de fusion prévue
Décompresser l'archive maîtresse, entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, puis extraire ce ZIP à cet emplacement. Ne pas ajouter un dossier englobant et ne pas extraire à la racine du système.
