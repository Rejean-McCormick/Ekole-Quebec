# Livraison et validation — `qc-pri-fls-004`

**Statut :** contenu pédagogique rédigé ; validation humaine requise, aucune publication ni certification.

## Périmètre exact

Deux fichiers `authoring/` remplacés et douze nouveaux fichiers sous `kristals/qc-pri-fls-004/`. Les invariants du YAML et du contrat originaux sont protégés. Aucun fichier d'un autre Kristal ni fichier central n'est inclus.

## Tests techniques réellement exécutés

- **508 assertions de préarchivage effectivement exécutées et réussies**, sans échec : 14 chemins et fichiers non vides; 12 sections numérotées, invariants YAML et JSON originaux, 10 items avec liens `obj-1` / `crit-1` / famille et grilles, deux contextes autonomes distincts, références, mentions de droits et d’accessibilité.
- **Vérification qualitative formelle :** les énoncés, scripts de partenaire, rubriques et commentaires sont présents et ont une taille substantielle; le corrigé déterministe de classement des quatre répliques est `Y → X → Z → W` (q-006). La fiabilité linguistique et la performance en situation n’ont pas été testées auprès d’élèves.
- **Simulation de fusion réussie** : remplacement de deux fichiers authoring, ajout de douze autres; comparaison SHA-256 des originaux protégés du dossier cible, sans changement. Aucun autre Kristal ni registre central modifié.
- **Test d’archivage ZIP** : absence de chemin englobant, 14 fichiers racine `kristals/qc-pri-fls-004/`, JSON parsables, CRC et inventaire exact contrôlés à la création du ZIP.
- **Contrôles documentaire de droits/accessibilité** : aucun audio/vidéo tiers ni captation ; possibilité de réponse intelligible et d’aides non directives ; aucun essai individuel ou audit juridique mené.

## Limites et revue humaine

- Vérifier le français québécois idiomatique et le registre des scripts auprès de spécialistes FLS ; la tolérance aux accents ne doit pas masquer des problèmes réels d'intelligibilité.
- Essayer les deux contextes avec des élèves et un partenaire formé : quatre tours, clarté des rôles, absence de soufflage, gestion des demandes de clarification.
- Vérifier avec professionnels compétents les aménagements de voix, d'audition, de communication assistée ou d'anxiété; aucune preuve orale équivalente n'est certifiée par les tests documentaires.
- Étudier la fidélité interévaluateurs des rubriques M1–M5. Les niveaux 0–2 sont éditoriaux, non étalonnés.
- Contrôler séparément les droits de tout média éventuellement ajouté; ce delta n'intègre ni audio ni photographie.

## Propositions à soumettre, pas à appliquer au noyau

1. Normaliser une notation des **quatre tours** et l'existence de **répliques du partenaire** dans le schéma de performance linguistique.
2. Autoriser, dans une version future de la banque, un champ de modalités d'accès approuvées, sans confondre production orale et transcription écrite.
3. Proposer une procédure commune d'étalonnage des rubriques orales et de détection de biais relatifs aux accents.

Aucun registre, graphe, gouvernance, canon, runtime, alignement ou document central n'a été modifié dans le delta.
