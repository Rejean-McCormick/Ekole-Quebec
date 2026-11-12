# Validation — qc-pri-fls-011, livraison v1.2

**Statut :** contrôles techniques effectués, revue humaine requise. **Ne pas confondre** succès structurel et qualification pédagogique ou publication.

## Contrôles exécutés

1. Examen des fichiers de gouvernance v1.2, du graphe pédagogique, de la frame `PARCOURS.md`, du contrat JSON et des documents locaux `ALIGNEMENT.md` et `BRIEF_REDACTION.md` de l'archive source fournie.
2. Comparaison automatique des clés YAML de `PARCOURS.md` avec la frame; **12 sections numérotées** exactement et invariants `id`, titre, discipline, objectif principal, critère, préalables vides, famille conservés. Révision de contenu incrémentée à `0.3.0`, statut conservé `en_rédaction`.
3. Contrôle automatique de parse JSON strict pour le contrat, la banque et le manifeste; maintien des clés canoniques du contrat d'origine; famille unique et champs de gouvernance ajoutés.
4. Contrôle automatique de **12 items distincts**, `q-001` à `q-012`, mêmes identifiants `kristal_id`, `objectif_id`, `critere_id` et `family_id`, champs requis non vides, niveau, modalité, source et rétroaction; aucun item paramétrique et aucune génération aléatoire (toutes les seeds nulles).
5. Contrôle des **deux contextes de maîtrise distincts** : `q-009` radio/Winnipeg avec S4/S1 et `q-010` cartel/Caraquet avec S2/S1; les seuils D1–D4 sont décrits sans compensation et la seconde preuve interdit l'aide de contenu.
6. Contrôle de présence d'au moins **2 exemples résolus, 2 contre-exemples, 2 diagnostics, 3 exercices accompagnés, 4 pratiques autonomes et 2 transferts**; corrigés modèles/rubriques relus pour cohérence interne avec les cartes factuelles S1–S4. Pas de corrigé numérique déterministe applicable.
7. Confrontation documentaire des faits aux pages des organisateurs consultées le **2026-10-09**; provenance et droits répertoriés, absence volontaire d'images, de musique et de citations longues de tiers. Cette recherche ne constitue pas une vérification indépendante de la tenue d'événements.
8. Contrôle des chemins de fichiers du manifeste et des références internes; test d'archive ZIP ouvrable, intégrité CRC, **14 fichiers non vides**, premier chemin sous `kristals/qc-pri-fls-011/`, sans chemin absolu, `../`, dossier englobant, autre Kristal ou fichier global. Les fichiers déjà existants `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `AGENTS.md`, `kristal.workspace.json`, les autres dossiers et registres n'ont pas été inclus ni modifiés.

## Limites et contrôles non exécutés

- **Non réalisé :** revue humaine par enseignant de français langue seconde, spécialiste de diversité culturelle et correcteur linguistique; étude de biais avec élèves réels, mesure de temps de passation, calibrage psychométrique, essai avec apprenants et validation des réponses ouvertes en situation.
- **Non réalisé :** validation ou import dans Moodle / LMS, qualification Framework ou publication dans le système Kristal; aucune certification d'items. `statut: en_rédaction` et `validation_status: a_revoir` demeurent.
- **Limite des faits :** pages de programmation révisables (Caraquet 2026, Francos 2027). Les sources vérifiées sont majoritairement des pages d'organisateurs; le cours décrit leurs annonces sans prétendre vérifier de manière indépendante chaque événement ou la représentativité des activités.
- **Droits :** courts résumés originaux et liens vers sites officiels; aucune licence externe présumée. Avant projection publique, valider politique locale d'accès aux textes, confidentialité des enregistrements et conservation des traces.
- **Accessibilité** : adaptations textuelles et orales documentées, mais **aucun audit WCAG ni test utilisateur** effectué. Aucun accent légitime, identité, croyance ou parcours familial n'est évalué.

## Propositions non appliquées aux bases centrales

1. Envisager dans une prochaine révision de la gouvernance un champ explicite `sources_verifiees_le` par famille / version de corpus pour détecter l'obsolescence documentaire.
2. Envisager un outillage de vérification transversal de la **double preuve indépendante**, incluant un suivi des aides de contenu et un registre de variantes validées humainement.
3. Normaliser à l'échelle du registre, **par proposition versionnée seulement**, les états « banque rédigée », « revue humaine terminée », « qualifié », sans en déduire une conformité ministérielle.

**Portée de la livraison :** delta fusionnable de ce seul Kristal, 14 chemins et aucun fichier global. Procédure de fusion : extraire ce ZIP **à l'intérieur** de `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` après extraction du maître, sans créer de dossier parent supplémentaire.
