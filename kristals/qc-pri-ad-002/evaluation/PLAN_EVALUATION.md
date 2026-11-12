# PLAN D’ÉVALUATION — qc-pri-ad-002

**Famille :** `qc-pri-ad-002-ev-01` | **Objectif immuable :** `obj-1` — Caractériser un personnage et une situation de jeu dramatique. | **Critère immuable :** `crit-1` — Improviser une entrée en scène manifestant un personnage identifiable. | **Mode privilégié :** `observation_ou_production`.

## Alignement et couverture de la banque

Tous les items évaluent une **production dramatique observable** (ou une interprétation de scène suivie d'une entrée jouée), et non les opinions ou la personnalité de la personne. La rubrique cible un personnage identifiable, une intention perceptible, un cadre et une relation dramatiques, un indice justifié et des conditions sûres. Les deux preuves de maîtrise sont `q-009` et `q-010`.

| N° | Item | Liens conservés | Difficulté | Variation | Cible particulière |
|---|---|---|---|---|---|
| 001 | `qc-pri-ad-002-q-001` | `obj-1` / `crit-1` / `qc-pri-ad-002-ev-01` | initial | fiche fixe | Lire une entrée jouée |
| 002 | `qc-pri-ad-002-q-002` | `obj-1` / `crit-1` / `qc-pri-ad-002-ev-01` | initial | fiche fixe | Un billet à transmettre |
| 003 | `qc-pri-ad-002-q-003` | `obj-1` / `crit-1` / `qc-pri-ad-002-ev-01` | intermediaire | deux variantes fermées, seed 2403 | Carte à variantes : demander ou signaler |
| 004 | `qc-pri-ad-002-q-004` | `obj-1` / `crit-1` / `qc-pri-ad-002-ev-01` | intermediaire | fiche fixe | La relation visible |
| 005 | `qc-pri-ad-002-q-005` | `obj-1` / `crit-1` / `qc-pri-ad-002-ev-01` | intermediaire | deux variantes fermées, seed 2404 | Carte à variantes : trouver une solution |
| 006 | `qc-pri-ad-002-q-006` | `obj-1` / `crit-1` / `qc-pri-ad-002-ev-01` | intermediaire | fiche fixe | Deux intentions, un même personnage |
| 007 | `qc-pri-ad-002-q-007` | `obj-1` / `crit-1` / `qc-pri-ad-002-ev-01` | intermediaire | deux variantes fermées, seed 2410 | Carte à variantes : faire apparaître le cadre |
| 008 | `qc-pri-ad-002-q-008` | `obj-1` / `crit-1` / `qc-pri-ad-002-ev-01` | intermediaire | fiche fixe | Corriger une entrée confuse |
| 009 | `qc-pri-ad-002-q-009` | `obj-1` / `crit-1` / `qc-pri-ad-002-ev-01` | transfert | fiche fixe | Preuve A — bibliothèque imaginaire |
| 010 | `qc-pri-ad-002-q-010` | `obj-1` / `crit-1` / `qc-pri-ad-002-ev-01` | transfert | fiche fixe | Preuve B — atelier de réparation fictif |
| 011 | `qc-pri-ad-002-q-011` | `obj-1` / `crit-1` / `qc-pri-ad-002-ev-01` | transfert | deux variantes fermées, seed 2421 | Carte à variantes : nouvelle relation |
| 012 | `qc-pri-ad-002-q-012` | `obj-1` / `crit-1` / `qc-pri-ad-002-ev-01` | transfert | fiche fixe | Transfert : une situation qui change |

## Blueprint et représentation

- **Initial (q-001, q-002)** : observations d'une mini-scène puis entrée simple; on distingue ce qui est vu de ce qui est inféré.
- **Intermédiaire (q-003 à q-008)** : relation, lieu, buts contrastés et correction d'une entrée insuffisante; scènes au comptoir, à l'atelier ou au kiosque.
- **Transfert (q-009 à q-012)** : jeu autonome dans des lieux nouveaux (bibliothèque, atelier, musée imaginaire) et modification du contexte.
- **Modes de réponse équivalents** : scène debout ou assise, figurine, marionnette, gestes, paroles ou communication alternative. L'entrée fictive doit rester *manifestée*, une description seule ne suffit pas comme preuve de maîtrise.

## Variations admises / interdites

- `q-003`, `q-005`, `q-007`, `q-011` : **2 variantes fermées** chacune. Index = `seed % 2`, avec seed entière précisée dans l'item; le stimulus et la réponse-type de même index sont indissociables. Les 2 jeux de traces sont documentés dans `BANQUE_ITEMS.json` (16 états : 4 scénarios × 2 variantes × stimulus/corrigé). Interdire paraphrase générée libre qui changerait l'objectif ou l'équité.
- Autres items : fixes; seuls les gestes, formulations, accessoires symboliques, identités fictives non stéréotypées et modalités d'accès peuvent varier.
- Pas de barème déterministe pour juger une performance artistique ouverte : la **rubrique critériée** guide une appréciation humaine documentée; ne pas confondre avec exactitude de calcul.

## Critères d'observation et rétroaction

Le correcteur note pour chaque item : (1) signe de personnage, (2) signe d'intention, (3) situation/relation reconnaissable, (4) justification d'un signe, (5) cadre sûr. Il consigne des **observations** (« la figurine s'oriente vers le comptoir »), puis une interprétation (« le personnage cherche une personne ») et une rétroaction ciblée. N'évalue pas talent perçu, aisance, timidité, morphologie, accent ni croyance.

## Décision de maîtrise

- `q-009` et `q-010` : deux preuves de 15–40 s dans des fictions **distinctes**; préparation comparable; aucune aide individualisée (ni geste soufflé, ni réplique proposée) pendant les deux prestations; trace datée.
- Chaque preuve doit être au moins **satisfaisante** pour personnage, intention, situation/relation et justification, avec règles de sécurité respectées. Un choix original différent du modèle reste accepté si cohérent.
- Une prestation non observable ou une modalité inaccessible conduit à adapter et réadministrer, pas à présumer la non-maîtrise. Une seule bonne note n'autorise pas la sortie.

## Protection, accessibilité et revue

L'adulte contrôle les limites de jeu, retire les obstacles, n'impose ni contact, ni costume, ni vidéo, ni rôles humiliants. Peut proposer un plateau miniature, un public choisi, un support visuel ou une technologie d'assistance sans réduire les critères. Les scènes sont **fictives** : aucune histoire familiale à raconter. **Revue humaine obligatoire** de l'âge, du contexte et de la sécurité avant usage; banque `a_revoir`, non certifiée.
