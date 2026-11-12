# Règles Kristal Framework v10 — GitHub

Sources : `Kristal-Framework/spec/v10/{Architecture,Nodes-and-Collections,GitHub-Reference-Profile,Host-Bindings,Publication-and-Discovery}.md` fournies dans la copie de référence épinglée.

L'hébergement v10 n'absorbe pas les États sémantiques v9. Une collection est un périmètre organisationnel opérationnel; les références de fédération sémantique exigent des états exacts épinglés. Un `kristal_node_manifest` déclare un noeud; un host binding relie ce noeud à GitHub; un répertoire signale où le trouver. `DIRECTORY != AUTHORITY`, `READ SURFACE != SEMANTIC STATE`, `SYNC != PUBLICATION != ACTIVATION`.

Aucun `kristal.github-read-surface` ou `kristal.github-collection-index` normatif n'est livré ici, car les 202 workspaces fournis sont encore `stub` et ne possèdent pas tous des `State Snapshot` v9 engagés. On ne doit pas produire des faux `state_commitment` pour satisfaire un schéma.

Ordre requis avant publication :
1. Revue pédagogique et qualification de la sémantique source.
2. Construire les États v9 exacts avec le Framework/Authoring Kit et des manifests de sources.
3. Qualifier et consigner les engagements canoniques.
4. Construire les read surfaces et l'index de collection par outils v10.
5. Tester les bindings GitHub réels sans secret embarqué.
6. Publier les ressources vérifiables; seulement ensuite activer un site choisi.

L'outil Ekole présent produit seulement des plans candidats. Il ne forge ni manifestes signés ni attestations.
