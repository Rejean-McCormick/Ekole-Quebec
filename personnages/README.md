# Personnages Ékole Québec — Collection v3

**38 rôles × 2 versions (garçon et fille) × 8 poses = 608 images.**

Le rôle pédagogique reste le même, mais chaque version est une identité visuelle distincte : portrait neutre maître + sept poses. Les portraits sont générés et détourés dans Atelier Images, puis publiés seulement après approbation.

- Garçon : `role-photographe`, `compagnon-photographe-pose-saluer`. IDs v2 préservés.
- Fille : `role-photographe-fille`, `compagnon-photographe-fille-pose-saluer`.
- Les deux versions d'un rôle peuvent être choisies comme compagnon.
- Les cartes de rôle affichent côte à côte les deux versions disponibles.
- Les contenus pédagogiques et les identifiants Kontexte ne sont pas dupliqués.

Le coût estimé est affiché dans Atelier Images pour FLUX.2 Pro avant de démarrer un lot. Le tarif réel dépend des mégapixels, références et reprises. Les 608 entrées ne représentent pas 608 images déjà créées.

## Historique du catalogue v2

# Ékole Québec — 38 compagnons-rôles, 8 poses (V2)

**Un rôle = une identité = un compagnon.** Le catalogue `catalogue.json` est la source canonique des 38 identités visuelles et des 304 ressources attendues (38 portraits neutres + 266 poses).

## Poses disponibles maintenant

- `neutre` — carte de rôle, sélection, miniature
- `saluer` — accueil
- `expliquer` — introduction de consignes
- `aider` — encouragement et nouvelle tentative
- `celebrer` — valoriser un effort ou une étape explorée, pas une note
- `reflechir` — chercher, comparer, réfléchir
- `ecouter` — écoute attentive et activités d'échange
- `presenter` — pointer/montrer une zone libre ou une ressource

## Contrat visuel

Le portrait neutre reste `role-<id>` et garde **l'ancien chemin** `images/roles/<id>.png`. Les poses utilisent `compagnon-<id>-pose-<pose>` et `images/compagnons/<id>/pose-<pose>.png`. Cela évite de dédoubler l'identité d'un rôle dans les missions et le compagnon.

Chaque fichier public est un PNG transparent 512 × 512, sans texte intégré, servi **uniquement** après validation et statut `pret`. Le fichier `catalogue.v1.archive.json` conserve le brouillon précédent (Mila, Léo, Alex, variantes par année, etc.). Ce brouillon ne fait pas partie du nouveau catalogue actif.

## Production / publication

1. Dans `Atelier-Images`, choisir **les 38 portraits neutres**, en générer d'abord 2–3 pour vérifier le style.
2. Contrôler et sélectionner chaque candidat neutre, puis cliquer **Approuver comme maître** : cela fournit la référence d’identité pour les sept poses dérivées.
3. Générer les 266 poses (par sous-lots si possible), vérifier les fonds transparents et la fidélité du visage/costume.
4. Publier explicitement les candidats acceptés dans Ékole Québec (sauvegardes des destinations et du catalogue).
5. Redémarrer le serveur Ékole pour relire le catalogue, puis lancer `python ekole-quebec/tools/verifier_personnages.py` depuis le dossier parent.

Une référence de style globale est conseillée. **Il n'est pas prévu de multiplier systématiquement les images par thème ni par année scolaire.** Des variantes contextuelles pourront être ajoutées ultérieurement de façon ciblée.

## Intégration

La page élève affiche maintenant un **choix facultatif de 38 compagnons-rôles** avec recherche. Les cartes de rôles et les missions utilisent le même portrait neutre; le parcours pédagogique peut demander une pose particulière. Les portraits absents ont un sigle de repli. Les choix sont conservés seulement pendant la session de l'onglet, sans suivi individuel. L'activation dépend de `personnages_compagnons_actifs` dans `pack.json`.

**Aucune image payante n'est générée dans ce pack.** Les 304 emplacements sont `a_generer` jusqu'à la publication humaine. Les ancien(ne)s scripts/plans de découpe 80 images sont historiques, non applicables au nouveau contrat.


### Catalogue v3 : 38 rôles × garçon/fille × 8 poses
Les IDs historiques `role-{role}` et `compagnon-{role}-pose-{pose}` restent rattachés aux variantes garçon. Les variantes fille sont `role-{role}-fille` et `compagnon-{role}-fille-pose-{pose}`. Les deux versions apparaissent ensemble dans les cartes de rôles; chaque version peut être choisie individuellement comme compagnon. Les images existantes ne sont pas écrasées lors de la migration.
