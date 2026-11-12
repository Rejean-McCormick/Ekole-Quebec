# VALIDATION TECHNIQUE ET PÉDAGOGIQUE — qc-pri-ap-008

**Livrable :** `qc-pri-ap-008_livraison_v1.2.zip` — delta de 14 fichiers, racine `kristals/qc-pri-ap-008/`. **Statut :** `a_revoir` (non publié, non homologué, non certifié).

## Contrôles effectivement exécutés (scripts locaux de fabrication/validation)

1. **Lecture des sources de la base réelle :** documents de gouvernance, graphe JSON, fichiers `authoring` initiaux et référence locale `REFERENCES_EVIDENCE.md` depuis le ZIP maître inclus dans `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`; cible repérée sans nouveau dépôt.
2. **Contrat natif :** relecture JSON; champs d'origine du contrat et de sa famille conservés avec mêmes valeurs et identifiants; champs requis de génération ajoutés; pas de modification des autres familles ou workspaces.
3. **YAML :** parse PyYAML et comparaison du bloc initial de `PARCOURS.md` avec la base, **tous les champs et valeurs de frontmatter identiques**; 12 sections numérotées 1 à 12 et renseignées.
4. **Graphe :** JSON parsé; `qc-pri-ap-008` possède une relation sortante `requires` vers `qc-pri-ap-007`, aucune autre relation propre; objectif, preuve, liens et famille identiques à la base.
5. **Contenus :** présence des dix planches A–J, de deux diagnostics D1/D2, de deux exemples et deux contre-exemples, de trois pratiques guidées G1/G2/G3 à indices dégressifs, de quatre pratiques autonomes A1–A4 et de deux transferts T1/T2; contrôles par sections et inspection rédactionnelle, non essai sur élèves.
6. **Évaluation :** `BANQUE_ITEMS.json` strict parsé; dix identifiants q-001 à q-010 distincts et ordonnés; chaque item comporte tous les champs du format imposé, un stimulus complet avec description neutre, une réponse ou production possible, des critères et un feedback; deux preuves terminales q-009 et q-010 sur des contextes différents; `mode=fixe`, `seed=null`, `parametres=null`, `validation_status=a_revoir`.
7. **Fidélité :** les grilles fixes et les observations-modèles ont été vérifiées manuellement en comparaison avec la matrice déclarée, sans prétendre garantir une seule interprétation esthétique. Aucun solveur mathématique requis : il s'agit d'appréciations humaines à critères explicites.
8. **Sécurité, droits, accessibilité :** relecture des passages relatifs aux outils non coupants, accès visuel/textuel/tactile, non-évaluation des goûts, scénarios fictifs et créations didactiques originales; aucune image protégée importée. Vérification documentaire seulement, sans audit juridique, contraste mesuré ni essai réel d'accessibilité.
9. **Paquet :** contrôle automatisé final du ZIP, de l'ordre/quantité des chemins (14 exacts), de leur taille non nulle, de la racine imposée, de l'absence de `../`, chemins absolus, fichiers globaux ou dossiers additionnels, du manifeste exact et des JSON, puis CRC de toutes les entrées et simulation de fusion par superposition avec les chemins autorisés.

## Limites, décisions et revue humaine indispensable

- Relecture par spécialiste des arts plastiques et par personne connaissant le français québécois, pour précision des critères et richesse culturelle; ajuster si le corpus de grilles est trop schématique pour une vraie appréciation d’œuvres.
- Revue d'une personne spécialiste de l'accessibilité (rendu variable des carrés colorés/emoji, descriptions neutres, perception de couleur, lecteur d'écran et matériel tactile). Les alternatives doivent préserver la tâche sans livrer les jugements.
- Essais avec élèves/enseignants : vérifier durée, compréhension des instructions, stabilité des notations, désaccords inter-évaluateurs et faisabilité des deux prestations sans indices; calibrer le seuil 7/8, qui est un choix de conception non étalonné.
- Audit de droits si ajout ultérieur d'œuvres réelles; aucun lien web de référence externe consulté comme source indépendante dans ce mandat. Aucune certification de droit universel sur les glyphes/emoji des plateformes.
- Les impressions et avis ne peuvent pas être corrigés comme résultats numériques déterministes; validation humaine indispensable. Les exemples donnés ne sont pas des goûts attendus.

## Propositions de structure — **non appliquées**

- Prévoir dans un futur schéma central un champ stable de description textuelle neutre et référence de rendu visuel/tactile contrôlé pour chaque stimulus.
- Séparer explicitement dans le moteur d’évaluation `aide_acces` et `indice_cognitif`, et documenter les preuves indépendantes P1/P2 sans moyenne.
- Ajouter plus tard un emplacement approuvé pour des œuvres authentiques avec champs `source`, `licence`, `credit`, `version_visuelle`, sans modifier ce delta de 14 fichiers ni les registres globaux.

**Conclusion :** les validations techniques automatisées recensées sont réalisées; la qualification pédagogique et l'accessibilité réelle restent à revoir. Aucun statut « publié », « homologué » ou « certifié » n'est revendiqué.
