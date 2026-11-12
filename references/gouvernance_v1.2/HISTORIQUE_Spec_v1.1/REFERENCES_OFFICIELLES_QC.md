# REFERENCES_OFFICIELLES_QC — Primaire (1re à 6e année)

**Statut : registre central de références du projet (norme 1.1.0).**  
**Périmètre : les 14 disciplines du PFEQ primaire; révision documentaire : 2026-10-08.**  
**Autorité du registre : interne au projet.** Les liens `quebec.ca` renvoient aux pages gouvernementales; nos codes `FR`, `MA`, `CCQ`, etc. et `qc-pri-…` sont **internes** et ne sont pas des codes ministériels.

## 1. Principe obligatoire

1. **Aucun code administratif de matière, cours, programme ou épreuve n'est inféré d'un identifiant éditorial, d'une URL, d'un PDF ni d'une compétence.** La similitude du format ne constitue jamais une preuve de signification.
2. Pour un **alignement officiel revendiqué**, il faut `document_id` / `source_id` réellement existant ou URL officielle, `édition`, `variante`, `localisateur précis`, `année/cycle` applicable, `libellé de compétence ou cible PDA` et `statut de vérification`. Un lien de page disciplinaire seul ne prouve **aucun** microparcours.
3. `A-Kristal-ScolQc` demeure **la source de vérité intégrée pour les documents et le curriculum**. Le présent registre est un index contrôlé de découverte et de codes, non un deuxième modèle de curriculum.
4. Chaque conversation parallèle **lit** le registre central, ne le modifie pas. Toute correction passe par une proposition de changement documentée, puis intégration centrale.
5. En l'absence de preuve, écrire **`à_vérifier`** pour la référence pédagogique ou **`non_etabli`** pour un code administratif introuvable. Ne pas remplacer l'inconnu par un numéro inventé.

## 2. Nomenclature : trois systèmes distincts

| Couche | Exemple | Nature | Décision |
|---|---|---|---|
| Discipline officielle | `Mathématique` | Appellation du PFEQ | Reproduire le libellé |
| Référence curriculaire | Document de progression + section + année | Source ministérielle contextualisée | Transcrire avec preuve |
| Code administratif (cours / matière / épreuve / publication) | **Aucun code présumé dans cette version** | Peut exister dans des systèmes ou publications distincts | Enregistrer uniquement si confirmé et typé |
| Identifiant de Kristal | `qc-pri-ma-012` | Code **interne** de microparcours | Ne pas confondre avec les codes officiels |

Le site gouvernemental du primaire présente les **programmes d'études, progressions et cadres d'évaluation**, et le portail de bulletin présente les **libellés et pondérations**. Les pages examinées ne constituent pas une table générale de codes de microcours du primaire équivalente à `MAT-1010`. La conclusion **n'est pas** que de tels codes administratifs n'existent nulle part : leur portée et leur éventuelle nomenclature doivent être établies source par source.

## 3. Répertoire des 14 disciplines

