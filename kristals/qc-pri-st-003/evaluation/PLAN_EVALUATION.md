# Plan d'évaluation — `qc-pri-st-003` (v1.2)

**Objectif `obj-1` :** Choisir un instrument et relever des mesures traçables et reproductibles. **Critère `crit-1` :** Tenir un tableau de données sur deux essais comparables. **Famille `qc-pri-st-003-ev-01` :** `generee_sous_contraintes` (type natif inchangé). Les tâches fixes, les tableaux fictifs et les observations authentiques sont séparés sans confusion.

## Couverture et lien de chaque item

**Pour chacun des dix items de ce tableau :** `objectif_id=obj-1`, `critere_id=crit-1`, `family_id=qc-pri-st-003-ev-01`, `validation_status=a_revoir` (mêmes valeurs inscrites dans chaque objet JSON).

| Item (ID complet) | Difficulté | Mode | Représentation / observation attendue | Dimension ciblée |
|---|---|---|---|---|
| `qc-pri-st-003-q-001` | initial | fixe | choix de règle parmi 3 instruments, grandeur et unité | M1 instrument adapté |
| `qc-pri-st-003-q-002` | initial | fixe | tableau de deux lignes avec valeurs fictives de longueur | M2–M3 trace et comparabilité |
| `qc-pri-st-003-q-003` | initial | fixe | distinction lecture et cause + écart de 1 cm | M4 observation / inférence |
| `qc-pri-st-003-q-004` | intermédiaire | fixe | critique de 2 objets non comparables | M2 identité du phénomène |
| `qc-pri-st-003-q-005` | intermédiaire | fixe | graduation de règle, calcul 9 − 2 = 7 cm | M1–M3 lecture et unité |
| `qc-pri-st-003-q-006` | intermédiaire | fixe | tableau de durées fictives et écart 0,2 s | M3–M4 deux essais et prudence |
| `qc-pri-st-003-q-007` | intermédiaire | parametrique | trois cas approuvés de longueur en dixièmes de cm, sélection reproductible | M1, M3, M4 sur données simulées |
| `qc-pri-st-003-q-008` | transfert | parametrique | trois cas approuvés de durée en dixièmes de s | M1, M3, M4, transfert de grandeur |
| `qc-pri-st-003-q-009` | transfert | fixe | **Preuve autonome A** : mesurer deux fois la même largeur de cahier et produire son tableau | M1–M5, mesure réelle de longueur |
| `qc-pri-st-003-q-010` | transfert | fixe | **Preuve autonome B** : chronométrer deux fois le même trajet d'un petit jouet | M1–M5, mesure réelle de durée |

## Administration et barème

- **Formative :** 001–008 identifient les besoins sans conclure à une maîtrise à eux seuls. Le mode paramétrique porte uniquement sur un **corpus de données simulées**, jamais sur des résultats authentiques laissés au hasard.
- **Preuves de maîtrise :** 009 et 010 sont **indépendantes**, dans deux contextes et deux grandeurs distinctes. Les critères M1–M5 doivent être établis sur chacune; une moyenne ou un total ne compense pas l'absence de la seconde preuve.
- **Grille :** M1 choix instrument/unité; M2 conditions et répétition du protocole; M3 deux mesures authentiques consignées; M4 observation, comparaison et inférence prudente; M5 autonomie, sécurité, adaptation. Niveaux 0/1/2 dans `GRILLE_MAITRISE.md`.
- **Enregistrement :** le responsable décrit l'instrument choisi, les deux lignes et les aides fournies. Les valeurs d'un cahier ou du jouet ne sont **pas** prévisibles : exactitude jugée par lecture authentique, cohérence avec graduation et protocole, pas par une réponse magique.

## Règle reproductible du paramétrique (007 et 008)

- `mode=parametrique`, `seed` entier immuable dans chaque item (`2026100807`, `2026100808`), `parametres.corpus_ferme` = exactement 3 entrées par item.
- Algorithme **entier** : `index = seed % 3`; sélectionner `a_dixiemes`, `b_dixiemes` et l'unité de l'entrée indexée; lectures = valeurs / 10; `ecart_dixiemes = abs(a_dixiemes - b_dixiemes)` puis résultat = écart / 10. Chaque enregistrement est une représentation de données **simulées**; les calculs sont exacts en arithmétique entière.
- Contrainte : objet, grandeur, instrument, unité et conditions spécifiés par cas; même phénomène dans les deux essais; trois cas de longueur (`cm`) pour q-007 et trois cas de durée (`s`) pour q-008. Domaine **fermé** aux six cas listés, sans génération de textes libres.
- **Exemples contrôlés :** q-007 : `[11,5;11,5]→0,0 cm`, `[8,3;8,4]→0,1 cm`, `[12,7;12,5]→0,2 cm`; q-008 : `[2,9;3,1]→0,2 s`, `[4,0;4,0]→0,0 s`, `[3,8;3,6]→0,2 s`.
- **Limite :** le même jeu fictif n'autorise pas un jugement sur la capacité de lire une mesure réelle; l'observation instrumentée n'est évaluée que dans 009 et 010.

## Variabilité et invariants

| Dimension | Variation permise | Invariant |
|---|---|---|
| Objet matériel A | cahier ou pochette non coupante de dimensions différentes | même objet et même largeur lors des deux essais de A |
| Objet mobile B | jouet sûr et longueur de piste adaptée aux locaux | mêmes marques, jouet, surface et protocole **dans** les deux essais de B |
| Accès | règle tactile, grands chiffres, aide à tenir ou déclencher sur commande, dictée à scribe | l'élève choisit instrument, unité, procédé et consigne deux valeurs authentiques |
| Simulation 007/008 | uniquement cas indexé par seed entier dans le corpus fermé | énoncé, corrigé arithmétique et statut de données fictives |
| Traces | papier, tableau numérique, pictogramme, oral transcrit | unité, deux essais, comparabilité et remarque de qualité de mesure |

## Sécurité, équité, données et limites

Matériel stable et léger; aucune activité chimique, électrique, thermique ou acrobatique. Aucun enfant obligé de pousser un jouet, de se déplacer ou d'être filmé. Contrôle d'accessibilité avant le début; assistance uniquement non directive et consignée. Si aucun instrument équivalent n'est accessible, l'administration est **non concluante** et nécessite un jugement humain/adaptation appropriée; ne pas attribuer automatiquement la maîtrise sur la base d'une fiche simulée. Les données pédagogiques sont consignées localement et non dans un registre central du Kristal. Révision de contenu, de durée, de biais et essai interévaluateurs encore requis; banque `a_revoir`, sans certification.
