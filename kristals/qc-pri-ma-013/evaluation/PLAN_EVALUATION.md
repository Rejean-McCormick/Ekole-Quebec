# Plan d'évaluation — `qc-pri-ma-013` v1.2

**Objectif unique immuable :** `obj-1` — Construire des fractions équivalentes et comparer des fractions de référence. **Critère `crit-1` :** Ordonner des fractions avec justification visuelle ou numérique. **Famille native :** `qc-pri-ma-013-ev-01` (`paramétrique_controle`). Les dix items sont individuellement liés à ces trois identifiants dans `BANQUE_ITEMS.json`.

## Matrice de couverture et complexité

| Item | Niveau | Représentation | Tâche / preuve spécifique | Utilisation |
|---|---|---|---|---|
| `qc-pri-ma-013-q-001` | initial | bande égale + notation | Construire `1/2=2/4`, définir l'unité | formatif |
| `qc-pri-ma-013-q-002` | initial | droite commune / conversion | `1/4<1/2` et justification | formatif |
| `qc-pri-ma-013-q-003` | initial | multiplication entière | Équivalence paramétrique bornée | formatif |
| `qc-pri-ma-013-q-004` | initial | notation commune | Comparaison avec même dénominateur, égalité possible | formatif |
| `qc-pri-ma-013-q-005` | intermédiaire | calcul croisé | Comparer deux dénominateurs différents | formatif |
| `qc-pri-ma-013-q-006` | intermédiaire | fractions + PPCM/droite | Ordonner trois fractions générées d'une table contrôlée | formatif |
| `qc-pri-ma-013-q-007` | intermédiaire | équivalences | Reconnaître `3/6=4/8` | formatif |
| `qc-pri-ma-013-q-008` | transfert | critique d'une erreur | Corriger le raisonnement sur les dénominateurs | formatif |
| `qc-pri-ma-013-q-009` | transfert | bandes de ruban (fictives) | **Preuve autonome A :** ordre de 3 valeurs et conversion en douzièmes | décision A |
| `qc-pri-ma-013-q-010` | transfert | sentier `0—1` (fictif) | **Preuve autonome B :** ordre de 3 positions et conversion en huitièmes | décision B |

L'ensemble des items contribue à l'objectif `obj-1` et au critère `crit-1`; les items 001–008 documentent des compétences composantes et ne suffisent pas seuls à la conclusion de maîtrise.

## Paramètres et contrôle algorithmique

- **003–006 seulement : `mode=parametrique`.** Chacun possède une `seed` entière fixée (1203, 1204, 1205, 1206) et **exactement quatre cas approuvés** conservés dans `parametres.cas`, avec résultats et justifications déjà calculés.
- **Sélection :** `index = seed % 4`. Une même seed et la table inchangée redonnent le même énoncé. Modification de la seed = nouvelle variante préapprouvée seulement; aucune génération linguistique libre.
- **003 — équivalence :** triplets entiers `(a,b,k)`, `b>0`, `k>=2`, `0<a<b`, résultat `(a*k)/(b*k)`.
- **004 — même dénominateur :** triplets `(a,c,d)`, `d>0`, `0<a,c<d`, comparer `a` à `c`, avec un cas d'égalité.
- **005 — dénominateurs différents :** quadruplets `(a,b,c,d)`, `b,d>0`, fractions dans `(0,1)`, comparer les produits entiers `a*d` et `c*b`, avec un cas d'égalité. Le signe exact vient de ces produits, pas d'une approximation décimale.
- **006 — liste de trois :** trois fractions distinctes, entre 0 et 1; calcul `L = ppcm(d1,d2,d3)` puis `ni=ai*(L/di)` et classement des `ni` croissants. Dénominateurs positifs et tableaux fermés.
- **Correcteur indépendant :** `fractions.Fraction` du module standard Python pour vérifier valeur et ordre, comparé aux réponses calculées par produits entiers et PPCM. Tous les seize cas, y compris les égalités, sont testés lors du conditionnement. Les valeurs et justifications correspondantes restent inscrites dans la banque.
- **009–010 : `mode=fixe`** pour empêcher une variation masquée des preuves et conserver deux contextes stabilisés. La famille demeure paramétrique contrôlée par ses items 003–006.

## Administration, variabilité et accessibilité

- Présenter fractions et même tout à tous; laisser le choix entre bandes vierges, droite graduée vierge et démarche arithmétique, sans imposer un seul moyen de communication.
- Ne **pas** dévoiler le corrigé ou fournir un dénominateur commun pendant la prestation. La lecture de consigne ou le scribe neutre ne doivent ni choisir l'opération ni ordonner les valeurs.
- Paramètres numériques uniquement dans les tables ci-dessus; aucune variation libre de thème, de triplet ni de barème des preuves 009 et 010.
- Réponses possibles en grands caractères, braille mathématique, tableau tactile, oral avec trace par l'adulte. Vérifier que les parts restent égales et la même unité est maintenue, y compris en description accessible.
- Contexte fictif; aucune donnée d'élève ou achat réel; les fractions et bandes ne présentent pas de risque matériel. Les outils de découpe ne sont jamais obligatoires.

## Décision et limites

Chaque preuve A et B exige ordre correct des trois fractions **et** justification valide **sans aide mathématique**. Rubrique M1–M4 de `evaluation/GRILLE_MAITRISE.md` cotée distinctement par contexte; pas de maîtrise par score de QCM ni moyenne globale. Réviser le seuil et les modalités lors d'un contrôle humain; items tous `a_revoir`, non certifiés.
