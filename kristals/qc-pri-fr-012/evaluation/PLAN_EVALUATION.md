# Plan d'évaluation — qc-pri-fr-012 (v1.2, à revoir)

| Paramètre | Valeur conservée |
|---|---|
| Kristal | `qc-pri-fr-012` — Orthographe d’usage |
| Discipline | Français, langue d’enseignement |
| Objectif | `obj-1` — Écrire correctement un ensemble ciblé de mots et expliquer une stratégie de mémorisation. |
| Critère | `crit-1` — Produire des mots en contexte puis corriger ses erreurs avec justification. |
| Famille | `qc-pri-fr-012-ev-01` — `réponse_argumentée` |
| Dépendances | Aucune `requires`; ordre conseillé `qc-pri-fr-002` non bloquant |
| Modalité | Items `fixe` uniquement, sans tirage ni génération IA libre; graphies et rubriques verrouillées |

## Plan de couverture item par item

**Chaque item porte** `objectif_id=obj-1`, `critere_id=crit-1`, `family_id=qc-pri-fr-012-ev-01`. Pour les items de découverte et de révision, seul un **aspect** du critère est observé; `q-009` et `q-010` sont les preuves complexes complètes.

| ID abrégé | Difficulté | Représentation | Contenus | Type de preuve |
|---|---|---|---|---|
| q-001 | initial | indices de sens / réponses lexicales | maison, saison, raison, liaison; `-aison` | formative, rappel |
| q-002 | initial | trois phrases à compléter | grand, petit, chant; familles | formative, justifications |
| q-003 | initial | quatre mots dictés | toujours, beaucoup, demain, jamais | formative, rappel |
| q-004 | intermédiaire | court message erroné | maison, chanteur, toujours, beaucoup | formative, révision |
| q-005 | intermédiaire | assertion réfutable et deux phrases | raison, maison; `s`/`z` | formative, explication |
| q-006 | intermédiaire | trois phrases contextuelles | grande, petite, chanter | formative, production |
| q-007 | intermédiaire | comparaisons de familles | grand/grande, petit/petite, chant/chanter | formative, stratégie |
| q-008 | intermédiaire | note à corriger, justification | liaison, saison, demain, jamais | formative, transfert proche |
| **q-009** | **transfert** | **dictée + note de bibliothèque erronée** | **6 graphies + 5 corrections + 2 justifications** | **preuve A complète** |
| **q-010** | **transfert** | **dictée + affiche de fête erronée** | **5 graphies + 5 corrections + 2 justifications** | **preuve B complète** |

## Administration et protection des preuves

1. Réviser le corpus étudié **avant** la passation, puis retirer les modèles et les listes écrites. Chaque stimulus est **fixé** : aucune substitution non contrôlée, y compris du contexte ou des mots cibles. `seed=null`, `parametres=null`, `variables=[]`.
2. Dans `q-009` et `q-010`, le lecteur dispose de `texte_dicte_lecteur`, **non présenté visuellement à l'élève**. L'élève entend le texte et écrit uniquement les mots annoncés dans le protocole; le lecteur indique ces cibles **oralement**, sans épeler, sans montrer les graphies. Lorsqu'un mot du texte n'est pas ciblé, son orthographe est hors barème.
3. Ramasser/horodater la **phase 1** avant d'afficher `texte_a_corriger_phase2`. Ne jamais montrer le texte erroné avant la dictée; il pourrait amorcer les graphies. La phase 2 mesure la correction de cinq erreurs; ne pas afficher le corrigé pendant cette phase.
4. Faire demander deux justifications précises sur des mots nommés dans la tâche. Une stratégie doit réellement correspondre aux lettres retenues ou rectifiées, et ne pas être une affirmation phonétique générale. Si la réponse est oralement dictée à un scripteur, ce dernier transcrit exactement les lettres de l’élève sans corriger ni orienter.
5. Organiser A puis B dans **deux contextes différents**, de préférence des séances distinctes; aucune correction détaillée du corpus commun entre A et B si les deux sont utilisées pour l’attestation. Noter les aides reçues. Si les tâches ont été divulguées pendant l'entraînement, elles **ne peuvent pas** servir d'attestation indépendante sans nouveau lot examiné par un humain.

## Rubrique et seuils descriptifs

- **Exactitude de l’écriture initiale** : A au moins **5/6** graphies exactes parmi `demain, grande, maison, chanteur, toujours, beaucoup` ; B au moins **4/5** parmi `petit, chant, grand, saison, jamais`. La forme doit être lexicalement exacte; pas de points pour une équivalence phonétique. Erreur d’accent sur un autre mot = hors cible.
- **Autocorrection identifiée** : A au moins **4/5** corrections (`Demen, mezon, chenteur, toujour, beaucou`), B au moins **4/5** (`peti, chan, grant, sèzon, jamai`). Pour compter, l’élève remplace explicitement chaque mot fautif par sa graphie exacte sans voir les réponses. Ne pas sanctionner une omission de ponctuation hors cible.
- **Justification stratégique** : chaque preuve inclut **deux justifications** désignant l’indice correct : A `maison` (`-aison` avec *saison*) et `chanteur` (`chant-` avec *chant* / *chanter*); B `grand` (`grande` et `d`) et `saison` (suite `-aison` avec *maison*). Une explication alternative linguisticquement valide et précise peut être acceptée après revue par un évaluateur; aucun mot-clé seul ne vaut comme preuve.
- **Maîtrise** : toutes les exigences **sur A ET B** satisfaites en autonomie, sans correcteur orthographique ni aide lexicale. Un succès à un seul item ou une moyenne compensatoire ne suffisent pas. Un échec oriente vers la dimension précise et entraîne une nouvelle vérification sur tâches inédites **validées humainement**.

## Validité, variabilité et sécurité

- **Variabilité autorisée** : répétition identique de la dictée (jusqu'à deux lectures complètes ou davantage comme adaptation documentée), durée raisonnablement modulée, clavier sans correction, format accessible de consigne. **Pas** de changement de mot cible, d'orthographe corrigée ou d'indice donnant les lettres pendant une preuve.
- **Invariance** : toutes les phrases et clés du JSON sont fixes dans cette livraison. Aucun paramètre ni algorithme génératif n’est exploité; aucune validation de solveur mathématique n'est pertinente.
- **Accessibilité** : l'orthographe **écrite** est la compétence visée. Ne pas évaluer l’accent, la voix, la motricité fine ou la rapidité. En cas d'obstacle auditif, équivalence d’une présentation sémantique sans graphie à **faire approuver avant attestation**. Des réponses dictées lettre par lettre à un scripteur neutre peuvent remplacer le geste manuel.
- **Confidentialité et biais** : scénarios fictifs ordinaires, aucune donnée personnelle obligatoire, aucune affirmation sur l’identité de l’élève; pas de reproduction d’œuvre tierce.
- **Statut** : `a_revoir` pour chaque item. Il reste une revue humaine de correction linguistique, clarté, charge de mémoire, adaptations et étalonnage empirique des seuils. Ne pas déclarer la banque « certifiée », « homologuée » ou « publiée ».

## Références de vérification

Voir `contenu/01_NOTIONS_ET_EXEMPLES.md` (graphies ciblées), `contenu/05_PRATIQUE_AUTONOME.md`, `contenu/06_REMEDIATION_ET_TRANSFERT.md`, `evaluation/GRILLE_MAITRISE.md` (décisions), `sources/REFERENCES_CONTENU.md` (provenance).
