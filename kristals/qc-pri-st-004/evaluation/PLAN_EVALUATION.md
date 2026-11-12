# Plan d'évaluation — `qc-pri-st-004`

**Objectif immuable `obj-1` :** Relier des observations à une conclusion en distinguant constat et interprétation.  
**Critère immuable `crit-1` :** Présenter un résultat, son indice et une limite de la conclusion.  
**Famille unique :** `qc-pri-st-004-ev-01` (`generee_sous_contraintes` au niveau du blueprint). **Banque :** corpus fermé d'items `fixe` / `scenario_controle`; **aucune génération IA libre ou correction par IA non validée**.

## Matrice exhaustive de correspondance

Tous les items ci-dessous sont liés à `obj-1`, `crit-1`, `qc-pri-st-004-ev-01`. La difficulté renvoie à la tâche, pas à l'âge de l'élève.

| Item | Fonction / contexte | Difficulté | Représentation | Preuve attendue | Variation autorisée |
|---|---|---|---|---|---|
| `qc-pri-st-004-q-001` | Diagnostic — ombre du poteau | initial | texte_chronologique | Résultat, indice, interprétation distincte, limite | Aucune : source figée |
| `qc-pri-st-004-q-002` | Diagnostic — deux roulettes | initial | mesures_par_essai | Résultat, indice, interprétation distincte, limite | Aucune : source figée |
| `qc-pri-st-004-q-003` | Pratique guidée — papier absorbant | initial | fiche_de_mesures | Résultat, indice, interprétation distincte, limite | Aucune : source figée |
| `qc-pri-st-004-q-004` | Pratique guidée — bateaux de papier | intermediaire | phrase_de_donnees | Résultat, indice, interprétation distincte, limite | Aucune : source figée |
| `qc-pri-st-004-q-005` | Pratique guidée — tours en papier | intermediaire | comptage_sur_cinq | Résultat, indice, interprétation distincte, limite | Aucune : source figée |
| `qc-pri-st-004-q-006` | Pratique autonome — ponts en papier | intermediaire | ratio_et_texte | Résultat, indice, interprétation distincte, limite | Aucune : source figée |
| `qc-pri-st-004-q-007` | Pratique autonome — feuilles de plantes | intermediaire | ratio_et_texte | Résultat, indice, interprétation distincte, limite | Aucune : source figée |
| `qc-pri-st-004-q-008` | Pratique autonome — glaçons | intermediaire | horodatage_narratif | Résultat, indice, interprétation distincte, limite | Aucune : source figée |
| `qc-pri-st-004-q-009` | PREUVE M-1 — insectes de jardin (vivant) | transfert | tableau | Résultat, indice, interprétation distincte, limite | Présentation fidèle uniquement, après revue |
| `qc-pri-st-004-q-010` | PREUVE M-2 — avions de papier (technologie) | transfert | liste_chronologique | Résultat, indice, interprétation distincte, limite | Présentation fidèle uniquement, après revue |
| `qc-pri-st-004-q-011` | Transfert — étangs et oiseaux (environnement) | transfert | note_de_terrain | Résultat, indice, interprétation distincte, limite | Présentation fidèle uniquement, après revue |
| `qc-pri-st-004-q-012` | Transfert — mini-pare-vent (technologie) | transfert | compte_rendu_oral | Résultat, indice, interprétation distincte, limite | Présentation fidèle uniquement, après revue |
| `qc-pri-st-004-q-013` | Pratique autonome — ombre sur la cour | intermediaire | note_avec_unites | Résultat, indice, interprétation distincte, limite | Aucune : source figée |

## Couverture, critères et pondération pédagogique

Le corpus comprend **13 situations distinctes** : diagnostic 2; accompagnement 3; pratique autonome 4 (ponts, feuilles, glaçons, ombre, dont l'une est `q-013`); **preuves indépendantes de maîtrise 2** (`q-009`, `q-010`); transferts 2. Les pratiques du fichier 05 sont des entraînements, pas des substituts aux deux preuves de maîtrise. **Contextes distincts obligatoires :** vivant / coccinelles (`q-009`, tableau) et technologie / avions de papier (`q-010`, liste). Ni l'un ni l'autre ne répète les chiffres du modelage. Deux milieux distincts, deux présentations, et un travail autonome explicite sont vérifiables.

**Rubrique de jugement pour chaque item :** C1 résultat exact et conditions/unités; C2 indice valide; C3 conclusion proportionnée aux données et sans cause inventée; C4 distinction constat–interprétation/explication; C5 limite spécifique et conséquence. Échelle 0/1/2 par critère (`GRILLE_MAITRISE.md`). Le plan est **critérial**; une note ou un total ne vaut pas maîtrise. Les items 001–008 et 011–013 servent au diagnostic, à la formation ou au transfert; les deux preuves 009–010 sont examinées séparément pour la décision.

**Conditions des deux preuves :** sans indice, sans modèle affiché, sans intervention sur le fond; adaptation de canal permise, mais traçabilité de l'aide et identité des données conservées. Les cinq critères doivent atteindre le niveau 2 **dans chacune** des deux preuves. Sinon : diagnostic de l'obstacle, remédiation ciblée, puis une nouvelle preuve en contexte inédit après revue humaine; pas de promotion sur moyenne.

## Génération, contrôle et limites de variation

- Le **contrat de famille** demeure `generee_sous_contraintes`. Pour la présente livraison, son implémentation est **un corpus fermé**; les énoncés et corrigés sont entièrement écrits et vérifiables. `seed: null` sur les items signifie qu'aucun tirage n'est exécuté; cela ne simule pas un générateur reproductible.
- `fixe` : aucune variation de valeurs, d'unités, de texte de consigne ou de réponse.
- `scenario_controle` : seul le canal de présentation du **même scénario figé** peut éventuellement être changé (tableau ou transcription équivalente); cette autre présentation **n'a pas été générée ni validée dans ce lot**. Identité et valeurs de la source demeurent obligatoirement identiques; toute nouvelle version exige vérification humaine avant usage.
- Toute extension paramétrique future doit spécifier variables, domaines, contraintes, algorithme/seed stables et vérification indépendante des résultats chiffrés, puis ajouter des items sans contredire le blueprint; elle n'est **pas** prétendue réalisée ici. Un correcteur IA libre ne vaut pas solveur ni grille validée.

## Sécurité, équité et accessibilité

Aucun exercice pratique dangereux : seules des situations simulées en texte, tableaux ou listes; aucune réelle mesure de chaleur, de courant, de produits chimiques ou de terrain. Réponses orales (transcrites fidèlement), écrites ou assistées possibles. Tableaux toujours lisibles linéairement; nombres et unités conservés; pas de dépendance au seul code de couleur, à une image ou à une aisance rédactionnelle non ciblée. Revoir la charge langagière, la compréhension de « cause », les biais de contextes, le temps et la rubrique avec une personne qualifiée avant évaluation à enjeu.

## Contrôle de qualité et état

Corrigés ancrés aux données inventées (comparaisons élémentaires, aucune généralisation), présence d'un indice et d'une limite examinées lors de la validation technique documentée dans `livraison/VALIDATION.md`. Les faits des scénarios ne sont pas des mesures de terrain; les articles externes cités dans `sources/REFERENCES_CONTENU.md` ne sont pas présentés comme sources de ces chiffres. **Statut des items : `a_revoir`; pas de certification ni de publication.**
