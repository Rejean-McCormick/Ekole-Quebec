# Plan d’évaluation — `qc-pri-mu-009`

**Famille unique :** `qc-pri-mu-009-ev-01` · **objectif :** `obj-1` · **critère :** `crit-1`. **Type :** `observation_ou_production` par écoute suivie d’une appréciation justifiée. **Statut :** `a_revoir`, aucune certification d’items ni homologation officielle.

## Contrat d’observation

Énoncé commun : exprimer une appréciation liée à **au moins deux éléments auditifs différents, exacts et vérifiables**; une préférence négative, positive ou nuancée a valeur égale si elle est justifiée. La grille `evaluation/GRILLE_MAITRISE.md` fournit quatre dimensions sans noter le goût, la culture, l’interprétation instrumentale ou les aptitudes vocales.

Les pistes audio originales S01–S11 se trouvent intégrées en HTML5/WAV dans `contenu/01_NOTIONS_ET_EXEMPLES.md`. Leur partition lisible et le SHA-256 du WAV permettent au correcteur d’examiner les faits; la partition-correcteur est cachée à l’élève en passation ordinaire. Toutes les banques emploient le mode `fixe` : aucune variable aléatoire et `seed=null`, `parametres=null`; la seule variabilité admise porte sur le format oral/écrit/communication alternative, le nombre de réécoutes et l’ordre des items (hors preuves, que l’on documente). **Jamais** d’IA génératrice comme arbitre libre.

## Couverture détaillée et traçabilité (chaque ligne → `obj-1`, `crit-1`, `qc-pri-mu-009-ev-01`)

| Item | Phase / difficulté | Représentation et propriété ciblée | Correctif ou contrôle | Preuve de maîtrise? |
|---|---|---|---|---|
| `q-001` | Diagnostic / initial | Écoute S01, hauteur montante et espacement des départs; appréciation | Deux faits distincts auditifs comparables | Non |
| `q-002` | Diagnostic / initial | S02 vs S01, rapidité relative et répétition de hauteur | Pas de confusion rapide/aigu | Non |
| `q-003` | Accompagné 1 / initial | S03, répétition et intensité décroissante | Premier indice fourni; noter aide | Non |
| `q-004` | Accompagné 2 / intermédiaire | S04, grave/aigu et notes courtes | Indice seulement sous forme de question | Non |
| `q-005` | Accompagné 3 / intermédiaire | S11, intensité alternée, fin longue | Aucun indice initial; question possible après | Non |
| `q-006` | Autonome 1 / intermédiaire | S05, pauses et note finale; contexte capsule radio | Deux indices et argument libre | Entraînement |
| `q-007` | Autonome 2 / intermédiaire | S06, descente et durées; promenade imaginaire | Deux indices et argument libre | Entraînement |
| **`q-008`** | **Maîtrise A / transfert** | **S07, coin lecture : longueur/espacement et hauteurs descendantes** | **Grille complète sans aide : preuve A** | **Oui** |
| **`q-009`** | **Maîtrise B / transfert** | **S08, course solidaire : rythme rapide et accentuation/hauteur** | **Grille complète sans aide : preuve B** | **Oui** |
| `q-010` | Transfert 1 / transfert | S09, marionnettes : montée, silence et tenue | Deux faits exacts + effet personnel | Complément |
| `q-011` | Transfert 2 / transfert | S10, exposition : hauteur constante, timbre alterné | Deux faits exacts + effet personnel | Complément |

**Contrôle de couverture :** deux diagnostics, trois accompagnées à guidage décroissant, quatre tâches autonomes, deux transferts; les deux preuves de maîtrise appartiennent au sous-ensemble autonome, sont dans deux contextes distincts et n’utilisent pas la même piste ni les mêmes phénomènes dominants. Chaque item reprend explicitement les repères d’ID dans `BANQUE_ITEMS.json`.

## Critères, complexité et variabilité

**Rubrique commune :** appréciation exprimée (0–2), deux éléments auditifs exacts et distincts (0–2), lien argumentatif et effet sans généralisation (0–2), autonomie de contenu (0–2). **Règle non compensatoire de sortie :** chacune des épreuves `q-008` et `q-009` doit avoir appréciation ≥1, exactitude=2, justification=2, autonomie=2, sans indice factuel faux contredisant l’extrait. En cas de litige, réécoute contradictoire avec second correcteur, pas seuil arbitraire sur le total de 8.

- **Initial :** deux faits guidés ou décrits directement (S01/S02/S03); complexité perceptive basse.
- **Intermédiaire :** deux propriétés indépendantes et argument simple, avec indices progressivement retirés (S04/S11/S05/S06).
- **Transfert :** appréciation libre dans un contexte nouveau avec deux faits et un lien; aucune valeur de goût imposée (S07/S08/S09/S10).
- **Variations admissibles :** voix/texte/CAA, pauses, réécoutes, matériel de lecture adapté, ordre hors effets de fatigue documenté. **Variations exclues :** changer les WAV, jouer à une vitesse modifiée, substituer des enregistrements commerciaux, faire varier automatiquement les indices avec une IA ou exposer les réponses-témoins.
- **Paramétrage :** famille au corpus fermé (11 identifiants de pistes); aucun item paramétrique, aucune seed aléatoire, et pas de « génération sous contraintes » algorithmique invoquée pour la correction.

## Droits, sécurité, accessibilité et revue

- Synthèses et mélodies courtes créées pour cette livraison; **aucun extrait externe**; page de provenance et droits à `sources/REFERENCES_CONTENU.md`. Un contrôle automatisé ne certifie pas l’absence de coïncidence musicale ou l’existence de droits cessibles.
- Volume adapté au confort, contrôle individuel, écouteurs non obligatoires, droit d’arrêter, aucun contrôle d’audition; ne pas inférer de trouble ou d’identité à partir des réponses.
- Modalité orale/écrite/CAA au choix, consignes claires, lecteur HTML5 testé techniquement par lecture du WAV (non un test de compatibilité LMS). Si dispositif interdit l’URI `data:`, exporter la piste d’origine et vérifier son empreinte. Descriptions textuelles et partitions réservées aux accommodements; si aucune écoute effective, **noter** que la preuve ne documente pas directement le critère « entendus », sans disqualifier la personne.
- Revue humaine encore nécessaire : volume perçu sur matériel réel, reconnaissance des contrastes à l’oreille, compréhension par élèves d’âges variés, biais de contexte « sport/lecture », droits/propriété intellectuelle, compatibilité HTML5 et lecture d’écran dans le LMS, cohérence des mesures d’autonomie, lecture francophone québécoise.
