# Rapport de validation réellement exécutée — qc-pri-ma-030

**Version source :** archive `initbundle(1).zip`, workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, frame de départ v1.2.  
**Statut :** vérifications techniques locales concluantes; items et textes **à revoir humainement**, sans publication ni certification.  
**Décision :** delta prêt pour vérification de fusion et revue humaine, mais non qualifié comme cours publié.

## Contrôles exécutés (script local de construction et de validation)

- **123 assertions** de cohérence et de présence exécutées sans échec, dont préservation exacte de l'en-tête YAML source et validation de ses 12 sections.
- Comparaison du contrat JSON d'origine avec sa version enrichie : identifiant, objectif, notion, preuve, champs et famille d'origine préservés; nouveaux paramètres réglementaires internes présents.
- Banque `qc.learning-item-bank/1.0` : **12 items complets**, numérotés q-001 à q-012 sans doublon; références `obj-1`, `crit-1` et `qc-pri-ma-030-ev-01` présentes sur chaque item.
- Chaque item a été revérifié en **recomptant ses observations brutes depuis la chaîne de stimulus** et en comparant catégories, effectifs, somme, indices de position et tableau corrigé; aucune réponse corrigée par simple génération libre.
- **600 instances paramétriques** (= 6 modèles × 100 graines entières dans leurs domaines bornés) calculées avec la formule de référence, puis revérifiées par décompte indépendant de la liste produite; en outre les **18 exemples embarqués** (3 par item) ont été comparés à leurs corrigés calculés.
- Deux preuves de maîtrise distinctes : q-011 (inventaire sportif, 15 observations, trois catégories) et q-012 (véhicules, 16 observations, quatre catégories); autonomie et non-compensation explicitement exigées dans la grille.
- Présence contrôlée de deux diagnostics, trois activités guidées à indices dégressifs, quatre pratiques autonomes, deux exemples expliqués, deux contre-exemples et deux transferts distincts.
- Vérification des listes de préalables stricts et de l'ordre conseillé : vides dans le cadre original; aucune arête sortante dans le graphe central pour ce Kristal.
- Vérification rédactionnelle **de présence**, et non audit exhaustif, des consignes d'accessibilité et des notes de provenance/droits.

## Contrôle du livrable ZIP

L'archive finale est construite exclusivement à partir des **14 chemins** dans `MANIFEST.json` sous `kristals/qc-pri-ma-030/`. Le script de finalisation vérifie : correspondance exacte des entrées au manifeste, absence de dossier englobant, chemins sans `../` ou chemin absolu, premier chemin sous le préfixe exigé, absence d'entrées supplémentaires, fichiers non vides, lecture/parsing des trois fichiers JSON, et test d'intégrité ZIP avec `testzip()`. Ces contrôles finaux sont exécutés après écriture du rapport. Aucun autre workspace n'est modifié ni empaqueté.

## Ce qui demeure non résolu

- **Revue pédagogique et mathématique humaine** des formulations, étendue et progressivité des exercices, exactitude pratique de la grille et acceptabilité du niveau de langue.
- **Essai en situation réelle** : ergonomie sur écran et matériel, modalités vocales/tactiles, fonctionnement des adaptations, conditions et durée de passation.
- **Revue des droits de diffusion** propres au projet : ce delta est rédigé de manière originale; les sources internes ont servi de références, sans vérification juridique d'une licence de distribution.
- **Validation de qualification locale/framework** et insertion effective dans une copie d'intégration du workspace : seules la structure ZIP et sa compatibilité de chemins sont vérifiées ici; aucun build canonique v9, déploiement, ni publication.
- **Vérification des rendus didactiques** dans le LMS choisi : aucun LMS n'a été utilisé.

## Propositions de structure, non appliquées

1. Centraliser un schéma JSON de validation stricte de `BANQUE_ITEMS.json` et des rubriques, avec versions explicites.
2. Ajouter au moteur d'items une fonction de contrôle indépendante stockant le hash des observations et de leurs effectifs.
3. Prévoir un adaptateur d'accessibilité pour lire chaque observation et sa position sans fournir les effectifs.
4. Documenter dans le registre de revue humaine la décision sur les seuils d'autonomie, plutôt que changer la gouvernance pendant la rédaction d'un Kristal.

**Aucun fichier de `governance/`, `registry/`, `AGENTS.md`, `kristal.workspace.json` ni aucun autre ID n'est inclus dans le ZIP.**
