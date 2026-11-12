# PLAN D’ÉVALUATION — qc-pri-eps-011
**Identifiants invariants :** `obj-1` / `crit-1` / `qc-pri-eps-011-ev-01`. **Tâche-ancre :** « Sélectionner des choix sains dans des situations scolaires fictives. » **Mode pédagogique :** observation_ou_production, dont 10 scènes fixes et 2 scénarios contrôlés A/B. **Statut :** à revoir.

## Alignement item par item
Chaque ligne relie explicitement le même `obj-1`, le même `crit-1` et la même famille `qc-pri-eps-011-ev-01`; la banque contient les questions, corrigés, critères et rétroactions.

| Item | Référence objectif/critère/famille | Notion / preuve | Niveau | Représentation | Variation |
|---|---|---|---|---|---|
| q-001 | `obj-1` · `crit-1` · `qc-pri-eps-011-ev-01` | hygiène, prévention | initial | Scène fictive + décision justifiée (texte/oral/cartes) | Aucune, texte fixe |
| q-002 | `obj-1` · `crit-1` · `qc-pri-eps-011-ev-01` | repos, hydratation | initial | Scène fictive + décision justifiée (texte/oral/cartes) | Aucune, texte fixe |
| q-003 | `obj-1` · `crit-1` · `qc-pri-eps-011-ev-01` | repos | initial | Scène fictive + décision justifiée (texte/oral/cartes) | Aucune, texte fixe |
| q-004 | `obj-1` · `crit-1` · `qc-pri-eps-011-ev-01` | prévention, hygiène | initial | Scène fictive + décision justifiée (texte/oral/cartes) | Aucune, texte fixe |
| q-005 | `obj-1` · `crit-1` · `qc-pri-eps-011-ev-01` | hygiène | intermediaire | Scène fictive + décision justifiée (texte/oral/cartes) | Aucune, texte fixe |
| q-006 | `obj-1` · `crit-1` · `qc-pri-eps-011-ev-01` | hygiène, prévention | intermediaire | Scène fictive + décision justifiée (texte/oral/cartes) | Aucune, texte fixe |
| q-007 | `obj-1` · `crit-1` · `qc-pri-eps-011-ev-01` | hydratation | intermediaire | Scène fictive + décision justifiée (texte/oral/cartes) | Aucune, texte fixe |
| q-008 | `obj-1` · `crit-1` · `qc-pri-eps-011-ev-01` | repos, prévention | intermediaire | Scène fictive + décision justifiée (texte/oral/cartes) | Aucune, texte fixe |
| q-009 | `obj-1` · `crit-1` · `qc-pri-eps-011-ev-01` | hydratation, prévention | intermediaire | Scène fictive + décision justifiée (texte/oral/cartes) | Aucune, texte fixe |
| q-010 | `obj-1` · `crit-1` · `qc-pri-eps-011-ev-01` | repos, hydratation | intermediaire | Scène fictive + décision justifiée (texte/oral/cartes) | Aucune, texte fixe |
| q-011 | `obj-1` · `crit-1` · `qc-pri-eps-011-ev-01` | repos, hygiène, hydratation, prévention; preuve de maîtrise | transfert | Scénario multi-indices, décisions observées + justifications | A/B textes verrouillés, seed paire=A/ impaire=B |
| q-012 | `obj-1` · `crit-1` · `qc-pri-eps-011-ev-01` | repos, hygiène, hydratation, prévention; preuve de maîtrise | transfert | Scénario multi-indices, décisions observées + justifications | A/B textes verrouillés, seed paire=A/ impaire=B |

## Couverture et progression
- **Repos :** q-002, 003, 008, 010, 011, 012; **hygiène :** q-001, 004, 005, 006, 011, 012; **hydratation :** q-002, 007, 009, 010, 011, 012; **prévention :** q-001, 004, 006, 008, 009, 011, 012. Les scènes couvrent choix initial, justification, contraintes et transfert.
- `q-001`–`q-010` : repères formatifs avec réponses justifiées, pas de score isolé de maîtrise. `q-011` et `q-012` : deux manifestations autonomes de `crit-1`, dans **atelier bibliothèque** et **fête sportive scolaire**; l’une ne remplace pas l’autre.
- Réponses observables en 4 dimensions : D (choix sûrs et adaptés), E (explications par notions), S (sécurité, alternative et non-stigmatisation), A (autonomie et adaptation). Échelle 0–3 par dimension dans la grille. Chaque preuve exige au moins le niveau 2 sur les 4 dimensions, sans choix dangereux; décision après deux preuves, pas une moyenne.

## Variabilité, correction et fiabilité
- 10 cas fixes, énoncés et réponses verrouillés. q-011 et q-012 possèdent chacun deux **seules** variantes autorisées A/B intégralement écrites dans le JSON; graine entière stable, A si paire, B si impaire (q-011: 11010/11011; q-012: 12010/12011). Aucun appel IA ou banque libre; vérification déterministe de la sélection.
- Les formulations de réponses peuvent varier si elles sont **équivalentes en sécurité et en justification**. Aucune quantité universelle de liquide, aucune recommandation médicale pour une personne particulière; l’adulte responsable aide lorsqu’une ressource est absente ou qu’une situation devient dangereuse.
- Les « corrigés » sont des décisions attendues et **rubriques de production**, non des QCM forcés. L’observateur peut noter textuellement l’indice utilisé et la justification, puis évaluer avec la grille.

## Accessibilité, sécurité et équité
- Textes de cartes imprimables avec descriptions; lecture oralisée neutre, temps additionnel, communication alternative/assistée, clavier ou pointage avec raison communiquée. Une limite motrice n’invalide pas une décision correcte.
- Aucune donnée personnelle, alimentation réelle, sommeil familial, handicap, maladie, morphologie, consommation d’eau réelle, performance ou exercice physique ne doit être mesuré. Ne pas comparer les corps ni traiter une préférence culturelle comme défaut.
- Scénarios fictifs, disponibilité explicite des ressources ou présence d’un adulte; demander aide est une réponse valide. En cas de vrai danger, appliquer les procédures de l’école. Gestion d’hygiène réelle seulement sous supervision appropriée.
- Évaluation non certifiée. Avant utilisation sommative : revue humaine pour exactitude santé publique, langage, sensibilités, difficultés, durée, accessibilité et essais avec personnes représentatives.
