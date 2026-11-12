# Validation et limites — `qc-pri-us-014`

**Archive de base effectivement consultée :** `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`, contenant sous `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` les fichiers v1.2 demandés. Le fichier indépendant nommé `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis.zip` n'a pas été fourni séparément; le dossier intégré dans l'archive reçue sert de source. **Aucun nouveau dépôt reconstitué.**

## Contrôles réellement exécutés (script local)

Cette section consigne uniquement les tests automatisés programmés et exécutés sur les fichiers de la livraison; les vérifications humaines ci-dessous restent ouvertes.

- RÉUSSI — Archive maîtresse consultable et chemins sources présents
- RÉUSSI — Conservation stricte de la section YAML native
- RÉUSSI — Conservation des sections 1 à 12 (une fois chacune)
- RÉUSSI — Conservation des champs racine et valeurs natifs du contrat
- RÉUSSI — Conservation de tous les champs existants de la famille
- RÉUSSI — Présence des 13 champs minimum de génération
- RÉUSSI — Famille et identité dans le contrat
- RÉUSSI — Objectif, preuve et concepts immuables
- RÉUSSI — Relations de graphes immuables
- RÉUSSI — Banque JSON au format exigé
- RÉUSSI — Exactement huit items
- RÉUSSI — Numéros uniques q-001 à q-008
- RÉUSSI — Chaque item complet non vide
- RÉUSSI — Huit contextes distincts dans les stimuli
- RÉUSSI — Preuves de maîtrise distinctes 1912 et 2024
- RÉUSSI — Deux réponses détaillées de maîtrise et limites
- RÉUSSI — Tous corrigés cohérents avec les dates de stimuli (contrôle semi-automatique)
- RÉUSSI — Item q-006 distingue date objet/date rédaction
- RÉUSSI — Au moins 2 exemples et 2 contre-exemples explicites
- RÉUSSI — Diagnostic D1/D2
- RÉUSSI — Guidage 3 tâches avec indices dégressifs
- RÉUSSI — 4 autonomes A1-A4 avec corrigés
- RÉUSSI — Deux transferts différents T1/T2
- RÉUSSI — Plan d’évaluation trace tous 8 items
- RÉUSSI — Grille décision non basée sur score unique
- RÉUSSI — Sources historiques URL vérifiables incluses
- RÉUSSI — Droits et perspective autochtone balisés
- RÉUSSI — Accessibilité décrite
- RÉUSSI — Contenu non homologué et qualification humaine
- RÉUSSI — JSON strict banque / contrat / manifeste
- RÉUSSI — Liste manifeste des 14 chemins exacts
- RÉUSSI — Absence de ../ et chemins absolus
- RÉUSSI — Aucune entrée autre ID dans manifeste
- RÉUSSI — Liens structurels livrés connus dans les MD
- RÉUSSI — Formats 8 items sans paramètres aléatoires simulés
- RÉUSSI — 8 textes et rubriques contiennent des indices contrôlables

**Bilan de ces contrôles avant empaquetage : 36/36 réussis.** Les confirmations supplémentaires sur le ZIP final sont inscrites en fin de document ci-dessous. Le contrôle de qualité des corrigés est principalement **éditorial interne** (comparaison manuelle des réponses et des énoncés pendant la rédaction) ; la vérification automatisée ne prouve pas l'exactitude historique ou didactique.

## Limites non résolues

- **Validation scientifique :** les pages UNESCO et Parcs Canada ont été consultées, mais aucune expertise historique contradictoire ni archive primaire n'a été auditée. Les études de cas inventées sont des fictions didactiques, **pas** des constats historiques réels.
- **Rubriques/corrigés :** pas d'essai sur apprenants; des réponses ouvertes nécessitent une modération humaine. Le contrôle automatisé des items vérifie présence, référents et quelques correspondances, non toutes les inférences possibles. Les seuils de maîtrise sont des décisions de conception non étalonnées.
- **Droits :** aucune reproduction d'image, carte ou document externe dans le ZIP. Les conditions de réemploi futur des médias tiers demandent une vérification distincte; les courtes synthèses sont des paraphrases originales attribuées.
- **Accessibilité :** supports conçus pour pouvoir être lus à voix haute et linéarisés; aucun test effectif de lecteur d'écran, de contraste, de navigation clavier, d'enregistrement oral ni d'import LMS n'a été réalisé.
- **Biais et perspectives :** revue indispensable pour ne pas faire passer les descriptions patrimoniales coloniales pour des histoires complètes; les Premiers Peuples ne sont pas décrits à partir de voix imaginées.

## Révisions humaines impératives avant qualification

1. Historien/ne ou spécialiste de l'univers social : période, vocabulaire « société », limites des sources, perspectives des peuples concernés.
2. Enseignante/enseignant et évaluateur : praticabilité des tableaux, charge de lecture, variation acceptable, interprétations équivalentes et niveau des deux preuves.
3. Réviseure/réviseur de français québécois : clarté des consignes et adéquation primaire, sans prétendre à un alignement détaillé au PFEQ.
4. Responsables des droits et de l'accessibilité : descriptions de sources, licences et essais effectifs en contexte LMS.

## Propositions centrales à soumettre, **non appliquées**

- Documenter dans le schéma central un `critere_id` par item si une traçabilité machine plus forte que le texte de `criteres` est souhaitée.
- Ajouter au moteur un champ facultatif `type_de_source` et `epoque_decrite` distincts de `date_de_publication`, afin de détecter les confusions chronologiques.
- Normaliser le statut `a_revoir` et le contrôle humain pour toute variante `scenario_controle`, sans modifier le registre ni les dossiers voisins.

**Statut de la présente livraison :** `a_revoir`, non publiée, non certifiée, non homologuée.

## Résultat des tests sur le ZIP de livraison final

- RÉUSSI — ZIP premier chemin commence exactement par la racine attendue
- RÉUSSI — ZIP exactement 14 fichiers sans dossier englobant
- RÉUSSI — ZIP aucune entrée répertoire libre/absolute/../
- RÉUSSI — ZIP 14 fichiers non vides
- RÉUSSI — ZIP test CRC
- RÉUSSI — JSON du ZIP parsables
- RÉUSSI — Manifeste ZIP identique liste ZIP

**Bilan total : 43/43 contrôles réussis.**
