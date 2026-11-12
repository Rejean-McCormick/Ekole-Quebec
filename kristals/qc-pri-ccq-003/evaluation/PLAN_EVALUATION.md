# Plan d'évaluation — qc-pri-ccq-003

**Objectif invariant :** `obj-1` — Explorer plusieurs réponses possibles à une question de sens. **Critère invariant :** `crit-1` — Comparer des points de vue sans exiger d’adhésion personnelle. **Famille v1.2 préservée :** `qc-pri-ccq-003-ev-01` (`observation_ou_production`).

**Ce qui est évalué :** rapport fidèle de perspectives fictives, appui sur les arguments explicites, comparaison des similitudes/différences, distinction entre texte et interprétation, formulation neutre. **Ce qui n'est jamais évalué :** conviction, religion, identité, histoire familiale, expérience intime, adhésion à la « bonne » opinion ou participation à une discussion publique. Absence de révélation personnelle = **zéro conséquence**.

## 1. Matrice item → objectif/critère/famille et couverture

| Item | Objectif | Critère | Famille | Niveau | Représentation | Preuve spécifique |
|---|---|---|---|---|---|---|
| `q-001` | obj-1 | crit-1 | qc-pri-ccq-003-ev-01 | initial | observation + phrase interprétative | Séparer fait/interprétation |
| `q-002` | obj-1 | crit-1 | qc-pri-ccq-003-ev-01 | initial | deux cartes de personnages | Raison + valeur prudemment inférée |
| `q-003` | obj-1 | crit-1 | qc-pri-ccq-003-ev-01 | initial | dialogue | Argument vs affirmation circulaire |
| `q-004` | obj-1 | crit-1 | qc-pri-ccq-003-ev-01 | initial | deux phrases | Similitude + différence sans adhésion |
| `q-005` | obj-1 | crit-1 | qc-pri-ccq-003-ev-01 | intermédiaire | deux vignettes verrouillées | Comparer deux fonctions d'un objet |
| `q-006` | obj-1 | crit-1 | qc-pri-ccq-003-ev-01 | intermédiaire | cartes et production | Lier valeur possible à raison textuelle |
| `q-007` | obj-1 | crit-1 | qc-pri-ccq-003-ev-01 | intermédiaire | tableau ou dictée | Deux arguments, commun, différence |
| `q-008` | obj-1 | crit-1 | qc-pri-ccq-003-ev-01 | intermédiaire | copie fautive à réviser | Corriger jugements et fausse équivalence |
| `q-009` | obj-1 | crit-1 | qc-pri-ccq-003-ev-01 | transfert | musée fictif / oral ou texte | Preuve **A** : comparaison complète autonome |
| `q-010` | obj-1 | crit-1 | qc-pri-ccq-003-ev-01 | transfert | station de questions / oral ou texte | Preuve **B** : comparaison complète autonome |

Tous les identifiants complets ont la forme `qc-pri-ccq-003-q-NNN`. Q1–Q8 apportent des indices formatifs, Q9 et Q10 établissent la maîtrise si **les deux** satisfont la grille, sans moyenne compensatoire.

## 2. Rubriques et barèmes

- **Items q-001 à q-008 :** juger chaque critère de l'item comme `démontré`, `partiel` ou `non démontré`; feedback descriptif spécifique. Exemple de réponse dans `BANQUE_ITEMS.json`, alternatives recevables explicitement si elles s'appuient sur la vignette. Les mots « mémoire », « partage » ou « coopération » ne sont **pas** des mots de passe obligatoires.
- **Items q-009 et q-010 :** cinq dimensions C1–C5 sur les niveaux 0, 1, 2, 3 décrits dans `GRILLE_MAITRISE.md`. Seuil par preuve : C1≥2, C2≥2, C3≥2, C4≥2 et C5≥2, avec autonomie documentée. **Maîtrise seulement si A ET B**, contextes distincts; échec sur l'une → remédiation ciblée et nouvelle preuve inédite soumise à revue. La somme sur 15 n'est **pas** un critère de sortie.
- **Aucune correction automatisée par génération libre.** Le correcteur humain applique les critères; la variabilité linguistique acceptable ne change pas les exigences d'idées.

## 3. Variabilité contrôlée et reproductibilité

- Q1–Q4, Q9 et Q10 : `fixe`; question, vignette et exemple de correction verrouillés. `seed:null`, `parametres:null`.
- Q5–Q8 : `scenario_controle`; **exactement deux** variantes préécrites A/B avec correction propre à chacune. `seed` fixe respectivement 205, 206, 207, 208. **Algorithme :** `indice = seed % 2`, ordre A=0, B=1; la banque expose le stimulus sélectionné et les deux variantes annotées. Variantes testables : Q5 B, Q6 A, Q7 B, Q8 A; la graine suivante choisit l'autre scénario. On ne permute pas personnages/arguments entre variantes et on ne produit pas de nouveaux textes par IA libre.
- Modifications permises : agrandissement, mise en cartes, typographie, lecture à voix haute ou transcription neutre. Modifications interdites sans revue : remplacement d'un argument, d'un jugement, du genre de question ou de la formulation qui pourrait faire croire à un dévoilement personnel.

## 4. Validité et limites

- **Couverture** : valeur (Q2, Q6, Q9–10), interprétation (Q1, Q6, Q9–10), pluralité (Q4–Q10), argument (Q3, Q5–Q10). Q9–Q10 visent le critère complet en deux situations distinctes.
- **Accessibilité** : choix équivalent entre écrit, oral capté avec consentement, dictée neutre et tableau annoté; lecture des stimuli, temps additionnel, large interlignage, aucune information uniquement colorée. Les modalités ne doivent pas souffler les réponses.
- **Protection** : toutes les personnes et institutions sont imaginées. Aucune demande de croyance, d'identité, de culture familiale, de vécu intime, ni de position politique/religieuse. Le dialogue face au groupe est facultatif; une réponse individuelle sur papier suffit.
- **Équité** : les exemples de réponse sont des **ancrages, non des formulations exclusives**; le correcteur accepte des termes simples, différentes valeurs prudemment justifiées et des comparaisons équivalentes. Ne pas récompenser une interprétation parce qu'elle coïncide avec celle de l'adulte.
- **Contrôle de biais à finaliser** : revue humaine du vocabulaire, des éventuelles connotations de jugements, des variantes et de la longueur des stimuli avec un public du primaire; essai en situation réelle non effectué.

## 5. Procédure d'administration

1. Montrer la vignette et demander une production limitée au cas fictif. La grille n'est pas présentée comme un choix de « bonne croyance ».
2. Pour Q9 et Q10, ne fournir **aucun indice sémantique**, aucune correction pendant la production; documenter l'autonomie. Les aides d'accès restent possibles.
3. Garder les traces dans l'environnement d'apprentissage autorisé, **pas** dans les métadonnées du Kristal. Protéger les éventuels enregistrements et préférer une grille anonyme quand elle suffit.
4. Après la décision, donner un feedback précis par dimension; en cas de niveau inférieur à 2, cibler une micro-remédiation. Une nouvelle preuve nécessite un **nouveau cas revu**, pas un recyclage de la même copie.

**Statut des items : `a_revoir`.** Aucun certificat, homologation ni alignement détaillé au PFEQ.
