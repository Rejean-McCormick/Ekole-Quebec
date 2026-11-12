# VALIDATION ET JOURNAL DE LIVRAISON — qc-pri-us-007

## Périmètre et provenance
Delta exclusivement `kristals/qc-pri-us-007/` issu de l'archive originale `initbundle(1).zip`, dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. 2 fichiers authoring remplacés entièrement, 12 nouveaux fichiers. Aucune modification de `kristal.workspace.json`, `AGENTS.md`, `authoring/ALIGNEMENT.md`, `registry/`, `governance/`, `canon/`, `state/`, `runtime/`, `docs/`, ni d'un autre Kristal. Les identifiants, objectif et liens v1.2 ont été repris de la frame et du graphe.

## Contrôles automatisés effectués
Les validations du livrable utilisent le script de vérification local `us007verify.py` (non inclus dans le ZIP). Voir les résultats exécutés avant empaquetage :
- Décompte, chemins exacts, première entrée, absence de chemin absolu/`../`, fichiers non vides, absence de dossiers englobants et d'entrées non autorisées.
- Analyse stricte des JSON du contrat, de la banque et du manifeste; cohérence du manifeste; numérotation q-001 à q-012 sans doublons et champs obligatoires.
- Analyse YAML du frontmatter si PyYAML disponible; comparaison des clés/valeurs v1.2 originales; contrôle de présence et ordre des 12 sections.
- Comparaison des métadonnées canoniques du contrat (identifiant, objectif, concepts, préalable, ordre, preuve, famille, type, propriétés `generation` et dimensions natives); champs additionnels requis présents.
- Vérification de `obj-1`, `crit-1`, identifiant de famille, deux contextes distincts et deux relations décrites; sources S1–S5 référencées avec URLs.
- Scénarios déterministes : pour q-011 et q-012, contrôle index `seed % 2`, variantes A/B, réponses verrouillées et deux exemples de graines par item; aucune génération libre.
- Contrôle de l'intégrité ZIP via CRC, noms et tailles internes, et comparaison exacte avec le manifeste.

## Révision factuelle et humaine restant à faire
1. **Revue par une ou plusieurs personnes qualifiées pour les perspectives inuites**, idéalement des personnes inuites concernées : choix des cas, vocabulaire, biais et voix absentes.
2. Revue d'un professionnel de l'enseignement de l'univers social : pertinence des activités et calibrage des niveaux pour les élèves visés.
3. Réévaluation datée des pages S1–S5 avant diffusion publique et vérification des licences de chaque document tiers, même si aucune image ou longue citation n'est incluse.
4. Essai de compréhension par élèves, accessibilité réelle (lecture vocale et dispositifs d'assistance), fidélité du barème entre correcteurs, étalonnage interjuges.
5. Vérification externe de l'implémentation LMS; aucun `check`, `build-v9`, `check-ai` ou examen certifié revendiqué.

## Limites scientifiques / éditoriales
Les sources institutionnelles décrivent des cas et initiatives situés; un texte de projet relatant des programmes lancés en 2010 ou 2013 **n'atteste pas qu'ils sont toujours en activité en 2026**. Corrigés argumentatifs examinés éditorialement mais non validés par un comité historique/culturel indépendant. Choix de variantes déterministe ≠ contrôle automatique du sens. Aucun accord de la communauté ni validation de droits de reproductions externes présumé.

## Propositions (NE PAS modifier la structure centrale)
- Ajouter lors d'une version future un schéma canonique de traçabilité par assertion : `source_id`, `section`, `date_de_consultation`, `portee_geographique`, `portee_temporelle`, `niveau_inference`, `statut_revue`.
- Prévoir dans un service d'évaluation externe un champ pour validateur humain, variante réellement utilisée, accommodements et double revue sensible; ne stocker ici ni notes ni données personnelles.
- Examiner à l'échelle du programme une politique de revue communautaire avant publication d'activités sur les Premiers Peuples.

**Décision :** `controle_technique_effectue_revue_humaine_requise`, sans publication, certification ni homologation.