| Clé **interne** | Appellation officielle | ID de discipline **ScolQc** (existant) | `source_id` **ScolQc** (si existant) | Page officielle du programme primaire |
|---|---|---|---|---|
| `FR` | Français, langue d'enseignement | `primaire:francais_langue_d_enseignement` | `pfeq_francais_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/francais-langue-enseignement) |
| `ALE` | Anglais, langue d'enseignement | `primaire:anglais_langue_denseignement` | —¹ | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/anglais-langue-enseignement) |
| `ALS` | Anglais, langue seconde | `primaire:anglais_langue_seconde` | `pfeq_anglais_langue_seconde_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/anglais-langue-seconde) |
| `FLS` | Français, langue seconde | `primaire:francais_langue_seconde` | `pfeq_francais_langue_seconde_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/francais-langue-seconde) |
| `ILSS` | Intégration linguistique, scolaire et sociale | `primaire:integration_linguistique_scolaire_et_sociale` | `pfeq_ilss_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/integration-linguistique-scolaire-sociale) |
| `MA` | Mathématique | `primaire:mathematique` | `pfeq_math_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/mathematique) |
| `ST` | Science et technologie | `primaire:science_et_technologie` | `pfeq_science_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/science-technologie) |
| `US` | Géographie, histoire et éducation à la citoyenneté | `primaire:geographie_histoire_et_education_a_la_citoyennete` | `pfeq_univers_social_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/geographie-histoire-education-citoyennete) |
| `AP` | Arts plastiques | `primaire:arts_plastiques` | `pfeq_arts_plastiques_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/arts-plastiques) |
| `AD` | Art dramatique | `primaire:art_dramatique` | `pfeq_art_dramatique_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/art-dramatique) |
| `DA` | Danse | `primaire:danse` | `pfeq_danse_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/danse) |
| `MU` | Musique | `primaire:musique` | `pfeq_musique_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/musique) |
| `EPS` | Éducation physique et à la santé | `primaire:education_physique_et_a_la_sante` | `pfeq_eps_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/education-physique-sante) |
| `CCQ` | Culture et citoyenneté québécoise | `primaire:culture_et_citoyennete_quebecoise` | `pfeq_ccq_primaire` | [Programme](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/culture-citoyennete-quebecoise) |

¹ Pour **Anglais, langue d'enseignement**, le `curriculum_catalog.json` observé renvoie au `pfeq_primaire_integral`, mais ne donne pas d'ID de source disciplinaire spécifique dans le champ `source_ids` de cette discipline. Ne pas en fabriquer un : la page officielle peut être utilisée comme point d'entrée, tandis que la source ScolQc dédiée reste à résoudre.

**Attention :** `source_id` de ScolQc est une clé propre à **ScolQc**, pas un « numéro de programme » attribué par le ministère. Les pages officielles permettent de découvrir les documents. Les PDF, années d'effet, variantes, éditions et sections citées doivent être résolus et vérifiés avant d'autoriser un mapping précis.

## 4. Sources gouvernementales transversales

- [PFEQ primaire — point d'entrée officiel](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire) : disciplines et documents d'accompagnement.
- [À propos du PFEQ — progression des apprentissages](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/a-propos) : rôle des PDA dans l'apprentissage par année.
- [Cadres d'évaluation des apprentissages](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/epreuves-ministerielles-evaluation-apprentissages/cadres-evaluation/primaire-secondaire) : balises ministérielles d'évaluation par discipline.
- [Pondérations et libellés du bulletin au primaire](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/epreuves-ministerielles-evaluation-apprentissages/ponderations-libelles-bulletin/prescolaire-primaire) : libellés et pondérations; **ce n'est pas un répertoire de codes de microparcours**.
- [Français, langue d'enseignement — programme courant et actualisé](https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/francais-langue-enseignement) : le nouveau programme est présenté pour appropriation 2026–2027 et devient obligatoire en **2027–2028**; les éditions doivent rester séparées.

## 5. Registre des codes administratifs réellement vérifiés

**Pour le primaire, la présente révision n'homologue aucun code administratif de discipline ou de cours.** Le registre ci-dessous est volontairement vide jusqu'à preuve documentaire permettant d'identifier clairement le *type*, l'*autorité*, la *période*, la *portée* et la *valeur exacte* d'un code.

| Identifiant de l'entrée | Type (`matiere`, `cours`, `programme`, `epreuve`, `publication`) | Code exact | Autorité | Portée | Édition / applicabilité | URL officielle et localisateur | Statut |
|---|---|---|---|---|---|---|---|
| *Aucune entrée qualifiée* | — | — | — | — | — | — | `non_etabli` |

**Ne pas considérer** un code d'épreuve ministérielle comme un code de cours, ni un numéro de publication comme un code de programme. Les codes figurant dans des documents de secondaire ne sont pas transférables par analogie au primaire.

## 6. Chaîne de résolution officielle — à utiliser pour chaque Kristal

1. Partir de l'ID de feuille gelé : ex. `qc-pri-ma-012`.
2. Trouver sa clé de discipline **interne** dans `docs/02_TAXONOMIE_ET_IDENTITÉS.md` et son `discipline_id` dans ce registre.
3. Ouvrir la **page officielle** de cette discipline et identifier le **type** de document pertinent (programme, PDA, cadre, bulletin ou paliers).
4. Résoudre le document, l'édition, la variante et la section; retrouver les IDs `source_id`, `edition_id`, `source_component_id`, `sem:*`, `pda:*` dans ScolQc **uniquement s'ils existent**.
5. Écrire l'alignement *objectif par objectif* dans `ALIGNEMENT.md` avec statut `officiel_verifie`, `extraction_scolqc` ou `à_vérifier`, selon les preuves.
6. Si un code administratif est découvert, **ne pas** l'inscrire directement comme autorité : soumettre la fiche du code à l'intégration centrale, avec type, portée et source exacte.
7. Les familles d'examen doivent citer le **cadre d'évaluation applicable**, jamais uniquement le code de la matière.

## 7. Décisions d'applicabilité à préserver

- **Cycles du primaire** : 1er (1re–2e années), 2e (3e–4e), 3e (5e–6e). Ne pas déduire l'année exacte du seul cycle.
- **Français, langue seconde** : `base` et `immersion` ont des documents propres. Éviter toute assimilation.
- **Intégration linguistique, scolaire et sociale** : évaluer selon les **paliers** applicables; ne pas imposer arbitrairement une année de primaire.
- **Anglais, langue seconde** : programme distinct au 1er cycle et aux 2e–3e cycles; ne pas fusionner sans preuves.
- **Culture et citoyenneté québécoise** : appellation officielle inchangée; critères d'évaluation et contenus propres à chaque cycle.
- **Français, langue d'enseignement** : éditions 2026–2027 et 2027–2028 explicitement distinctes.

## 8. Schéma minimal d'une référence externe

```yaml
reference_externe:
  type: curriculum  # curriculum | matiere | cours | programme | epreuve | publication
  code_officiel: null  # seulement si attesté; ce n'est pas un ID Kristal
  statut_code: non_etabli  # non_etabli | officiel_verifie | à_vérifier
  autorite: "Ministère de l'Éducation du Québec"
  source_id_scolqc: pfeq_math_primaire  # ID préexistant et vérifiable, pas un code ministériel
  edition_id_scolqc: null  # remplir à partir de la source exacte, sans invention
  url_officielle: "https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/mathematique"
  document_exact: null
  localisateur_exact: null
  annee_scolaire: null
  cycle: null
  variante: null
  consulte_le: "2026-10-08"
  revendication_alignement: à_vérifier
