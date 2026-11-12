# VALIDATION — qc-pri-ilss-009 (livraison v1.2)

## Nature et périmètre

Delta limité à `kristals/qc-pri-ilss-009/`; **2 remplacements natifs** (`authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`) et **12 fichiers nouveaux**. Aucun changement de `AGENTS.md`, `kristal.workspace.json`, `ALIGNEMENT.md`, des registres, de la gouvernance ou d'un autre Kristal. `base_version` : v1.2. Aucun processus canon, build v9, qualification ou publication n'a été lancé.

## Contrôles effectivement réalisés (script local `ilss009package.py`)

- **173 assertions pré-emballage réussies**, qui couvrent la conservation valeur par valeur de tous les champs YAML/JSON natifs, les 12 sections, l'objectif et la preuve inchangés, `requires=[]`, l'absence d'arête sortante bloquante dans le graphe, la présence des champs de famille attendus, les 12 items (ID et modes), les corrigés non vides, les variantes fermées A/B et les exemples de seeds `31010`/`31013`, deux contextes, 2 diagnostics, 3 exercices guidés, 4 pratiques autonomes, 2 transferts, accessibilité et références/droits. **Une assertion de présence n'est pas une validation experte de qualité.**
- **10 assertions d'emballage exécutées avec succès** : premier chemin correctement préfixé, ordre/manifeste exact, 14 fichiers non vides, absence de parent/chemin absolu/traversée, ZIP CRC, JSON internes parsables et absence de dossier protégé. Le ZIP final a été soumis à ce contrôle après l'écriture de ce rapport.
- **Corps des corrigés** : pour les 10 items fixes, contrôle non vide, alignement sur les cas présents et critères explicites par inspection de contenu; pour les 2 scénarios contrôlés, tous les seeds échantillonnés et les exemples A/B sont contrôlés par comparaison déterministe aux variantes stockées. Les réponses sont des rubriques d'observation, non des solutions calculées; **aucun étalonnage inter-évaluateurs ou test avec des enfants**.

## Revue humaine requise avant usage et publication

1. **Pédagogie/ILSS :** vérification par une personne connaissant l'intégration linguistique des élèves plurilingues et les soutiens accessibles, charge de lecture, adéquation à l'âge, vocabulaire et absence de stéréotypes.
2. **Clarté locale et sécurité :** confirmer que les supports de l'école fictive sont clairement présentés comme fictifs; adapter les pratiques réelles avec les responsables, notamment la demande d'aide urgente (adulte immédiatement).
3. **Évaluation :** juger de la validité des rubriques R/S/A/C et du seuil interne retenu (aucune mesure psychométrique); former les observateurs et tester les variantes A/B sans indices cognitifs; examiner équivalence des modes de réponse.
4. **Droits/données :** confirmer le régime d'exploitation du workspace maître et tout matériel visuel/audio ajouté ultérieurement; aucune autorisation de réutilisation des textes externes n'est postulée; ne pas collecter de données personnelles non pertinentes.
5. **Liens :** disponibilité future des pages externes, présence des fichiers du workspace et cohérence avec toute modification ultérieure de la gouvernance.

## Limites non résolues

- Aucun entretien/essai d'élève, aucune observation réelle et aucune validation humaine indépendante. Aucun statut de cours terminé, publié, certifié, homologué ou aligné à la PDA/PFEQ n'est revendiqué.
- Les règles et services scolaires varient selon le milieu; seules les consignes *énoncées dans les scénarios* déterminent les corrigés. L'apprentissage ne doit pas servir de test de conformité culturelle.
- Les validations automatisées de contenu repèrent structure, présence, références et déterminisme; elles ne prouvent pas l'absence de biais, une authenticité locale ni une bonne interprétation de productions ambiguës.

## Propositions d'évolution (non appliquées)

- Ajouter dans une version **proposée**, sans modifier la base centrale, un champ standard `modalite_reponse_equivalente`, un indicateur distinct « indice cognitif vs aide d'accessibilité », et une référence versionnée aux cartes locales fictives.
- Documenter à terme un protocole de revue inter-évaluateurs et un registre de vérification des droits pour ressources audiovisuelles.

**Statut :** techniquement vérifié sur son périmètre; **revue humaine requise**. Aucun changement structurel central exécuté.
