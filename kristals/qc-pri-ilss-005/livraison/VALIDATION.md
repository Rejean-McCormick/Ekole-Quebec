# Validation technique et limites — `qc-pri-ilss-005`

**État :** 14 fichiers rédigés en delta v1.2, banque d'items `a_revoir`. Les tests ont été consignés à la fin de la construction; aucune qualification, publication, homologation, certification ou validation avec apprenants.

## Contrôles réellement réalisés

**Exécuté : 7918 assertions préarchivage réussies.** Le script de contrôle a vérifié :
- les 14 fichiers et leurs chemins sûrs, la présence des douze sections ordonnées, le YAML préservant l'identité et les champs canoniques;
- les trois JSON, la famille native et ses paramètres supplémentaires, le préalable strict `qc-pri-ilss-003`, ainsi que l'absence de nouveau verrou;
- dix items complets et uniques, leurs corrigés explicites, et les quatre fiches de maîtrise **A/B dans les deux contextes 009/010** : les passages preuves cités figurent littéralement dans les textes approuvés;
- la couverture dans le plan, les rubriques, les soutiens d'accessibilité et la documentation des droits;
- une fusion simulée intégrale : **2 remplacements**, **12 ajouts**, **7320 fichiers sources protégés identiques en SHA-256**, aucune suppression ni modification hors `kristals/qc-pri-ilss-005/`.
- les contrôles ZIP CRC, chemins, manifeste, non-vacuité et parsage JSON archivés sont exécutés après création (voir sortie de validation du ZIP).

## Limites non résolues

- Aucun essai avec élèves ni mesure interévaluateurs; les textes peuvent nécessiter un ajustement de difficulté après observation dans un cadre pédagogique réel.
- Les paliers A et B sont des supports pédagogiques créés ici, non une taxonomie validée de littératie ou une attribution d'année scolaire.
- Décider si une adaptation individuelle atteste une lecture indépendante exige un jugement humain; le modèle ne déclare pas équivalente une simple compréhension à l'écoute.
- Les sources anglophones éclairent la méthode et l'inclusion, sans prescrire les correspondances françaises ni l'organisation ILSS au Québec.
- Les droits des éléments originaux sont documentés mais n'ont pas fait l'objet d'un audit juridique indépendant.

## Revue humaine préalable

1. **Littératie et français :** contrôler la décodabilité de chaque support par rapport aux graphèmes **réellement enseignés**, la qualité des stratégies et les variations de français québécois acceptables.
2. **ILSS et équité :** évaluer l'accessibilité pour une diversité d'expériences de littératie sans inférence sur l'identité, le parcours migratoire ou les capacités intellectuelles.
3. **Évaluation :** passer les mêmes tâches à plusieurs évaluateurs, juger stabilité des rubriques et adéquation de la sélection A/B; ne pas présenter les items comme certifiés.
4. **Diffusion et données :** confirmer l'usage d'un stockage minimal des observations, les supports tactiles ou numériques disponibles, et l'absence de collecte de données identitaires inutiles.

## Propositions de structure, sans modification centrale

- Un champ de preuve `reading_evidence_mode` permettrait de différencier lecture personnelle, compréhension après oralisation tierce et technologie d'accès; proposition seulement, pas de changement du schéma central.
- Un vocabulaire commun documenté de `palier_diagnostic` non lié à l'identité personnelle pourrait améliorer la traçabilité des ajustements; proposer au responsable du référentiel avant toute adoption.
- Une procédure commune de revue de décodabilité des textes français par niveau de correspondances enseignées serait à formaliser dans la gouvernance future, sans toucher au registre de ce lot.
