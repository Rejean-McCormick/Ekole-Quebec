# 04 — Contrat normatif d'un Kristal-feuille

## 4.1 Définition

**Un Kristal-feuille** est un microparcours centré sur **un résultat observable principal**, avec au besoin 1 à 3 objectifs secondaires qui servent ce résultat. Il DOIT avoir un point d'entrée (préparation), une progression pédagogique, une sortie observable et une remédiation possible.

Une définition isolée, une vidéo, un quiz ou une fiche d'exercice **ne constitue pas** un Kristal-feuille. Une feuille ne devrait pas mélanger des résultats indépendants qui exigeraient des évaluations différentes.

## 4.2 Contrat exact d'auteur (source Markdown)

Fichier **`authoring/PARCOURS.md`** conforme à [MODELE_MICROPARCOURS.md](../modeles/MODELE_MICROPARCOURS.md). Les clés de frontmatter suivantes sont **obligatoires**. Le type `null` est autorisé **seulement** pour les champs explicitement incertains; `[]` signifie « vérifié, aucun », et **ne signifie pas** « inconnu » :

| Clé | Type | Contraintes |
|---|---|---|
| `format` | chaîne | `qc.learning-path/1.0` |
| `id` | chaîne | ID gelé du registre |
| `titre` | chaîne | titre de travail clair |
| `discipline_code` | chaîne | code officiel interne connu |
| `statut` | énumération | voir doc 14 |
| `revision_contenu` | chaîne | version SemVer du contenu éditorial |
| `langue_contenu` | chaîne | code BCP 47 (`fr-CA`, `en-CA`…) |
| `resultat_principal` | chaîne | comportement observable, non « comprendre » seul |
| `objectifs_secondaires` | liste | 0 à 3 résultats vérifiables |
| `criteres_reussite` | liste | au moins un critère observable pour chaque résultat |
| `prealables_declares` | liste | IDs reconnus; `null` si non vérifié |
| `alignement_statut` | énumération | `à_vérifier`, `partiel`, `verifie`, `conflit` |
| `alignement_ref` | chaîne | chemin relatif vers `ALIGNEMENT.md` |
| `familles_evaluation` | liste | IDs de familles définies dans la section Évaluer; peut être `[]` en brouillon |
| `provenance_statut` | énumération | doc 14 |
| `auteur` | chaîne | rôle/identifiant de contribution, pas identité d'élève |
| `reviseur` | chaîne ou null | null tant que non revu |

**Sections obligatoires dans cet ordre** : (1) Intention et frontières; (2) Notions et représentations; (3) Préparation / diagnostic; (4) Enseignement guidé; (5) Pratique accompagnée; (6) Pratique autonome; (7) Feedback et erreurs typiques; (8) Évaluation formative et preuves; (9) Remédiation / enrichissement; (10) Accessibilité; (11) Critères de sortie; (12) Références pédagogiques et limites.

## 4.3 Exigences de substance

- Chaque résultat correspond à au moins une **tâche observable** et un **critère d'appréciation**.
- Au moins **un exemple correct**, **un contre-exemple ou une erreur anticipée**, **une activité guidée** et **une activité autonome** doivent exister avant statut `prêt_validation`.
- Les activités DOIVENT donner instruction, matériel/contexte, production attendue, rétroaction, adaptation et lien vers un critère.
- Les représentations (texte, schéma, manipulation, audio, mouvement) sont choisies par pertinence; ne pas forcer des QCM sur les compétences de création ou d'action.
- Les exercices produits et les examens ne sont **pas** une source curriculaire.
- Une feuille sans preuves curriculaires peut être pédagogiquement rédigée, mais **ne peut pas atteindre `qualifié`** comme alignée PFEQ.

## 4.4 Notions croisées

Si une notion intervient dans plusieurs feuilles, déclarer une référence à son propriétaire ou à une notion conceptuelle, sans recopier la définition canonique. Les explications spécifiques au contexte **peuvent** être adaptées, en mentionnant qu'il s'agit d'une variante pédagogique et non d'une nouvelle vérité.

## 4.5 Années et cycles

Les champs `annees_admissibles` et `cycle` ne figurent pas comme vérité intrinsèque au microparcours : ils appartiennent à `ALIGNEMENT.md` et aux assemblages versionnés. Une même feuille peut avoir des phases `learn_with_teacher`, `expected_end_of_year`, `reuse` à des années différentes. L'âge ciblé affiché dans une projection peut donc changer sans mutation du contenu propriétaire.
