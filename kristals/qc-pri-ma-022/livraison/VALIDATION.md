# Validation de livraison — qc-pri-ma-022 — v1.2

**Produit :** `qc-pri-ma-022_livraison_v1.2.zip`, delta unique fusionnable sous `kristals/qc-pri-ma-022/`.  
**Statut :** `a_revoir_revue_humaine_requise`, ni publié, ni homologué, ni certifié.  
**Auteur technique :** production assistée, sans passation auprès d'élèves.

## Contrôles techniques effectués dans l'environnement de production

Tests automatisés réalisés sur les documents produits et l'archive finale avec un script de validation local (`_ma022_qa.py`, **non inclus** dans le ZIP). Le journal de l'exécution confirme :

1. **Identité / gouvernance :** lecture et conservation exacte des champs de front matter YAML v1.2; 12 sections `PARCOURS.md` ordonnées; conservation des identifiants, concepts et champs natifs du contrat JSON; complétude de la famille suivant `GENERATEUR_ET_EXAMENS.md`; comparaison de l'arête de graphe : aucun préalable `requires`, une recommandation non bloquante `qc-pri-ma-021`.
2. **Évaluations :** JSON strict parsable; 12 items continus `q-001` à `q-012`, sans doublons; champs et rattachements `obj-1` / `crit-1` / `qc-pri-ma-022-ev-01` remplis, statuts « a_revoir »; deux preuves dans des contextes distincts.
3. **Correction mathématique indépendante :** construction de 5 polyèdres par listes explicites de sommets de faces; chaque arête est incidence de deux faces; contrôle de F/A/S et de F+S=A+2. Recalcul des trois générateurs par `seed % 3` ou `seed % 4` sur 100 seeds chacun; comparaison des résultats aux comptes combinatoires indépendants. Cette vérification concerne les cas documentés, **pas** des variantes arbitraires.
4. **Patrons :** propagation informatique des orientations de six carrés dans un cube (six normales différentes sans conflit) : la croix décrite est pliable; le rectangle plein 2 × 3 et la bande 1 × 6 ne le sont pas. La compatibilité arithmétique et géométrique du patron de pyramide régulière à base carrée est documentée, mais **aucun essai physique en classe n'a été effectué**.
5. **Couverture et droits :** présence de deux diagnostics, trois tâches guidées, quatre tâches autonomes, deux transferts, exemples/contre-exemples, remédiations et indications d'accessibilité; provenance distinguant sources locales, dérivations et textes originaux; aucun visuel de tiers embarqué.
6. **Livraison :** exactement 14 fichiers autorisés et non vides; manifeste identique à la liste livrée; premier chemin et toutes entrées commencent par `kristals/qc-pri-ma-022/`, sans dossier englobant ni traversée `../`; CRC de chaque entrée contrôlé et JSON reparsés depuis le ZIP.

**Portée du mot « contrôlé » :** détection automatisée de fautes de structure, de cohérence et de calcul dans les cas bornés. Ce résultat n'est pas une preuve de qualité empirique d'apprentissage, d'équité de passation ni d'accord entre correcteurs.

## Limites non résolues et revue humaine requise

- Une personne compétente en didactique de la géométrie doit lire les formulations, distinguer les descriptions potentiellement ambiguës et valider la progression des indices dégressifs.
- Vérifier physiquement ou dans un moteur géométrique les patrons fabriqués avec les matériaux retenus; confirmer qu'une représentation tactile / orale présente exactement les mêmes indices que le texte.
- Faire relire et essayer les deux rubriques de maîtrise auprès d'un petit groupe : clarté des consignes, longueur adaptée, variance entre évaluateurs, biais linguistiques, accessibilité et durée.
- Les corpus paramétriques sont **fermés et déterministes**, mais leurs formulations pourraient rester trop prévisibles pour un examen exposé aux élèves : la banque ne doit pas être présentée comme sécurisée contre mémorisation.
- Aucun examen externe de licence, d'alignement fin au PFEQ, d'homologation ou de performance psychométrique n'est revendiqué. Aucune expérimentation sur personnes, aucune mesure de fiabilité humaine, aucune évaluation du risque réel d'une classe n'a eu lieu.

## Propositions de changement structurel — non appliquées

1. Créer **dans une future version centrale autorisée** un champ typé « référentiel de solides et de patrons » avec preuves combinatoires normalisées, plutôt que de recopier les tableaux dans chaque feuille.
2. Prévoir un validateur central de patrons géométriques et de rubriques d'arguments, distingué de la simple parsabilité du JSON et des contrôles de seed.
3. Prévoir des champs séparés pour traces de preuves A/B, modalités accessibles et consentements de stockage dans l'adaptateur LMS, sans écrire de données personnelles dans les workspaces.

Aucun `governance/`, `registry/`, `canon/`, `runtime/`, `docs/`, `state/`, autre Kristal, `AGENTS.md`, `kristal.workspace.json`, ni `authoring/ALIGNEMENT.md` n'a été modifié ou inclus dans la livraison.
