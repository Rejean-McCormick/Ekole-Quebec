# Journal de validation technique — `qc-pri-eps-006`

**Périmètre :** livraison delta de 14 fichiers `kristals/qc-pri-eps-006/` pour le workspace existant v1.2. **Statut :** documents rédigés, items `a_revoir`, revue pédagogique et motrice humaine nécessaire. Ce rapport de validation technique consigne des tests automatisés exécutés au moment de la production du ZIP; il ne qualifie pas les jeux pour une réalisation autonome des élèves.

## Contrôles réellement exécutés

- **7782 assertions préarchivage exécutées et réussies** par le script local `verify_eps006.py`, sans échec.
- Fichiers : 14 chemins exacts, tous existants et non vides; seuls deux chemins source remplacés.
- YAML de `PARCOURS.md` : frontmatter **identique au texte original** et métadonnées analysées; 12 titres numérotés présents.
- JSON : les 3 documents JSON parsés; champs natifs de contrat préservés; famille enrichie sans nouvelle famille ni perte d'ID.
- Banque : 10 items uniques numérotés, complets, reliés à `obj-1`, `crit-1`, `qc-pri-eps-006-ev-01`, statut `a_revoir` et corrigés observationnels substantiels.
- Deux manifestations autonomes distinctes `q-009` et `q-010` avec limites fixées, critères R1–R5 et corrigés conditionnels contrôlés : des choix ouverts explicites, non une réponse esthétique unique.
- Safety/access : contrôle **textuel** des règles STOP/sans contact/adaptations dans les six modules, grille et plan. Aucune sécurité réelle ou équité n'a été évaluée.
- Fusion simulée avec **7322 fichiers source du workspace maître** : **2 remplacés**, **12 ajoutés**, **7320 autres fichiers inchangés après comparaison de leurs SHA-256**; le registre, la gouvernance, le canon et les autres Kristals n'ont pas été modifiés.

## Conformité du périmètre livré

- 2 remplacements exclusivement : `authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json` ; **12 ajouts** dans les sous-répertoires `contenu`, `evaluation`, `sources`, `livraison`.
- Aucun dossier `Frames_202.../` à la racine ZIP, ni `AGENTS.md`, `kristal.workspace.json`, `ALIGNEMENT.md`, fichier du graphe ou de la gouvernance; aucune modification du canon, state, docs, runtime ou d'un autre Kristal.
- YAML d'identité conservé **à l'octet près** de la source pour le frontmatter; statut natif `en_rédaction` demeure intact, ce qui est compatible avec la nécessité d'une revue avant qualification.
- Dix items fixes, non certifiés; pas de générateur libre ni d'algorithme de correction imaginaire. Les preuves 009 et 010 sont indépendantes, dans des jeux différents et à décisions concrètes vérifiables.

## Limites non résolues

1. **Sécurité :** tests documentaires seulement; aucune inspection des installations réelles, du matériel fourni ni des risques individuels. Chaque activité doit être approuvée et surveillée sur place par une personne compétente, avec STOP et règles institutionnelles.
2. **Accessibilité :** conformité textuelle aux adaptations vérifiée; besoin individuel, participation équivalente et acceptabilité d'un exécutant non décideur à évaluer humainement.
3. **Qualité pédagogique :** jeux, barème et seuils non testés auprès d'élèves; fidélité et équité de la cotation interévaluateurs non établies.
4. **Droits/provenance :** pas de contenu tiers sous licence dans le ZIP, mais contrôle juridique approfondi non effectué; autorisations locales pour images et données nécessaires seulement si une école décide d'en collecter.
5. **Harmonisation réglementaire :** aucune conformité détaillée au PFEQ, aucune certification ni examen homologué revendiqué; les références ont rôle descriptif.

## Actions et propositions hors delta (aucun changement central)

- Proposer ultérieurement dans le schéma de famille des champs standardisés « safety_stop », « physical_access_options » et « independent_decision_evidence » pour faciliter l'audit EPS, **sans modifier la norme dans le présent lot**.
- Organiser une revue motrice, une revue d'accessibilité et une calibration humaine des seuils R1–R5 à partir d'observations d'essai avant toute publication qualifiée.
- Vérifier institutionnellement matériel, consentement, supervision, nombre d'élèves, accessibilité de chaque plateau et éventuels risques de frustration dans des groupes réels.
