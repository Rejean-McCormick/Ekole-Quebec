# Plan d'évaluation contrôlée — qc-pri-ma-007

**Famille unique :** `qc-pri-ma-007-ev-01` · **objectif :** `obj-1`, « Modéliser la soustraction comme retrait, différence ou complément. » · **critère :** `crit-1`, « Résoudre un problème de différence et vérifier par addition. » · **mode privilégié :** `paramétrique_controle`. Le plan documente des items **à revoir**, pas un examen certifié.

## Périmètre, grille et couverture

Pour tout item : 1) identifier si l'on retire, compare ou complète; 2) construire ou expliquer le modèle (bande, matériel décrit ou équation contextualisée); 3) calculer `d = a − b` et préciser l'unité; 4) **vérifier par addition** `b + d = a`. La réponse attendue comprend l'opération, le résultat contextualisé et le contrôle; une réponse numérique isolée ne satisfait pas `crit-1`.

| Item — tous liés à `obj-1`, `crit-1`, `qc-pri-ma-007-ev-01` | Difficulté | Représentation exigée | Sens/couverture | Variation et contrôle |
|---|---|---|---|---|
| `q-001` | initial | jetons + équation | retrait | fixe, 14 et 6 |
| `q-002` | initial | deux bandes + addition | comparaison | fixe, 23 et 15 |
| `q-003` | initial | barre cible/partie + équation | complément | fixe, 17 et 9 |
| `q-004` | intermédiaire | partie-partie-tout + addition | retrait | paramétrique LCG, seed 700704, domaines contrôlés |
| `q-005` | intermédiaire | bandes de mesure + addition | comparaison de longueurs | paramétrique LCG, seed 700705, domaines contrôlés |
| `q-006` | intermédiaire | diagnostic de réponse + addition | relation inverse / correction | fixe, 25 et 9 |
| `q-007` | intermédiaire | bande cible + addition | complément contextuel | scénario contrôlé, deux variantes verrouillées |
| `q-008` | intermédiaire | comparaison de bandes identiques + addition | cas limite zéro | fixe, 19 et 19 |
| `q-009` | transfert | bandes ou équation expliquée + addition | **preuve autonome A : collections, bibliothèque** | fixe, 42 et 27; aucun indice |
| `q-010` | transfert | bandes ou équation expliquée + addition | **preuve autonome B : longueur, jardin** | fixe, 36 cm et 19 cm; aucun indice |

Les identifiants longs sont `qc-pri-ma-007-q-001` à `qc-pri-ma-007-q-010`, sans réutilisation. **Couvrir** les trois sens (retrait, comparaison, complément), la relation inverse, le cas zéro, la correction d'erreur et deux contextes de preuve autonome. Ne pas confondre diagnostic et preuve.

## Variabilité permise et génération reproductible

- **Fixes :** valeurs et contextes figés; `seed: null`, `parametres: null`. Toute modification impose une revue des réponses.
- **Paramétriques (`q-004`, `q-005`) :** aucune valeur décidée par IA. Générateur exact LCG sur entier 32 bits : `next(s) = (1664525 × s + 1013904223) mod 4294967296` (arithmétique entière), initialiser avec la `seed` enregistrée; calculer `x1 = next(seed)`, `x2 = next(x1)`. Pour q-004 : `a = 15 + (x1 mod 16)` et `b = 5 + (x2 mod 10)`; donc `15 ≤ a ≤ 30`, `5 ≤ b ≤ 14`, `a ≥ b`; réponse `d = a − b`, contrôle `d + b = a`. Pour q-005 : `a = 30 + (x1 mod 21)` et `b = 10 + (x2 mod 16)`; donc `30 ≤ a ≤ 50`, `10 ≤ b ≤ 25`, `a ≥ b`; réponse `d = a − b` cm, contrôle `b + d = a` cm. Les exemples issus des seeds ont été calculés par script puis vérifiés indépendamment par l'identité inverse. Pas de tirage libre ni d'arrondi.
- **Scénario contrôlé (`q-007`) :** remplacer uniquement le scénario complet parmi les deux alternatives textuelles et numériques inscrites dans la banque, avec leur propre corrigé. Par défaut scénario `A`. Pas de substitution d'unité, pronom, quantité ou arrière-plan libre.
- **Filtrage :** aucune combinaison non valide; `b ≤ a` garanti pour les paramètres. On peut répéter la même seed à des fins d'audit, mais pas présenter deux instanciations d'une même structure comme deux contextes de maîtrise indépendants.

## Conditions et barème formatif

Grille `../evaluation/GRILLE_MAITRISE.md` : sens du problème / modèle / calcul / addition inverse avec unité. Chaque dimension reçoit `acquis`, `fragile` ou `non_demontre` sur trace observable. Une preuve satisfaisante exige les quatre dimensions acquises **sans aide de contenu**. Utiliser `q-009` ET `q-010` après des entraînements analogues mais non identiques, à deux occasions si possible; ne pas déduire la maîtrise d'une note unique. En cas d'erreur, utiliser les remédiations ciblées de `../contenu/06_REMEDIATION_ET_TRANSFERT.md` puis collecter une nouvelle preuve autonome dans un contexte différent.

## Équité, accessibilité, sécurité, droits

- Lire oralement les énoncés, proposer police lisible, affichage des nombres en chiffres, bandes avec descriptions verbales, jetons manipulables, réponse dictée ou orale enregistrée et transcription fidèle. Ne pas accorder de points pour rapidité, soin du dessin ou lecture autonome non visée. Tracer les **aides de contenu** séparément des adaptations d'accès.
- Contextes fictifs ordinaires; aucune donnée personnelle, aucune production dangereuse ni manipulation de matériel risqué. Les longueurs sont déjà données en cm; aucune conversion cachée.
- Énoncés, variantes, chiffres, corrigés et grilles produits ici; aucune reproduction d'une banque protégée ou d'illustration externe. Principes de conception référencés dans `../sources/REFERENCES_CONTENU.md`.
- Un vérificateur automatique contrôle structure, calculs et seeds, **mais ne remplace pas** la relecture humaine pour clarté des consignes, biais et qualité des rubriques. Tous les items portent `validation_status: a_revoir`.
