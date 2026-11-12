# PLAN D’ÉVALUATION — qc-pri-us-001

**Objet invariant :** Positionner et ordonner des événements selon une échelle temporelle cohérente.  
**Critère invariant :** Construire une ligne du temps et expliquer l’ordre retenu.  
**Famille :** `qc-pri-us-001-ev-01` — type canonique `generee_sous_contraintes`. **Statut :** ébauches révisables, non certifiées.

## Ce qui est mesuré

- **Examen de source** (2 points) : date du fait repérée; éviter la confusion date du document/date du fait, signaler si le support est fictif ou historique.
- **Succession** (2 points) : tri croissant des années sans créer un ordre injustifié quand deux événements partagent l’année.
- **Échelle** (2 points) : origine et unité explicitement indiquées; distances proportionnelles au nombre d’années. La réponse peut être une bande dessinée ou un tableau « date, position » entièrement équivalent.
- **Argumentation et limite** (2 points) : expliquer le calcul/tri à partir des données et une limite (précision annuelle, source partielle, événements manquants) adaptée au cas.

**Rubrique par dimension (0, 1, 2) :** 2 = correct et autonome sans aide; 1 = partiellement correct ou justification incomplète; 0 = incorrect/non démontré. La simple addition (sur 8) ne suffit **jamais** pour attester la maîtrise : consulter `GRILLE_MAITRISE.md`, deux contextes requis et aucune dimension cruciale éliminée par compensation.

## Carte d’alignement et couverture des douze items

Chaque ligne se réfère explicitement à `obj-1`, `crit-1` et à la famille ci-dessus. Une variante est choisie dans un corpus fermé puis résolue par calcul déterministe; l’enseignant ne doit pas improviser de dates dans les versions validées.

| Item | Difficulté | Mode / variation | Point distinct travaillé | Liens obligatoires |
|---|---|---|---|---|
| `qc-pri-us-001-q-001` | initial | 2 variantes A/B, seed 4100 | jalons école, ordre et échelle | obj-1 / crit-1 / qc-pri-us-001-ev-01 |
| `qc-pri-us-001-q-002` | initial | 2 variantes A/B, seed 4103 | date du fait vs date du document | obj-1 / crit-1 / qc-pri-us-001-ev-01 |
| `qc-pri-us-001-q-003` | intermediaire | 2 variantes A/B, seed 4104 | ordre de quatre jalons | obj-1 / crit-1 / qc-pri-us-001-ev-01 |
| `qc-pri-us-001-q-004` | intermediaire | 2 variantes A/B, seed 4107 | écarts inégaux et événement médian | obj-1 / crit-1 / qc-pri-us-001-ev-01 |
| `qc-pri-us-001-q-005` | intermediaire | 2 variantes A/B, seed 4111 | deux faits la même année | obj-1 / crit-1 / qc-pri-us-001-ev-01 |
| `qc-pri-us-001-q-006` | intermediaire | 2 variantes A/B, seed 4114 | situer une décennie | obj-1 / crit-1 / qc-pri-us-001-ev-01 |
| `qc-pri-us-001-q-007` | transfert | 2 variantes A/B, seed 4122 | preuve autonome A, jardin scolaire | obj-1 / crit-1 / qc-pri-us-001-ev-01 |
| `qc-pri-us-001-q-008` | transfert | 2 variantes A/B, seed 4128 | preuve autonome B, Expo 67 documentée | obj-1 / crit-1 / qc-pri-us-001-ev-01 |
| `qc-pri-us-001-q-009` | initial | fixe | date source / fait | obj-1 / crit-1 / qc-pri-us-001-ev-01 |
| `qc-pri-us-001-q-010` | intermediaire | fixe | pas de 2 ans | obj-1 / crit-1 / qc-pri-us-001-ev-01 |
| `qc-pri-us-001-q-011` | intermediaire | fixe | même année | obj-1 / crit-1 / qc-pri-us-001-ev-01 |
| `qc-pri-us-001-q-012` | transfert | fixe | pas de 5 ans | obj-1 / crit-1 / qc-pri-us-001-ev-01 |

**Couverture :** reconnaissance documentaire (002, 009); tri et échelle 1 an (001, 003, 004); cas limite même année (005, 011); notion d’époque (006); échelle de 2 ans et de 5 ans (010, 012); preuve d’autonomie 1 scolaire fictive (007); preuve d’autonomie 2 historique BAnQ (008). Les items 007 et 008 sont conservés pour des tentatives distinctes, à moments espacés; ne pas présumer qu’une variante remplace l’autre contexte.

## Contraintes de variation et contrôles de validité

1. Pour `q-001` à `q-008`, **deux variantes complètes** sont enregistrées dans `BANQUE_ITEMS.json`. Choisir l’indice `seed % 2` (0=A, 1=B). Chaque variante comporte son énoncé daté, son origine, son pas, ses positions de référence, sa réponse/limite et ses données de provenance; aucune création libre de faits historiques.
2. Corrigé : trier les événements par année croissante; placer à `(année - origine)/pas`; si les années sont égales, même repère et ordre mutuel inconnu. Le pas est positif et divise exactement les différences dans les cas contrôlés. Recalculer si un jeu de variantes est enrichi **après** une procédure de revue.
3. Les tâches `q-009` à `q-012` sont fixes et servent de repères comparables. Garder les précisions documentaires (année du fait vs date de publication) et préciser si des données sont inventées.
4. Variabilité admise **dans la forme de production** : sens d’écriture explicité, tracé papier/tactile/numérique, équivalent textuel, réponse orale transcrite. Variabilité non admise : inventer dates, changer une unité sans recalculer, transformer une liste simple en ligne graduée proportionnelle par affirmation, attribuer des faits aux Premiers Peuples sans source.

## Administration sûre et accessible

- Fiches haute lisibilité, lisibles à voix haute, non dépendantes de couleurs, cartes manipulables, possibilité de zoom/tactile ou de tableau structuré.
- Aucun récit autobiographique obligatoire. Les scénarios scolaires sont tous explicitement fictifs. Les faits d’Expo 67 sont réduits à des jalons documentés, sans inférence culturaliste.
- Pas de recherche libre nécessaire pour l’élève : données et mentions d’origine incluses. Temps et adaptations raisonnables sans changer le critère chronologique.
- Les dates historiques et la pertinence des rubriques requièrent une **revue humaine** avant emploi sommatif. Les items créés ne sont pas homologués ou certifiés.

## Décision après deux preuves

En contextes distincts, `q-007` (jardin scolaire fictif) et `q-008` (Expo 67 documentée) montrent l’ordre, l’échelle et la justification **sans indice**. Sur chaque production : dimensions « succession » et « échelle » à 2/2 et « source » et « argumentation » chacune ≥ 1/2, accompagnées d’une explication exploitable; la grille décrit les exceptions et remédiations. Si une preuve manque, proposer une correction ciblée et une **nouvelle tâche** de contexte équivalent, pas un simple rattrapage par points.
