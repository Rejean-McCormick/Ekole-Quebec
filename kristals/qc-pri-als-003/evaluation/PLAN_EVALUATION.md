# Plan d'évaluation — `qc-pri-als-003-ev-01`

**Objectif lié sans modification :** `obj-1` — Identifier le sens global et quelques détails d’un texte oral rythmé.  
**Critère observable lié sans modification :** `crit-1` — Répondre à des questions simples après une chanson ou histoire entendue.  
**Famille :** `qc-pri-als-003-ev-01` · `type: observation_ou_production` · **statut : `a_revoir`.**

## Instrument et protocole

Chaque item présente **à la personne évaluatrice** un script anglais original, à lire ou interpréter oralement **deux fois en entier** sans afficher de transcription à l'élève. Les questions sont posées **après** l'écoute, dans une langue comprise de l'élève; la réponse peut être anglaise, française, gestuelle ou par pointage documenté, sans indice de contenu. Consigner textuellement/sémantiquement chaque réponse, les deux écoutes, le mode de réponse et toute adaptation. Pas de jugement sur l'accent, le chant juste, la lecture, l'écriture, la vitesse ou l'âge. Éviter qu'une image ne donne directement la réponse. Pas de piste audio fournie dans le delta : une personne doit dire le script.

## Matrice d'alignement et de couverture

| Item | Alignement | Difficulté | Représentation / genre audible | Mesures / corrigé de référence | Variation permise |
|---|---|---|---|---|---|
| `q-001` | `obj-1`, `crit-1`, `qc-pri-als-003-ev-01` | initial | comptine (départ à l'école) | idée générale + objet entendu | voix/débit seulement |
| `q-002` | mêmes trois IDs | initial | récit du lapin | lieu précis + action finale | voix/débit seulement |
| `q-003` | mêmes trois IDs | initial | comptine de pluie | répétition *splash* + action | voix/débit seulement |
| `q-004` | mêmes trois IDs | initial | comptine chat/abeille | rime *cat/hat* + idée générale | voix/débit seulement |
| `q-005` | mêmes trois IDs | intermédiaire | récit de deux tasses | couleur/personne, boisson, action | voix/débit seulement |
| `q-006` | mêmes trois IDs | intermédiaire | récit de bibliothèque | thème, livre sur la Lune, refrain | voix/débit seulement |
| `q-007` | mêmes trois IDs | intermédiaire | comptine en bateau | étang, papa, *row* | voix/débit seulement |
| `q-008` | mêmes trois IDs | intermédiaire | comptine de jeu | répétition, rime *play/day*, thème | voix/débit seulement |
| `q-009` | mêmes trois IDs | transfert | comptine d'arts en classe | activité, couleur, lieu | voix/débit seulement |
| `q-010` | mêmes trois IDs | transfert | récit de chèvres | thème, nombre, eau, phrase répétée | voix/débit seulement |
| `q-011` / P1 | mêmes trois IDs | transfert | comptine de jardinage | thème + 3 détails + refrain/rime, 5 points descriptifs | voix/débit seulement |
| `q-012` / P2 | mêmes trois IDs | transfert | histoire de mitaine à l'arrêt d'autobus | thème + 3 détails + question répétée, 5 points descriptifs | voix/débit seulement |

**Références complètes :** `evaluation/BANQUE_ITEMS.json` porte pour chaque item stimulus, consigne, réponse, critères, rétroaction et bornes de variation. Le tableau ci-dessus abrège les références de q-002 à q-012 sans les dissocier : **chacun** reste explicitement lié aux trois identifiants dans la banque.

## Barème descriptif et deux preuves

- P1 (`q-011`) et P2 (`q-012`) valent chacun **5 observations** : 1 thème, 3 détails et 1 indice sonore. La rime peut compléter l'indice de P1; dans P2 la question répétée est ciblée.
- Condition **dans chaque contexte** : thème adéquat **ET** au moins 2 des 3 détails exacts **ET** indice sonore/refrain exact, **sans aide sur le contenu**. Il s'agit d'une conjonction de composantes, pas d'un total ≥N.
- Satisfaire P1 **et** P2 à des moments distincts dans deux genres/contextes; noter les stratégies observées (référence à une ligne répétée ou à un fait entendu) et les modalités. En cas de divergence, ne pas déclarer la maîtrise; pratiquer le composant fragile et demander de nouvelles preuves, distinctes de la correction affichée.
- Les `q-001` à `q-010` servent de vérifications formative/étalonnage interne, non de raccourci à une note unique.

## Sécurité, équité, accessibilité et contrôle de variation

- Corpus de douze textes anglais **fixes**; **aucune permutation automatique** des personnages, couleurs, lieux, réponses, rhymes ou phrases. Ne pas utiliser la génération IA libre comme correcteur. `seed=null`, `parametres=null` parce qu'aucun item n'est paramétrique.
- Seuls le timbre vocal, une diction intelligible, le débit non dénaturant le rythme et une traduction fidèle des **consignes** sont permis. Reprise ou interprétation additionnelle pendant la preuve doit être consignée; elle peut invalider la comparabilité.
- Aucune donnée privée ni piste audio d'enfant incluse; volume sûr, environnement acoustique adéquat. Adapter les modalités expressives, distinguer clairement l'accès au message sonore d'une aide qui révèle les faits. Une transcription intégrale fait intervenir la **lecture** et réclame une évaluation d'équivalence; ne pas l'assimiler sans réserve à de l'écoute.
- Valider humainement avant usage sommatif : prononciation/rimes selon les accents, durée des scripts, difficultés lexicales, neutralité culturelle, clarté des consignes, adéquation des seuils et des modes d'accès.
