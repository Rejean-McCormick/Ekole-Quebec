# Validation et journal de livraison — qc-pri-ad-004 (v1.2)

**Statut :** delta développé, contrôles techniques exécutés, **revue pédagogique humaine et publication non effectuées**. Archive finale : `qc-pri-ad-004_livraison_v1.2.zip`. Version source : frame v1.2 incluse dans `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip` sous `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Le ZIP distinct du seul workspace maître n'a pas été fourni séparément; les 8 fichiers sources requis ont néanmoins été retrouvés dans l'arborescence d'origine.

## Contrôles réellement exécutés

1. **Présence de la source** : lecture des trois documents de gouvernance, du graphe, et des quatre fichiers `authoring` locaux; existence et taille non nulle confirmées.
2. **Identité conservée** : frontmatter YAML v1.2 reparsé, comparé champ à champ à la frame (format, ID, titre, discipline, objectif, critère, statut, version, préalables, liens, auteur, autres champs); douze sections numérotées 1 à 12 présentes une fois chacune.
3. **Contrat JSON préservé** : tous les champs et valeurs d'origine conservés récursivement, famille initiale inchangée pour les champs existants; champs obligatoires de famille ajoutés.
4. **Graphe et références** : arête sortante stricte `qc-pri-ad-004 -> qc-pri-ad-003` vérifiée; aucune arête d'ordre recommandé sortante; les arêtes ENTRANTES ne deviennent pas des préalables.
5. **Banque** : JSON strict parsé, identifiants `q-001` à `q-010` sans doublons, dix items avec champs obligatoires, références `obj-1` / `crit-1` / famille identiques, réponses observables, critères, feedbacks et limites de variation non vides; modes fixes, seed/paramètres `null` cohérents.
6. **Deux preuves** : q-009 (station météo imaginaire) et q-010 (musée de fossiles imaginaires), situations distinctes, prestations réellement jouées, observation d'un pair et justifications a posteriori.
7. **Cohérence qualitative vérifiée dans les documents** : quatre notions, deux exemples commentés, deux contre-exemples, deux tâches diagnostiques, trois exercices guidés à soutien décroissant, quatre pratiques autonomes, deux transferts, remédiations, protections de sécurité, droits et accessibilité documentés. Il s'agit d'un contrôle éditorial **documentaire**, pas d'une expérience utilisateur ni d'une validation externe des critères.
8. **ZIP/fusion** : exactement 14 entrées non vides, chacune dans `kristals/qc-pri-ad-004/`, premier chemin conforme, sans racine englobante, fichier central, autre Kristal, doublon, chemin absolu ou `../`; manifeste identique à la liste réelle; `ZipFile.testzip()` sans erreur et fichiers JSON relus depuis le ZIP.

Les assertions automatisées ont été lancées dans l'environnement de création et leurs résultats sont consignés ci-dessous; aucune homologation, essai auprès d'élèves ni contrôle automatique de valeur artistique n'en découle.

## Limites ouvertes / révision humaine

- **Revue disciplinaire obligatoire** : vérifier authenticité du jeu dramatique, neutralité des scénarios, interprétabilité des quatre critères et seuil descriptif (trois dimensions à 2/2 et une à 1/2 minimum, sur chaque preuve), durée des tâches et qualité du retour par pair.
- **Essai réel obligatoire** : intelligibilité des scènes q-009/q-010 par des pairs naïfs, sécurité, accessibilité motrice, verbale et sensorielle, alternatives avec aides techniques et communication alternative; vérifier les cas où les spectateurs ne peuvent pas observer l'effet.
- **Droits** : aucun contenu tiers incorporé ou droit externe affirmé. Toute illustration, musique, vidéo ou capture ajoutée en aval nécessite contrôle des licences, consentement et règles locales de conservation.
- **Technique** : non testé dans le moteur de questions, LMS ni chaîne de qualification finale; la structure JSON du manifeste est locale, sans prétention de schéma central validé.
- **Méthode d'évaluation** : aucune « génération IA libre » en contrôleur; les dix stimuli sont fixes. La qualité des rubriques reste à revoir humainement. Aucune conformité détaillée au PFEQ requise ni revendiquée.

## Propositions à soumettre au niveau central (aucune base modifiée)

1. Ajouter au format standard un marqueur optionnel `preuves_maitrise` permettant de lier explicitement q-009/q-010, l'observateur et la modalité, sans changer les objectifs.
2. Autoriser une structure standardisée de rubriques qualitatives à 4 dimensions avec niveau 0/1/2 et preuve descriptive de chaque niveau.
3. Prévoir un champ standard `adaptations_autorisees` distinct des indices qui briseraient l'autonomie narrative; documenter la preuve d'équivalence diagnostique du préalable.
4. Évaluer un protocole de confidentialité/consentement pour les captations éventuelles; aucune captation n'est requise ici.

## Journal de changements du delta

- Remplacement complet du `PARCOURS.md` local tout en conservant le YAML v1.2, les 12 sections et l'identité.
- Remplacement complet du `CONTRAT_PEDAGOGIQUE.json` local, sans suppression des champs originaux; instrumentation de la famille.
- Création de six documents de contenu, trois documents d'évaluation, référence de provenance, manifeste et ce rapport.
- Aucun ajout, écrasement ou inclusion de `kristal.workspace.json`, `AGENTS.md`, `ALIGNEMENT.md`, `docs/`, `canon/`, `state/`, `runtime/`, `governance/`, `registry/`, ni d'autres IDs.

**Résumé d'exécution automatisée :** voir la ligne `TESTS_FINAL` à la fin du présent rapport.
