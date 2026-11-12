# Validation et fusion — qc-pri-ma-006 (delta v1.2)

## Source réellement utilisée

L’archive fournie sous le nom `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip` contient le workspace embarqué `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Les documents de gouvernance, le graphe et les fichiers d'auteur de `qc-pri-ma-006` ont été lus depuis ce workspace. Ce delta vise donc le workspace embarqué existant; il ne fabrique aucun registre ou nouveau dépôt.

## Contrôles techniques réellement exécutés

- Analyse Python/YAML : en-tête valide et exactement 12 sections numérotées dans `PARCOURS.md`.
- Comparaison des identifiants et clés d'origine des deux fichiers d'auteur; maintien de l'objectif littéral, la preuve littérale, des concepts, des liens de graphe et de la famille d'évaluation.
- Analyse JSON stricte de la banque, du contrat et du manifeste; vérification des champs et du statut `a_revoir` des items.
- Banque : 10 IDs consécutifs sans doublons, liés à `obj-1`, `crit-1` et `qc-pri-ma-006-ev-01`; deux preuves différentes, bibliothèque/réunion et potager/augmentation.
- Vérification indépendante des huit sommes fixes; recomptage exhaustif de **131** paires admissibles pour q-006 et de **540** paires admissibles pour q-009, soit **671** paires : contrôle de la conservation des termes pour chaque paire, de la graine stable, de l'instance choisie et de la valeur calculée.
- Présence des deux diagnostics, trois exercices guidés avec indices dégressifs, quatre pratiques autonomes et deux transferts; ce contrôle automatique constate la présence, **pas** la qualité pédagogique.
- Résolution de l'ensemble explicite des liens internes utilisés entre les nouvelles pièces, plus la référence à `ALIGNEMENT.md` conservée dans le workspace source.
- Examen documentaire des mentions de droits, source, accessibilité et limites.
- ZIP : vérification après écriture de 14 entrées uniquement, non vides, dans `kristals/qc-pri-ma-006/`, chemin initial adéquat, absence de préfixe englobant, de chemin absolu ou de `../`, manifeste identique aux entrées et tous JSON reparsés.

## Résultats

**Contrôles automatiques : réussite des assertions exécutées dans ce lot.** Les tests certifient uniquement des propriétés syntaxiques, arithmétiques et de structure; aucune certification pédagogique, légale ou institutionnelle n'en découle.

## Limites non résolues et revue humaine indispensable

1. Faire réviser les justifications, la formulation des problèmes, la difficulté, les stratégies alternatives et les rubriques par une personne qualifiée en mathématique et pédagogie; les items demeurent `a_revoir`.
2. Tester l'usage avec des élèves et plusieurs modalités d'accès (lecture orale, vue réduite, aides techniques); la compatibilité LMS et les temps de passation ne sont pas testés.
3. Contrôler les droits de diffusion de l'archive maîtresse et les conditions institutionnelles locales; les nouvelles histoires et explications sont originales, sans preuve juridique de propriété de l'ensemble du workspace.
4. Aucune consultation directe des pages externes IES/EEF/CAST, ni audit PFEQ; les références sont secondaires à la gouvernance interne.
5. Aucun essai psychométrique, aucune vérification de biais par échantillon représentatif et aucune publication; le barème de décision est un choix de conception interne.

## Changements de structure proposés (non réalisés)

- Ajouter ultérieurement au registre central un schéma JSON versionné pour les banques d'items paramétriques (`variables`, `filtres`, `indexation`, `seed`, `instance_validee`) et un validateur indépendant partagé; **aucun registre central modifié dans cette archive**.
- Envisager un champ d'horodatage et de revue pédagogique humaine (`reviewer`, `review_date`, `evaluation_trial`) dans une prochaine version de contrat, après décision centralisée; aucun champ obligatoire existant supprimé.

## Instructions de fusion

Décompresser l'archive maîtresse et entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Extraire `qc-pri-ma-006_livraison_v1.2.zip` à **cet endroit**, en écrasant exclusivement `kristals/qc-pri-ma-006/authoring/PARCOURS.md` et `kristals/qc-pri-ma-006/authoring/CONTRAT_PEDAGOGIQUE.json`; les douze autres fichiers sont ajoutés. Ne pas extraire au dossier parent du workspace, sinon les chemins ne se superposent pas correctement. Aucun contenu `canon/`, `docs/`, `state/`, `registry/`, `governance/` ou `runtime/` inclus ou changé.
