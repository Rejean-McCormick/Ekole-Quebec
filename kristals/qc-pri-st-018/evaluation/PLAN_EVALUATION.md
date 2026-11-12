# PLAN D’ÉVALUATION — QC-PRI-ST-018
**Famille unique :** `qc-pri-st-018-ev-01` · **Objectif :** `obj-1` · **Critère :** `crit-1`.
**Objectif invariant :** Relier besoins vitaux et fonctions d’organes ou systèmes étudiés.
**Preuve invariante :** Construire un schéma fonctionnel simplifié d’un besoin vital.

## Couverture des items
Tous les items ci-dessous portent **simultanément** les identifiants `obj-1`, `crit-1` et `qc-pri-st-018-ev-01` dans `BANQUE_ITEMS.json`. Ils évaluent des traces préparatoires ou les productions de maîtrise, avec critères explicites.

| Item | Difficulté | Représentation | Couverture/critère spécifique | Variabilité |
|---|---|---|---|---|
| `q-001` | initial | cartes textuelles | organes ↔ fonctions | fixe |
| `q-002` | initial | réparation de modèle | digestion ≠ poumons | fixe |
| `q-003` | initial | schéma fléché | O₂ et transport | fixe |
| `q-004` | intermédiaire | cartes / schéma | digestion + absorption | fixe |
| `q-005` | intermédiaire | schéma mouvement | muscles, os, articulation | fixe |
| `q-006` | intermédiaire | image/texte | observation vs modèle | fixe |
| `q-007` | intermédiaire | scénario contrôlé | oxygène au repos | 3 cas corpus |
| `q-008` | intermédiaire | scénario contrôlé | nutriments après un aliment | 3 cas corpus |
| `q-009` | transfert | scénario contrôlé | mouvement fictif | 3 cas corpus |
| `q-010` | transfert | scénario contrôlé | séparer systèmes | 3 cas corpus |
| `q-011` | transfert | schéma autonome | P1 sentier, besoin O₂ | fixe, réservé |
| `q-012` | transfert | schéma autonome | P2 cantine, nutriments | fixe, réservé |

## Contrôles des stimuli et corrigés
- **q-001 à q-006 :** formulations fixes et réponses expliquées. Accepter synonymes scientifiques corrects; jamais « estomac = poumons » ou « os se contracte ».
- **q-007 à q-010 :** scénarios contrôlés à **corpus fermé de 3 situations par item**; `index = seed modulo 3`; graines 1807, 1808, 1809 et 1810. Les corrections fonctionnelles restent constantes pour les trois variantes; toute variation hors corpus exige révision préalable. Les cas calculés sont dans `parametres.exemple_calcule`.
- **q-011 et q-012 :** contextes réservés, non utilisés dans les exemples enseignés et **non paramétrés**, pour éviter la mémorisation. Diffèrent à la fois par lieu et par besoin (oxygène vs nutriments).
- **Réponse acceptable :** toute formulation anatomiquement et fonctionnellement correcte, même si des étapes détaillées sont ajoutées sans inverser les relations. Une présentation esthétique ne rapporte pas de point supplémentaire.

## Administration, sécurité, accessibilité
- Diagnostic : items 001–003; enseignement/pratique : 004–010; maîtrise : 011 puis 012 lors de deux occasions ou dans deux phases bien distinctes. Ne jamais conclure à partir d'une note sur un seul item.
- Les deux preuves sont faites **sans indices sur les organes ou les flèches**; lecteur neutre, dictée mot à mot, schéma à cartes vierges, temps supplémentaire et police agrandie sont permis. Les réponses peuvent être orales séquentielles avec description explicite des flèches.
- Mesurer uniquement les liens besoin–organe–fonction, la qualité des deux explications et l'autonomie. Aucun exercice physique, apnée, ingestion, test médical ni questions sur symptômes, poids ou habitudes.
- Une preuve incomplète entraîne remédiation ciblée et nouvelle situation inédite revue humainement; pas de « note de passage » automatique. Vérifier la précision des rubriques auprès d'un réviseur scientifique et pédagogique avant usage sommatif.

## Matrice des critères pour les deux preuves
P1 : besoin d'oxygène ; fonction d'échange des poumons ; transport du sang ; 2 flèches justifiées ; autonomie.
P2 : besoin de nutriments ; trajet du système digestif ; absorption principalement dans l'intestin grêle ; 2 flèches justifiées ; autonomie.
**Contrôle de couverture :** respiration (001,003,006,007,010,011), alimentation (002,004,008,010,012), mouvement (001,005,009), besoin/organe/fonction (tous). Les deux preuves sont interprétées avec `GRILLE_MAITRISE.md`.
