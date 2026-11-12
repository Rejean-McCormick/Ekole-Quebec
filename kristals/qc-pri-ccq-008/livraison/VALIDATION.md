# Rapport de validation — `qc-pri-ccq-008` v1.2

**Objet :** delta de 14 fichiers exclusivement sous `kristals/qc-pri-ccq-008/` pour fusion au workspace v1.2 existant. **Statut :** contrôles techniques effectués, revue pédagogique humaine requise; ni publication, ni homologation, ni certification.

## Source et périmètre

Sources natives extraites de l’archive `initbundle(1).zip` contenant `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`; lecture des trois documents de gouvernance requis, du graphe central et des cinq fichiers locaux de conception (incluant `AGENTS.md`). Une seule feuille modifiée; aucune inclusion de `kristal.workspace.json`, `AGENTS.md`, `authoring/ALIGNEMENT.md`, `docs/`, `canon/`, `runtime/`, `state/`, `registry/`, `governance/` ou d’un autre Kristal.

## Changements précis

- Deux remplacements natifs : `authoring/PARCOURS.md` (frontmatter d’identité et métadonnées maintenus sauf `statut`, passé en contenu rédigé sous revue; douze sections complétées); `authoring/CONTRAT_PEDAGOGIQUE.json` (anciens champs/famille/dimensions préservés, contrat du générateur complété, statut de progression modifié).
- Six fichiers `contenu/` originaux : définitions, 2 exemples résolus, 2 contre-exemples, 2 diagnostics, 3 guidés à indices décroissants, 4 autonomes, 2 transferts distincts, remédiations et rappels différés.
- Trois fichiers `evaluation/` : plan couvrant 12 items; banque de 12 items dont 10 fixes et 2 scénarios à variantes A/B préécrites; grille critériée pour deux dialogues complets en contextes coin lecture et activité extérieure.
- Un fichier de provenance/droits et deux fichiers de livraison, sans modifications des autres dossiers de l’archive maîtresse.

## Tests techniques réellement exécutés

Le validateur indépendant du contenu a été exécuté après génération. Il a vérifié :

1. Existence et non-vacuité des 14 fichiers, noms et ordre des 14 chemins (sans fichier supplémentaire, dossier englobant, chemin absolu ni séquence de remontée).
2. Parsing des trois JSON stricts (`CONTRAT_PEDAGOGIQUE`, `BANQUE_ITEMS`, `MANIFEST`) et du frontmatter YAML.
3. Préservation des métadonnées, identifiants, objectif/critère, domaine, préalables et famille originaux du workspace v1.2; conservation de toutes les clés natives et de celles de sa famille, hors changement de statuts documenté.
4. Concordance des liens v1.2 et du graphe : aucun `requires` sortant, aucune recommandation sortante; liens entrants non transformés en obligations.
5. Exactement douze sections ordonnées dans `PARCOURS.md`; couverture du diagnostic, guidage, autonomie, remédiation, accessibilité, maîtrise, rappel et transfert.
6. Douze items sans doublons (`q-001` à `q-012`) avec consigne, stimulus, réponse/rubrique, critères, feedback, mode, difficulté, objectif, critère, famille et `validation_status = a_revoir`.
7. Deux scénarios A/B exclusivement dans le corpus fermé : calcul déterministe de parité de seed, exemples opposés et correspondance au corrigé; aucune génération IA libre.
8. Deux preuves autonomes distinctes (`q-011`, `q-012`) avec chacune un protocole de trois tours apprenant, deux relances scriptées partenaire, critères et condition sans indice.
9. Présence des garanties d’accessibilité, de confidentialité, de protection des convictions et de traçabilité des droits. Cela n’est **pas** une certification de conformité juridique ou d’absence de biais.
10. Correspondance stricte du manifeste au ZIP, intégrité ZIP, absence de dossiers ou fichiers globaux, et vérification du premier chemin.

**Résultat :** contrôles automatisés exécutés et réussis; les vérifications sémantiques ponctuelles correspondent aux corrigés rédigés. Le journal du validateur est conservé hors livraison : seuls les 14 fichiers de la liste figurent dans le ZIP. Aucune application réelle, élève, enregistrement ou essai d’écoute/situation n’a été testé.

## Limites non résolues — revue humaine nécessaire

- Vérifier l’âge et le niveau langagier selon la projection primaire retenue; observer l’accessibilité réelle avec des moyens CAA.
- Faire relire les scénarios fictifs par une personne compétente pour vérifier équité culturelle, absence de stéréotypes, ambiguïtés de corrigé et situations involontairement sensibles.
- Tester les grilles et seuils sur des dialogues réels; les exemples de réponses sont des productions originales **illustratives**, pas un étalon certifié; l’évaluation critériée demande un observateur formé.
- Vérifier le dispositif de consentement, conservation minimale de traces et procédures de protection si un outil LMS enregistre les échanges.
- Aucune étude d’efficacité, épreuve standardisée, revue externe des droits ou homologation officielle n’a été réalisée.

## Propositions structurelles (NON appliquées)

- Ajouter dans un prochain schéma central un objet facultatif `preuves_dialogue` décrivant le nombre de tours et le protocole du partenaire, sans l’imposer rétrospectivement.
- Normaliser la distinction `aide_accessibilite` / `indice_contenu` dans le schéma de traces LMS plutôt que dans les connaissances du Kristal.
- Prévoir un registre versionné d’approbation humaine des scénarios A/B et rubriques, **sans** modifier `registry/` ou `governance/` dans ce delta.

## Instructions de fusion

Extraire l’archive maîtresse puis, dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, décompresser `qc-pri-ccq-008_livraison_v1.2.zip`. Toutes ses entrées commencent directement par `kristals/qc-pri-ccq-008/`; les deux fichiers `authoring/` existants sont les seules substitutions, les douze autres sont créés.
