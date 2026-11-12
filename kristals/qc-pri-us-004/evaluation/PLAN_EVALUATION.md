# Plan d’évaluation — `qc-pri-us-004` v1.2

**Objectif `obj-1` :** Décrire comment une société organise ses activités et son territoire.  
**Critère `crit-1` :** Présenter une société avec une grille commune de comparaison.  
**Famille immuable :** `qc-pri-us-004-ev-01` (`generee_sous_contraintes`).

## Cible commune et couverture

Chaque item `qc-pri-us-004-q-001` à `qc-pri-us-004-q-010` est lié à **`obj-1`, `crit-1`, `qc-pri-us-004-ev-01`** dans sa propre notice JSON. Les huit premiers entraînent des composantes du critère; les deux derniers documentent **deux manifestations indépendantes de la preuve entière**, dans des conditions d’autonomie vérifiables.

| Item exact | Difficulté | Représentation | Indices/rubrique vérifiables | Usage |
|---|---|---|---|---|
| `qc-pri-us-004-q-001` | initial | note datée → phrase | 120, résidents habituels, M2 et année | formatif |
| `qc-pri-us-004-q-002` | initial | note + plan → chaînes d’acteurs | bénévoles/jardin, bibliothécaire/prêt | formatif |
| `qc-pri-us-004-q-003` | initial | plan orienté textuel | jardin nord, atelier sud, voie | formatif |
| `qc-pri-us-004-q-004` | intermédiaire | trois énoncés à classer | fait, inférence, assertion injustifiée | formatif |
| `qc-pri-us-004-q-005` | intermédiaire | synthèse de deux sources | rôle + espace + coordination, limite | formatif |
| `qc-pri-us-004-q-006` | intermédiaire | fiche fictive F6 → grille P–R–L–O–S–I | 75, équipe/sentiers, coordination, date | formatif |
| `qc-pri-us-004-q-007` | intermédiaire | critique d’affirmations | deux généralisations dénoncées | formatif |
| `qc-pri-us-004-q-008` | transfert | dossier fictif X8 → grille | 140, rôles, route, calendrier, limite | préparation au transfert |
| `qc-pri-us-004-q-009` | transfert | A1/A2 → **preuve autonome A** | six rubriques, 180 habitants, lieux nord/centre/sud, relation, source et limite | maîtrise A |
| `qc-pri-us-004-q-010` | transfert | B1/B2 → **preuve autonome B** | six rubriques, 260 habitants, lieux ouest/centre/est, navette, source et limite | maîtrise B |

## Corpus contrôlé : ni IA libre, ni provenance fictive cachée

- Documents de pratique M1/M2 (Val-des-Cèdres), F6, X8; dossiers A1/A2 (Rivemoulin) et B1/B2 (Plateau-des-Pins). **Tous inventés, datés à l’intérieur des mises en situation**, sans prétention de vérité historique.
- **Mode JSON :** huit items `fixe`, deux items `scenario_controle` à **un seul scénario approuvé et verrouillé chacun**; aucune sélection aléatoire; `seed=null`, `parametres=null` donc pas de générateur paramétrique actif.
- **Variabilité autorisée :** reformulation du même fait documenté, ordre des rubriques dans la présentation, temps de préparation, lecture neutre et modalité orale/écrite. **Interdit :** changer chiffres, lieux, dates, auteurs fictifs, rubriques, grilles ou scénarios sans révision humaine explicite.
- Aucun argument sur une société réelle, un groupe autochtone, une religion ou un rôle culturel ne doit être inféré à partir des cas imaginaires.

## Conditions des deux manifestations de maîtrise

1. Fournir seulement A1/A2 et une grille vierge P–R–L–O–S–I à l’épreuve 009; recueillir une production sans indices directifs. Donner ensuite B1/B2 lors d’une autre séance ou après intervalle raisonnable; ne pas fournir la solution A.
2. Exiger P avec année et source, au moins deux relations acteur–activité–lieu, un mécanisme concret d’organisation, les deux documents datés et typés, une inférence **qualifiée** et une limite. Même critères pour A et B.
3. Corriger à l’aide des éléments factuels indiqués dans `BANQUE_ITEMS.json` et des niveaux M1–M5 dans `GRILLE_MAITRISE.md`. Un synonyme ou une paraphrase est permis si l’appui documentaire est inchangé.
4. **Maîtrise seulement si les deux contextes, cotés séparément, satisfont chacun les cinq dimensions essentielles**; une moyenne élevée ne compense pas une absence de provenance ou de lien entre rôles et territoire.
5. Si une tâche est interrompue ou inaccessible, fournir un autre mode de réponse sans changer le raisonnement exigé; si des indices portant sur le fond ont été donnés, cet essai redevient formatif.

## Accessibilité et risques de biais

- Plans textuels orientés, sans dependence à une couleur, et lecture neutre pour les élèves qui y accèdent mieux de cette manière.
- Réponses écrites, dictées ou orales possibles; valoriser l’argumentation, non vitesse, graphie, aisance à écrire ou récit personnel.
- Il ne s’agit pas d’un test de connaissances sur des groupes existants. Sources réelles nécessaires avant toute affirmation factuelle historique; ne pas inventer un contexte des Premiers Peuples.
- L’évaluation **n’a pas été étalonnée** avec des élèves ou évaluateurs; `a_revoir` pour tous les items. La qualification humaine est préalable à l’usage sommatif.
