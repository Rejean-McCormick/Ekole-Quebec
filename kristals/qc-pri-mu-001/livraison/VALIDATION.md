# Validation et journal de livraison — `qc-pri-mu-001` (v1.2)

## Périmètre et provenance

Archive effectivement lue : `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`, **contenant** le workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Les fichiers `governance/...`, `registry/...`, `authoring/ALIGNEMENT.md`, `BRIEF_REDACTION.md`, le frontmatter d'origine et le contrat d'évaluation natif ont été consultés. Le delta est uniquement sous `kristals/qc-pri-mu-001/` : deux fichiers `authoring/` remplacés, douze fichiers nouveaux. Aucun workspace complet, second ID ou registre central n'est inclus.

**À fusionner :** extraire ce ZIP **depuis l'intérieur de** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Les chemins internes s'y superposent sans dossier englobant. Ne pas écraser d'autres fichiers que `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json` dans ce Kristal.

## Contenu effectivement produit

- `authoring/PARCOURS.md` : frontmatter identique, 12 sections remplies; enseignement, diagnostics, guidage dégressif, quatre pratiques, remédiation, rappels et deux preuves indépendantes.
- `authoring/CONTRAT_PEDAGOGIQUE.json` : structure et champs v1.2 d'origine conservés; 13 champs minimaux de gouvernance complétés au niveau de la famille; statut `a_revoir`.
- Six fichiers `contenu/` : notions scientifiquement prudentes, exemples, contre-exemples, 38 recettes WAV synthétiques originales avec programme autonome Python standard **encapsulé dans un Markdown**, deux diagnostics, trois activités accompagnées, quatre pratiques autonomes, deux transferts et rappel différé.
- Trois fichiers `evaluation/` : plan des 12 items, JSON strict 12 tâches fixes avec réponses ou grilles, grille de maîtrise avec deux contextes distincts.
- `sources/REFERENCES_CONTENU.md` : sources internes/externe vérifiées, dérivations, productions originales et restrictions de droits.

## Contrôles techniques réellement exécutés avant emballage

Tests automatisés locaux (programme de génération fourni et banc de tests privé exécuté) :

- **OK** — regles du graphe : zero prerequisite strict
- **OK** — champs identitaires d origine conserves
- **OK** — frontmatter YAML identique aux 20 champs v1.2 origine
- **OK** — 12 sections ordonnees et une occurrence chacune
- **OK** — frontmatter, valeurs immuables et statut non publie
- **OK** — champ contrat initial conserve : format
- **OK** — champ contrat initial conserve : kristal_id
- **OK** — champ contrat initial conserve : objectif_id
- **OK** — champ contrat initial conserve : objectif_observable
- **OK** — champ contrat initial conserve : concepts
- **OK** — champ contrat initial conserve : preuve_attendue
- **OK** — champ contrat initial conserve : prerequis_bloquants
- **OK** — champ contrat initial conserve : ordre_conseille
- **OK** — champ contrat initial conserve : familles
- **OK** — champ contrat initial conserve : statut
- **OK** — champ contrat initial conserve : referentiel_technique
- **OK** — cle et types contractuels conserves
- **OK** — champ famille initial conserve : family_id
- **OK** — champ famille initial conserve : type
- **OK** — champ famille initial conserve : tache_cible
- **OK** — champ famille initial conserve : rubric_dimensions
- **OK** — champ famille initial conserve : generation
- **OK** — champ famille initial conserve : review_status
- **OK** — parametre de generation preexistant conserve : validite_contenu
- **OK** — parametre de generation preexistant conserve : variations_admissibles
- **OK** — parametre de generation preexistant conserve : interdiction
- **OK** — parametre de generation preexistant conserve : seed_reproductible
- **OK** — 13 champs gouvernance famille
- **OK** — famille unique identique au canon
- **OK** — banque JSON contractuelle parseable
- **OK** — 12 items distincts consecutifs
- **OK** — tous champs communs et textes non vides
- **OK** — item par objectif, famille, critere et mode fixe
- **OK** — difficulte couverte initial intermediaire transfert
- **OK** — deux contextes maitres dans la banque
- **OK** — generateur audio embarque en texte executable
- **OK** — 38 WAV synthetiques temporaires effectivement crees
- **OK** — 38 fichiers WAV mono PCM16 22050 Hz parsables
- **OK** — durees WAV verifiees sur 38 fichiers
- **OK** — durees contraste A 0.4 1.4
- **OK** — durees contraste B 1.6 toutes
- **OK** — silence interne numeriquement exact B2
- **OK** — silence interne numeriquement exact B4
- **OK** — silence interne numeriquement exact S1
- **OK** — silence interne numeriquement exact X1
- **OK** — silence interne numeriquement exact X4
- **OK** — silence interne numeriquement exact D3
- **OK** — aucun silence central inopine B1
- **OK** — aucun silence central inopine B3
- **OK** — aucun silence central inopine S2
- **OK** — aucun silence central inopine X2
- **OK** — aucun silence central inopine X3
- **OK** — intensite relative A3/A1 facteur 3 amplitude (ratio RMS 3.0000)
- **OK** — temoins timbre U1 U2 ont formes differenciees
- **OK** — fondamentale approximative verifiee Q1 (330.0 Hz)
- **OK** — fondamentale approximative verifiee Q2 (660.0 Hz)
- **OK** — fondamentale approximative verifiee B1 (330.0 Hz)
- **OK** — fondamentale approximative verifiee B3 (660.0 Hz)
- **OK** — fondamentale approximative verifiee X2 (740.0 Hz)
- **OK** — fondamentale approximative verifiee X3 (370.0 Hz)
- **OK** — table de verite A couvre 2x2 unique
- **OK** — table de verite B couvre 2x2 unique
- **OK** — double preuve B sans ancien stimulus de modelage
- **OK** — deux taches diagnostiques documentees
- **OK** — trois exercices accompagnes documentes
- **OK** — quatre pratiques autonomes documentees
- **OK** — deux transferts et rappel differe
- **OK** — sources droits et acces explicites

