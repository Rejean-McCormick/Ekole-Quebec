# Plan d'évaluation — `qc-pri-da-003-ev-01` (v1.2)

**Identifiants stables pour CHAQUE item :** `kristal_id=qc-pri-da-003` ; `objectif_id=obj-1` — « Composer une phrase dansée structurée avec un début et une fin. » ; `critere_id=crit-1` — « Présenter une phrase chorégraphique originale mémorisable. » ; `family_id=qc-pri-da-003-ev-01`. **Type de famille :** `observation_ou_production`. Les `q-001` et `q-002` servent uniquement au diagnostic des ressources préalables associées à cet objectif : ils **n'attestent pas** directement la preuve finale.

## Règles générales

- **Représentations :** observation gestuelle accessible, plan de jalons, oral/dictée/pointage et deux passages d'une composition; une réponse écrite seule qui ne rend pas la composition observable ne remplace pas la performance, mais peut documenter choix et structure.
- **Différenciation :** tempo, amplitude, appui stable, position assise ou debout, geste de main/bras/regard et support de communication choisis; pas de mouvement impossible imposé.
- **Grille E1–E5 :** début/fin; motif/reprise; transition/structure; mémoire/reproductibilité; intention/initiative. Ancrages 0/1/2 dans `GRILLE_MAITRISE.md`. Pour `q-011` et `q-012`, E1–E4 doivent chacun être à 2 dans **les deux** contextes, E5 au moins à 1 avec choix autonome documenté.
- **Variabilité :** les scénarios, textes, objectifs, limites de sécurité et grilles sont fixes; aucune permutation improvisée, aucune génération IA libre. Les mouvements eux-mêmes restent originaux et libres dans ces limites. `mode=fixe`, `seed=null`, `parametres=null` pour les 12 items.
- **Pondération :** *aucune somme ou moyenne ne décide seule de la maîtrise*. Diagnostics non notés; guidés et autonomes servent la rétroaction; preuve A et preuve B sont toutes deux requises et chacune soumise aux seuils par dimension.

## Table de couverture — chaque ligne renvoie à `obj-1` / `crit-1` / `qc-pri-da-003-ev-01`

| Item | Phase | Difficulté | Représentation | Critères principalement observés | Variabilité permise (dans les limites ci-dessus) |
|---|---|---|---|---|---|
| `q-001` | Diagnostic du préalable (non sommative) | initial | Geste + comparaison orale/gestuelle | Deux variantes intentionnelles du même geste sont distinguables., Le paramètre temporel changé est nommé ou indiqué., Mouvement choisi confortable, sans contrainte d’amplitude. | Geste/tempo/adaptation de communication |
| `q-002` | Diagnostic du préalable (non sommative) | initial | Geste + direction indiquée | Deux orientations volontaires distinctes sont observées ou communiquées., La différence spatiale est repérée par la personne., Modalité motrice sécuritaire et adaptée. | Geste/tempo/adaptation de communication |
| `q-003` | Accompagnée (formative) | initial | Cartes D/M/M/F + mouvement | E1 , E2 , E4  | Gestes/personnalisation/adaptations sûres, scénario fixe |
| `q-004` | Accompagnée (formative) | initial | Mouvement + explication transition | E2 , E3 , E1  | Gestes/personnalisation/adaptations sûres, scénario fixe |
| `q-005` | Accompagnée (formative) | intermediaire | Mouvement deux fois + questions | E1 , E2 , E3  | Gestes/personnalisation/adaptations sûres, scénario fixe |
| `q-006` | Autonome (formative) | intermediaire | Mouvement deux fois + carte personnelle | E1 , E2 , E4  | Gestes/personnalisation/adaptations sûres, scénario fixe |
| `q-007` | Autonome (formative) | intermediaire | Mouvement + justification intention | E1 , E2 , E3  | Gestes/personnalisation/adaptations sûres, scénario fixe |
| `q-008` | Autonome (formative) | intermediaire | Mouvement + explication liaison | E1 , E2 , E3  | Gestes/personnalisation/adaptations sûres, scénario fixe |
| `q-009` | Autonome (formative) | intermediaire | Mouvement adapté + comparaison des jalons | E1 , E2 , E3  | Gestes/personnalisation/adaptations sûres, scénario fixe |
| `q-010` | Transfert (formatif) | transfert | Carte A–détour–B + danse | E1 , E2 , E3  | Gestes/personnalisation/adaptations sûres, scénario fixe |
| `q-011` | Preuve A de maîtrise | transfert | Jardin imaginaire + danse 2 fois | E1, E2, E3 | Gestes/personnalisation/adaptations sûres, scénario fixe |
| `q-012` | Preuve B de maîtrise | transfert | Formes imaginaires + danse 2 fois | E1, E2, E3 | Gestes/personnalisation/adaptations sûres, scénario fixe |

## Couverture conceptuelle

- **Motif et répétition :** `q-003`, `q-005` à `q-012` avec reprise d'une cellule reconnaissable.
- **Transition :** `q-004`, `q-005`, `q-007` à `q-012` avec liaison choisie.
- **Structure, entrée, fin et mémoire :** `q-003` à `q-012` en difficulté croissante.
- **Préalable espace/temps/énergie :** `q-001`, `q-002`; attestation d'équivalence possible à `qc-pri-da-002`.
- **Intentions et autonomie :** `q-005` à `q-012`, particulièrement les deux preuves.
- **Deux manifestations contextuelles distinctes :** `q-011` « jardin imaginaire », `q-012` « atelier de formes », observations séparées.

## Critères concrets et réponse attendue

Chaque item de `BANQUE_ITEMS.json` conserve : consigne complète, stimulus fixe, production observable acceptée, critères explicites, rubrique, rétroaction corrective, limites de variation et statut `a_revoir`. Pour une performance artistique, **il n'existe pas une chorégraphie unique « correcte »** : le « corrigé » est la combinaison de critères observables, exemples non contraignants et ancrages publiés dans la grille.

## Sécurité, accessibilité, droits et biais

- Déplacer les obstacles; pas d'obligation de saut, contact, déplacement, rotation, musique, costume ou vidéo. Si inconfort, arrêter et offrir une modalité équivalente sans inférer de déficience.
- Une aide d'accès (interprétation, lecture des consignes, cartes, aménagement postural) ne prescrit jamais le motif ou la liaison; consigner la distinction.
- Évaluer la composition et les décisions de l'élève, **pas** apparence, fluidité « idéale », vitesse, portée, genre ou correspondance à une esthétique personnelle.
- Stimuli originaux et scénarios fictifs sans musique, photo ni chorégraphie tierce; ne pas filmer sans cadre de consentement applicable.
- Une revue humaine demeure requise : pertinence des tâches en contexte réel, biais d'observation, sécurité locale, calibration des niveaux, clarté des consignes et durée. Aucun examen certifié.
