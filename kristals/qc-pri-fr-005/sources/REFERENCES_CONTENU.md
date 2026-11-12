# Références et provenance du contenu — qc-pri-fr-005

**Objet :** traçabilité de la livraison pédagogique v1.2, pas qualification canonique ou homologation ministérielle. Les faits utilisés dans les exercices sont des **faits intratextuels fictifs**; ils sont contrôlés par comparaison avec les stimuli, non avec une source extérieure.

## 1. Sources primaires réellement ouvertes dans l'archive jointe

Les fichiers suivants ont été **lus dans** `initbundle(1).zip`, sous la racine source `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Ce sont les autorités de **conception et de métadonnées internes**; « vérifiées » signifie ici présence et lecture dans l'archive fournie, **pas validation scientifique externe** :

| Chemin dans le workspace maître (en lecture seule) | Usage précis |
|---|---|
| `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` | Frontière Québec/Kristal, démarche diagnostic → modelage → pratique → preuves en deux contextes; statut non certifié. |
| `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` | Champs minimaux d'une famille, modes fixes, nécessité des corrigés verrouillés et revue humaine. |
| `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` | Appellation conservée « Français, langue d’enseignement »; aucun alignement détaillé PFEQ présumé. |
| `governance/Norme_Pedagogique_Autonome_v1.2/REFERENCES_EVIDENCE.md` | Répertoire *interne* d'approches EEF, IES/WWC et CAST. |
| `registry/GRAPHE_PEDAGOGIQUE_202.json` | `recommends_before(qc-pri-fr-005,qc-pri-fr-003)` et liens entrants d'autres Kristals; aucun `requires` sortant. Aucun lien modifié. |
| `kristals/qc-pri-fr-005/authoring/PARCOURS.md` (version source) | YAML initial, les douze sections, `obj-1`, `crit-1`, statut, référence d'alignement et famille d'évaluation. |
| `kristals/qc-pri-fr-005/authoring/CONTRAT_PEDAGOGIQUE.json` (version source) | Schéma natif `qc.education-assessment-blueprint/1.2`, identité, notions, liens et paramètres existants de famille. |
| `kristals/qc-pri-fr-005/authoring/ALIGNEMENT.md` et `BRIEF_REDACTION.md` | Frontières de correspondance et exigences éditoriales; fichiers non écrasés. |
| `kristals/qc-pri-fr-005/AGENTS.md` | Réserve entre préparation de contenu, canon et qualification de publication; fichier non modifié. |

## 2. Références externes mentionnées par la gouvernance, non revérifiées dans cette livraison

Les références qui suivent sont **rapportées depuis** le document de gouvernance `REFERENCES_EVIDENCE.md` et n'ont **pas** fait l'objet d'une consultation directe, d'une vérification de date, de statut de licence ou d'un examen complet de leur méthodologie ici :

- IES / What Works Clearinghouse, *Organizing Instruction and Study* — `https://ies.ed.gov/ncee/wwc/PracticeGuide/1` (espacement, exemples résolus).
- Education Endowment Foundation, *Cognitive science approaches in the classroom* — `https://educationendowmentfoundation.org.uk/education-evidence/evidence-reviews/cognitive-science-approaches-in-the-classroom`.
- Education Endowment Foundation, *Improving Literacy in Key Stage 1* — `https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/literacy-ks-1` (distinguer langage, lecture, écriture).
- Education Endowment Foundation, *Teacher Feedback to Improve Pupil Learning* — `https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/feedback`.
- CAST, *Universal Design for Learning Guidelines 3.0* — `https://udlguidelines.cast.org/more/downloads/`.

Ces liens documentent les inspirations présentes dans l'archive source, **pas** une preuve que les seuils de maîtrise proposés ou les exemples locaux ont été validés expérimentalement. Aucun extrait, tableau protégé ou image de ces sources n'a été reproduit.

## 3. Raisonnements dérivés : règles de design internes, non faits scientifiques attestés

- Séparer **réponse** et **indice** operationalise exactement `crit-1`, et est justifié par la possibilité de contrôler le lien entre la question et les mots de la source.
- Faire décroître les indices vise une autonomisation observable. Ce choix est didactique et à évaluer, pas un résultat de recherche spécifique revendiqué.
- Exiger deux démonstrations (récit/avis) applique la gouvernance v1.2; exiger **4/4 questions et 4/4 indices par texte** est un seuil local strict proposé, à piloter et à soumettre à une revue humaine.
- Prévoir un rappel autour de sept jours est un **choix éditorial suggéré**, non une valeur normative empruntée à une source scientifique.
- Accepter une lecture neutre ou une transcription verbatim isole ici la compréhension visée du décodage et de la graphomotricité. L'impact d'une adaptation donnée sur l'équivalence des épreuves requiert revue humaine.

## 4. Productions originales de cette livraison et droits

- **Écrits originaux générés dans cette livraison** : toutes les microhistoires, scènes, avis, notes, explications, questions, réponses, exemples, contre-exemples, grilles et feedback dans `contenu/`, `evaluation/` et le corps révisé de `authoring/PARCOURS.md`.
- Personnes et situations fictives, sans photographie, illustration, audio, logo ni citation littéraire tiers. Les données des items sont *internes aux textes inventés*; elles ne prétendent pas décrire des événements réels.
- **Droits :** aucune autorisation de tiers n'a été nécessaire pour reproduire un texte tiers dans ce delta parce qu'aucun texte tiers n'y est inclus intentionnellement. Cette déclaration ne remplace **ni** une vérification de similarité/exclusivité, **ni** la revue juridique et éditoriale des droits avant publication. Les noms de méthodologies et les titres bibliographiques sont attribués, sans reproduction de leurs contenus.
- Les fichiers maîtres `registry/`, `governance/`, `canon/`, `docs/`, `state/`, `runtime/`, `AGENTS.md`, `ALIGNEMENT.md` et `kristal.workspace.json` sont **en lecture seule** et absents de ce delta.

## 5. Limites et revue requise

Faire réviser par une personne compétente en littératie du français québécois : exactitude des rubriques, possibilités de paraphrase, ambiguïtés locales, équité des deux genres textuels, durée et effets de la lecture orale. Avant toute publication, procéder au contrôle des droits et à un essai d'administration. L'absence d'audit PFEQ est **intentionnelle**.
