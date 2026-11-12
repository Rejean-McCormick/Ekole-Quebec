# Validation et limites de livraison — `qc-pri-als-010`

**Statut :** rédaction documentaire complète, `a_revoir`, aucune certification, homologation ou essai auprès d'élèves. Les résultats ci-dessous sont issus du script Python de validation réellement exécuté avant la création du ZIP.

## Étendue

- Delta de 14 fichiers exactement sous `kristals/qc-pri-als-010/` : deux remplacements `authoring/`, douze nouveaux livrables; aucun autre Kristal ni base centrale.
- Identité officielle de la discipline préservée, ainsi que `obj-1`, `crit-1`, `qc-pri-als-010-ev-01`, lien bloquant `qc-pri-als-002` (diagnostic d'équivalence possible) et recommandation non bloquante `qc-pri-als-007`.
- Dix items de production contextualisée avec corrigés d'ancrage linguistique et grilles, dont deux preuves différentes : invitation et note d'information.

## Contrôles réalisés

- **545 assertions préarchivage réussies :** présence des 14 fichiers, non-vacuité, YAML natif et 12 sections, JSON strict, champs/identifiants immuables, liens du graphe, 10 items complets et uniques, deux preuves écrites autonomes et corrigés de quatre phrases, références, accessibilité et droits.
- **Exemples de maîtrise :** les textes d'ancrage de q-009 et q-010 ont été divisés en phrases pour vérifier **exactement quatre** unités par exemple; adéquation du contenu et variantes libres restent sujettes à revue humaine.
- **Fusion réellement simulée en mémoire :** remplacement des seuls fichiers `PARCOURS.md` et `CONTRAT_PEDAGOGIQUE.json`, ajout des 12 autres; autres fichiers originaux du dossier vérifiés identiques par SHA-256.
- **Intégrité ZIP :** contrôle des chemins, du manifeste, de trois JSON relus et CRC exécuté après compression (résultat d'archivage ci-dessous).

## Limites non résolues et revue humaine

1. Relecture experte de l'anglais en contexte québécois, pertinence des stimuli, fidélité des données et caractère naturel des tournures modèles.
2. Revue de la grille 0–2, des seuils proposés et de la constance entre évaluateurs; la variation libre des réponses n'est pas mesurable par comparaison de chaînes.
3. Accessibilité de la saisie écrite, support oral ou pictographique des consignes, conditions d'autonomie; l'équivalence d'une dictée à scribe doit être tranchée humainement.
4. Absence d'essais en classe, de tests de réussite d'apprenants et de validation d'impact pédagogique.
5. Les droits des œuvres futures (illustrations, textes modèles externes, voix ou photographie) nécessiteraient une vérification spécifique; aucun de ces éléments n'est inclus.

## Propositions de structure, **sans changement du workspace maître**

- Définir à l'avenir une structure de trace `production_trace` et `assistance_observee` pour l'écriture sans imposer un canal moteur unique.
- Documenter une procédure humaine de validation des réponses alternatives à la phrase d'ancrage (sens, destinataire, fidélité et erreurs mineures).
- Prévoir des exemples d'aménagements évaluatifs approuvés localement, sans modifier les champs canoniques ou les relations du graphe.
