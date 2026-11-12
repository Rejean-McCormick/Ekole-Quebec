# Validation de livraison — `qc-pri-st-020`

**Statut :** rédaction préparée pour fusion dans le workspace v1.2. À **revoir pédagogiquement et scientifiquement**; aucune homologation PFEQ, certification ou validation de terrain.

## Tests effectivement exécutés

**7700 assertions préarchivage exécutées avec succès** par le script de contrôle Python. Elles comprennent : comparaison avec les fichiers canoniques du workspace (objectif, concepts, deux relations de graphe, YAML et champs JSON conservés), complétude des 14 chemins, étude des 10 items, strict JSON, 2 scénarios fermés, règles et chemins du graphe, rubriques, liens, accessibilité et droits. **7320 fichiers d'origine protégés du workspace** ont été comparés par empreintes de contrôle après application des 14 fichiers dans une simulation de fusion en mémoire sans écriture sur le workspace; seul le delta local a deux chemins déjà présents et ajoute les 12 autres. Aucun échec préarchivage.

**Contrôle ZIP postarchivage :** liste exacte des 14 chemins, pas de chemin absolu ou parent, aucun fichier vide, CRC `testzip()` sans erreur, manifeste identique aux entrées et trois JSON stricts décodables. Aucune exécution de code de générateur aléatoire (aucun n'est livré) : le catalogue fermé est vérifié par reconstruction algorithmique de tous ses chemins et arêtes.

**Nature du contrôle des corrigés :** les liens et chemins du graphe ont été vérifiés par un algorithme indépendant des chaînes déclarées; les prédictions textuelles ont été vérifiées comme chaînes non vides et reliées aux cartes mais **pas** validées empiriquement ni par une étude de terrain.

## Limites et décisions de revue humaine

1. **Scientifique :** les cartes de régime alimentaire sont conçues pour ce modèle didactique; leur usage pour décrire un habitat réel nécessiterait de la documentation naturaliste spécifique. Les effets d'une ressource réduite ne sont pas des mesures de changements d'effectifs.
2. **Pédagogique :** dix items rédigés, mais aucun essai en classe, aucune mesure de fidélité entre correcteurs et aucune validation du seuil M1–M5 n'ont été réalisés.
3. **Accessibilité :** schémas textuels/tactiles et réponses orales proposés; l'équivalence réelle pour des apprenants différents n'a pas été étudiée, et requiert un jugement humain.
4. **Droits :** sources référencées, absence d'images, musiques et vidéos tierces; pas d'audit juridique exhaustif.
5. **Sécurité :** seules des cartes, descriptions et schémas sur papier/écran sont demandés; pas de collecte ni manipulation vivante prescrite. L'environnement effectif de la classe n'a pas été audité.

## Propositions au mainteneur de la structure (non appliquées)

- Ajouter, lors d'une future révision contrôlée du schéma central, un champ facultatif `epistemic_status` par carte : *donnée didactique fictive* / *observation* / *source externe vérifiée*.
- Standardiser un `catalogue_scenarios` de corpus verrouillé avec équivalents accessibles (tableau d'arêtes, description textuelle), et tests de chemins, plutôt que laisser un générateur produire des relations zoologiques libres.
- Prévoir un protocole de revue humaine interévaluateurs et d'essai des adaptations sur les représentations de graphes.

**Aucun** registre, fichier de gouvernance, fichier `canon/`, autre Kristal ou workspace global n'est inclus ou modifié dans cette livraison.
