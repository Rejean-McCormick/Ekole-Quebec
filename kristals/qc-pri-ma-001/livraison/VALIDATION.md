# VALIDATION — qc-pri-ma-001 (delta v1.2)

## Statut honnête

**Contrôles automatiques positifs; revue humaine toujours requise.** Le présent rapport ne certifie ni les items ni la qualité pédagogique, ne publie pas de contenu et ne revendique aucune conformité au PFEQ. Aucun `canon/`, état v9 ou registre global n'a été modifié. Les essais auprès d'élèves et les tests de fonctionnement dans Moodle/LMS ne sont **pas réalisés**.

## Entrées et identité vérifiées

- Archive source réellement ouverte : `initbundle(1).zip`, racine interne `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, utilisée **uniquement** comme workspace maître de référence.
- Textes lus : `CONTRAT_PEDAGOGIQUE_V1.2.md`, `GENERATEUR_ET_EXAMENS.md`, `CHARTE_CONVERSION_QC.md`, graphe v1.2, et quatre fichiers `authoring` propres à ce Kristal; lecture complémentaire de `AGENTS.md` et `REFERENCES_EVIDENCE.md`.
- Comparaison à la source : frontmatter YAML de `PARCOURS.md` **inchangé**, 12 sections numérotées conservées; identité, titre, `MA`, résultat principal, preuve, préalables vides et famille immuables.
- Contrat JSON : schéma natif et toutes les clés existantes conservés, y compris `generation`; 13 attributs du générateur complétés dans la famille; famille `qc-pri-ma-001-ev-01` et statuts `a_revoir` contrôlés.
- Graphe consulté : aucune relation sortante pour ce Kristal, une relation entrante — aucun verrou ajouté, aucune base centrale modifiée.

## Contrôles de contenu effectivement exécutés

- Analyse YAML réelle via PyYAML; lecture JSON stricte via `json.loads` pour le contrat et la banque d'items.
- **12 items**, numérotés q-001 à q-012, tous distincts avec consigne, stimulus, réponse, critères, rétroaction, niveau et état `a_revoir`; **6 paramétriques** bornés et reproductibles.
- **6 006 instanciations de paramètres contrôlées** (1 001 seeds par chacun des 6 items) : bornes, recomposition des groupes et cardinal attendu, avec calcul de référence par soustractions itératives plutôt que par appel au générateur de la banque. Les six instances livrées, la quantité explicite de symboles par stimulus et **18 exemples de seeds** ont été confrontés à la formule.
- q-011 et q-012 : deux contextes distincts, nombres exacts de pictogrammes (**14 étiquettes** et **17 pots**), solutions non données dans les stimuli, rubrique C1–C4 et demande explicite de contrôle autonome.
- Documents vérifiés pour présence de deux diagnostics, trois essais guidés, quatre pratiques autonomes, deux transferts, deux exemples résolus, contre-exemples, remédiations, accessibilité et rappel différé. Ce contrôle atteste la **présence**, non l'efficacité sur des personnes.
- Sources et droits : distinction entre sources internes lues, pages IES consultées, raisonnements dérivés et créations originales. Aucun visuel tiers intégré. Un audit juridique de distribution reste nécessaire selon contexte.

## Contrat de fusion contrôlé

- **Exactement 14 chemins** inclus dans le manifeste, tous préfixés `kristals/qc-pri-ma-001/`; exactement deux fichiers auteur remplacent leurs homologues préexistants, les douze autres sont des ajouts.
- ZIP attendu et testé après fabrication : première entrée sous le préfixe; pas de dossier enveloppe, aucune entrée hors Kristal, aucun `../`, aucun chemin absolu; fichiers non vides, JSON analysables, contenu ZIP identique aux fichiers de montage et test CRC.
- Mode d'extraction : décompresser l'archive maîtresse et entrer dans le dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`; extraire le ZIP **dans ce dossier**, sans monter de dossier additionnel. Ce delta ne contient pas les bases centrales.

## Limites ouvertes et revue humaine nécessaire

1. **Pédagogie et linguistique :** vérifier la progression effective du concret au schéma et à la notation, la clarté orale des consignes et le vocabulaire fr-CA pour les publics ciblés.
2. **Essai auprès d'élèves :** observer l'autonomie, la charge cognitive, l'effet des groupes déjà visibles, l'écart entre performance diagnostique et transfert et la stabilité dans le temps.
3. **Accessibilité réelle :** tester le rendu des caractères (`●`, `□`, `✿`, `▣`) sur lecteurs d'écran, supports tactiles, imprimés en fort contraste et outils de communication; adapter si nécessaire sans changer les quantités ni aider au calcul.
4. **Outils techniques :** intégrer séparément les vues « élève » et « correcteur »; le JSON livré ne cache pas les réponses par lui-même. Tester l'import LMS/Framework et toute qualification v9 par les circuits dédiés; aucun `check/build-v9/check-ai` n'a été exécuté, puisqu'aucun canon n'est modifié ici.
5. **Validité :** relire les rubriques C1–C4, vérifier la robustesse aux stratégies alternatives et aux adaptations équivalentes; revoir les paramètres avant diffusion à grande échelle.
6. **Droits :** le contenu textuel est original, mais les conditions de redistribution publique et de rendu des polices devront être auditées au niveau du produit intégrateur.

## Propositions de modification de structure — **non appliquées**

- Définir ultérieurement un schéma JSON officiel pour `MANIFEST.json` et la structure détaillée `parametres`, afin de valider par JSON Schema.
- Ajouter côté LMS une séparation contrôlée des champs destinés à l'élève et des corrigés, plus un registre de passation et des aides fournies.
- Offrir un champ d'accessibilité par représentation (ex. source tactile équivalente au pictogramme), sans lier l'identité canonique à un fournisseur d'images.
- Conserver les propositions dans la revue centrale; ne modifier ni `registry/`, ni `governance/`, ni les dossiers des autres Kristals.
