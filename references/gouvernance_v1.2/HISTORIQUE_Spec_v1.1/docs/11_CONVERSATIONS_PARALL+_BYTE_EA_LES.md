# 11 — Protocole non négociable de travail en conversations parallèles

## 11.1 Modèle de coordination

**Un responsable d'intégration** maintient la norme, le registre des IDs, les relations inter-feuilles et les assemblages. **Un rédacteur par lot de feuilles** crée exclusivement les livrables de son lot. Une conversation n'a **aucun pouvoir de modifier seule** l'ontologie partagée ou de qualifier une source comme officielle.

- Les conversations doivent recevoir **la même version exacte de la norme** et une **copie gelée du registre**.
- Chaque mandat contient liste fermée d'IDs, discipline, édition curriculaire, sources disponibles et révision de base.
- Les contributions sont livrées en fichiers complets pour leurs seuls IDs; **pas** de nouvelles définitions de statut, relation, arborescence ou numérotation.
- Toute demande touchant une autre feuille ou le registre est déposée via `MODELE_CHANGEMENT.md` et **n'est pas appliquée localement**.
- Les alignements non vérifiés restent marqués `à_vérifier`. Le rédacteur peut avancer sur la pédagogie sans prétendre à l'alignement PFEQ.

## 11.2 Propriété exclusive et zones partagées

| Objet | Peut modifier | Autre conversation |
|---|---|---|
| `kristals/<ID>/authoring/PARCOURS.md` | Rédacteur propriétaire de l'ID | lecture / propositions |
| `kristals/<ID>/authoring/ALIGNEMENT.md` | Rédacteur puis relecteur curriculaire | lecture / propositions |
| `registry/ids`, `registry/relations` | Responsable d'intégration | RFC seulement |
| `assemblages/` | Responsable d'assemblage | RFC seulement |
| `evaluations/plans/` | Responsable d'évaluation | proposition par feuille |
| `governance/` (norme) | Responsable de norme | RFC seulement |
| `release/`, publication et activation | Responsable de publication | aucun changement direct |

## 11.3 Processus en cinq échanges

1. **Brief immuable** : numéro de lot, IDs, normes, fichiers et sources, statut cible.
2. **Inventaire** : détecter connaissances existantes, lacunes, contradictions, statut d'extraction ScolQc.
3. **Production** : PARCOURS + ALIGNEMENT + éventuelles propositions de relations et de familles de tâches; pas d'épreuve ministérielle imaginée.
4. **Auto-audit** : liste G0–G6 avec résultat `ok`, `bloqué`, `non_testé`; aucune affirmation de test non exécuté.
5. **Livraison** : manifest de fichiers, journal des choix, questions ouvertes, propositions de changements, versions de sources, limites.

## 11.4 Fusion déterministe

- Une contribution porte `base_spec_version`, `base_catalogue_version`, `id`, `revision_base`, `revision_livrée` et `responsable`.
- Si le fichier canonique de base a changé entre temps : **rebase manuel**, pas de dernière-écriture-gagnante.
- Les RFC sont examinées séparément, éventuellement après acceptation des feuilles qui ne dépendent pas du changement.
- Toute modification au graphe provoque contrôle de cycles et recalcul des assemblages affectés.
- L'intégrateur recalcule commitments après merge; aucun autre agent ne les invente dans le Markdown.

## 11.5 Phrases de blocage obligatoires

- « **À vérifier :** correspondance non établie avec la progression officielle. »
- « **Proposition inter-feuilles :** ne pas intégrer au registre sans arbitrage. »
- « **Non testé :** validation technique n'a pas été exécutée. »
- « **Non qualifié pour examen :** famille de tâche ou barème insuffisamment vérifié. »

Pour chaque nouvelle conversation, copier intégralement [BRIEF_CONVERSATION_PARALLELE.md](../modeles/BRIEF_CONVERSATION_PARALLELE.md), puis renseigner seulement le mandat, les IDs et les documents de référence.

## 11.6 Registre des codes et sources (ajout v1.1)

Le mandat reçu par chaque conversation **DOIT joindre** [REFERENCES_OFFICIELLES_QC.md](../REFERENCES_OFFICIELLES_QC.md). Le rédacteur consulte ce registre en lecture seule. Un nouveau code officiel suggéré est livré via [MODELE_PROPOSITION_CODE_OFFICIEL.md](../modeles/MODELE_PROPOSITION_CODE_OFFICIEL.md); seul l'intégrateur peut le qualifier et le publier dans le registre.
