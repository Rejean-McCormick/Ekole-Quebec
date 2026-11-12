# Plan d'évaluation — qc-pri-ma-017

## Identifiants et portée

- **Objectif immuable :** `obj-1` — Relier pourcentage, fraction de cent et situations proportionnelles simples.
- **Critère immuable :** `crit-1` — Déterminer une quantité correspondant à un pourcentage simple et la vérifier.
- **Famille :** `qc-pri-ma-017-ev-01`; `type` dans le contrat d'origine : `paramétrique_controle`.
- **Décision** : ni moyenne unique ni examen certifié; observer deux preuves de maîtrise autonomes dans des **contextes différents** (`Q009` fabrication de maquettes, `Q010` culture en potager fictif). Toutes les propositions restent `a_revoir` jusqu'à contrôle humain.

## Tableau de couverture

| Item | Liens | Difficulté | Représentations | Rôle |
|---|---|---|---|---|
| Q001 | `obj-1` / `crit-1` / `qc-pri-ma-017-ev-01` | initial | grille 10 × 10, fraction sur 100 | formative |
| Q002 | `obj-1` / `crit-1` / `qc-pri-ma-017-ev-01` | initial | groupes de jetons, fraction | formative |
| Q003 | `obj-1` / `crit-1` / `qc-pri-ma-017-ev-01` | intermediaire | contre-exemple écrit, fraction, tableau | formative |
| Q004 | `obj-1` / `crit-1` / `qc-pri-ma-017-ev-01` | intermediaire | tableau de proportion, fraction sur cent | formative |
| Q005 | `obj-1` / `crit-1` / `qc-pri-ma-017-ev-01` | intermediaire | fractions équivalentes, tableau de proportion | formative |
| Q006 | `obj-1` / `crit-1` / `qc-pri-ma-017-ev-01` | intermediaire | barre fractionnée, écriture numérique | formative |
| Q007 | `obj-1` / `crit-1` / `qc-pri-ma-017-ev-01` | intermediaire | tableau temps/taux, ratio partie/tout | formative |
| Q008 | `obj-1` / `crit-1` / `qc-pri-ma-017-ev-01` | transfert | calcul rationnel, vérification par groupes | formative |
| Q009 | `obj-1` / `crit-1` / `qc-pri-ma-017-ev-01` | transfert | situation de fabrication, proportion, contrôle | M1 – maquettes |
| Q010 | `obj-1` / `crit-1` / `qc-pri-ma-017-ev-01` | transfert | situation de jardinage, barre fractionnée, complément | M2 – pots |

**Couverture** : Q001 relie taux et grille sur 100; Q002 partage le tout; Q003 détecte la confusion additive; Q004–Q008 couvrent tableaux, ratios, fractions et contrôles; Q009–Q010 exigent quantité + unité + explication + vérification sur deux nouvelles situations. Les deux tâches de maîtrise sont scorées avec la même grille.

## Mode paramétrique borné et corrigés

- Q001–Q003 sont `fixe` : texte et réponse verrouillés; `seed=null` et `parametres=null`.
- Q004–Q010 sont `parametrique` : corpus **fini et ordonné** de quatre couples `(p,N)` par item; seed entier fixe `17004` ... `17010`; sélection unique `indice=seed % len(paires)`. Le stimulus est un gabarit **fixe** avec seules substitutions numériques autorisées.
- Contrat de calcul : `p` = pourcentage entier, `N` = tout entier strictement positif et `q=(p*N)/100`; résultats entiers exigés, `0≤q≤N`. Résoudre par arithmétique rationnelle exacte, jamais par génération de texte libre; vérifier indépendamment `100*q=p*N` et les compléments `N-q`. Toutes les variantes sont listées avec leur corrigé numérique dans le JSON et testées.
- **Changement de seed** : seul un couple de la liste peut être sélectionné; le moteur doit alors **recalculer** le stimulus, le corrigé et les contrôles. Ne pas recycler la réponse de la variante par défaut. Changer le texte/contextes exige revue, pas variation automatique.
- **Variabilité permise** : supports visuels, manipulation, oral/écrit; pour les paramètres, seules les quatre paires de chaque item. **Interdit** : nombre hors corpus, nouveau contexte IA, taux donnant quantité non entière, changement des unités, modification de `obj-1` / `crit-1`.

## Barème analytique commun (quatre axes, chacun de 0 à 3)

1. Identifie exactement le **tout** et l'**unité**.
2. Établit une **relation proportionnelle** (taux sur 100 et méthode justificative).
3. Calcule exactement la quantité `q` dans la bonne unité.
4. **Vérifie** par un moyen distinct du calcul initial (répartition, tableau, produits croisés, somme avec complément).

Se reporter aux quatre niveaux observables dans `GRILLE_MAITRISE.md`. Les items formatifs orientent l'enseignement; aucune compensation d'un axe essentiel raté par un autre. Les deux preuves de maîtrise Q009 et Q010 sont réussies seulement si les **quatre axes** sont chacun ≥ 2 sur **chaque** contexte, sans indice ciblé. Réessai sur nouveaux couples contrôlés après remédiation si nécessaire.

## Sécurité, équité et accessibilité

- Tous les contextes sont inventés; aucun questionnaire sur les achats réels, le milieu familial ou l'identité.
- Présenter les tableaux avec en-têtes lisibles; employer aussi des barres textuelles/objets pour ne pas dépendre de la couleur.
- Autoriser oral avec transcription, calcul aligné, matériel de comptage et tableau adapté. L'accessibilité ne change pas l'exigence de proportionnalité et de vérification; tracer toute aide de contenu.
- Calculatrice possible uniquement si la modalité de passation choisie la prévoit uniformément; elle ne remplace pas la justification. Les adaptions sont consignées hors du fichier canonique.
- La clarté et la durée des deux épreuves, la facilité de la charge de lecture et les biais doivent être revus **humainement** avant usage sommatif; il n'y a ni certification d'items ni homologation PFEQ.
