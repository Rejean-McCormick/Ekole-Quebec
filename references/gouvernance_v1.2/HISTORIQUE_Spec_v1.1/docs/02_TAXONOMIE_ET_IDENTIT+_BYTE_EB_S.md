# 02 — Taxonomie, noms et identités immuables

## 2.1 Noms de disciplines — chaîne d'affichage officielle

| Code | Nom officiel | Branche d'offre interne | Kristals initiaux |
|---|---|---|---:|
| `FR` | Français, langue d'enseignement | `francophone` | 26 |
| `ALE` | Anglais, langue d'enseignement | `anglophone` | 14 |
| `ALS` | Anglais, langue seconde | `francophone` | 12 |
| `FLS` | Français, langue seconde | `anglophone` | 12 |
| `ILSS` | Intégration linguistique, scolaire et sociale | `accueil` | 10 |
| `MA` | Mathématique | `commun` | 33 |
| `ST` | Science et technologie | `commun` | 20 |
| `US` | Géographie, histoire et éducation à la citoyenneté | `commun` | 16 |
| `AP` | Arts plastiques | `arts_option` | 9 |
| `AD` | Art dramatique | `arts_option` | 9 |
| `DA` | Danse | `arts_option` | 9 |
| `MU` | Musique | `arts_option` | 9 |
| `EPS` | Éducation physique et à la santé | `commun` | 12 |
| `CCQ` | Culture et citoyenneté québécoise | `commun` | 11 |
| **Total** | **14 disciplines de référence** | | **202** |

Les branches `francophone`, `anglophone`, `accueil`, `commun`, `arts_option` sont des **configurations techniques internes**, et non des catégories officielles de certification. Pour `FLS`, distinguer obligatoirement `base` / `immersion` lorsque pertinent. Pour `ILSS`, gérer des paliers et non forcer les six années.

## 2.2 Identifiants

Syntaxe de feuille : **`qc-pri-{code_minuscule}-{nnn}`** : `qc-pri-ma-012`, `qc-pri-ccq-001`, `qc-pri-ilss-010`.

- Chaque ID du registre [REGISTRE_202_KRISTALS.md](../catalogue/REGISTRE_202_KRISTALS.md) est **réservé définitivement**, même si une feuille est fusionnée ou abandonnée.
- Le suffixe numérique n'indique **ni année**, ni cycle, ni séquence obligatoire, ni rang de difficulté.
- Changement de titre : garder l'ID. Changement substantiel de l'objet observable : évaluer scission ou remplacement via RFC (doc 13).
- Nouvelles feuilles : prochain entier libre **dans la discipline**, attribué exclusivement par la personne responsable du registre; on ne crée pas de suffixe `a`, `bis` ou d'ID basé sur le titre.
- Ancien ID remplacé : `retiré` avec `remplacé_par` explicite; jamais réaffecté.
- Dans les documents : l'identité logique métier est `id`; l'`artifact_id`, le `state_ref` et les commitments v9 sont produits/gérés par les outils Kristal suivant leurs schémas, **sans postuler qu'ils sont égaux à l'ID éditorial**.

## 2.3 Formes d'assemblage

- Identité de parcours annuel : `qc-pri-parcours-1` à `qc-pri-parcours-6` (gabarits existants, à paramétrer par variante).
- Pour éviter l'ambiguïté, les assemblages concrets utilisent **`qc-pri-ass-{type}-{variante}-{cible}`** avec révision, ex. `qc-pri-ass-annee-francophone-4`, `qc-pri-ass-cycle-anglophone-2`, `qc-pri-ass-discipline-commun-ma`.
- Ces noms sont des conventions du projet; le registre des assemblages devra inventorier leurs identifiants avant publication.
- Une même feuille PEUT être membre de plusieurs assemblages; son contenu canonique reste unique.

## 2.4 Nomenclature à ne jamais déformer

- Affichage : **Mathématique** (singulier), **Science et technologie**, **Culture et citoyenneté québécoise**, **Géographie, histoire et éducation à la citoyenneté**.
- Distinction obligatoire entre `Français, langue d'enseignement` et `Français, langue seconde` (idem anglais).
- Les titres de microparcours (`Fractions : représentations et sens`, etc.) sont des **noms de travail proposés par nous**, pas les intitulés ministériels.
- Conserver `nom_officiel` textuellement, et utiliser `code` seulement comme clé technique stable.

## 2.5 Granularité stable

Créer une **feuille distincte** si au moins un des critères suivants est vrai : objectif démontrable indépendant; progression de préalables différente; modalités d'évaluation fondamentalement différentes; gestion de versions curriculaires autonome; charge incompatible avec une seule boucle enseigner–pratiquer–vérifier. Sinon garder une feuille avec plusieurs activités. Scinder par décision documentée, jamais juste pour correspondre à un chapitre de manuel.

## 2.6 Codes officiels externes (ajout v1.1)

**Aucune équivalence administrative n'est présumée** entre `qc-pri-*`, les abréviations `FR/MA/...` ou les `source_id` ScolQc et un code officiel de cours/matière. Référencer un code officiel seulement par une entrée qualifiée du [registre central](../REFERENCES_OFFICIELLES_QC.md). Les codes d'épreuves et numéros de publications forment des types différents.
