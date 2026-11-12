# Journal de validation — qc-pri-fr-015 / v1.2

**Statut livré :** delta technique contrôlé localement; revue linguistique/pédagogique humaine **à réaliser**; banque d'items `a_revoir`. Ni cours publié, ni canon v9, ni conformité au PFEQ. Les vérifications ci-dessous décrivent uniquement les actions exécutées sur les fichiers de cette livraison.

## Contrôles effectivement exécutés

- **PASS** — Front matter YAML préservé octet à octet
- **PASS** — Les 12 sections conservées
- **PASS** — Front matter YAML parsable
- **PASS** — Champ natif conservé format
- **PASS** — Champ natif conservé kristal_id
- **PASS** — Champ natif conservé objectif_id
- **PASS** — Champ natif conservé objectif_observable
- **PASS** — Champ natif conservé concepts
- **PASS** — Champ natif conservé preuve_attendue
- **PASS** — Champ natif conservé prerequis_bloquants
- **PASS** — Champ natif conservé ordre_conseille
- **PASS** — Familles d’origine et sous-champs préservés
- **PASS** — Champ natif conservé statut
- **PASS** — Champ natif conservé referentiel_technique
- **PASS** — Contrat générateur champs complets
- **PASS** — Données d’identité et graphe
- **PASS** — Liens du graphe conseillés exacts
- **PASS** — Banque format identité
- **PASS** — 12 items et IDs uniques/séquentiels
- **PASS** — Schéma requis rempli chaque item
- **PASS** — IDs familiaux/objectif/critère constants
- **PASS** — Statuts et modes défendables
- **PASS** — Deux contextes de preuves distinctes
- **PASS** — Variants chacun au moins 2 sauf ancrage
- **PASS** — 12 corrigés, 23 formulations / contrôle de tous les groupes et prédicats. []
- **PASS** — 14 fichiers existent, aucun vide
- **PASS** — 3 JSON stricts parsables
- **PASS** — Manifeste exactement 14 chemins relatifs complets
- **PASS** — Liens relatifs internes existants. []
- **PASS** — Aucune donnée personnelle ou média tiers intégrés

## Contrôles de livraison et de droits

- **Provenance/licences :** `sources/REFERENCES_CONTENU.md` distingue les pages web consultées (Alloprof, OQLF), les sources internes, la conception déduite et les énoncés originaux. Contrôle manuel : aucune copie d'image, d'extrait tiers ou de document de gouvernance dans le delta. **Limite :** pas d'expertise juridique indépendante sur les droits d'auteur.
- **Accessibilité/sécurité :** contrôle éditorial effectué : supports texte/manipulables, lecture neutre ou scripteur sans aide syntaxique, aucun test de l'accent ou de la rapidité; scénarios fictifs, pas de données personnelles requises. **Limite :** aucune passation ou mesure d'accessibilité auprès d'élèves.
- **Liens :** liens relatifs internes contrôlés automatiquement; liens web vers OQLF et Alloprof consultés pour des règles précises, sans garantie de disponibilité permanente.
- **Corrigés :** contrôle algorithmique des groupes utilisés et du maintien sujet–verbe–objet pour les 12 items; examen éditorial des variantes et de la distinction CP/complément du verbe. **Limite :** absence de double correction humaine indépendante et de revue exhaustive des autres syntaxes grammaticales admissibles.

## Points à revoir avant qualification

1. Faire une relecture par une personne compétente en linguistique du français québécois : nuances sur déplacements possibles, pluriels, acceptabilité de chaque formulation et tolérances de ponctuation.
2. Essayer la banque, les consignes et la grille avec des élèves représentatifs; relever compréhension lexicale, durée, biais éventuels, variabilité des justifications et taux de désaccord entre correcteurs.
3. Vérifier dans le moteur cible la prise en charge des champs supplémentaires de `CONTRAT_PEDAGOGIQUE.json` et `BANQUE_ITEMS.json`, l'affichage de la dictée verbatim et la conservation hors canon des réponses.
4. Ne déclarer `validation_status` « validé » et le cours « terminé » qu'après revue humaine, corrections et décision formelle. Aucun test de build-v9, check-ai, publication réseau ou activation n'a été exécuté.

## Propositions de changement central (NON appliquées)

- Ajouter au contrat général un champ optionnel `preuve_contextuelle` pour relier deux séances indépendantes sans toucher au graphe.
- Prévoir un type de rubrique explicitement linguistique pour l'acceptation des variantes syntaxiques et la séparation graphie/syntaxe.
- Ajouter au moteur un journal des aides autorisées par item, conservé dans les données d'apprentissage et non dans le canon.

**Fichiers d'autorité non modifiés :** `governance/`, `registry/`, `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `docs/`, `canon/`, `state/`, `runtime/` et autres Kristals.

## Inspections de l’archive ZIP après création

- **PASS** — Premier chemin est sous racine attendue
- **PASS** — Exactly 14 entries, expected paths in expected order
- **PASS** — No zip slip / forbidden top-level
- **PASS** — All 14 nonempty
- **PASS** — Archive integrity (CRC testzip)
- **PASS** — JSON strict in ZIP
