# Norme de production — Kristals de parcours d’apprentissage, primaire Québec

**Version de la norme : `1.1.0` — ajout contrôlé du registre des références officielles du 8 octobre 2026.**  
**Statut : norme interne du projet, non homologuée par le ministère de l'Éducation.**  
**Portée : 1re à 6e année du primaire au Québec; enseignement, pratique, progression et évaluation.**

## Décision d'architecture

1. **Un Kristal-feuille = un microparcours pédagogique complet**, centré sur un résultat d'apprentissage observable, non une simple fiche de contenu ni une année scolaire.
2. **202 Kristals-feuilles sont réservés** dans le catalogue v0.1. Leurs identifiants sont gelés; leurs titres sont éditoriaux, leurs objectifs et liens curriculaires restent à valider. `202` n'est **pas** un objectif arbitraire d'exhaustivité : des scissions, ajouts ou désactivations documentés sont permis.
3. **Une collection de workspaces/states Kristal indépendants**, avec assemblages par discipline, cycle, année et variante, sans copie des contenus.
4. **`A-Kristal-ScolQc` reste propriétaire de la représentation du système scolaire et des sources curriculaires.** Notre collection possède les parcours pédagogiques et ses propositions d'évaluation.
5. **Un examen est une projection versionnée** d'objectifs, de compétences et de critères, non un tirage libre de questions.
6. **Moodle est une cible de projection**; les fichiers d'auteur du projet ne sont pas supposés être directement des artefacts Kristal v9 ou des activités Moodle importables.

## Lire dans cet ordre

| Document | Contrat |
|---|---|
| [01 — Autorité et limites](docs/01_AUTORITE_ET_PORTÉE.md) | Qui fait foi et ce qui reste non vérifié |
| [02 — Taxonomie et identités](docs/02_TAXONOMIE_ET_IDENTITÉS.md) | Intitulés, codes, identités gelées |
| [03 — Topologie et propriété](docs/03_TOPOLOGIE_ET_PROPRIÉTÉ.md) | Frontières sémantiques, fichiers et dépendances |
| [04 — Contrat du microparcours](docs/04_CONTRAT_MICROPARCOURS.md) | Sections et données obligatoires |
| [05 — Alignement curriculaire](docs/05_ALIGNEMENT_CURRICULAIRE.md) | Références officielles, années, versions |
| [06 — Graphe et assemblages](docs/06_GRAPHE_ET_ASSEMBLAGES.md) | Relations typées, parcours annuels |
| [07 — Conception de l'apprentissage](docs/07_DESIGN_PÉDAGOGIQUE.md) | Enseigner, pratiquer, maîtriser, remédier |
| [08 — Évaluation et examens](docs/08_ÉVALUATION_ET_EXAMENS.md) | Plan d'épreuve, génération, corrigés |
| [09 — Sources, sécurité et licences](docs/09_SOURCES_ET_DROITS.md) | Preuves, limites de réutilisation, données sensibles |
| [10 — Contrôle de qualité](docs/10_VALIDATION_ET_TESTS.md) | Gates formalisés et refus de publication |
| [11 — Contribuer en parallèle](docs/11_CONVERSATIONS_PARALLÈLES.md) | Protocole pour plusieurs conversations IA |
| [12 — Publication et intégrations](docs/12_INTÉGRATION_KRISTAL_MOODLE.md) | Build v9, fédération UCKK, exports |
| [13 — Gouvernance et changements](docs/13_GOUVERNANCE_ET_VERSIONS.md) | Gel, révisions, arbitrages |
| [14 — Vocabulaire contrôlé](docs/14_VOCABULAIRE_CONTRÔLÉ.md) | Champs et valeurs autorisées |
| [15 — Ordre de construction](docs/15_LOTS_DE_PRODUCTION.md) | Lots non concurrents, pilote et critères de sortie |
| [16 — Registre officiel et codes](docs/16_NOMENCLATURE_OFFICIELLE_ET_REGISTRE.md) | Source unique pour nomenclature, non-invention de codes |
| **[Registre officiel Québec](REFERENCES_OFFICIELLES_QC.md)** | **14 programmes et accès aux sources ministérielles; codes administratifs qualifiés seulement** |
| [Registre des 202 Kristals](catalogue/REGISTRE_202_KRISTALS.md) | Liste d'identités issue du catalogue précédent |

## Modèles à employer sans exception

- [Feuille d’apprentissage](modeles/MODELE_MICROPARCOURS.md)
- [Référence et preuves](modeles/MODELE_ALIGNEMENT.md)
- [Assemblage](modeles/MODELE_ASSEMBLAGE.md)
- [Plan d'épreuve](modeles/MODELE_PLAN_EPREUVE.md)
- [Livraison de conversation](modeles/MODELE_LIVRAISON.md)
- [Mandat de conversation](modeles/BRIEF_CONVERSATION_PARALLELE.md)
- [Proposition de modification](modeles/MODELE_CHANGEMENT.md)
- [Proposition de code officiel](modeles/MODELE_PROPOSITION_CODE_OFFICIEL.md)

## Interprétation normative

`DOIT` = obligatoire; `NE DOIT PAS` = interdit; `DEVRAIT` = recommandé; `PEUT` = optionnel. **Tout champ inconnu DOIT rester `à_vérifier`, jamais être deviné.** Les exemples ne sont pas des validations curriculaires.

**Ordre de priorité en cas de conflit :** document ministériel applicable → faits sourcés dans `A-Kristal-ScolQc` (avec édition et couverture contrôlées) → présente norme d'organisation interne → registre éditorial des 202 unités → propositions de rédaction IA. La norme ne peut contredire le contrat technique du Framework; celui-ci gouverne les artefacts techniques v9/v10.

**Avant une contribution :** fournir à la conversation `README.md`, documents 01–11, 13–14, 16, `REFERENCES_OFFICIELLES_QC.md`, le registre des 202 IDs et le modèle correspondant; remettre un paquet de fichiers complets sans modifier d'autres identifiants.

**Compatibilité :** le passage de 1.0.0 à 1.1.0 est documenté dans [MIGRATION_REGISTRE_OFFICIEL_V1.1.md](catalogue/MIGRATION_REGISTRE_OFFICIEL_V1.1.md). Les IDs gelés ne changent pas.
