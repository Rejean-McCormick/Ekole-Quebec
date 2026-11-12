# Validation du delta `qc-pri-mu-008` (v1.2)

**Statut :** rédaction instrumentée et revue pédagogique humaine requise. Aucune homologation, certification d'items ni validation terrain. Aucun ajout aux fichiers centraux du workspace.

## Contenu du delta

- 14 fichiers strictement sous `kristals/qc-pri-mu-008/` : 2 remplacements de fichiers authoring v1.2 et 12 ajouts locaux.
- Le contrat conserve ses champs et ses identifiants; le parcours conserve son frontmatter et ses douze sections; `ALIGNEMENT.md`, `BRIEF_REDACTION.md` et les fichiers canoniques restent protégés.
- Dix items `a_revoir`, scénarios **fixes** sans génération probabiliste. Chaque réponse attendue contient des constats observables et des repères de pulsations précis.

## Contrôles techniques effectivement réalisés

- **576 assertions de prévalidation réussies** (script local réellement exécuté). Contrôles : chemins, 14 fichiers non vides, YAML inchangé et 12 sections, JSON natif et invariants du contrat, famille d’évaluation, graphe, 10 items, toutes les réponses attendues, sécurité/accessibilité et couverture des rubriques.
- **Scores mathématiquement contrôlés par un second encodage indépendant** des 10 partitions : événements aux numéros de pulsation, 4 pulsations par groupe, correspondances avec les nombres et retours dans les corrigés; **76 attaques sonores** contrôlées.
- **Fusion simulée** dans le dossier propriétaire : 2 fichiers existants remplacés, 12 ajoutés et **34 fichiers originaux protégés inchangés** (comparaison SHA-256). Aucune modification du registre ou d’un autre Kristal.
- **ZIP final** : test CRC, liste exacte des 14 chemins, absence de répertoire englobant, de chemins absolus/traversants et de fichier vide, parse JSON dans le ZIP; résultat confirmé par le script après empaquetage.
- **Droits** : inspection documentaire, sans média enregistré ni contenu musical tiers livré. Ce n’est pas un audit juridique.
- **Accessibilité** : présence de modalités alternatives et de la limite quant à l’équivalence d’une partition lue et d’une écoute; aucun essai en classe effectué.

## Incertitudes non résolues

- **Il n'existe aucun fichier audio dans ce delta.** Les partitions sont exécutables par un adulte, mais leur uniformité acoustique d'une classe à l'autre n'est pas démontrée. Le contenu audio doit être vérifié humainement avant usage sommative.
- Aucune étude avec élèves, aucun étalonnage interévaluateurs, aucune vérification médicale de niveau sonore, aucune garantie d'accessibilité individualisée.
- Une partition écrite lue visuellement ne remplace pas automatiquement une observation d'écoute; toute décision d'équivalence pour un apprenant exige jugement professionnel, documentation de la modalité et accord du responsable pédagogique.
- Le droit de diffuser de futurs enregistrements et la gestion du consentement restent à définir localement. Les textes et partitions livrés sont originaux et ne contiennent aucun média commercial sous licence inconnue.

## Revue humaine nécessaire avant qualification

1. **Musicien ou pédagogue en musique** : tester réellement les timbres, constats de corrigé et perception des contrastes à faible volume.
2. **Évaluateurs** : comparer les cotations de deux personnes sur les mêmes réponses argumentées; ajuster les critères si nécessaire.
3. **Accessibilité** : tester les appuis auditifs, visuels et tactiles selon l'objectif individuel, sans abaisser implicitement la compétence.
4. **Droits et sécurité** : vérifier autorisations de diffusion ou de captation si un enregistrement est créé ultérieurement; vérifier matériel, volume, fatigue et durée.

## Propositions à soumettre séparément aux mainteneurs (aucune base centrale modifiée)

- Définir un support canonique facultatif de diffusion de partitions originales (`score_text`, `timing_units`, `approved_rendering_hash`) afin que le matériel acoustique employé soit contrôlable entre classes.
- Ajouter au futur schéma une traçabilité distincte de la modalité effectivement perçue lors d'une épreuve et des aménagements non directifs.
- Prévoir un protocole de validation humaine des extraits exécutés et de concordance entre correcteurs.
