# Validation de livraison — `qc-pri-ilss-006`

## Source, périmètre et statut

Delta fusionnable dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, extrait de l'archive **effectivement fournie** `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip` (qui contient l'arborescence maîtresse). Les **huit sources** demandées ont été ouvertes : trois textes de gouvernance, le graphe central et quatre fichiers d'`authoring/` de `qc-pri-ilss-006`. Aucun autre Kristal n'a été modifié. Les métadonnées YAML et les champs canoniques du JSON v1.2 ont été conservés.

## Contrôles exécutés localement

- **400 assertions préalables réussies** (voir le journal de construction) : fichiers présents, frontmatter YAML identique à l'original et parsable, 12 sections dans l'ordre, identité/titre/objectifs/preuve, préalable et liens du graphe, familles natives et 13 champs minimum, 10 items JSON complets sans doublon, statut `a_revoir`, consignes, réponses et repères textuels, 2 contextes de maîtrise non repris mot à mot de l'enseignement, présence des sections et tâches pédagogiques, droits, sécurité, accessibilité, plan et grille.
- **Contrôle des corrigés exécuté :** pour chacun des 10 items, présence des deux indices factuels ciblés dans la concaténation du stimulus et de son corrigé, ainsi que réponses annotées pour T/C/I/D et feedback; pour les 10, comparaison pédagogique de l'énoncé, des relations demandées et des faits du corrigé au moment de la rédaction. Ce test *ne prouve pas* l'exhaustivité des formulations équivalentes ni leur validation par un second évaluateur.
- **Contrôle d'emballage effectué par le script de livraison :** le ZIP est créé uniquement avec les 14 entrées prescrites, dans le même ordre que `MANIFEST.json`, au préfixe `kristals/qc-pri-ilss-006/`; test de décompression, de non-vacuité, d'absence de `../` et de chemin absolu, de validité JSON et d'intégrité CRC. Les valeurs numériques des tests post-ZIP se trouvent dans le journal d'exécution local; aucune fusion sur un workspace de production n'a été simulée.

## Exemples et critères de contrôle des réponses

- `q-005` : équipe 2 → dessin; équipe 1 → salle 4; lecture correcte de deux **lignes différentes** du tableau.
- `q-008` : d'abord placer le carton sans colle; enfin inscrire le nom du projet; ne pas inverser la séquence.
- `q-009` : séance de casse-têtes commençant à **13 h 10** (non 13 h 30); étagère verte = rangement final. **Preuve d'organisation**.
- `q-010` : suivi du pot A : **jour 7**, deux feuilles visibles, après la tige visible au jour 4; pas d'inférence sur les jours absents. **Preuve de lecture de tableau**.

## Limites et revue humaine nécessaire

1. **Revue linguistique et d'équité ILSS :** simplicité et neutralité des 10 documents, présupposés culturels éventuels, reconnaissance des réponses courtes ou plurilingues; essai auprès d'apprenants variés avant toute décision institutionnelle.
2. **Revue des critères :** stabilité des niveaux de maîtrise et cohérence des décisions entre deux évaluateurs sur productions réelles; aucun étalonnage empirique ni mesure de fidélité interjuges réalisé.
3. **Accessibilité réelle :** tester lecteurs d'écran et navigation linéaire des tableaux dans la plateforme cible; les supports textuels ont été conçus, mais aucun audit automatisé d'accessibilité de la plateforme n'a été exécuté.
4. **Modalité de lecture :** en cas de lecture complète du document par autrui, observer une seconde navigation écrite personnelle avant de statuer sur la compétence de lecture; les outils de suivi ne sont pas fournis ici.
5. **Droits et sources :** stimuli créés pour cette livraison, sans extraits tiers; la diffusion des fichiers maîtres fournis par le propriétaire et les éventuelles traductions ultérieures nécessitent un contrôle éditorial externe.
6. **Technicité :** le moteur LMS et les exigences d'un schéma JSON central non présent ne sont pas exécutés ici; JSON syntaxiquement valide et champs du contrat vérifiés. Aucun contenu qualifié de « certifié », « homologué » ni « publié ».

## Propositions **sans modification** de structure centrale

- Proposer au responsable du registre une métadonnée optionnelle `modalite_navigation_textuelle` pour distinguer lecture indépendante / audio / assistance, sans changer l'objectif.
- Proposer un format partagé d'enregistrement des traces de jugement T/C/I/D/O/A; ne pas inscrire les productions personnelles dans les connaissances canoniques.
- Proposer un protocole de revue de variantes linguistiques et un test d'accessibilité des tableaux à l'import LMS.

**Statut final demandé :** matériaux construits et vérifications techniques de delta réalisées; **relecture humaine et essai d'usage requis**.
