# Validation et journal de livraison — qc-pri-als-003

**Livraison ciblée :** `qc-pri-als-003_livraison_v1.2.zip`  
**Base :** workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, version v1.2.  
**Statut :** `a_revoir` — fichiers rédigés et techniquement contrôlés, non certifiés, non publiés et non homologués.

## Modifications réellement apportées

1. **Deux fichiers remplacés** : `authoring/PARCOURS.md` (en-tête YAML d'origine préservé à l'identique, 12 sections rédigées); `authoring/CONTRAT_PEDAGOGIQUE.json` (champs natifs et famille inchangés, paramètres d'observation complétés et statut de revue mis à jour).
2. **Six fichiers `contenu/` ajoutés** : définitions de rime/répétition/idée générale, deux exemples résolus, quatre contre-exemples, deux diagnostics, modelage, trois activités guidées à aides dégressives, quatre pratiques autonomes, deux transferts, corrections, remédiations et rappels différés.
3. **Trois fichiers `evaluation/` ajoutés** : plan détaillé, banque JSON de **12 items fixes** à scripts anglais originaux, grille critériée sur **deux preuves autonomes** distinctes : jardinage en comptine et restitution d'une mitaine dans une histoire entendue.
4. **`sources/REFERENCES_CONTENU.md` ajouté** : sources internes effectivement consultées, raisonnements dérivés, productions originales, droits et vérifications encore ouvertes.
5. **Deux fichiers `livraison/` ajoutés** : manifeste de 14 chemins autorisés et le présent rapport.

## Contrôles effectivement exécutés

- Script local `_als003_validate.py` exécuté sur le dossier de livraison : **54 tests / 54 réussis** après ajustement d'une vérification de casse dans le test de grille. Parmi eux : YAML parsable et métadonnées conservées, 12 sections numérotées, identité canonique, aucune dépendance entrante imposée, champs natifs du contrat conservés, banque JSON parsable, 12 IDs distincts, alignement de `obj-1`/`crit-1`/famille, champs d'items obligatoires, deux preuves distinctes, réponses attendues présentes, synchronisation des scripts d'A3/A4 avec les items 011/012, difficulté/couverture, exemples, transferts, liens internes, étiquettes, accessibilité et manifeste.
- Script local `_als003_anchor_audit.py` : **12/12** audits lexicaux ciblés d'ancrages de corrigés aux scripts et **5/5** vérifications de répétitions exactes. Ces contrôles ne remplacent **pas** une validation acoustique ni une double correction humaine des réponses.
- Manifestation de maîtrise **dans deux contextes** contrôlée : P1 `qc-pri-als-003-q-011` (comptine jardin); P2 `qc-pri-als-003-q-012` (histoire mitaine). Chaque preuve prévoit un thème exact, 3 détails et un indice audible; décision sur le thème + au moins 2 des 3 détails + un indice exact, de manière autonome **dans chacune** des deux épreuves.
- Les champs `seed=null` et `parametres=null` sont intentionnels : aucun item paramétrique ni génération aléatoire n'est utilisée. Variabilité limitée à la présentation vocale/intelligibilité et à l'expression des réponses, sans mutation des faits ou des corrections.

## Limites et points à réviser par une personne

- **Aucun fichier audio livré** : les scripts doivent être dits/chantés de façon intelligible. Faire valider les accents/rimes à l'oreille et la durée de chaque écoute auprès de spécialistes d'anglais langue seconde, notamment *spoon/afternoon*, *shore/more*, *day/away*.
- Effectuer deux corrections humaines indépendantes d'un échantillon d'items (voire des 12) pour tester la stabilité des rubriques, les réponses équivalentes, les erreurs d'attribution et la neutralité des contextes. Aucun essai avec des élèves ni audit externe scientifique ou PFEQ n'a été effectué.
- Les élèves ayant des limitations auditives, langagières ou attentionnelles peuvent nécessiter des adaptations individuelles; l'accès à une transcription ou une interprétation modifie ce qui est mesuré par une preuve de **compréhension orale anglaise**. Une personne qualifiée doit qualifier la comparabilité plutôt que déclarer l'équivalence automatiquement.
- Les chants et histoires sont des productions originales de cette livraison, mais les droits sur d'éventuelles mélodies, voix enregistrées ou images ajoutées ultérieurement **n'ont pas** été vérifiés. Aucune copie de paroles commerciales, de données privées ou d'œuvres externes ne figure parmi les livrables.
- **Points structurels proposés à la gouvernance (non appliqués) :** standardiser dans le schéma des items les champs facultatifs `critere_id`, `representation`, `protocole`, `variation_permise`, `preuve_maitrise` et un indicateur « script réservé à l'évaluateur »; prévoir un objet distinct pour les adaptations qui changent le construit. Ne modifier aucun registre ni aucune norme centrale dans ce delta.

## Fusion prévue et exclusions

Depuis la racine **intérieure** du workspace maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, extraire le ZIP. Les chemins sont `kristals/qc-pri-als-003/...` sans dossier enveloppe. Aucun `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `docs/`, `canon/`, `runtime/`, `state/`, `registry/`, `governance/` ni autre ID n'est livré. Les deux remplacements `authoring/` préservent les identifiants et contrats sources.

**Décision provisoire : `a_revoir`**, jamais `certifié`, `homologué` ou `publié`.
