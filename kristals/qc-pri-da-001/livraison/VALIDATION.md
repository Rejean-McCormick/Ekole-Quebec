# Validation et limites — `qc-pri-da-001`

Rapport de contrôles techniques du delta v1.2 — établi le 8 octobre 2026 à partir de la source locale. **Statut :** rédaction complète; revue pédagogique humaine requise; aucune certification, homologation, publication ou validation réelle de sécurité d'exécution.

## Contenu et périmètre

- 14 fichiers du delta `kristals/qc-pri-da-001/`, dont 2 remplacements `authoring/` et 12 nouveaux fichiers.
- Aucun changement dans `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `registry/`, `governance/`, `canon/`, `state/`, `runtime/`, `docs/`, ni dans un autre Kristal.
- Objectif immuable, preuve, concepts, identifiant de famille, titres et discipline préservés. Les textes et rubriques ont été ajoutés sous leur seul propriétaire local.

## Vérifications effectuées

- **529 assertions préarchivage ont réussi** dans un script Python exécuté (vérifications de fichiers, de champs YAML/JSON, des invariants, de la couverture des 10 items, de la diversité des épreuves 009 et 010, des rubriques, références et exigences de sécurité/accessibilité). Aucune assertion préarchivage n'a échoué.
- **YAML vérifié :** même jeu de clés de frontmatter et mêmes invariants canoniques que la source; 12 sections numérotées présentes exactement une fois.
- **JSON vérifiés :** `CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json` et `MANIFEST.json` parsés; famille initiale conservée et enrichie. Les items 001–010 sont uniques, complets, en statut `a_revoir` et liés à `obj-1`, `crit-1`, `qc-pri-da-001-ev-01`.
- **Corrigés :** les 10 productions attendues et leurs critères ont été contrôlés par présence et cohérence formelle (pas d'oracle mathématique ni de génération IA libre). Leur adéquation réelle à chaque élève reste à revoir humainement.
- **Fusion simulée :** les deux anciens fichiers `authoring/` seulement ont été remplacés, et les 12 autres sont nouveaux; tous les autres fichiers sources du dossier sont demeurés identiques par SHA-256. Aucun changement hors du Kristal n'est présent dans le delta.
- **Provenance et droits :** référence externe CAST vérifiée, pas de musique, d'image, de vidéo ni de chorégraphie tierce intégrée; aucune vérification juridique exhaustive entreprise.
- **Accessibilité :** présence documentée d'accommodements sans imposer d'amplitude ni de posture et d'une clause de décision humaine en cas d'absence de preuve corporelle équivalente. Test matériel réel non effectué.
- **Test ZIP :** contrôle d'intégrité et des 14 chemins effectué après archivage (voir résultat de génération).

## Limites non résolues

- Aucun essai en classe, aucune observation d'apprenants ni mesure de fidélité interévaluateurs.
- La sécurité du contexte physique, les adaptations individuelles et les aménagements selon les besoins spécifiques ne peuvent être certifiés par des tests documentaires. Supervision et jugement professionnel requis.
- Les seuils de la grille sont des décisions éditoriales non étalonnées; acceptabilité et équité à évaluer.
- Aucune projection ni qualification du canon v9; aucune conformité PFEQ revendiquée.

## Revue humaine avant usage décisionnel

1. **Danse et motricité :** s'assurer que chaque geste, amplitude et consigne est sûr pour le contexte et que des variantes adaptées sont réalisables.
2. **Pédagogie et accessibilité :** observer la clarté des consignes, les conditions d'autonomie et la concordance des critères pour différentes mobilités et modes de communication.
3. **Évaluation :** réviser les 10 rubriques, le caractère distinct des épreuves A/B et la stabilité de la cotation; essayer avec plusieurs évaluateurs.
4. **Droits et protection :** confirmer les règles locales de consentement et de conservation des traces; aucune musique ni vidéo n'est nécessaire ici.

## Propositions (sans modifier les bases centrales)

- Un futur champ standardisé de preuve motrice (`evidence_mode`, `accommodations_approved`) pourrait décrire de manière stable les aménagements non directifs; à proposer au mainteneur du schéma, pas à ajouter au registre.
- Une annexe commune de consentement et de sécurité pour les disciplines artistiques motrices serait utile; aucune modification centrale incluse.
- Proposer une procédure d'étalonnage humain interévaluateurs sur les rubriques M1–M5 avant toute prétention sommative.
