# VALIDATION — qc-pri-ap-001 (delta v1.2)

**État de livraison :** rédaction complète, contrôles techniques locaux; **non certifié, non publié, non homologué**, revue pédagogique humaine requise.

## Contrôles techniques effectivement réalisés

- Présence de l'archive source, lecture des trois règles de gouvernance et des métadonnées originales; lecture des arêtes du graphe touchant ce Kristal.
- Conservation stricte des champs initiaux du contrat JSON et du frontmatter YAML, avec ses IDs, son objectif, ses préalables vides, sa référence d'alignement et sa famille; les ajouts d'évaluation sont des champs supplémentaires dans la famille existante.
- Vérification de la présence et de la numérotation des 12 sections; cohérence `obj-1` / `crit-1` / `qc-pri-ap-001-ev-01`.
- Contrôle de 12 identifiants distincts `q-001` à `q-012`, JSON strict parsable, modes fixes avec seed/paramètres nuls, images SVG XML parsables et descriptions alternatives présentes.
- Contrôle automatique des quatre catégories et de la présence d’un emplacement et d’une justification par annotation; analyse XML des scènes SVG et cohérence rédactionnelle vérifiée manuellement. La concordance perceptive des dessins et des corrigés demande encore une revue humaine.
- Vérification de deux preuves distinctes `q-011` et `q-012`, et de leur non-présentation complète parmi les exemples et entraînements. Règle de maîtrise à deux preuves, pas de note unique.
- Contrôle de sécurité et d'accessibilité par recherche des rubriques et indications; droits des images originaux décrits dans `sources/REFERENCES_CONTENU.md`.
- ZIP : exactement 14 fichiers tous non vides, chemins sous `kristals/qc-pri-ap-001/` uniquement, premier chemin correct, aucun `../` ni chemin absolu, JSON reparsés depuis ZIP, test d'intégrité CRC, liste exactement égale au manifeste.
- Fusion simulée sur l'index du workspace maître : 2 chemins existants remplacés, 12 nouveaux chemins ajoutés, aucun autre chemin modifié par le delta.

## Points non établis — revue humaine nécessaire

1. Exactitude perceptive des couleurs selon les appareils, contrastes, imprimantes et ressources tactiles; une perception adaptée n'est pas automatiquement équivalente.
2. Qualité didactique réelle selon l'âge, durée, vocabulaire et critères d'observation; essai avec élèves non exécuté.
3. Concordance des annotations d'évaluation entre deux correcteurs et validation du seuil : aucun essai d'accord intercorrecteurs exécuté.
4. Affichage du SVG brut dans un LMS/Markdown cible; aucun test d'intégration navigateur, Moodle ou appareil réel exécuté. Le texte de remplacement ne doit pas simplement dicter des réponses en évaluation.
5. Droit de mise en ligne sous la licence globale du workspace : régime du repo non établi ici; aucune vérification juridique externe exhaustive.
6. Validation du contenu comme canon v9 / build Framework / qualification officielle : **non exécutée**. Le ZIP n'active ni ne publie quoi que ce soit.

## Propositions sans modification des bases centrales

- Pour l'intégrateur : ajouter une conversion automatique du SVG inline en ressource graphique cacheable, assortie d'une version textuelle et d'un contrôle d'accessibilité; proposer ce changement à la gouvernance du moteur, pas dans ce delta.
- Ajouter à un processus de qualification un essai de rendu, un essai d'annotations en classe et une vérification croisée des rubriques; conserver les observations dans un outil de suivi hors des fichiers canoniques.
- Si une seconde épreuve est nécessaire après remédiation, faire homologuer en interne de nouvelles scènes sans modifier les `requires` ou le contrat central.

**Résumé du delta :** 2 remplacements intégralement compatibles (`authoring/PARCOURS.md`, `authoring/CONTRAT_PEDAGOGIQUE.json`) + 12 ajouts. Aucun `AGENTS.md`, `kristal.workspace.json`, `ALIGNEMENT.md`, ni `docs/`, `canon/`, `state/`, `runtime/`, `registry/` ou `governance/` modifié.
