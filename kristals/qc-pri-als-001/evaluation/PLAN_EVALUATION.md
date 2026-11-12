# Plan d'évaluation — qc-pri-als-001

**Objectif immuable :** `obj-1` — Exécuter et reformuler des consignes orales courantes en anglais.  
**Preuve immuable :** `crit-1` — Suivre trois instructions inédites puis indiquer leur sens.  
**Famille :** `qc-pri-als-001-ev-01` · type : `observation_ou_production` · banque : `BANQUE_ITEMS.json` · statut : **à revoir**.

## Architecture et couverture

L'épreuve mesure la compréhension **auditive** des commandes anglaises, l'exécution ou indication motrice accessible, et la reformulation **sémantique**. Les premiers items sont des observations ponctuelles; ils documentent les progrès, **pas** la décision finale. Les deux dernières séries comportent chacune **trois instructions nouvelles**, non reprises du parcours enseigné, et sont les **deux manifestations autonomes obligatoires**.

| Item | Objectif | Critère | Famille | Difficulté | Représentation et cible | Fonction |
|---|---|---|---|---|---|---|
| `q-001` | `obj-1` | `crit-1` | `qc-pri-als-001-ev-01` | initial | oral → ouvrir livre et sens; *open / please* | ancrage |
| `q-002` | `obj-1` | `crit-1` | `qc-pri-als-001-ev-01` | initial | oral → carte dans boîte; *inside* | ancrage |
| `q-003` | `obj-1` | `crit-1` | `qc-pri-als-001-ev-01` | initial | message descriptif → indiquer sens sans action | discriminer message/ordre |
| `q-004` | `obj-1` | `crit-1` | `qc-pri-als-001-ev-01` | initial | oral → montrer boîte; *point to* | discriminer l'action |
| `q-005` | `obj-1` | `crit-1` | `qc-pri-als-001-ev-01` | intermédiaire | oral → gomme sous livre et sens | relation spatiale |
| `q-006` | `obj-1` | `crit-1` | `qc-pri-als-001-ev-01` | intermédiaire | demande polie → déplacer cahier | forme *Could you* |
| `q-007` | `obj-1` | `crit-1` | `qc-pri-als-001-ev-01` | intermédiaire | deux messages oraux → distinguer remerciement/consigne | pragmatique |
| `q-008` | `obj-1` | `crit-1` | `qc-pri-als-001-ev-01` | transfert | oral → enveloppe sur boîte, jeu postal | nouveau contexte |
| `q-009` | `obj-1` | `crit-1` | `qc-pri-als-001-ev-01` | transfert | 3 scripts oraux → 3 actions + 3 sens en classe | **maîtrise A** |
| `q-010` | `obj-1` | `crit-1` | `qc-pri-als-001-ev-01` | transfert | 3 scripts oraux → 3 actions + 3 sens au comptoir fictif | **maîtrise B** |

## Instructions d'administration obligatoires

1. **Avant l'essai**, présenter oralement **les seuls noms des objets** du scénario, sur des objets neutres; vérifier qu'ils sont identifiables sans faire pratiquer les phrases retenues. Pour `q-010`, préenseigner isolément *envelope, stamp, card, box* et la disponibilité de l'objet; ne pas préenseigner **les trois phrases exactes**.
2. Mettre tous les objets à la position initiale décrite dans la banque. Ne pas montrer de transcription anglaise de l'item et ne pas décrire en français la relation ou le verbe ciblé avant l'action.
3. Lire **une fois** chaque phrase orale, à débit clair, avec intonation naturelle sans mimer; au maximum **une répétition verbatim** sur demande. Même procédure pour les deux contextes. Noter lecture supplémentaire imprévue comme déviation.
4. Après **chaque** instruction de q-009/q-010, laisser l'élève agir, puis lui demander « Qu'est-ce que cela voulait dire? » et relever sens/action **avant** de donner la phrase suivante; aucune rétroaction corrective entre les trois.
5. Une fois l'épreuve finie seulement, donner le feedback. Si une série échoue, entraîner des formulations différentes puis construire/revoir **une série équivalente inédite**, ne pas réadministrer indéfiniment la même série en faisant croire qu'elle est nouvelle.

## Barème et règle de décision (rubrique, pas QCM)

Pour **chacune** des trois consignes de chaque preuve : `A=1` si la cible/l'action/le rapport de position sont exacts; `S=1` si l'élève indique le sens en conservant les éléments distinctifs; sinon `0`. `I=0` si aucun indice sémantique n'est fourni (deuxième lecture littérale non considérée comme indice). Une réponse peut être en français, anglais simple, pointage conventionné ou CAA; ne pas noter accent, orthographe ou qualité stylistique. **Série satisfaisante : A=3/3 et S=3/3 avec I=0**. **Maîtrise : séries q-009 et q-010 toutes deux satisfaisantes** dans des contextes différents, sans correction intermédiaire avant la fin de chaque série; noter dates et adaptation. Si besoin, reprendre le cycle avec **deux** nouvelles preuves après remédiation; ne pas moyenner en un score unique. Consulter `GRILLE_MAITRISE.md`.

## Variabilité contrôlée, limites et sécurité

- Items **fixes** (q-001 à q-008) et scénarios **contrôlés mais scripts figés** (q-009, q-010). `seed=null` et `parametres` ne permettent **aucune génération IA libre**. Toute nouvelle phrase constitue un nouvel item à rédiger, contrôler et réviser.
- Autorisé : grands objets équivalents, aide motrice **neutre** sur instructions de l'élève, communication alternative et débit de voix clairement intelligible; **documenter** les modalités. Interdit : traduction préalable de la phrase testée, mots écrits fournis au lieu du son, mime de la solution, indice *under/on*, réorganisation qui révèle l'action.
- Adapter les éléments matériels pour motricité fine, vision et sécurité; proscrire petits timbres véritables susceptibles d'ingestion. Si le stimulus oral n'est pas accessible sans une modalité substitutive non auditive, distinguer cette situation de la mesure d'écoute orale et demander une revue spécialisée — ne pas attribuer silencieusement une même conclusion.
- Respecter accents non natifs (enseignant et élève), variantes intelligibles; absence de besoin d'une prononciation « native »; scripts anglais simples originaux, sans éléments identitaires ou faits personnels.

## Assurance qualité

Les corrigés des dix items sont des décisions pédagogiques **déterminées et contrôlables par lecteur humain** (action cible et paraphrase). Ils ne sont pas mathématiques et n'ont pas de « solveur » prétendu; revue d'un spécialiste ESL, essai en situation, fiabilité intercorrecteurs et adéquation des accommodations demeurent requis avant usage sommatif. Le statut de tous les items reste `a_revoir`.
