# Stockage et nouveau dépôt Git

## Organisation retenue

| Élément | Emplacement et suivi |
|---|---|
| Contenus JSON/Markdown, sources pédagogiques, scripts, catalogues, plans, approbations | Git normal |
| Images originales utiles et images finales, notamment `personnages/images/` et `kristals/*/experience/images/` | Git LFS, chemins inchangés |
| Essais, exports de travail, aperçus et caches | Dossiers ignorés; aucune sauvegarde implicite par Git |
| Historique et anciens fichiers retirés | Archive séparée fournie, à garder hors de ce dépôt |
| Planches originales des personnages | Dans le paquet de découpe voisin ou une sauvegarde média dédiée; elles sont absentes du snapshot fourni |

Les fichiers ignorés ne sont pas sauvegardés par Git. Conserver ailleurs tout essai ou original qu’on souhaite garder. Une image finale et ses métadonnées doivent être sauvegardées ensemble; ne pas ajouter une règle qui ignore tous les PNG.

Les modèles de génération et le catalogue des personnages restent versionnés, même si aucune image n’est encore prête. Les données du système d’images de cours et leurs approbations restent à leurs emplacements existants.

## Initialiser un dépôt propre

Le dossier livré ne contient ni `.git`, ni remote, ni ancien historique. Utiliser uniquement le dossier `nouveau-depot/ekole-quebec` comme racine du dépôt. Les archives livrées séparément restent en dehors.

Installer Git et Git LFS, puis, depuis ce dossier :

```sh
git lfs version
git init -b main
git lfs install --local
git add .
git lfs ls-files
git status
git commit -m "Base Ekole Quebec optimisee"
```

Les règles LFS sont déjà dans `.gitattributes`; elles prennent aussi en charge les extensions en majuscules. `git lfs ls-files` doit afficher les 15 images WebP actuellement présentes. Les prochaines images PNG seront prises en charge aux mêmes chemins. Effectuer `git lfs install --local` avant le premier ajout des fichiers, y compris avant d’utiliser `GitSink.bat`.

Créer un dépôt distant vide, puis remplacer le texte `URL_DU_NOUVEAU_DEPOT` par son adresse :

```sh
git remote add origin URL_DU_NOUVEAU_DEPOT
git push -u origin main
```

Aucun push ni effacement distant n’est effectué par ce livrable. L’hébergement doit prendre en charge LFS; les quotas dépendent de votre fournisseur. Le hook LFS installé transmet les fichiers lors du push.

Un commit qui efface les anciens fichiers dans le dépôt existant conserve l’ancien historique. Pour repartir sans cet historique, utiliser le nouveau dépôt ci-dessus puis archiver l’ancien une fois le nouveau vérifié. Les issues, PR, réglages et autres données du service Git ne sont pas contenus dans ce snapshot de fichiers.

## Récupérer le dépôt ailleurs

Avec Git LFS installé :

```sh
git clone URL_DU_NOUVEAU_DEPOT ekole-quebec
cd ekole-quebec
git lfs pull
python tools/verifier_optimisation.py
```

Les vrais fichiers images apparaissent à leurs chemins habituels. Un petit fichier texte commençant par `version https://git-lfs.github.com/spec/v1` est un pointeur dont le média reste à télécharger; exécuter `git lfs pull`.

Pour une installation par ZIP téléchargé depuis GitHub, activer l’inclusion des objets LFS dans les archives du dépôt ou utiliser le clonage ci-dessus : les archives GitHub peuvent contenir seulement les pointeurs. Le ZIP de livraison fourni ici inclut les 15 fichiers réels disponibles.

## Maintenir un dépôt léger

- Conserver les originaux utiles et la version finale retenue; ranger les essais dans `travail-medias/`.
- Supprimer les exports reproductibles lorsqu’ils ne servent plus; ne pas supprimer les sources de génération pour économiser leur seule sauvegarde.
- Utiliser les scripts Kristal partagés. `pack` produit un export autonome en réintégrant outil et modèles.
- Les commandes d’origine `init` et `migrate-v10` peuvent installer un outil complet dans leur cible; ce comportement est maintenu pour les espaces autonomes.
- LFS réduit le poids des binaires dans l’historique Git, mais les fichiers restent présents dans le dossier de travail et les anciennes versions LFS occupent du stockage distant.

La factorisation des 205 copies identiques économise surtout de l’espace dans l’arborescence et facilite la maintenance : Git déduplique déjà les blobs identiques. Aucun gain sur un ancien historique Git n’est mesuré ici, car le snapshot fourni ne contient pas cet historique.

## Références officielles

- Git LFS : https://git-lfs.com/
- Installation et utilisation : https://github.com/git-lfs/git-lfs
- Archives GitHub avec LFS : https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-git-lfs-objects-in-archives-of-your-repository
