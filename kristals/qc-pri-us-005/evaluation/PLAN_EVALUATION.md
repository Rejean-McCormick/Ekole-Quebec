# Plan d’évaluation · `qc-pri-us-005`

**Autorité interne :** norme autonome v1.2, sans homologation PFEQ. **Objectif immuable :** `obj-1` — Distinguer source, affirmation et interprétation dans un document historique. **Critère de preuve :** `crit-1` — Comparer deux sources et relever ce qu’elles établissent réellement. **Famille :** `qc-pri-us-005-ev-01` (`generee_sous_contraintes`). **Statut :** banque rédigée, `a_revoir` pour chaque item.

## Architecture de l’épreuve

- **Matériel :** deux pièces entièrement fictives et contextualisées par item, avec créateur, type, date de création, extrait textuel. Elles sont déjà fixées dans `BANQUE_ITEMS.json`; aucune source générée librement en cours d’épreuve.
- **Opération attendue :** relever une affirmation exacte de A et de B, situer leurs positions, distinguer ce qu’elles attestent dans les pièces de l’événement externe à corroborer et formuler une limite. Répondre par texte, tableau, dictée fidèle ou audio transcrit.
- **Critères :** R1 = nature/créateurs/dates; R2 = affirmation textuelle correctement attribuée; R3 = inférence mesurée, limite et distinction affirmation/fait; R4 = points de vue comparés et vérification pertinente. Chaque item renvoie à `obj-1`, `crit-1` et `qc-pri-us-005-ev-01`.
- **Complexité :** initial (une différence facile comme annoncé/inscrit); intermédiaire (nuances, décalages entre dates, cause non garantie); transfert (deux traces de types distincts et portée problématique).
- **Barème indicatif :** 4 dimensions × niveaux 0, 1, 2 (maximum 8). Pas de verdict à partir d’une seule somme numérique; référer à la grille analytique et aux deux situations autonomes.

## Matrice des 12 items (alignement exhaustif)

| Item | Phase | Difficulté | Représentation | Situation / couverture | Liens immuables |
|---|---|---|---|---|---|
| `q-001` | diagnostic | initial | avis public et carnet personnel | Un horaire annoncé et une visite vécue — Marché local fictif, 1904 | `obj-1`, `crit-1`, `qc-pri-us-005-ev-01` |
| `q-002` | diagnostic | initial | affiche et registre | Une fête annoncée et des traces de participation — Fête locale fictive, 1922 | `obj-1`, `crit-1`, `qc-pri-us-005-ev-01` |
| `q-003` | guidée | initial | note de gestion et lettre | Une bibliothèque et son public — Bibliothèque locale fictive, 1909 | `obj-1`, `crit-1`, `qc-pri-us-005-ev-01` |
| `q-004` | guidée | intermediaire | avis municipal et carte postale | Des travaux et un trajet — Pont fictif, 1915 | `obj-1`, `crit-1`, `qc-pri-us-005-ev-01` |
| `q-005` | guidée | intermediaire | invitation et souvenir rétrospectif | La date d’un récit et celle d’un événement — Souvenir fictif d’une inauguration, 1920/1941 | `obj-1`, `crit-1`, `qc-pri-us-005-ev-01` |
| `q-006` | autonome | intermediaire | rapport et carnet | Le jardin scolaire — École fictive, 1907 | `obj-1`, `crit-1`, `qc-pri-us-005-ev-01` |
| `q-007` | autonome | intermediaire | horaire imprimé et carte | La traversée par bateau — Service de bateau fictif, 1913 | `obj-1`, `crit-1`, `qc-pri-us-005-ev-01` |
| `q-008` | autonome | intermediaire | registre technique et journal | Une pompe à eau entretenue — Équipement communal fictif, 1928 | `obj-1`, `crit-1`, `qc-pri-us-005-ev-01` |
| `q-009` | autonome | transfert | programme et reçu | La foire et les ventes — Foire fictive, 1934 | `obj-1`, `crit-1`, `qc-pri-us-005-ev-01` |
| `q-010` | maitrise | transfert | avis collectif et feuille de distribution | La distribution de bois en hiver — Organisation d’entraide fictive, 1916 | `obj-1`, `crit-1`, `qc-pri-us-005-ev-01` |
| `q-011` | maitrise | transfert | avis de service et récit de voyage | Changer un quai de gare — Transport ferroviaire fictif, 1931 | `obj-1`, `crit-1`, `qc-pri-us-005-ev-01` |
| `q-012` | transfert | transfert | plan textuel et souvenir oral retranscrit | Comparer une carte à un témoignage — Chemins d’une localité fictive, 1926 | `obj-1`, `crit-1`, `qc-pri-us-005-ev-01` |

