# Validation de livraison — `qc-pri-st-003`

**Statut :** rédaction complète, contrôles documentaires préarchivage réussis, **banque `a_revoir`**, revue professionnelle requise. Aucune homologation PFEQ ni calibration métrologique certifiée.

## Contrôles réalisés

- **545 assertions préarchivage réussies**, par exécution du script `verify_st003.py` : filetree 14 fichiers, YAML original intégral conservé, 12 sections, contrat et génération native préservés, champs d’items, corrigés et liens.
- **Calculs indépendants exécutés** : les 3 variantes de chaque item paramétrique (q-007, q-008), soit **6 cas**, ont été recalculées en entiers de dixièmes et une deuxième fois en décimaux exacts (`decimal.Decimal`) ; règle de sélection `seed % 3` testée ; les réponses fixes `1 cm`, `7 cm` et `0,2 s` vérifiées en tant que textes de corrigé.
- **Identité et fusion contrôlées** : seuls les deux fichiers `authoring/PARCOURS.md` et `CONTRAT_PEDAGOGIQUE.json` existaient dans les 14 chemins de livraison, les 12 autres sont nouveaux; aucun chemin de registre, de gouvernance ou de Kristal tiers livré. Les sources protégées restent intactes sous la simulation par superposition logique du delta.
- **Accessibilité, sécurité, droits** : vérification documentaire de la présence des adaptations, de la distinction entre données simulées et lectures réelles, des références et des restrictions de capture; pas de contrôle expérimental, clinique ni juridique.
- **Archive finale** : ZIP construit ensuite et testé (CRC, chemins, contenu non vide, manifeste, JSON strict).

## Vérifications non réalisables automatiquement

- Aucune observation d'élève ou essai de mesure réalisé physiquement avec un cahier ou un jouet; les valeurs de ces situations restent inconnues avant épreuve.
- Validité des choix d'accessibilité, fiabilité des jugements entre correcteurs, sûreté du matériel selon le local, précision des instruments et effets pédagogiques non évalués expérimentalement.
- Ne pas affirmer une chaîne de traçabilité SI : seuls les tableaux rendent la méthode retraçable dans le sens documentaire du parcours.

## Revue humaine exigée avant publication ou usage décisionnel

1. Vérifier que chaque station et protocole sont sûrs, accessibles et administrables localement.
2. Vérifier clarté des consignes, observation autonome, distinction des deux contextes, traitement des écarts authentiques et seuils de maîtrise.
3. Faire corriger des réponses variées par plusieurs adultes et vérifier leur accord; relire chaque grille, paramètre, droit et adaptation.
4. Vérifier l'intégration au LMS sans altérer les registres centraux et sans stocker de données d'enfants dans le corpus.

## Propositions structurelles, sans modification de bases centrales

- Proposer au mainteneur un champ standard `evidence_origin = observed | simulated` pour éviter de confondre une lecture réelle et un corpus de génération.
- Proposer une fiche commune de journal de calibration et de résolution instrumentale si un usage métrologique plus avancé était requis, sans introduire cette obligation dans le workspace actuel.
- Proposer un dispositif commun de revue d'aménagements et de sécurité des stations pour les futurs Kristals scientifiques.
