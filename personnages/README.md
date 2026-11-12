# Catalogue visuel Québec

Référence : `catalogue.json`, format `ekole.personnages/1`, déclaré dans `pack.json`.

## Périmètre arrêté

| Compagnon | Univers | Variantes scolaires | Poses supplémentaires | Rôle associé |
|---|---|---:|---|---|
| Mila | quotidien | 1 à 6 | saluer, apprendre, aider, célébrer | — |
| Léo | quotidien | 1 à 6 | saluer, apprendre, aider, célébrer | — |
| Alex | quotidien | 1 à 6 | saluer, apprendre, aider, célébrer | — |
| Fermier | ferme | 1 à 6 | — | fermier |
| Extraterrestre | cosmos | 1 à 6 | — | extraterrestre |

Les années représentent des variantes illustrées du parcours scolaire, pas des âges réels. Les quatre poses sont communes aux années pour chacun des trois personnages humains; il n’y a pas de produit « six années × quatre poses ».

Le rôle `explorateur` est distinct du rôle `extraterrestre`. L’ancien choix de compagnon `cosmos` pointe explicitement vers l’extraterrestre. Un univers peut contenir plusieurs personnages : Mila, Léo et Alex ne sont pas trois univers différents.

## Une image par rôle

Les 38 rôles Kontexte ont chacun un seul portrait partagé entre toutes les activités, sans variante d’année ni de pose. Cela comprend 23 rôles utilisés dans les 11 missions actuelles et 15 rôles de réserve. La liste canonique vient de `Kontexte/data/roles/`. Une image de rôle fermier reste une ressource distincte de ses six variantes de compagnon.

Total prévu : **42 variantes de compagnons + 38 illustrations de rôles = 80 images**. Aucune image nouvelle n’est générée pendant cette passe. Le snapshot ne contient pas les quatre planches historiques ni leurs PNG découpés; ils ne sont pas remplacés par des fichiers factices.

## Contrat de fichier et intégration ultérieure

Chaque entrée `assets` possède un identifiant, un type, un chemin PNG relatif à ce dossier, un texte alternatif et un statut :

- `a_generer` : image attendue, aucun affichage public;
- `a_verifier` : sortie de découpe à contrôler, aucun affichage public;
- `pret` : illustration vérifiée, affichable seulement si le fichier existe et son en-tête PNG passe le contrôle du moteur.

Conserver les identifiants et chemins pendant la génération. Les PNG standardisés font 512 × 512 pixels RGBA, personnage entier et centré. La marge de sécurité de 32 pixels appartient au contenu de chaque case; la découpe conserve toute la case. Le texte et les noms sont affichés par l’interface, hors image. Fond transparent souhaité; le découpeur conserve l’alpha et ne fabrique pas un détourage parfait.

Les plans se trouvent dans le dépôt voisin `Ekole_Avatars_Decoupes/plans/`. Leur ordre de lecture est gauche à droite, puis haut en bas. Les cellules restantes de la dernière planche de rôles restent vides.

Après génération : découper, contrôler la planche de vérification, copier le sous-dossier `exports/images/` vers `personnages/images/`, puis passer les seules entrées vérifiées à `pret`. Ne pas copier `manifest_standard.json` sur `catalogue.json`. Redémarrer Ekole pour relire le catalogue. Aucun passage automatique à `pret`.

Depuis le dossier parent des quatre dépôts :

```sh
python ekole-quebec/tools/verifier_personnages.py
# Plus tard, une fois toutes les images intégrées :
python ekole-quebec/tools/verifier_personnages.py --exiger-images
```

Le moteur Ekole et les règles de découpe restent génériques; cette sélection de personnages appartient au paquet Québec. Les images pédagogiques des Kristals et leur système de prompts restent séparés.