## Deux manifestations obligatoires de maîtrise

1. **`qc-pri-us-005-q-010` :** entraide fictive (avis de livraisons / relevé de dépôts). L’élève distingue action annoncée, trace d’action et livraison aux familles non démontrée.
2. **`qc-pri-us-005-q-011` :** transport fictif (avis de quai / lettre de voyage). L’élève confronte règle annoncée et voyage observé, sans généraliser à tous les trains.

Ces contextes sont **distincts** (service solidaire et déplacement ferroviaire), les documents et les créateurs sont différents. Les tâches se passent **sans indices de raisonnement ni exemples identiques**. Les aménagements d’accès ne doivent pas révéler ce qui constitue la limite d’inférence. Pas de crédit pour répéter la réponse de la preuve 1 à la preuve 2.

**Décision :** aux deux productions, chacune des quatre dimensions R1–R4 atteint au moins 1, et R2 et R3 atteignent 2. Noter l’indépendance (oui/non) et expliciter les traces de raisonnement; si une seule preuve est satisfaisante, ne pas conclure à une maîtrise stable. Refaire une instruction ciblée puis proposer deux **nouveaux** scénarios contrôlés et relus; ne pas réutiliser une preuve exposée à son corrigé.

## Corrigés et variabilité

- Tous les stimuli, dates, auteurs et réponses attendues sont **figés et explicités** dans `BANQUE_ITEMS.json`. Le correcteur s’appuie sur l’extrait attribué et sur le raisonnement; les réponses sémantiquement équivalentes et bien justifiées sont admissibles.
- **Mode item :** `scenario_controle` (un scénario fixe, susceptible d’être choisi parmi les scénarios déjà révisés). **Mode de famille :** `generee_sous_contraintes`; il ne donne pas le droit à une génération ouverte de textes ni à une correction par IA seule. `seed=null`, `parametres=null` car aucun mode paramétrique n’est utilisé et il n’y a pas de tirage pseudo-aléatoire.
- **Variations autorisées :** adaptation typographique ou orale fidèle; variation de l’ordre de présentation à condition de conserver la correspondance A/B; sélection manuelle d’un item déjà contrôlé. **Interdit :** changer une date, un auteur, un quantificateur, inventer un troisième texte, alterner annoncé/réalisé ou créer un corrigé sans nouvelle validation.
- **Limites de correction :** un document simulé ne permet pas de vérifier une histoire réelle. La justesse évaluée est l’extraction et l’inférence **par rapport aux textes de l’exercice**, pas la vérité de l’événement fictif. Ne pas pénaliser une proposition d’enquête plausible différente de l’exemple si elle répond à l’incertitude identifiée.

## Couverture et sécurité

- **Notions :** document (12/12), auteur/créateur (12/12), date de création et temps évoqué (12/12), point de vue (12/12). Des scénarios ciblent explicitement annoncé/réalisé (D1, G2, A2, M2), inscription/participation (D2), mémoire rétrospective (G3, T1), cause non déduite (A3), coïncidence de dates (A4) et livraison annoncée/réelle (M1).
- **Accessibilité :** texte lisible et vocalisable, références à la date en clair, pas de couleur nécessaire, réponse vocale/écrite/tableau autorisée, lecture neutre du stimulus possible. L’adaptation ne change pas l’exigence d’attribuer les faits et d’expliquer une limite.
- **Respect :** données fictives sans noms d’élèves réels, évitement des stéréotypes culturels, aucune demande de révéler une histoire personnelle ou familiale. Aucun document des Premiers Peuples inventé ou présenté comme authentique.
- **Sources et droits :** les pièces didactiques sont originales, sans copie de fonds archivistique; références de méthode vérifiées séparément. Revue humaine historique, didactique, linguistique et d’accessibilité, ainsi qu’essai de correction interjuges, requis avant qualification ou publication.
