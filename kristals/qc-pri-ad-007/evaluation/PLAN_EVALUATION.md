# Plan d'évaluation — `qc-pri-ad-007-ev-01`

**`obj-1` (immuable) :** Décrire ce qui se passe dans une représentation théâtrale. **`crit-1` (immuable) :** Noter des éléments observables d’une scène sans juger les personnes. **Domaine :** Art dramatique. **Mode v1.2 :** observation_ou_production avec tâches fixes et quatre catalogues de variantes contrôlées.

## Couverture et attribution des items

| Item | Difficulté | Représentation / situation | Preuve précise | Référence constante |
|---|---|---|---|---|
| `qc-pri-ad-007-q-001` | initial | scène jouée / gestes et lieu | Réponse factuelle + justification; jugement interdit | `obj-1` / `crit-1` / `qc-pri-ad-007-ev-01` |
| `qc-pri-ad-007-q-002` | initial | classement fait–inférence–jugement | Réponse factuelle + justification; jugement interdit | `obj-1` / `crit-1` / `qc-pri-ad-007-ev-01` |
| `qc-pri-ad-007-q-003` | intermediaire | plateau et déplacement (catalogue A/B) | Réponse factuelle + justification; jugement interdit | `obj-1` / `crit-1` / `qc-pri-ad-007-ev-01` |
| `qc-pri-ad-007-q-004` | intermediaire | voix / gestes / position (A/B) | Réponse factuelle + justification; jugement interdit | `obj-1` / `crit-1` / `qc-pri-ad-007-ev-01` |
| `qc-pri-ad-007-q-005` | intermediaire | chronologie en scène (A/B) | Réponse factuelle + justification; jugement interdit | `obj-1` / `crit-1` / `qc-pri-ad-007-ev-01` |
| `qc-pri-ad-007-q-006` | transfert | théâtre d’objets ou d’ombres (A/B) | Réponse factuelle + justification; jugement interdit | `obj-1` / `crit-1` / `qc-pri-ad-007-ev-01` |
| `qc-pri-ad-007-q-007` | intermediaire | scène d’action et correction neutre | Réponse factuelle + justification; jugement interdit | `obj-1` / `crit-1` / `qc-pri-ad-007-ev-01` |
| `qc-pri-ad-007-q-008` | transfert | théâtre d’objets fixe | Réponse factuelle + justification; jugement interdit | `obj-1` / `crit-1` / `qc-pri-ad-007-ev-01` |
| `qc-pri-ad-007-q-009` | transfert | **P1** — scène jouée inédite | Quatre observations + deux justifications, sans indices | `obj-1` / `crit-1` / `qc-pri-ad-007-ev-01` |
| `qc-pri-ad-007-q-010` | transfert | **P2** — théâtre d’ombres inédit | Quatre observations + deux justifications, sans indices | `obj-1` / `crit-1` / `qc-pri-ad-007-ev-01` |


## Procédure d'administration
1. Présenter la consigne et le stimulus à chaque élève sous une forme accessible (texte, lecture par l'adulte, gros caractères, tactile simplifié, synthèse vocale ou traduction de modalité non linguistique) sans en modifier les indices. Le texte **est** la scène observable et contient tous les éléments nécessaires. Aucun rôle joué par un enfant n'est obligatoire.
2. Items 001–008 : usage formatif; noter les corrections et réactions, puis donner du feedback descriptif. Certains items portent sur un sous-aspect et **ne prouvent pas seuls** la maîtrise.
3. Pour `q-003` à `q-006` : seule variante A ou B prédéfinie par `(seed + index_version) modulo 2` (A=0, B=1), `index_version` entier ≥0 consigné avant passation; afficher simultanément le `stimulus` et son `reponse_attendue` correspondants dans le catalogue, **jamais le corrigé d'une autre variante**. Graines et exemples sont fixés dans le JSON. Les variantes ne sont ni des productions IA libres ni des permutations automatiques de faits.
4. Deux preuves finales P1 `q-009` et P2 `q-010` dans des **contextes distincts et non utilisés au modelage**. Le professeur lit/donne le stimulus, n'indique pas les éléments à noter au-delà de la consigne standard et n'apporte aucune correction pendant la production. Il accepte les adaptations convenues d'accès.
5. Sur chaque preuve : quatre notes de faits; couverture **jeu, espace et action**; chronologie cohérente; deux notes justifiées en citant leurs indices; aucune qualification du talent, de la personnalité ou de l'apparence. Une formulation alternative est valide si elle renvoie à la scène; l'orthographe n'est pas mesurée ici.

## Rubrique, difficulté et décision
- Barème descriptif à quatre dimensions **E** exactitude (3/4 notes justes, 0 fait inventé dans les notes comptées), **C** couverture jeu/espace/action (chaque composante présente), **N** neutralité (aucun jugement de personnes, y compris sous-entendu), **O** ordre + justification (chronologie juste et deux indices vérifiables). Barème détaillé `evaluation/GRILLE_MAITRISE.md`.
- **Initial** = relever 1–3 éléments identifiables; **intermédiaire** = combiner plusieurs dimensions ou trier des phrases; **transfert** = description complète d'une forme différente sans guidage. La difficulté indique la mobilisation demandée, pas une hiérarchie de genres théâtraux.
- **Maîtrise = P1 et P2 satisfaisantes séparément**, sans indice individualisé et avec adaptation documentée; une moyenne de points ne compense pas une épreuve non démontrée.
- Réponses ouvertes : la `reponse_attendue` propose un exemple étayé, **pas** une phrase obligatoire. Les corrigés sont des critères textuels contrôlables; pas de jugement esthétique ou de conformité à une opinion.

## Variabilité, sécurité, biais et accès
- Autorisé : paraphrase fidèle, ordre des quatre notes libre, oral transcrit, pictogrammes annotés/maquette décrite, police agrandie, lecture du stimulus, modalités de communication assistée; les **mêmes indices doivent être fournis**.
- Interdit : inventer des intentions personnelles, imposer une émotion unique, créer de nouveaux scénarios au hasard, filmer obligatoirement, évaluer la diction/écriture de l'élève ou la qualité artistique d'un camarade.
- Consentement et protection : aucune captation d'élèves requise; préférer les vignettes fictives originales. Si un établissement utilise des vidéos externes, vérifier licences et autorisations hors de ce produit; elles ne font pas partie du stimulus figé.
- Limite : grilles rédigées mais ni calibrées par plusieurs correcteurs ni essayées avec enfants. Toutes les entrées sont `a_revoir` jusqu'à validation humaine.
