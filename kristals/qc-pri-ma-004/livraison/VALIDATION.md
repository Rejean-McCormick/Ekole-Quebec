# Validation réelle — livraison `qc-pri-ma-004` v1.2

## Périmètre et résultats exécutés

La livraison est **un delta pour le workspace existant**, pas un dépôt autonome. Les contrôles ci-dessous ont été réellement exécutés par script Python local avant la génération du rapport; la vérification ZIP finale est effectuée ensuite.

- **PASS** — présence sources v1.2 et graphe sortant : 1 recommande, 0 requires.
- **PASS** — YAML parsable, clés originales conservées et 12 sections identiques.
- **PASS** — blueprint : formes, originaux et 13 champs gouvernance préservés.
- **PASS** — 12 items uniques (8 paramétriques, 4 fixes), 2 contextes de maîtrise.
- **PASS** — générateur indépendant : 8 domaines exhaustifs, 16 exemples avec corrigés.
- **PASS** — quatre items fixes et 11 suites exemplaires recalculés.
- **PASS** — fichiers préparatoires non vides et aucun fichier parasite.
- **PASS** — liens locaux documentés, accessibilité, droits et réserves de revue.

## Contrôles de paquet et simulation de fusion

- Structure attendue : exactement **14 fichiers non vides** sous `kristals/qc-pri-ma-004/`, dans l'ordre déclaré par `MANIFEST.json` et sans dossier englobant; JSON et YAML parsables.
- **Deux remplacements permis :** `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`; **douze créations** sous `contenu/`, `evaluation/`, `sources/` et `livraison/`.
- ZIP testé par CRC (`ZipFile.testzip()`), toutes les entrées à racine relative sûre, première entrée sous le préfixe demandé. La simulation de superposition vérifie que seuls les deux chemins originaux autorisés existent déjà et qu'aucun autre Kristal ou dossier global n'est touché.
- Tests mathématiques : deux méthodes indépendantes (`t(n)=a+(n−1)d` et itération d'une récurrence) sur tous les couples autorisés par chacun des huit domaines paramétriques, avec 16 exemples en seeds nominatives et alternatives; vérification des valeurs à restituer. Cette vérification prouve l'accord du **calcul programmé**, pas la qualité pédagogique de chaque énoncé.

## Limites non résolues

1. **Revue humaine de contenu encore nécessaire :** adéquation à des apprenants réels, précision orale des consignes, équité des situations, charge cognitive, niveaux/thresholds de la grille, acceptabilité des réponses verbales équivalentes.
2. **Accessibilité :** descriptions textuelles, options orales/manipulables et consignes non fondées sur la couleur prévues; **aucun essai avec apprenants ou technologies d'assistance n'a été réalisé**.
3. **Droits et sources :** textes nouveaux originaux; la licence effective du bundle d'origine n'a pas été auditée, et les renvois EEF/IES/CAST ne sont pas présentés comme des sources primaires vérifiées.
4. **Cadre technique :** pas de commande `check/build-v9/check-ai` exécutée sur le workspace complet, ni de test LMS/déploiement/publication. Aucune conformité PFEQ ni qualification d'examen certifié n'est affirmée.
5. Les items `q-010` et `q-011` sont **proposés** pour les deux preuves; les observations réelles de deux manifestations autonomes restent à recueillir.

## Journal de changements et propositions de structure (non appliquées)

- Remplacé intégralement `authoring/PARCOURS.md` sans perdre son front matter YAML ni les douze sections; précisé définitions, cours, pratique, remédiation, rappel et preuves.
- Enrichi la famille existante de `authoring/CONTRAT_PEDAGOGIQUE.json` sans supprimer ses clés, références canoniques ou sous-champs.
- Ajouté six contenus, trois fichiers d'évaluation, la provenance et les deux fichiers de livraison.
- **Proposition non exécutée au registre central :** définir éventuellement un schéma JSON formel partagé pour `parametres`, la serialisation du calcul de graines et les adaptations orales. **Aucun** changement au registre, à la gouvernance, aux fichiers canoniques ou aux autres IDs.

**Statut :** prêt pour revue humaine après contrôles techniques; ni publié, ni homologué, ni certifié.
