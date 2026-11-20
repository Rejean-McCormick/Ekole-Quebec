# Ekole Québec — dépôt de contenu optimisé

Paquet indépendant pour le moteur voisin `ekole/` : **202 cours et six parcours**, avec sources Kristal, publications élève et catalogue visuel. Le corpus reste candidat à révision; aucune validation scolaire officielle n’est ajoutée par ce nettoyage.

## Démarrer

Placer ce dépôt à côté des versions alignées de `ekole`, `Kontexte`, `Kompose` et `Ekole_Avatars_Decoupes`. `LANCER_EKOLE_QUEBEC.bat` ou `lancer-ekole-quebec.sh` lance Ekole avec ce contenu. Les outils de base ne nécessitent que Python 3.10+; le découpeur voisin utilise Pillow.

## Ce qui reste versionné

- `pack.json`, `cours/`, `kristals/`, `publications/` : contenu, sources et publications existantes, conservés sans modification pédagogique.
- `personnages/catalogue.json` : cinq compagnons, 38 rôles, 80 références d’images préparées.
- `visuels/` et les manifestes `experience/RESSOURCES_VISUELLES.json` : système d’images de cours inchangé.
- Images originales utiles et images finales : mêmes chemins, stockage **Git LFS**.
- `historique/` : uniquement les 202 cours d’origine nécessaires au contrôle d’intégrité et les deux sources Spek encore utilisées par B2.
- `outils/vendor/kristal-local/3.2.3/` : une copie exacte de l’outil partagé et de ses modèles. Les 205 commandes locales `tools/kristal.py` restent utilisables; la variante différente du modèle d’organisation humaine reste autonome.

Le reste des archives historiques, les pilotes d’origine, les anciens rapports racine `livraison/` et les index du snapshot sont conservés dans l’archive séparée livrée avec ce dépôt. Ils ne sont pas nécessaires au démarrage actuel.

## Outils Kristal

Les commandes locales gardent leur syntaxe. Les chemins désignant un Kristal restent explicites, comme auparavant :

```sh
python kristals/qc-pri-fr-002/tools/kristal.py inspect kristals/qc-pri-fr-002 --compact
python kristals/qc-pri-fr-002/tools/kristal.py check kristals/qc-pri-fr-002
python kristals/qc-pri-fr-002/tools/kristal.py pack kristals/qc-pri-fr-002 --output ../exports/qc-pri-fr-002.zip
```

`pack` réintègre l’outil complet et les modèles : le ZIP obtenu reste autonome hors du dépôt. Copier manuellement un dossier Kristal muni d’un point d’entrée partagé exige aussi ces dépendances; utiliser `pack` pour l’export autonome. `init` et `migrate-v10` conservent le comportement de l’outil d’origine et peuvent réinstaller un outil complet dans leur cible. Le nettoyage n’a exécuté aucune migration ni aucun build canonique.

## Git et médias

Lire `docs/STOCKAGE_ET_NOUVEAU_DEPOT.md` avant le premier commit. `.gitattributes` configure LFS; `.gitignore` n’exclut pas les images finales, les contenus ni les approbations. Les contenus conservent leurs octets sous Windows pour préserver les empreintes.

```sh
python tools/verifier_optimisation.py
python tools/verifier_personnages.py
python -m unittest discover -s tests
```

Le second contrôle exige les dépôts alignés voisins. Le premier contrôle et les tests d’optimisation fonctionnent sans moteur frère.

## Compagnons-rôles visuels V2 (novembre 2026)

`personnages/catalogue.json` définit désormais **38 compagnons-rôles × 8 poses = 304 ressources**. Les portraits neutres sont partagés avec les cartes de rôle; les autres poses se génèrent dans **Atelier Images** après approbation du maître. Détails : `personnages/README.md`. Le catalogue précédent de 80 ressources est archivé dans `personnages/catalogue.v1.archive.json`. Aucune image nouvelle n’est incluse par défaut.
