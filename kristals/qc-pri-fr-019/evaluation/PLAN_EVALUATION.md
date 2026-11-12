# Plan d’évaluation — qc-pri-fr-019

**Objectif :** `obj-1` — Utiliser majuscules et signes de ponctuation pour segmenter et clarifier un écrit. **Critère :** `crit-1` — Ponctuer un passage dépourvu de signes et motiver les choix. **Famille :** `qc-pri-fr-019-ev-01` (réponse argumentée).

## Protocole d’administration et couverture
- **Mode de tous les items :** `fixe`, avec stimulus et correction verrouillés. Aucune substitution IA, aucun générateur paramétrique, `seed: null`, `parametres: null`. Les énoncés sont des créations originales. Les paragraphes en plusieurs lignes conservent leurs sauts de ligne prévus, notamment les prises de parole.
- **Représentations :** phrase isolée, deux phrases, énumération, alerte, dialogue, passage informatif et question directe/indirecte; l’élève doit écrire ou placer les signes et motiver le sens. La lecture à voix haute sert uniquement d’accès.
- **Difficulté :** initiale 001–004, intermédiaire 005–008, transfert 009–010. Les deux preuves sont en **contextes différents** (kiosque informatif / échange théâtral).
- **Durée à tester humainement :** environ 4–7 min/item initial, 6–10 min/intermédiaire, 10–15 min/preuve, sans imposer une vitesse. Les durées n’ont pas été étalonnées.

## Matrice complète d’alignement
| Item complet | Objectif | Critère | Famille | Difficulté | Représentation | Critères / couverture | Variations |
|---|---|---|---|---|---|---|---|
| `qc-pri-fr-019-q-001` | `obj-1` | `crit-1` | `qc-pri-fr-019-ev-01` | initial | Frontière déclarative + majuscule | 2 phrases | Aucune, item fixe |
| `qc-pri-fr-019-q-002` | `obj-1` | `crit-1` | `qc-pri-fr-019-ev-01` | initial | Question directe / réponse | ? + . | Aucune, item fixe |
| `qc-pri-fr-019-q-003` | `obj-1` | `crit-1` | `qc-pri-fr-019-ev-01` | initial | Virgule en liste simple | énumération | Aucune, item fixe |
| `qc-pri-fr-019-q-004` | `obj-1` | `crit-1` | `qc-pri-fr-019-ev-01` | initial | Avertissement expressif | ! + 2 . | Aucune, item fixe |
| `qc-pri-fr-019-q-005` | `obj-1` | `crit-1` | `qc-pri-fr-019-ev-01` | intermediaire | Liste + deuxième phrase | virgule + maj | Aucune, item fixe |
| `qc-pri-fr-019-q-006` | `obj-1` | `crit-1` | `qc-pri-fr-019-ev-01` | intermediaire | Dialogue à 2 répliques | colon + tirets + ?/. | Aucune, item fixe |
| `qc-pri-fr-019-q-007` | `obj-1` | `crit-1` | `qc-pri-fr-019-ev-01` | intermediaire | Réplique et narration | colon + tiret + . | Aucune, item fixe |
| `qc-pri-fr-019-q-008` | `obj-1` | `crit-1` | `qc-pri-fr-019-ev-01` | intermediaire | Interrogation indirecte/directe | . vs ? | Aucune, item fixe |
| `qc-pri-fr-019-q-009` | `obj-1` | `crit-1` | `qc-pri-fr-019-ev-01` | transfert | Preuve autonome A — kiosque | segmentation, liste, question, justification | Aucune, item fixe |
| `qc-pri-fr-019-q-010` | `obj-1` | `crit-1` | `qc-pri-fr-019-ev-01` | transfert | Preuve autonome B — théâtre | répliques, signes finaux, justification | Aucune, item fixe |

## Conditions de réussite et types de corrigés
- Les corrections fournissent la **solution de référence** et l’explication linguistique, non une valeur numérique ni une solution issue d’une IA libre. Corriger les marques finales, frontières, majuscules, virgule et marques de dialogue indépendamment.
- La rubrique `evaluation/GRILLE_MAITRISE.md` évalue quatre dimensions (0–2) : segmentation/majuscules, signe final, organisation interne/démarcation du dialogue, justifications et autonomie. Les priorités varient par contexte mais **les dimensions essentielles ne se compensent pas**.
- Pour chaque preuve, recueillir le texte annoté ET au moins deux justifications. Une option stylistique différente (p. ex. avertissement moins expressif) peut être défendue dans la langue en général; l’item 004 **annonce explicitement** une alerte autonome, afin d’éviter un barème arbitraire.
- Dans les dialogues, la présentation des répliques est imposée en lignes distinctes, avec tirets simples de dialogue `—`. Une autre convention reconnue n’est pas jugée « incorrecte dans toute la langue », mais doit être examinée humainement si proposée; ne pas faire varier les stimuli automatiquement.

## Sécurité, accessibilité et équité
- Textes fictifs sans information privée; pas d’images, d’audio tiers ni de contenu sensible. Permettre typographie agrandie, lecteur d’écran, clavier, pointage de signes et scribe neutre : **le scribe ne décide jamais du signe ni de sa place**.
- Ne pas noter prononciation, accent du français québécois, performance orale, décodage ni graphomotricité non pertinente. La justification peut être dite, dictée ou produite par écrit.
- `qc-pri-fr-015` demeure `requires`, mais un diagnostic d’équivalence peut valider la segmentation des phrases et permettre l’accès sans faire réciter le Kristal préalable.

## Validation et limites
- Les tests automatisés vérifient que les corrections n’ajoutent/ne retirent/ne réordonnent aucun mot : seules majuscules, espaces typographiques et ponctuations spécifiées changent. Ils ne prouvent pas à eux seuls la justesse grammaticale de toutes les variantes réelles.
- Révision humaine recommandée : acceptabilité en français québécois, lisibilité au primaire, durée, calibration des dimensions, cas stylistiques et accessibilité. Tous les items restent `validation_status: a_revoir`.
