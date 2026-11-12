# PLAN D’ÉVALUATION — qc-pri-ma-015

**Objet unique :** `obj-1` — Relier les écritures décimales aux décompositions en dixièmes et centièmes.  
**Critère de réussite :** `crit-1` — Représenter un même décimal par un dessin et une décomposition.  
**Famille v1.2 conservée :** `qc-pri-ma-015-ev-01` ; famille native `paramétrique_controle`.  
**Statut :** items instrumentés `a_revoir`; ni publiés, ni homologués, ni certifiés.

## Conception d'épreuve et couverture

Chaque item de ce tableau est associé **explicitement à `obj-1`, `crit-1` et `qc-pri-ma-015-ev-01`**, comme les objets JSON individuels. La banque contient douze items uniques, répartis par niveaux et modes :

| Item | Niveau | Mode | Représentation et notion couverte | But de l'observation | Variation permise |
|---|---|---|---|---|---|
| Q001 | initial | fixe | Deux quadrillages `0,5` / `0,05`, dixième vs centième | Distinguer 50 cases de 5 cases | Aucune; dessins équivalents acceptés |
| Q002 | initial | fixe | Grille `0,36`, droite en centièmes, décomposition | 3/10 + 6/100, place 36/100 | Aucune; hachures/permutations acceptées |
| Q003 | intermédiaire | fixe | Deux grilles `1,24` | Représenter la partie entière | Aucune |
| Q004 | initial | parametrique | Grille décimale et décomposition | Traduire N centièmes en bandes + cases | Valeurs bornées de Q004; seed stable |
| Q005 | intermédiaire | parametrique | À partir de u,d,c construire dessin | Lire positions et zéros | Valeurs bornées de Q005 |
| Q006 | intermédiaire | parametrique | Droite `0–1`, grille, décomposition | Position exacte sur 100 pas | Valeurs bornées de Q006 |
| Q007 | intermédiaire | parametrique | Zéro final (`0,70 = 0,7`) | Comprendre équivalence | Valeurs bornées de Q007 |
| Q008 | intermédiaire | parametrique | Plus d'une grille; 1,09, etc. | Partie entière et centièmes | Valeurs bornées de Q008 |
| Q009 | intermédiaire | parametrique | Diagnostic d'une inversion dixièmes/centièmes | Détecter, justifier et corriger | Valeurs bornées de Q009 |
| Q010 | transfert | parametrique | Cases→notation→dessin nouveau | Transfert de représentation inverse | Valeurs bornées de Q010 |
| **Q011 / M1** | **transfert** | scenario_controle | **Aire fictive : mosaïque 1,26** | **Preuve 1 : dessin + décomposition autonome** | **Valeur/contexte fixes; mise en page adaptable** |
| **Q012 / M2** | **transfert** | scenario_controle | **Longueur : ruban 0,84 m** | **Preuve 2 : dessin + décomposition autonome** | **Valeur/contexte fixes; représentation accessible** |

## Définition exhaustive du générateur paramétrique

Les Q004 à Q010 sont des **versions calculables sans modèle génératif libre**. Chaque `parametres` d'item est un enregistrement autonome et contient les listes de centièmes admissibles, la valeur déterministe sélectionnée, contraintes, algorithme et tous les échantillons calculés. Pour l'item concerné :

