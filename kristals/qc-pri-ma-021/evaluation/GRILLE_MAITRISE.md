# Grille critériée de maîtrise — `qc-pri-ma-021`

`obj-1` : Décrire un trajet ou une position au moyen de repères spatiaux stables.  
`crit-1` : Donner puis suivre un parcours spatial précis sans ambiguïté.  
Famille : `qc-pri-ma-021-ev-01`. Deux preuves indépendantes **A bibliothèque (`q-010`)** et **B robot de jardin (`q-011`)** sont indispensables.

## Éléments à observer séparément pour chaque preuve

| Dimension | 0 — Non attesté | 1 — En développement | 2 — Atteint de façon autonome |
|---|---|---|---|
| R1 Repère et départ | Aucun cadre stable ou départ incorrect. | Cadre reconstruit avec indice, ou axes x/y parfois inversés. | Départ, nord et convention `(x ; y)` annoncés/utilisés sans ambiguïté. |
| R2 Précision du parcours | Commandes incomplètes ou impossibles; un point illégal. | Route exécutable seulement après correction ou aide. | Commandes ordonnées, unitaires, exactement conformes aux contraintes, sans pas interdit. |
| R3 Exécution/trace | Arrivée fausse ou étapes manquantes. | Arrivée parfois bonne mais trace corrigée avec soutien. | Énumère ou matérialise **tous** les points successifs dans le bon ordre, arrivée correcte. |
| R4 Reproductibilité | Un autre exécutant ne peut pas suivre sans deviner. | Compléments nécessaires après questions stratégiques. | Départ, repère, suite et arrivée suffisent à reproduire la même route. |
| R5 Justification | Aucune vérification compréhensible. | Vérification seulement sur demande orientée. | Explique au moins un changement de coordonnée ou une contrainte de passage/obstacle et contrôle sa route. |

**Niveau 2** exige chacune des conditions de la ligne, pas seulement l'arrivée. Un indice du type « vas vers l'est » ou « contourne par le bas » rend l'essai non autonome. Lire la consigne, fournir un support tactile et retranscrire fidèlement sous dictée sans calculer à la place de l'élève sont des adaptations *neutres*, qui ne retirent pas l'autonomie cognitive.

## Preuve A — plan de bibliothèque

- Situation fictive : départ `(1 ; 2)`, comptoir obligatoire `(4 ; 2)`, destination `(4 ; 4)`, nord en haut, grille de points 6 × 6; communiquer puis suivre une route de **5 pas**.
- Trace de référence : `E3, N2`; `(1 ; 2),(2 ; 2),(3 ; 2),(4 ; 2),(4 ; 3),(4 ; 4)`.
- Contrôler en particulier **passage par le comptoir**, ordre de visite et chaque point intermédiaire. Demander à l'élève une vérification de 3 pas vers l'est puis 2 vers le nord, sans orienter sa réponse.

## Preuve B — robot de jardin

- Situation fictive : départ `(2 ; 5)`, destination `(5 ; 5)`; points bloqués `(3 ; 5),(4 ; 5),(3 ; 4),(4 ; 4),(3 ; 6),(4 ; 6)`, nord en haut, grille de points 6 × 6; communiquer puis suivre une route de **7 pas**.
- Trace de référence : `S2, E3, N2`; `(2 ; 5),(2 ; 4),(2 ; 3),(3 ; 3),(4 ; 3),(5 ; 3),(5 ; 4),(5 ; 5)`.
- Vérifier **aucun point bloqué**, aucun pas diagonal, tous les points internes à 1…6 et justification du détour; la performance peut être simulée par un pion, par commandes vocales ou par description textuelle.

## Règle de décision (pas une note globale)

| A | B | Décision |
|---|---|---|
| R1–R5 tous à 2, sans indice | R1–R5 tous à 2, sans indice et à une autre occasion | **Maîtrise attestée en interne** pour `obj-1`/`crit-1`, sous réserve de validation humaine du dispositif. |
| Tous à 2 | Une dimension inférieure à 2 ou aide cognitive | **Non encore attestée** : remédiation ciblée sur B, nouvelle variante/histoire vérifiée, puis recueillir deuxième preuve indépendante. |
| Une dimension inférieure à 2 ou aide | Tous à 2 | **Non encore attestée** : remédiation ciblée sur A et nouvelle preuve distincte. |
| Insuffisant / absent | Insuffisant / absent | Réenseigner le maillon concerné; ne pas inférer une maîtrise de la seule réussite d'items formatifs. |

Enregistrer pour chaque occasion : support (papier, tactile, oral), parcours **donné**, parcours **suivi**, trace, présence/absence d'indices, erreurs, justification et jugement de chaque dimension. Les dates et données d'élèves résident dans le LMS, **jamais** dans les fichiers de contenu de ce delta.

## Décisions de remédiation et rappel

- R1 manquant : axes et orientation; R2 manquant : suite/obstacle/bord; R3 : pas intermédiaires; R4 : qualité de communication de la route; R5 : demander de vérifier un pas et le passage obligatoire.
- Ne pas utiliser un item déjà corrigé comme nouvelle preuve; proposer une variante humainement revue avec même construit et contraintes mathématiques vérifiées. Retester **au moins deux contextes distincts** en autonomie.
- Rappel J+2/J+7 (`contenu/06_REMEDIATION_ET_TRANSFERT.md`) pour stabilité; ces rappels sont des suivis, non une certification automatique.

**Statut des rubriques :** proposées, à réviser par une personne compétente (difficulté, accessibilité, fiabilité inter-évaluateurs, biais et appropriation). Aucune évaluation d'élèves ni standardisation réalisés ici.
