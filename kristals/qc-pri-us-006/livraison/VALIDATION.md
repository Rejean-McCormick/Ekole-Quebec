# Validation de livraison — `qc-pri-us-006` (v1.2)

**Statut : `a_revoir` — rédaction de delta pédagogique, non certifiée, non publiée et non homologuée.** L'objectif observable, la preuve et la famille sont conservés de la frame source. La **sécurité culturelle** d'un dossier sur les Premiers Peuples exige une lecture compétente et, si possible, une consultation appropriée des personnes/Nations concernées; les contrôles automatiques ne garantissent pas la conformité historique ou culturelle.

## Portée et changements réellement produits

- `authoring/PARCOURS.md` : conservation intégrale du frontmatter YAML v1.2, des **12 titres et sections**; enrichissement de leur contenu avec diagnostic, séquençage, enseignement, pratique, différenciation, rappels et décision de maîtrise.
- `authoring/CONTRAT_PEDAGOGIQUE.json` : conservation des champs et valeurs d'origine, des familles et identifiants; ajout des paramètres de famille gouvernés sans altération des propriétés natives.
- Six fichiers `contenu/` : définitions, fiches historiques synthétisées W/I/L/M avec provenance, deux exemples résolus, deux contre-exemples, deux diagnostics, trois exercices guidés à étayage dégressif, quatre pratiques autonomes, deux transferts et six remédiations identifiées.
- Trois fichiers `evaluation/` : plan des 12 items; banque de 12 items dont deux scénarios à variantes fermées, avec seed et sélection reproductible; grille analytique à quatre dimensions et deux preuves d'autonomie indépendantes.
- `sources/REFERENCES_CONTENU.md` : sources externes consultées [S1–S8] distinguées des raisonnements dérivés et productions originales; limites de datation, de vocabulaire et de droits.
- `livraison/MANIFEST.json` : exactement les 14 fichiers autorisés, tous sous `kristals/qc-pri-us-006/`.

## Contrôles effectivement exécutés

**Contrôle automatisé de la livraison**, sur les fichiers produits, via le validateur local :

1. Correspondance du manifeste à l'ensemble des **14 fichiers** présents et non vides; préfixe, ordre du premier fichier et absence de répertoire parent supplémentaire.
2. Parsing JSON strict des trois fichiers JSON; parsing du YAML; comparaison exacte avec **toutes les valeurs** du frontmatter original, et conservation des titres/numéros des 12 sections.
3. Comparaison des valeurs de base du contrat d'évaluation et de **toutes les propriétés préexistantes** de la famille; présence des 13 champs requis par `GENERATEUR_ET_EXAMENS.md`.
4. Accord des `requires` vides et des trois liens conseillés avec le graphe source; IDs objectif/famille/critère cohérents; numéros `q-001` à `q-012` uniques et sans trous.
5. Existence du stimulus, de la consigne, des critères, du corrigé et de la rétroaction pour chaque item; 12 statuts `a_revoir`; deux preuves indépendantes W/I et L/M avec 4 critères observables chacune.
6. Pour q-008 et q-010, contrôle **algorithmique** des seeds, du choix `index = seed % 2` et du couplage énoncé/corrigé; exemples pair/impair explicités dans le plan (ce test est technique, pas historique).
7. Présence des quantités pédagogiques minimales; cohérence des références de sources [S1–S8]; vérification des liens relatifs aux fichiers internes; vérification de l'absence de données multimédias ou d'un autre ID que ceux conseillés.
8. Test après emballage : 14 chemins ordonnés comme le manifeste, première entrée sous le bon Kristal, fichiers non vides, protection contre les chemins absolus ou `../`, parsing JSON/YAML depuis le ZIP et contrôle intégral CRC `testzip()`.

**Contrôle documentaire humain non équivalent à validation experte :** consultation des pages Wendake/Nation Wendat, Nametau innu, Musée canadien de l'histoire et Yale eHRAF. Les informations sont **paraphrasées**, et non reproduites sous forme d'images ou de témoignages. Les fiches W/I/L/M restent des simplifications historiques éducatives.

## Limites non résolues et revues humaines exigées

- Vérifier en détail la portée « **vers 1500** » pour chaque cas : certaines informations viennent du XVIe siècle, d'une synthèse archéologique plus tardive ou de mémoires transmises. **1534** est une attestation de rencontre et d'échange, non l'origine du commerce ni un relevé de 1500.
- Faire réviser la séparation **Nation Wendat / Iroquoiens du Saint-Laurent** et la présentation des réalités innues et mi'gmaq par des personnes compétentes en histoire et, idéalement, des interlocuteurs légitimes des Nations concernées; éviter toute usurpation de parole.
- Faire vérifier auprès d'enseignants la charge de lecture, la compréhension des termes, les variantes de réponse recevables, l'accessibilité et les rubriques. Tester les activités avec des élèves avant qualification.
- Les références externes appartiennent à leurs ayants droit : **aucun droit de republication des images, citations longues, traditions ou médias n'est présumé**. Toute version qui les inclurait exige un audit de licence et, au besoin, des autorisations.
- La dissymétrie documentaire entre L (portrait de pratiques) et M (rencontre datée) est **intentionnelle** pour évaluer le raisonnement critique, mais doit être testée pour ne pas pénaliser un élève exprimant correctement une « ressemblance non démontrable ».
- Aucun essai sur le LMS, aucune vérification formelle de l'architecture canonique v9, aucune revue communautaire/enseignante ni essai d'élèves, ni qualification de publication n'a été réalisé dans ce mandat.

## Propositions de changement de structure (sans modification des bases centrales)

- Étudier dans une version future du schéma un champ optionnel `evidence_provenance` par assertion (source, époque, type de témoignage, degré de certitude, point de vue) avec validation humaine.
- Prévoir dans les épreuves une rubrique sur le **silence documentaire et la dissymétrie des sources**, plutôt que forcer une similitude de faits non attestée.
- À l'échelle du workspace global uniquement, étudier un registre de relectures par spécialistes des Nations concernées, distinct des validations automatiques et de l'homologation scolaire.

**Fusion :** depuis `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, extraire le ZIP de livraison. Seuls `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json` sont remplacés; les 12 autres fichiers sont ajoutés. Ne modifier aucun fichier global ou autre Kristal.
