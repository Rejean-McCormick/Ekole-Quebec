# Journal de validation et limites — `qc-pri-fr-022`

**Périmètre :** delta de 14 fichiers, uniquement sous `kristals/qc-pri-fr-022/`, superposable au workspace d’origine sans remplacer les fichiers centraux. **Source de la base :** dossier `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` contenu dans le ZIP `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`, et non une archive Frames indépendante.

## Contrôles réalisés localement (résultats de la passe de validation)

1. **Base vérifiée :** présence et lecture des huit entrées demandées (trois fichiers de gouvernance, graphe, quatre fichiers d’authoring); le graphe contient `qc-pri-fr-022/requires/qc-pri-fr-021`.
2. **Identité et métadonnées :** YAML lisible; 12 sections numérotées conservées; identifiant, titre, discipline, résultat, preuve, préalable et famille strictement conservés; seul `revision_contenu` passe de `0.2.0` à `0.3.0`. Le statut `en_rédaction` reste inchangé. Comparaison structurelle des champs v1.2 originaux du JSON de contrat : aucune suppression ni altération d’une valeur préexistante.
3. **Évaluation :** JSON strict et parsable; 11 items numérotés `001`–`011` sans doublons, chacun lié à `obj-1`, `crit-1`, `qc-pri-fr-022-ev-01`; chaque stimulus contient les étiquettes présentes dans son ordre attendu, sans double emploi. Vérification automatique que les justifications couvrent chaque transition de la clé d’ordre.
4. **Deux manifestations :** `q-008` et `q-009` sont autonomes, sans indices, et correspondent à des contextes et à des représentations différentes (récit / explication). Couverture constatée : 2 diagnostics, 3 guidés, 4 autonomes et 2 transferts.
5. **Structure du paquet :** 14 fichiers listés exactement dans le manifeste, tous non vides; racine interne `kristals/qc-pri-fr-022/`; ni dossier englobant ni autre Kristal; aucune entrée absolue ni séquence `../`; aucun fichier central du workspace dans le ZIP. Le premier chemin commence bien par le préfixe imposé.
6. **Droits, sécurité et accessibilité (contrôle documentaire, non audit externe) :** énoncés fictifs originaux; pages externes listées dans les références, aucune reproduction de leurs exemples; pas de données personnelles ni de contexte à risque identifiés dans les énoncés. Consignes et grille prévoient lecture neutre, manipulation d’étiquettes, justification transcrite et distinction des aides d’accès / aides de contenu.
7. **Liens internes :** chemins de renvoi vers `contenu/`, `evaluation/` et `sources/` contrôlés sur les fichiers livrés; `qc-pri-fr-021` n’est référencé que comme préalable et n’est ni modifié ni empaqueté.

La vérification de l’ordre des étiquettes, des clés et de leurs transitions est **technique**, non une preuve de correction sémantique automatisée ou d’équivalence psychométrique. Une relecture manuelle du corpus et des réponses a été effectuée lors de la rédaction, mais **aucune revue humaine externe** n’a eu lieu.

## Limites non résolues — publication interdite tant que non traitées

- **Validation linguistique et didactique par une personne compétente :** confirmer naturalité des phrases, unicité des chaînes de référence, possibilité de réponses alternatives et adéquation du barème aux enfants destinataires.
- **Essais en situation réelle :** qualité des consignes, temps de passation, fatigue, difficultés inattendues, effets des aménagements et constance entre évaluateurs; aucune donnée d’essai ni étalonnage n’est disponible.
- **Accès numérique / Moodle / Framework :** aucun test d’intégration LMS, de synthèse vocale, de manipulation au clavier, de lecteurs d’écran ou de contraste rendu à l’écran; l’accessibilité est seulement prévue à l’écrit.
- **Droits :** aucune expertise de droits d’auteur, aucune vérification automatisée d’originalité ni attestation formelle de licence; conditions de diffusion à décider séparément.
- **Normes centrales :** aucune validation de conformité détaillée au PFEQ requise; `alignement_statut: à_vérifier` est conservé, sans assertion d’homologation.
- **Génération de variantes :** le mode livré est `fixe` uniquement; toute variante sémantique ou banque de remplacement demanderait nouveaux énoncés, corrigés et revue. Les items gardent `validation_status: a_revoir`.

## Propositions de changement structurel, sans modification des bases centrales

1. Introduire **dans un futur schéma central versionné** une propriété facultative `critere_id` dans les familles d’évaluation; aujourd’hui le contrat natif est préservé avec le champ additionnel `critere` et une description.
2. Ajouter plus tard un champ explicite `modalite_acces` et un indicateur `aide_sur_contenu` dans les traces de passation pour distinguer lecture neutre et indice affectant l’autonomie.
3. Prévoir un workflow de revue humaine versionné des items fixes et un jeu d’items neufs pour les reprises après remédiation. Aucun nouveau statut canonique n’est créé ici.

**Statut de livraison :** contrôles techniques locaux effectués; **revue humaine nécessaire**, non qualifié, non certifié, non publié, non homologué.
