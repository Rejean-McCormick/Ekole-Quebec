# Validation et journal de livraison — qc-pri-eps-002

**Contrat :** delta local v1.2; deux remplacements authoring et douze ajouts, sans registre ni canon central. **Statut :** contrôles techniques passés sur une archive de travail; **relecture EPS humaine obligatoire** avant toute utilisation/qualification. Tous les items portent `a_revoir`.

## Contrôles effectivement exécutés (avant emballage)

1. Archive maîtresse v1.2 ouverte et ses fichiers gouvernance, registre, alignement, brief, parcours et contrat consultés.
2. YAML natif conservé textuellement; parsing par PyYAML réussi; **12 sections numérotées et libellés natifs** conservés; identité, titre, discipline et critères inchangés.
3. JSON du contrat chargé; tous les champs/valeurs initiaux (racine et famille) préservés; 13 champs requis du générateur présents dans la même famille native.
4. Graphe lu : aucune relation `requires` sortante; `qc-pri-eps-001` apparaît uniquement comme ordre conseillé non bloquant.
5. Banque JSON chargé : **12 items à ID consécutifs**, chacun relié à `obj-1`, `crit-1` et `qc-pri-eps-002-ev-01`; 8 fixes, 4 scénarios contrôlés. **8 variantes** ont été vérifiées pour la présence d'un stimulus et d'une réponse/grille, ainsi que les index `seed % 2`. Les performances d'élèves ne sont pas simulées.
6. Matrice du plan contrôlée pour les 12 items; deux tâches de maîtrise distinctes A (salle) et B (cour ou autre espace intérieur différent) et grilles descriptives présentes.
7. Vérification textuelle de l'existence des 2 exemples, 2 contre-exemples, 2 diagnostics, 3 guidages, 4 pratiques, 2 transferts et quatre remédiations; références locales résolues; vocabulaire sécurité, accessibilité et droits documenté.
8. **Simulation d'overlay exécutée** après extraction effective de la source entière dans un dossier temporaire : modification de **2 fichiers**, ajout de **10 fichiers pédagogiques**, **0 suppression** à ce stade (les deux fichiers livraison sont ajoutés ensuite au ZIP). Vérification de hachage de fichiers protégés : registre, gouvernance, `ALIGNEMENT.md`, `kristal.workspace.json` inchangés. Inventaire initial : **7322 fichiers**.
9. Au total **73 assertions préalables de conformité** sont passées (dont vérifications individuelles des huit variantes et des liens). Elles démontrent une cohérence mécanique, **pas** la qualité d'une performance réelle ni l'étalonnage de la grille.

## Revue humaine encore indispensable

- Tester les trajets dans un lieu accessible aux enfants concernés et valider sol, largeur, circulation et surveillance; substituer/annuler si risque réel.
- Faire revoir l'acceptabilité pédagogique d'une adaptation individuelle, les niveaux T/A/S/J et la pertinence d'au moins deux observations différentes par un professionnel EPS.
- Vérifier les consignes par essai réel, l'absence de biais envers les aides à la mobilité et la disponibilité des consignes orales/visuelles.
- Évaluer les autorisations locales d'utilisation et de diffusion; aucun matériel externe incorporé, mais aucun certificat de droits n'est délivré.
- Aucune validation de l'efficacité sur des élèves ni audit Framework v9/build-v9/check-ai n'ont été exécutés.

## Propositions de structure seulement (non appliquées)

- Ajouter **dans une future version centrale validée**, un schéma pour les traces motrices T/A/S/J, les mentions d'essai annulé et les conditions d'accès sans données sensibles.
- Proposer un champ de traçabilité des variantes fermées sélectionnées au LMS; ne pas modifier ici le registre ou la gouvernance.

## Contrôle final du ZIP

Un contrôle indépendant **après emballage** est prévu et effectivement exécuté par le script de validation : 14 entrées fichiers non vides, première entrée sous `kristals/qc-pri-eps-002/`, chemins sans traversée, manifeste strict correspondant, JSON parsables, contrôle CRC, même archive_root, aucun autre Kristal, **2 remplacements / 12 ajouts** à la fusion. Les résultats imprimés par ce script constituent la preuve d'exécution; aucune certification institutionnelle n'est revendiquée.
