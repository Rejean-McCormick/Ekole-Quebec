# Rapport de validation — `qc-pri-us-005` (v1.2)

**Statut :** contrôles de structure et de cohérence effectués; **revue pédagogique, historique, linguistique, interculturelle et d’accessibilité humaine requise**. Aucun statut certifié, homologué ou publié. **Date du contrôle :** 2026-10-09.

## Provenance et delta

- Source lue : `Spec_Kristals_Parcours_Primaire_Qc_v1.1(1).zip`, contenant le répertoire maître `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` et la frame `kristals/qc-pri-us-005/`. Le nom du ZIP conteneur est v1.1, mais le sous-dossier et les normes lus portent la version pédagogique **1.2**; aucune nouvelle frame n’a été inventée.
- Ont été consultés sans être livrés : normes v1.2 (contrat, générateur, charte), graphe, `authoring/ALIGNEMENT.md`, `authoring/BRIEF_REDACTION.md` et les fichiers d’origine du parcours et du contrat.
- Deux remplacements : `authoring/PARCOURS.md` et `authoring/CONTRAT_PEDAGOGIQUE.json`. Douze fichiers de contenu, évaluation, sources et livraison ont été rédigés. Aucun changement au registre central ni aux autres Kristals.
- Frontmatter YAML : tous les champs natifs conservés à l’identique **sauf** `statut` et `revision_contenu` mis à jour pour identifier le contenu rédigé; les 12 sections ont été conservées dans leur ordre. Contrat JSON : format et identifiants v1.2 conservés, famille étendue avec les champs minimaux du générateur; `seed=null` aux items fixes contrôlés.

## Tests effectivement exécutés sur les fichiers de travail

Script de vérification : analyse Python des contenus avec parseurs `json`, `yaml` et expressions régulières. **231 assertions positives avant empaquetage**, dont :

- **Emballage : 32 tests réussis**, exhaustivité des 14 fichiers, noms, encodage, contenu non vide et absence de marqueurs provisoires.
- **Métadonnées : 36 tests réussis**, YAML lisible, champs canoniques conservés, 12 sections, quatre notions et référence facultative.
- **Contrat : 33 tests réussis**, préservation du schéma original, champs de famille ajoutés, absence de requires et séquence bloquante dans le graphe, lien de renforcement.
- **Évaluations : 100 tests réussis**, JSON strict, 12 IDs uniques et contigus, champs et rattachements, 2 contextes de maîtrise, consignes et corrigés présents, absence de tirage libre.
- **Corrections : 13 tests réussis**, présence des indices factuels attendus dans les scénarios/solutions et d’une limite formulée; contrôle de cohérence interne, pas validation historique des faits fictifs.
- **Contenu : 13 tests réussis**, deux exemples/contre-exemples, deux diagnostics, trois guidages, quatre pratiques, deux transferts, accessibilité, droits et références explicités.
- **Manifeste : 4 tests réussis**, format, version, ID, archive_root, liste des 14 chemins et statut non publié.

**Portée des tests de corrigés :** vérification mécanique de la présence des indices textuels clés et des limites dans les 12 réponses attendues, suivie d’une relecture rédactionnelle des conclusions proposées. Cela **n’est pas** un vérificateur indépendant des interprétations et ne valide pas des événements historiques réels. Les scénarios sont expressément fictifs.

**Contrôles du ZIP final :** 16 assertions complémentaires sont exécutées après l'écriture du rapport : fichier ouvrable, premier chemin, nombre et ordre des entrées, racine unique, absence d'éléments hors périmètre, chemins sûrs, entrées non vides, CRC, parsing des trois JSON, extraction temporaire et identité des octets, manifeste synchronisé, rapport non provisoire. Le livrable n'est déclaré prêt qu'après la réussite de ces 16 tests. Ces contrôles ne constituent pas un audit de sécurité complet.

## Limites et revue humaine ouverte

1. Relecture par une personne compétente en enseignement de l’histoire : justesse des inférences, couverture des concepts, distinction entre trace écrite et événement réel, qualité des consignes et des corrigés.
2. Revue de l’âge scolaire visé, de la lisibilité des stimuli et de leur durée de passation, essai de correction interjuges, biais possibles et validation du seuil R1–R4 sur deux dossiers distincts.
3. Revue d’accessibilité réelle (assistive technology, oral/transcription, lecture en classe), et validation culturelle avant intégration; ne pas inférer que de simples options rédigées prouvent une accessibilité testée.
4. Droits : les mini-sources ont été créées pour ce Kristal et ne reproduisent pas d’images d’archives; aucune licence externe présumée, tout emprunt futur exige examen de droits et provenance.
5. Aucune homologation ou correspondance fine au PFEQ n’a été testée ni demandée. Aucun examen n’est certifié; tous les items demeurent `a_revoir`.

## Propositions de structure **non appliquées**

- Un champ central facultatif distinguant « scénario fictif d’apprentissage » et « source archivistique authentifiée » pour éviter toute confusion en LMS.
- Un champ de traçabilité `date_evenement_evoque` distinct de `date_creation` et `date_transcription` pour les futurs stimuli.
- Une procédure de revue interjuges et un inventaire versionné de paires sources/corrigés approuvées avant toute variation automatisée.

Ces changements ne sont proposés qu’à la gouvernance future; **aucun fichier `registry/`, `governance/`, `canon/`, `runtime/`, `state/`, `docs/`, `AGENTS.md` ou `kristal.workspace.json` n’a été modifié ni inclus.**
