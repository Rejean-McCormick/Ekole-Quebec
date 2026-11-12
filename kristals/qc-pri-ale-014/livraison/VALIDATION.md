# Validation de la livraison — `qc-pri-ale-014` (v1.2)

**Statut documentaire:** contenu entièrement rédigé; banque d'items `a_revoir`; ni certification, ni qualification pédagogique finale, ni conformité PFEQ affirmée.

## Vérifications techniques

**532 assertions préarchivage exécutées et réussies** dans `verify_ale014.py` (Python) : 14 chemins et fichiers non vides, structure et invariants du YAML, 12 sections du parcours, contrats et familles JSON natifs préservés, 10 items complets/uniques, liens `obj-1`/`crit-1`/famille, difficultés, consignes anglaises, critères, notes de correction et deux situations de maîtrise distinctes.

- **Graphe :** préalable `qc-pri-ale-013` inchangé, pas de recommande/renforce ajouté.
- **Validité des exemples :** cohérence formelle des scénarios et des réponses modèles examinée par auteur, et vérifiée via les assertions de correspondance des questions, buts et rubriques. **Aucune épreuve en classe ni double correction humaine n'a été effectuée.**
- **Intégrité source :** simulation de fusion sur la copie du dossier original de l'archive maîtresse : 2 remplacements autorisés, 12 créations, 34 fichiers existants protégés inchangés en SHA-256.
- **Sources et droits :** aucun contenu audio/visuel tiers, références internes vérifiées; absence d'audit juridique exhaustif.
- **ZIP :** validé après création (14 entrées uniquement, racine locale, aucun chemin de traversée, tailles non nulles, CRC et JSON strict), voir le journal d'exécution.


## Limites non résolues

- Aucun enfant, enseignant ou groupe d'élèves n'a participé à un essai réel de compréhension, de durée, de stabilité interévaluateurs ou de validité des prompts oraux.
- Aucune certitude automatique sur la justesse de toutes les réponses ouvertes : les modèles ont été examinés par le rédacteur, et les rubriques doivent être validées et appliquées par un humain.
- Les adaptations pour difficultés auditives ou d'élocution nécessitent évaluation locale; une réponse écrite seule ne prouve pas silencieusement un objectif oral.
- Les seuils M1–M5 sont des propositions éditoriales non étalonnées.
- Aucun audit juridique de toutes les possibilités futures de réutilisation n'a été réalisé. Aucun média tiers n'est fourni; les pistes audio éventuelles requièrent une revue des droits.

## Revue humaine avant décision

1. Enseignant expert en **English Language Arts** : vérification des énoncés et interactions anglaises, authenticité, variété, syntaxe et lexique.
2. Évaluation pédagogique : équité entre les contextes A/B, stabilité de la cote 0–2 et caractère réellement réactif de l'échange.
3. Accessibilité et accompagnement : modalités de restitution pour handicaps auditifs/de parole, confidentialité et absence de stigmatisation d'accents.
4. Responsable technique : intégrer le delta v1.2 dans une copie du workspace et tester les adaptations, sans toucher aux bases canoniques v9.

## Propositions de structure sans changement central

- Envisager un champ de provenance des accommodations (`delivery_mode`, `access_approved_by`) dans une prochaine version du schéma; cela nécessite une décision de gouvernance et n'est pas ajouté au registre.
- Prévoir une carte de passation A/B locale à l'évaluateur et une grille d'accord interévaluateurs; ces fichiers n'ajoutent **aucun** quinzième fichier à ce ZIP.
- Conserver le type natif `réponse_argumentée` pour la famille tout en documentant l'observation réelle de l'oral dans `representation`; proposer une normalisation uniquement par changement central versionné.
