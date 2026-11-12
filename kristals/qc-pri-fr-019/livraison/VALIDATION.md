# Rapport de validation exécutée — qc-pri-fr-019 / v1.2

**Statut :** delta rédigé; contrôles techniques préarchivage réussis; **revue humaine obligatoire** (`validation_status: a_revoir` pour les dix items). Ce rapport ne certifie ni cours, ni examens, ni alignement PFEQ.

## Sources de référence réellement lues

Les trois fichiers `governance/Norme_Pedagogique_Autonome_v1.2/` obligatoires, les références `registry/GRAPHE_PEDAGOGIQUE_202.json`, les quatre documents `authoring/` natifs ainsi que les pages OQLF citées dans `sources/REFERENCES_CONTENU.md`. La gouvernance et les fichiers protégés ne sont pas modifiés.

## Résultats des tests préarchivage effectivement exécutés

- **326 assertions préarchivage réussies** dans le script de vérification, sans assertion en échec.
- Même frontmatter YAML natif textuellement préservé, syntaxe YAML analysée, 12 sections numérotées dans le bon ordre.
- Contrat JSON conforme aux champs natifs préexistants : aucune suppression de clé/famille, identité et champs canoniques inchangés; paramètres obligatoires de la famille complétés.
- Préalable strict unique `qc-pri-fr-015` confirmé depuis le registre, ordre conseillé sortant nul, diagnostic d'équivalence décrit.
- Banque JSON stricte : **10 items fixes** uniques, numérotés `001` à `010`, avec liens `obj-1`, `crit-1`, famille `qc-pri-fr-019-ev-01`, consigne, stimulus, corrigé, raisons, feedback, statut `a_revoir`, accessibilité et variabilité bornée.
- **Comparaison automatisée des dix couples stimulus/corrigé :** après suppression des signes et normalisation des majuscules/espaces, même suite de mots dans le même ordre. Aucun mot changé, ajouté ni omis dans le corrigé de référence. Cela ne remplace **pas** la revue linguistique humaine.
- Deux preuves autonomes distinctes contrôlées : `q-009` texte informatif et `q-010` dialogue. Plan et grille liés, critères observables et décision non compensatoire.
- Contrôles de présence et de volume : deux exemples, deux contre-exemples, deux diagnostics, trois pratiques guidées, quatre pratiques autonomes, deux transferts, rappels différés, droits/provenance et aménagements d'accès.
- Liens relatifs du parcours résolus vers les fichiers locaux du Kristal; vérification des 14 chemins manifestés et non-vides avant archivage.

## Vérifications finales et contraintes de fusion

- Le script reconstruit et lit l'archive finale, vérifie **CRC (`testzip`)**, 14 noms exacts sans doublon, premier chemin correct, aucun `../`, aucun chemin absolu ni dossier parent, JSON parsés **à partir du ZIP**, comparaison octet-à-octet des 14 contenus avec ceux construits.
- Comparaison avec la liste des fichiers de l'archive maître : les seuls anciens fichiers superposés sont `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`; les 12 autres sont nouveaux. Ni dossier global, ni autre ID, ni `ALIGNEMENT.md`, `AGENTS.md`, `kristal.workspace.json`, `docs`, `canon`, `state` ou `runtime` livrés.
- **Limite :** une simulation d'extraction complète du workspace maître n'a pas été nécessaire à cet audit; l'intersection des chemins source avec les chemins livrés a été contrôlée directement. Aucune publication LMS ni test Framework n'a été exécuté.

## Questions nécessitant une revue humaine

1. Vérifier chaque corrigé et les formulations de justification dans la variété écrite du français québécois; examiner toute ponctuation alternative stylistiquement recevable.
2. Évaluer le niveau réel, les demandes de lecture et la durée auprès d'élèves; contrôler l'accessibilité des tirets et deux-points sur lecteurs d'écran et en dictée neutre.
3. Comparer les jugements de deux évaluateurs sur les dimensions D1–D4; aucune fidélité intercorrecteurs n'a été mesurée.
4. Confirmer les droits du workspace maître avant redistribution hors du projet. Aucun texte ou image source tiers n'a été reproduit.

## Propositions de structure non appliquées

- À envisager pour une évolution centrale versionnée : un schéma décrivant les **variantes stylistiques recevables** et leur niveau d'examen manuel, distinct du corrigé de référence.
- Documenter ultérieurement la preuve d'équivalence d'un prérequis et les adaptations de réponse au niveau du LMS; aucun changement au registre ni au canon dans ce delta.