```

Ce gabarit **ne signifie pas** que `qc-pri-ma-012` est déjà aligné à une section donnée : il ne contient volontairement ni cible ni année présumée.

## 9. Modifications et responsabilités

| Action | Responsable |
|---|---|
| Signaler un nouveau lien officiel | Auteur du lot, dans une proposition |
| Vérifier édition, cible et localisateur | Relecteur curriculaire |
| Confirmer et classer un code administratif | Référent du registre / intégrateur |
| Modifier ce registre | Intégrateur, après preuve et revue |
| Associer un objectif Kristal à la source | Auteur de `ALIGNEMENT.md`, puis relecteur |
| Publier un état Kristal qualifié | Responsable de publication, après gates G0–G8 |

## 10. Pistes de vérification et limites

- Relevé de sources **ScolQc** : `knowledge-base/sources/curriculum_catalog.json`, `source_catalog.json`, `semantic_curriculum.json`, `progression_semantics.json`, `assessment_semantics.json` dans l'archive fournie.
- Source officielle accessible pour chacune des 14 disciplines; revue documentaire des pages de programme et des pages transversales effectuée le **2026-10-08**.
- **Non accompli à cette étape** : relever toutes les éditions et tous les localisateurs dans les PDF des 14 disciplines, attribuer les 202 feuilles à leurs compétences, établir une taxonomie complète de codes administratifs locaux ou qualifier les examens.
- L'absence de code au présent registre signifie « **code non établi à la présente révision** », pas « preuve de non-existence ».