**Sens exact des tests acoustiques numériques :** 38 WAV mono 16 bits/22 050 Hz ont été **générés temporairement hors du ZIP** à l'aide du programme embarqué puis inspectés pour l'en-tête, les durées en échantillons, les pauses numériques au centre de certaines pistes, le rapport RMS entre des niveaux relatifs et la fréquence dominante d'un sous-ensemble. Le contrôle des deux tables de vérité A et B exploite directement les recettes déterministes. Cela **ne constitue pas une audition humaine**, une calibration d'intensité en dBA, une évaluation de la compréhension des élèves ou une validation de l'adéquation perceptive des contrastes.

## Limites non résolues et points de revue humaine **obligatoires**

1. **Audio matériel non livré :** les 14 fichiers demandés n'incluent aucun WAV. Avant une première passation, produire les WAV depuis le code de `01_NOTIONS_ET_EXEMPLES.md`, écouter **toutes les séries réellement utilisées** sur le matériel cible, vérifier contraste perceptible, niveau confortable, pauses internes et absence de clics ; consigner un procès-verbal de contrôle.
2. **Exactitude sensible au dispositif :** volume principal, égalisation, compression automatique, bruit ambiant, haut-parleurs et capacités d'accès modifient intensité/timbre. Si contraste non vérifiable, **retirer l'item** et ne pas considérer sa réponse incorrecte.
3. **Revue pédagogique musicale** : juger la pertinence des sons synthétiques, des tâches de composition, des dimensions écoute/organisation/intention et des critères sans jugement esthétique ni physiologique; vérifier l'adéquation à l'âge et essayer les consignes avec un public pilote.
4. **Accessibilité et sécurité** : revue humaine pour les besoins de personnes malentendantes, hypersensibles au bruit ou nécessitant d'autres moyens d'expression; ne pas présenter une lecture de schéma comme une discrimination *auditive* effectivement prouvée.
5. **Droits** : aucun son tiers dans le ZIP. Les échantillons originaux synthétisés sont seulement un point de départ; tout remplacement par un enregistrement tiers exige une vérification des droits et une nouvelle revue du corrigé.
6. **Publication/Framework** : aucune procédure `check`, `build-v9`, `check-ai`, essai LMS ou qualification du canon n'a été lancée; aucune activation ni homologation n'est inférée.
7. **Épreuve sommatif locale** : validation humaine des rubriques, clarté des consignes, durée et biais avant usage à enjeu; `validation_status: a_revoir` maintenu.

## Décisions et propositions **sans changement du workspace central**

- **Proposition seule :** étudier au niveau gouvernance un éventuel `media_asset_id`/empreinte SHA-256 pour rendre vérifiables les WAV effectivement administrés, sans ajouter un objet central dans ce delta.
- **Proposition seule :** prévoir un registre local (LMS) documentant contrôle sonore, adaptation d'accès et répétitions. Aucune donnée personnelle ne doit être stockée dans le canon.
- **Proposition seule :** envisager un statut distinct `techniquement_valide__revue_humaine_en_attente` dans la taxonomie future des livraisons plutôt que `publié`.

**Conclusion :** les contrôles automatisés listés sont exécutés et réussis; la livraison demeure **à revoir par un humain** avant usage scolaire ou publication. Les assertions sur la perception et les droits d'audios externes ne sont **pas certifiées**.


## Contrôles sur le ZIP effectivement fabriqué (étape finale)

- **OK** — 14 entrées régulières, toutes non vides, sous la seule racine `kristals/qc-pri-mu-001/`, premier fichier sous cette racine et aucun dossier englobant.
- **OK** — noms exacts concordant avec les 14 entrées du manifeste; aucun second ID, chemin absolu ou composant `..`.
- **OK** — contrôle CRC de l’archive, les trois JSON parsables, `format`, `archive_root`, `kristal_id` et `base_version` cohérents.
- **OK** — 13 références de chemins locaux explicites relevées dans le Markdown résolvent vers un des 14 fichiers du delta ou une frame source inchangée (dont `ALIGNEMENT.md` et `BRIEF_REDACTION.md`).
- **Non exécuté** — test d’intégration, audit humain musical, lecture des WAV au haut-parleur, passation pilote, calibration acoustique physique et qualification du framework/canon.
- **Résumé des tests exécutés :** 68 contrôles automatisés avant ZIP, 9 contrôles automatisés de l’archive finale, plus la vérification des liens locaux ci-dessus; aucun échec à la fin du processus.
