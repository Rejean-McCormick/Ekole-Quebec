# Journal de validation et limites — `qc-pri-ccq-005`

**Livraison :** `qc-pri-ccq-005_livraison_v1.2.zip`, delta de 14 fichiers seulement.  
**Racine interne :** `kristals/qc-pri-ccq-005/`.  
**Statut :** `a_revoir` — prêt pour revue de fond, **non publié / non certifié / non homologué**.

## Identité et limites de modification

- Source : `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` **présente à l'intérieur** de l'archive conversationnelle `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`. Base pédagogique v1.2 effectivement lue.
- YAML de `authoring/PARCOURS.md` conservé à l'identique, y compris `statut: en_rédaction`, `revision_contenu: 0.2.0` et autres métadonnées initiales; le corps est totalement instrumenté en douze sections.
- Tous les champs existants du JSON `authoring/CONTRAT_PEDAGOGIQUE.json` sont conservés, sauf l'actualisation voulue des champs de statut/génération; la **même famille** v1.2 est complétée et non recréée.
- Identité immuable : `qc-pri-ccq-005`, `obj-1`, `crit-1`, `qc-pri-ccq-005-ev-01`; objectif et preuve littéralement conservés; `requires=[]`, ordre conseillé `[]`, relation `reinforces` vers `qc-pri-fr-009` seulement.
- Aucun `AGENTS.md`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, registre, norme, canon, runtime, état global, autre Kristal ou métadonnée workspace inclus/écrasé.

## Construction de cours et épreuves

- Définitions média/source/publicité/réputation, six procédés, deux exemples commentés, deux contre-exemples, diagnostic D1/D2, modelage A/B, trois guides G1–G3 à aides décroissantes, quatre productions A1–A4, remédiations R1–R5, deux transferts T1/T2 et rappel différé.
- Dix items fixes et originaux avec stimuli complets, corrections argumentées, critères et feedback; q-009 (affiche/jardin) et q-010 (capsule audio/bibliothèque) sont **deux preuves de maîtrise distinctes**. Toutes les réponses restent à faire examiner humainement et la banque entière est `a_revoir`.
- Les corrigés sont des analyses justifiées de **textes fictifs fermés**, non des solutions d'opérations arithmétiques. Aucun générateur libre, solveur mathématique ou contrôle automatique de jugement humain n'a été invoqué.

## Contrôles réellement exécutés sur ce delta

_Voir le bilan de tests généré et consigné à la fin du présent document. Les vérifications de validité scientifique, d'âge et de jugement professionnel ne sont **pas** remplacées par ces tests._

## Révisions humaines avant diffusion

1. Enseignant ou spécialiste CCQ : vérifier la justesse de la distinction fait/opinion et des six procédés, le niveau de langue, les contextes et la sensibilité d'âge.
2. Responsable d'évaluation : juger l'équivalence de difficulté des preuves A/B, les seuils D1–D4, la durée, l'acceptation de réponses équivalentes et l'absence de biais culturels.
3. Accessibilité : réaliser un essai de lecture neutre/orale, valider le contraste d'une éventuelle mise en page et l'accès sans écran; aucun support multimédia réel n'a été testé.
4. Droits et protection : relire les droits de réutilisation de toute ressource future, les éventuelles ressemblances de noms fictifs et les règles LMS de conservation des traces.
5. Statut institutionnel : aucune procédure d'homologation, alignement PFEQ, approbation ministérielle ou essai en classe n'a été exécuté.

## Propositions de changement central — **aucune modification appliquée**

- Si l'équipe souhaite différencier « YAML original en_rédaction » et « delta de rédaction livré », centraliser une règle de synchronisation du statut; **ne pas altérer** le YAML canonique à partir d'un delta isolé.
- Si une taxonomie de procédés, une durée d'épreuve ou des adaptations d'âge devient normative, la versionner dans la gouvernance centrale après validation; **ne pas créer** de nouveaux préalables.
- Si une automatisation d'épreuves est envisagée, définir un schéma approuvé pour les rubriques qualitatives et un registre de corpus fermé avant toute variation algorithmique.

## Bilan des contrôles automatisés de cette livraison

- **PASSÉ — Base source** : contrat, charte, générateur, frame et graphe v1.2 lus dans l’archive maître embarquée; une seule relation sortante `reinforces` vers `qc-pri-fr-009`, aucun `requires`.
- **PASSÉ — Identité** : frontmatter YAML source conservé à l’identique, 12 sections numérotées 1 à 12; objectifs, critère, concepts, préalables vides, ID et famille conservés; clés et structure natives du contrat JSON préservées.
- **PASSÉ — Contenus** : présence textuelle de 2 exemples résolus, 2 contre-exemples, 2 tâches diagnostiques, G1–G3, A1–A4, R1–R5, T1–T2; contrôle de présence des notions et de la protection des droits.
- **PASSÉ — Banque** : dix items JSON complets, IDs `q-001` à `q-010` uniques et ordonnés, champs communs requis, `obj-1`/`crit-1`/famille corrects, `mode=fixe`, `seed=null`, `parametres=null`, statut `a_revoir` partout; traces présentes au plan.
- **PASSÉ — Deux preuves** : q-009 et q-010 identifiées, sans indice, difficulté transfert, supports différents (affiche et audio transcrit), leviers distincts attendus, citations des deux documents vérifiées par correspondance de chaînes, grille de niveaux 0–3 présente.
- **PASSÉ — Droits et sécurité documentaire** : inventaire textuel de sources et créations originales vérifié; aucun média externe, lien Web actif ni donnée réelle de mineur n’est requis dans les six fichiers de contenu.
- **PASSÉ — Assemblage** : manifeste avec 14 chemins autorisés; tous fichiers non vides; racine interne unique et absence de `../`, chemin absolu, workspace global ou autre Kristal; contrôlé avant compression et **recontrôlé dans le ZIP**.
- **NON EFFECTUÉ — Revue et essai externes** : absence de revue pédagogique CCQ, de passation réelle à l’âge cible, de validation psychométrique des seuils, de test de lecteur d’écran et de procédure de certification/institutionnelle.
