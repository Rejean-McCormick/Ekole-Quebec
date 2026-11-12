# Plan d'évaluation — `qc-pri-ma-011-ev-01`

**Objectif unique :** `obj-1` — Exécuter, vérifier et expliquer une procédure de calcul écrit.  
**Preuve attendue :** `crit-1` — Calculer puis détecter une erreur dans une procédure proposée.  
**Famille v1.2 :** `qc-pri-ma-011-ev-01`, mode prioritaire `paramétrique_controle` (items `mode: parametrique` dans le JSON).  
**Statut :** items rédigés et arithmétique contrôlée, **tous `a_revoir`**, sans certification.

## Ce qui est évalué (pas la vitesse)

Chaque item demande au moins de calculer et de diagnostiquer la copie; les critères à consigner séparément sont : **C1** calcul exact et placement des chiffres, **C2** premier pas erroné localisé et corrigé (ou résultat juste reconnu avant une erreur de contrôle), **C3** justification par valeur de position ou échange, **C4** vérification indépendante exacte (inverse; addition répétée pour multiplication). Les épreuves finales requièrent C1–C4 sans indice. Aucune simple réponse de QCM ne suffit.

## Matrice explicite par item (obj-1 / crit-1 / famille identiques sur toutes les lignes)

| Item | Niveau | Représentation et contexte | Variation admissible | Focus et contrôle |
|---|---|---|---|---|
| `q-001` | initial | Colonnes C-D-U, addition | fixe | Retenue centaines oubliée; soustraction inverse |
| `q-002` | initial | Échange en matériel/C-D-U, soustraction | fixe | Échange depuis 0 D; addition inverse |
| `q-003` | intermédiaire | Soustraction puis contrôle erroné | fixe | Distinguer procédure principale correcte et inverse faux |
| `q-004` | intermédiaire | Multiplication à 1 chiffre, distributivité | fixe | Retenue unités→dizaines; addition répétée |
| `q-005` | intermédiaire | Addition et retenue; C-D-U | jeu fini, seed fixé | Oubli d'1 centaine; inverse exact |
| `q-006` | intermédiaire | Soustraction avec 0 dizaine | jeu fini, seed fixé | Emprunt à travers zéro; inverse exact |
| `q-007` | intermédiaire | Colonnes avec terme à 2 chiffres | jeu fini, seed fixé | Décalage ×10 d'un opérande; inverse exact |
| `q-008` | initial | Soustraction colonne sans retenue | jeu fini, seed fixé | Dizaine augmentée de 1; addition inverse |
| `q-009` | intermédiaire | Multiplication courte | jeu fini, seed fixé | Report mal ajouté; addition répétée |
| `q-010` | intermédiaire | Calcul juste, contrôle inverse faux | jeu fini, seed fixé | Vérifier que somme−terme redonne l'autre terme |
| `q-011` | **transfert A** | Livres d'une bibliothèque, addition | jeu fini, seed fixé; aucun indice | **preuve autonome 1 :** calcul, erreur, justification, inverse |
| `q-012` | **transfert B** | Billets d'un centre communautaire, soustraction | jeu fini, seed fixé; aucun indice | **preuve autonome 2 :** calcul, erreur, justification, inverse |

**Lien de chaque item :** son `objectif_id` est `obj-1`, son `critere_id` est `crit-1`, son `family_id` est `qc-pri-ma-011-ev-01`. L'identifiant complet est `qc-pri-ma-011-q-001` à `...-q-012`.

## Génération et audit déterministes

- Les q-001 à q-004 sont fixes et vérifiées. Les q-005 à q-012 emploient un **jeu explicite** de couples et un calcul arithmétique : `index_0_base = seed % len(couples_autorises)`; les copies erronées sont **construites** par une transformation unique décrite dans chaque `parametres`, jamais par un modèle de langage au hasard.
- **Bornes :** nombres entiers naturels, opérandes explicitement énumérés, soustractions toujours non négatives; les emprunts, retenues, alignements et contrôles sont testés sur **chaque couple du jeu**. Ne pas extrapoler à tous les entiers sans nouveau test. Une modification du pool ou de la formule appelle nouveau recalcul + revue.
- **Indépendance du correcteur :** addition vérifiée par soustraction du total; soustraction par addition du reste et du terme soustrait; multiplication par addition répétée. Les critères d'explication et de localisation restent à évaluer humainement.
- **Couvre :** retenue, double report, emprunt à zéro, placement, contrôle inverse, multiplication courte, erreur procédurale et transfert. **Ne couvre pas :** fractions, décimaux, division posée, vitesse. La multiplication n'est pas une condition unique de maîtrise de base.

## Passation, accessibilité et sécurité

Avant évaluation : diagnostic court puis enseignement et pratiques distincts de q-011/q-012. Montrer consignes et chiffres lisibles, prévoir quadrillage ou objets regroupables sans indications de correction, autoriser explication orale transcrite, braille adapté ou saisie au clavier; conserver les quatre compétences évaluées. Pas de pénalité pour handicap, orthographe, graphisme ou vitesse hors critères mathématiques. Données des situations entièrement fictives, aucune situation de divulgation personnelle ou d'achat exigé. Pas de comparaison sociale entre élèves.

## Décision sans note unique

Une preuve A **et** une preuve B doivent satisfaire séparément C1–C4, dans deux contextes distincts, après enseignement et sans indices de contenu. On peut répartir sur deux séances pour vérifier la stabilité. Si la première passe et la seconde échoue, **pas de maîtrise déclarée** : micro-remédiation du maillon exact puis nouvel item différent dans le même contexte/type après délai. Les items q-001 à q-010 orientent la remédiation; ils ne remplacent pas les deux preuves.
