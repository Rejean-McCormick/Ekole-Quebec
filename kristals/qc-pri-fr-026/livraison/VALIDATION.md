# Validation de livraison — `qc-pri-fr-026` / delta v1.2

**Base inspectée :** l'archive effectivement disponible se nomme `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`, et **contient** le workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, ses fichiers normatifs, son registre et les fichiers initiaux de `qc-pri-fr-026`. Il n'a pas fallu créer de métadonnées de remplacement.  
**Cible à fusionner :** `kristals/qc-pri-fr-026/` à la racine **interne** du ZIP livré; extraction depuis la racine du workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`.

## Contrôles techniques effectivement réalisés

À la préparation de cette livraison, les contrôles ont été exécutés par scripts locaux Python (`json`, `zipfile`, comparaisons de chaînes/champs; parsing YAML via PyYAML). Après génération de `VALIDATION.md`, les vérifications de présence et liens ont été relancées.

| Contrôle | Résultat attendu et constat |
|---|---|
| Composition | **14 fichiers non vides**; chemins identiques à `MANIFEST.json`, tous préfixés `kristals/qc-pri-fr-026/`; aucun parent `Frames_.../`, `lot/`, `livraison/` global ou fichier hors cible. |
| Sécurité des chemins | Aucun chemin absolu, segment `..`, `.` ou segment vide; premier élément du ZIP sous `kristals/qc-pri-fr-026/`. |
| Formats structurés | JSON strict parsé pour `CONTRAT_PEDAGOGIQUE.json`, `BANQUE_ITEMS.json`, `MANIFEST.json`; front matter YAML lu par analyseur; **12** sections numérotées correctement. |
| Conservation d'identité | Comparaison de l'original : ID, format natif, `obj-1`, texte d'objectif, preuve, concepts, préalable `qc-pri-fr-025`, ordre vide, famille, type et anciennes clés conservés. Aucun changement au graphe central. |
| Contrat de génération | **13 champs** minimaux de la famille présents, sans effacer les anciens champs `generation`, `rubric_dimensions` ni `review_status`. |
| Banque | **13 items** `q-001` à `q-013`, numérotation contiguë sans doublon, chacun avec énoncé, stimulus, réponse/modèle, critères, rétroaction, difficulté, représentation et statut `a_revoir`; ID `obj-1`, `crit-1` et famille cohérents. |
| Diversité des preuves | 2 diagnostics, 3 tâches guidées, 4 pratiques indépendantes, 2 prestations M1/M2 autonomes **en contextes distincts** avec deux questions chacune, 2 transferts. |
| Corrigés et rubriques | Contrôle de **complétude et cohérence rédactionnelle** des réponses; `q-003 = C–D–A–B`, `q-004 = R2 + E2`; pour les performances, modèles **non exclusifs** et grilles plutôt que corrigés textuels uniques. Aucune validation psychométrique ni essai réel effectué. |
| Variations | Modes seulement `fixe` et `scenario_controle`; **aucune génération paramétrique** ni tirage IA libre; absence de seeds opérationnels indiquée (`null`). |
| Droits et accessibilité | Inventaire de références internes et externes, limites des droits, provenance des textes originaux; prise en charge documentaire de la sortie vocale, des adaptations d'accès, de la confidentialité et du non-jugement des opinions/accent. |
| Liens | Liens relatifs vers les pièces nouvelles contrôlés; référence au préalable retrouvée dans le registre source; aucune modification d'un autre Kristal. |
| Intégrité ZIP | Entrées du ZIP lues et comparées à la liste exacte du manifeste; aucune archive globale ni fichier supplémentaire. |

**Portée des contrôles :** les contrôles de complétude, chemins et schémas sont automatisés; l'exactitude pragmatique d'une prestation orale libre demeure un **jugement sur grille**. Les exemples de réponses sont des références plausibles pour les scénarios fictifs, pas des réponses verbatim obligatoires. Les vérifications automatisées n'attestent ni qualité d'enseignement en classe ni fidélité inter-correcteurs.

## Limites non résolues et points de revue humaine

1. **Révision pédagogique humaine indispensable :** naturel de la langue québécoise, caractère inclusif et compréhensible des scénarios, faisabilité des exigences aux différents profils d'apprenants, calibrage des niveaux 0/1/2; observation inter-évaluateurs en classe.
2. **Évaluation accessible :** valider les aides de communication à sortie vocale, l'interprétation de l'« audible », les adaptations de temps et de consigne, ainsi que les modalités de réponse pour les élèves ayant une impossibilité de production vocale; documenter toute équivalence approuvée individuellement.
3. **Difficulté et maîtrise :** vérifier empiriquement que M1 et M2 sont comparables sans être redondantes. La règle de 2/2 dans cinq dimensions est **une convention interne**, à étalonner; ne pas décider d'une maîtrise sans deux performances autonomes observées.
4. **Biais, droits et confidentialité :** revue de neutralité culturelle, demandes d'enregistrement, traitement des traces, règles de conservation et autorisations des ressources externes si un jour reproduites; aucun enregistrement fourni.
5. **Références extérieures :** seuls leurs noms/liens, listés dans les sources internes, ont été rapportés; ni les pages externes ni leurs licences n'ont été indépendamment auditées dans cette livraison.
6. **Intégration technique :** compatibilité avec le LMS, validateurs formels de runtime/canon, et pipeline de fusion/déploiement **non testés**; aucune conformité PFEQ, qualification sommaire, certification d'items ni publication affirmée.

## Propositions éventuelles à la gouvernance (non appliquées)

- Définir centralement un schéma de suivi de **deux preuves de maîtrise** et de leurs niveaux par dimension, avec champ explicite pour aides d'accès versus indices de contenu.
- Normaliser dans les familles d'évaluation `mode: scenario_controle` le corpus de substitutions révisées, afin de comparer la difficulté avant d'autoriser une variation contrôlée.
- Définir une convention sur la synthèse vocale et les autres réponses accessibles quand l'oral est la cible, sans imposer de score de volume ou d'accent.
- Prévoir une procédure de revue humaine indépendante des rubriques et de retour d'essai, avant toute qualification `publie` ou `certifie`.

**Aucune proposition ci-dessus n'a modifié** `governance/`, `registry/`, `canon/`, `runtime/`, `state/`, `docs/`, `kristal.workspace.json` ni un autre ID. **Statut final du delta :** fichiers livrables assemblés et contrôlés techniquement, **revue humaine requise**.
