# Plan d’évaluation — `qc-pri-ma-019` v1.2

**Objectif commun :** `obj-1` — Modéliser et résoudre une situation additive en distinguant les données utiles. **Critère :** `crit-1` — Résoudre deux problèmes verbaux nouveaux et expliquer les opérations. **Famille :** `qc-pri-ma-019-ev-01`. **Mode privilégié :** `paramétrique_controle`, avec ancrages fixes et scénarios contrôlés. Le plan ne fixe aucune équivalence PFEQ.

## Matrice d’items et couverture

Les **12** entrées ci-dessous ont toutes `objectif_id=obj-1`, `critere_id=crit-1`, `family_id=qc-pri-ma-019-ev-01`. Chaque réponse exige, selon l'item, identification de l'inconnue, sélection des données utiles, relation/schéma, résultat exact, unité et justification. Les rubriques de décision sont dans `GRILLE_MAITRISE.md`.

| ID | Niveau | Mode | Notion / tâche | Représentation | Variation autorisée | Rôle |
|---|---|---|---|---|---|---|
| q-001 | initial | fixe | réunion, donnée inutile | parties/tout + somme | aucune | formative |
| q-002 | initial | fixe | retrait, donnée inutile | matériel/barres + différence | aucune | formative |
| q-003 | intermédiaire | fixe | quantité de départ | état initial inconnu | aucune | formative |
| q-004 | intermédiaire | fixe | comparaison « de plus » | barres comparatives | aucune | formative |
| q-005 | intermédiaire | fixe | quantité distribuée inconnue | total et partie manquante | aucune | formative |
| q-006 | initial | paramétrique | total après ajout | barres + somme | 4 cas autorisés, seed 19004 | entraînement adaptatif |
| q-007 | intermédiaire | paramétrique | reste après retrait | barre + soustraction | 4 cas autorisés, seed 19008 | entraînement adaptatif |
| q-008 | intermédiaire | paramétrique | quantité initiale après retrait | état initial inconnu | 4 cas autorisés, seed 19012 | entraînement adaptatif |
| q-009 | intermédiaire | fixe | deux étapes ajout/retrait | ligne du temps | aucune | préparation transfert |
| q-010 | transfert | scénario contrôlé | deux changements, résultat final | flux et deux égalités | texte verrouillé | **preuve A** sans indice |
| q-011 | transfert | scénario contrôlé | départ inconnu, retrait ultérieur | états/équations | texte verrouillé | **preuve B** sans indice |
| q-012 | transfert | fixe | détection et correction d'erreur | critique d'égalité | aucune | métacognition |

## Gestion déterministe des variantes paramétriques

- **Familles numériques q-006/007/008 :** les seules combinaisons permises figurent dans `BANQUE_ITEMS.json`, dans `parametres.ensemble_autorise` (quatre triplets `[a,b,d]` par item). `a` et `b` sont des quantités de même unité; `d` représente une **catégorie différente** et doit être écarté.
- **Règle de sélection :** le système prend la `seed` entière `s ≥ 0`, calcule `i = s mod 4` et prend **uniquement** le triplet d'indice `i`, indexé à partir de 0. Seeds principales : q-006=19004, q-007=19008, q-008=19012; `i=0` dans les trois cas. Pour des essais contrôlés supplémentaires, utiliser `s+1`,`s+2`,`s+3`; n'autoriser aucune autre substitution.
- **Calcul :** q-006 `a+b`; q-007 `a−b`, avec `a≥b`; q-008 `a+b` (a = quantité restante, b = quantité retirée, donc initiale = a+b). Construire l’énoncé et le corrigé **uniquement** par remplacement dans les gabarits de la banque, sans texte généré librement.
- **Exemples seed principale vérifiés :** q-006 `[28,17,3] → 45 affiches` (`45−17=28`); q-007 `[94,37,4] → 57 cahiers` (`57+37=94`); q-008 `[46,25,3] → 71 objets` (`71−25=46`). Les douze triplets sont énumérés avec énoncé et réponse dans la banque; une exécution indépendante recalcule toutes les réponses avant diffusion.
- **Cas limites contrôlés :** n'employer que les triplets explicitement admis, pas de négatif, aucune unité mélangée dans l'opération; vérifier une soustraction inverse exacte. Toute augmentation des domaines numériques nécessite tests et revue de la formulation, hors du présent delta.
- **Sécurité d'évaluation :** ne pas choisir une variante en utilisant le nom, l'origine, un attribut sensible de l'élève ou un tirage de modèle IA. Journaliser seed, indice et version si déploiement. Les trois familles sont de l'entraînement, jamais l'unique preuve.

## Barème descriptif et autonomie

Chaque item est jugé sur cinq dimensions (définies précisément dans `GRILLE_MAITRISE.md`) : identification du problème et de l'inconnue; tri des données; représentation et justification des opérations; exactitude des calculs et unités; contrôle du sens. Les items simples préparent les preuves; **la maîtrise n'est reconnue que si q-010 ET q-011 sont chacun réussis sans indication de l'opération**. Une réponse numérique isolée, même juste, n’est pas suffisante.

## Modalités et accessibilité

Lecture littérale à voix haute, réponse orale enregistrée, texte agrandi, schéma tactile ou matériel de comptage sont permis si la décision de l'opération et les relations restent le fait de l'élève. Un adulte ne doit pas surligner les données utiles, reformuler pour suggérer « ajouter » ou « enlever », ni donner une opération pendant les deux preuves. Les contextes sont fictifs, non dangereux, sans information personnelle à dévoiler. Éviter de chronométrer comme critère. Transcrire fidèlement les justifications orales.

## Administration, renouvellement et limites

Les corrigés des transferts **d’entraînement** de `contenu/06_REMEDIATION_ET_TRANSFERT.md` ne doivent être divulgués qu’après leur réalisation. Les épreuves `q-010` et `q-011` ont des contextes distincts et leurs réponses restent réservées aux correcteurs. Si q-010 ou q-011 a déjà été travaillé avec corrigé, **ne pas le réutiliser comme preuve nouvelle** : construire une tâche équivalente et la vérifier humainement avant utilisation; aucune alternative non validée n'est prétendue déjà disponible ici. Après échec, remédier au maillon concerné et recueillir une nouvelle preuve d'un autre contexte. Revue humaine requise pour durée, neutralité contextuelle, adaptation d'énoncé et rubriques avant publication.

**Statut :** items `a_revoir`, ni certifiés ni homologués.
