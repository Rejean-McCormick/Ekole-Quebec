# Plan d'évaluation — qc-pri-ma-022 | v1.2

**Objectif inchangé (`obj-1`) :** Reconnaître et décrire des solides grâce à leurs éléments constitutifs.  
**Critère / preuve inchangée (`crit-1`) :** Associer une description à un solide et justifier à l’aide de ses propriétés.  
**Famille inchangée :** `qc-pri-ma-022-ev-01` (`paramétrique_controle` privilégié).  
**Statut :** banque instrumentée, `a_revoir`; aucune certification ni essai auprès d'élèves.

## Architecture et pondération descriptive

- **Diagnostic non sommative :** deux tâches `diag-1` et `diag-2` du contenu; adapter ensuite l'enseignement sans bloquer l'accès.
- **Entraînement formative :** 4 tâches autonomes de contenu et banque `q-001`–`q-010`. Scores locaux éventuels uniquement pour guider la remédiation. Choisir plusieurs modalités; ne pas traduire mécaniquement leur moyenne en maîtrise.
- **Preuve A de maîtrise :** `q-011` (scénographie d'un musée, prisme triangulaire). **Preuve B :** `q-012` (atelier de fabrication d'une lanterne froide, pyramide carrée). Conserver les deux productions distinctes, idéalement à des dates différentes; les noms et critères restent constants, les stimuli changent.
- **Dimension minimale pour chaque preuve :** identification correcte; F, A et S exacts; deux propriétés cohérentes, dont une discriminante; patron ou relation faces/pliage juste; réponse sans aide fournissant la solution. La grille décrit 4 niveaux et interdit la maîtrise déduite d'un score unique.

## Plan item par item

**Chaque ligne ci-dessous est explicitement rattachée à `obj-1` / `crit-1` / `qc-pri-ma-022-ev-01`.**

| Item | Difficulté | Représentation | Tâche et vérification principale | Variabilité autorisée |
|---|---|---|---|---|
| `q-001` | initial | Description verbale du cube | Nom, F6/A12/S8 et deux propriétés | Aucune, stimulus fixe |
| `q-002` | initial | Base carrée + pointe décrites | Pyramide carrée F5/A8/S5, contraste avec prisme | Aucune |
| `q-003` | initial | Deux triangles, trois rectangles | Prisme triangulaire F5/A9/S6, exclusion pyramide | Aucune |
| `q-004` | intermédiaire | Graphe de quatre sommets | Tétraèdre F4/A6/S4, exclusion pyramide carrée | Aucune |
| `q-005` | intermédiaire | Segment sur une face | Diagonale ≠ arête; A du cube=12 | Aucune |
| `q-006` | intermédiaire | Face mesurée 3 × 5 | Pavé non cubique, F/A/S non discriminants | Aucune |
| `q-007` | intermédiaire | Description textuelle de cas catalogué | Nom, F/A/S et deux raisons; 3 cas autorisés T/P/H | `seed modulo 3`, table fermée |
| `q-008` | intermédiaire | Dispositions textuelles de six carrés | Patrons cube : croix valide vs rectangle 2 × 3 ou bande 1 × 6 | `seed modulo 4`, orientation/cas bornés |
| `q-009` | transfert | Composition des faces + calcul d'incidences | F et A = somme(côtés)/2, S contrôlé; 4 cas | `seed modulo 4`, table fermée |
| `q-010` | intermédiaire | Deux patrons de pyramide carrée | Carré + 4 triangles (possible) vs 3 (incomplet) | Aucune |
| `q-011` | transfert | Scénario musée + patron décrit | **Preuve A** : prisme triangulaire, F5/A9/S6, 2 raisons et patron | Contexte verrouillé tant que non révisé |
| `q-012` | transfert | Scénario atelier + patron décrit | **Preuve B** : pyramide carrée, F5/A8/S5, 2 raisons et patron | Contexte verrouillé tant que non révisé |

**Couverture de contenu :** face (`q-001,002,003,004,006,007,009,010,011,012`), arête (`q-001..007,009,011,012`), sommet (`q-001..004,006,007,009,011,012`), patron (`q-008,010,011,012`), justification discriminante (`q-002..004,006,007,011,012`), deux contextes (`q-011,012`).

## Génération reproductible, non libre

- `q-007` : catalogues de trois solides, index `seed % 3`. Chaque entrée donne une description, une identité et F/A/S exacts; les corrections sont tabulées.
- `q-008` : index `seed % 4`; choisit deux dispositions invalides et inverse l'ordre A/B; la croix V est toujours la seule disposition repliable. Ne substituer aucun schéma extérieur au catalogue sans nouveau test de pliage.
- `q-009` : index `seed % 4`; choisir parmi cube, prisme droit triangulaire, pyramide à base carrée et tétraèdre. Calculer l'incidence de faces `I=sum(nombre de côtés de chaque face)`, `A=I/2`, puis vérifier `F+S=A+2` pour les cas convexes du catalogue. Comparer aussi à un comptage combinatoire indépendant des arêtes.
- Chaque paramètre, chaque cas admissible, le seed, un échantillon rendu et l'algorithme figurent dans `BANQUE_ITEMS.json`. **Ne jamais** générer par simple demande de texte variable à une IA comme preuve de conformité du corrigé. Les stimuli fixés dans la banque correspondent à leur seed.

## Critères, sécurité et accessibilité

**Grille analytique par preuve :** I — identification; P — propriétés discriminantes et justification; C — comptes F/A/S; N — patron et pliage. Les quatre dimensions doivent atteindre le niveau « satisfaisant » pour **chacune** des deux manifestations; sinon le parcours est en consolidation. La maîtrise ne se déduit ni d'une note unique ni d'une compensation par une autre force. `evaluation/GRILLE_MAITRISE.md` fait autorité pour la décision locale.

**Modalités équivalentes :** lecture neutre du texte, braille ou schéma tactile, pièces pré-assemblées, description textuelle structurée, réponse enregistrée ou transcrite fidèlement. Évaluer la géométrie et la justification, pas la vitesse, l'habileté manuelle, la vision en couleur, l'écriture ou l'aisance orale. Aucun objet chauffant ni outil tranchant nécessaire (lanterne de papier symbolique); superviser la manipulation si des découpages sont proposés. Limiter les informations personnelles; rien n'est stocké dans les fichiers du Kristal.

**Sécurité de l'examen :** séparer séances et stimuli A/B, ne pas dévoiler les corrigés à l'élève avant ses deux productions; les seeds d'entraînement sont reproductibles, et une banque accessible publiquement ne constitue pas à elle seule un examen sécurisé. Revue humaine de formulations, barèmes, biais et accessibilité avant usage sommatif.

## Contrôles et limites

Contrôles techniques rapportés dans `livraison/VALIDATION.md` : parsabilité, cohérence identifiants, seeds, comptages combinatoires, structure ZIP. Cela n'équivaut ni à une validation empirique des patrons manipulés par différents élèves, ni à une étude de fidélité entre correcteurs; une validation pédagogique humaine reste requise.