1. `L = domaine_N_autorise` est la liste **ordonnée et finie** d'entiers de centièmes N; `seed = 15015 + 83 × n_item` (avec indices 4 à 10).
2. Sélection `N = L[seed % len(L)]`. La seed et l'ordre de L sont enregistrés pour reproduire exactement l'énoncé affiché. Aucune dépendance à un hasard de machine.
3. Calcul `u = N//100`, `d = (N%100)//10`, `c = N%10` avec division entière; écriture `u,dc` (deux chiffres après virgule); décomposition `u + d/10 + c/100`.
4. Dessin-référence : `u` grilles pleines de 100 cases, puis `d` bandes distinctes de 10 cases et `c` cases isolées dans la grille suivante. Pour la droite, le point est le `N`-ième centième à partir de 0 ou la partie fractionnaire après `u`, entre `u` et `u+1`.
5. **Contrôle exact :** `Fraction(N,100) == u + Fraction(d,10) + Fraction(c,100)` pour chaque valeur annoncée. Vérifier séparément le nombre de cases `100u+10d+c = N`. Pas de conversion en nombres flottants pour les corrigés.
6. **Variation autorisée :** exclusivement un changement de N au sein de L, avec recalcul intégral du stimulus, de la réponse et des critères inchangés. L'édition humaine d'un contexte ou le changement de difficulté exige une nouvelle validation avant diffusion.

**Barème local non sommatif :** axes `unité stable`, `dessin exact`, `décomposition égale`, `justification`, chacun évalué de 0 à 3 (voir `GRILLE_MAITRISE.md`). L'unité doit demeurer la même au fil des représentations; les décompositions algébriquement équivalentes sont permises quand justifiées. La correction du dessin et de la décomposition ne peut pas être remplacée par une réponse QCM.

## Maîtrise : deux manifestations indépendantes

M1 (Q011) = mosaïque : un carré entier et 26 centièmes, `1,26 = 1+2/10+6/100`; M2 (Q012) = ruban : 84 centièmes de 1 m, `0,84 = 8/10+4/100`. Contextes et grandeurs diffèrent (**aire conventionnelle** contre **longueur**), alors que les mêmes regroupements sont utilisés. Recueillir pour chacune la trace visuelle ou tactile décrite, la décomposition et l'explication. **Aucun indice conceptuel n'est autorisé pendant ces collectes**; outil ou scribe neutre accepté. Niveau minimal de 2 sur les quatre critères essentiels pour **les deux tâches**, sans moyenne entre tâches. La maîtrise ne repose ni sur le score d'une tâche ni sur des durées de réponse.

**Précaution d'indépendance :** si les stimuli des preuves M1 ou M2 ont servi d'exemples guidés devant l'élève (y compris le fichier de remédiation), ne pas les réutiliser comme preuve nouvelle. Élaborer alors deux variantes contextuelles distinctes, garder le même objectif, et soumettre leurs corrigés et rubriques au contrôle et à la revue humaine. Les deux stimuli actuels sont complets mais ne prouvent pas à eux seuls l'indépendance de la situation d'administration.

## Accessibilité, équité, sûreté

Grilles à contraste élevé avec hachures/numérotation, versions tactiles, dictée descriptive ou sélection électronique de cases avec restitution neutre possibles. Pour la droite, employer un segment manipulable comportant 100 divisions égales; une bande en dix segments que l'élève subdivise est équivalente si les centièmes sont explicités. Évaluer les relations numériques, non le trait de crayon, la rapidité, la capacité visuelle ou le contexte culturel. Les scénarios sont fictifs et ne demandent ni achat ni données personnelles. Revoir les consignes avec enseignants et intervenants en accessibilité avant usage de grande ampleur.

## Protocole de décision et limites

- Diagnostic `contenu/02_DIAGNOSTIC.md` peut reconnaître les acquis équivalents pour les deux préalables `qc-pri-ma-003` et `qc-pri-ma-012`.
- Items Q001–Q010 sont formatifs/entraînement; Q011 et Q012 sont des **candidats** pour deux preuves autonomes. Conserver l'aide effectivement donnée dans le journal d'évaluation LMS.
- Une incohérence dessin/écriture, une unité manquante, ou un indice conceptuel invalide la preuve comme manifestation autonome même si la quantité a été devinée.
- Tous les items restent `a_revoir` jusqu'à examen humain des formulations, biais, accessibilité, lisibilité des affichages et expérimentation pédagogique. Aucun suivi d'élève n'est inclus dans ce delta.
