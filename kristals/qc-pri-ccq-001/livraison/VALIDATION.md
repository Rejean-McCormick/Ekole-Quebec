# Journal de validation — `qc-pri-ccq-001`

**Base :** workspace maître v1.2 fourni; delta de **14 fichiers**, limité à `kristals/qc-pri-ccq-001/`.  
**Statut :** techniquement vérifié sur les contrôles listés ci-dessous, **revue pédagogique, culturelle et éthique humaine requise**. Pas de publication, certification ou homologation.

## Tests effectivement exécutés

- Lecture des huit documents sources demandés et des entrées pertinentes du graphe. Contrôles du contrat natif v1.2 : tous les champs conservés, champs de famille ajoutés, objectif/preuve/famille, zéro prérequis et zéro lien d'ordre imposé.
- Comparaison **octet pour octet du contenu du frontmatter YAML** initial avec la livraison; parsing du YAML via PyYAML effectué.
- Présence des **12 sections du parcours**, deux exemples résolus, deux contre-exemples, deux diagnostics, trois exercices guidés à indices dégressifs, quatre pratiques autonomes et deux transferts distincts.
- Banque : JSON parsé, format, **12 items uniques**, références `obj-1`/`crit-1`/`qc-pri-ccq-001-ev-01`, consignes/stimuli/réponses/rubriques/feedback présents, modes et difficultés autorisés, tous les statuts `a_revoir`.
- Corpus fermé : **4 items à deux scénarios**, validation reproductible des sélections sur **800 graines de test** au total, vérification de la correspondance de la variante initiale avec son corrigé préparé. Les 8 autres items sont fixes, dont les deux preuves de maîtrise.
- **Deux manifestations inédites et distinctes :** `q-011` (radio scolaire, Noa) et `q-012` (jardin collectif, Ari); les stimuli complets n'apparaissent pas dans les documents d'enseignement; grille analytique D1–D4 et autonomie vérifiables textuellement.
- Provenance : références institutionnelles explicites, distinction sources/raisonnements/productions, aucune image ni texte long de tiers importés. Contrôles éditoriaux de confidentialité et d'accessibilité par lecture et recherche dans les documents.
- ZIP : contrôle des 14 chemins attendus, première entrée sous `kristals/qc-pri-ccq-001/`, contenu non vide, absence de chemin absolu ou `../`, absence d'autres workspaces et de `governance/`, `registry/`, `docs/`, `canon/`, vérification de l'intégrité CRC. **Résultats : voir la section finale ci-dessous.**

## Limites explicites de ces tests

Les vérifications de schéma sont des contrôles JSON/YAML et d'invariants locaux, **pas** des tests d'un moteur Framework ou d'un schéma officiel absent. Le contrôle des variations démontre une sélection déterministe et des corrigés associés, **pas** la validité psychométrique ni un jugement automatique fiable des analyses ouvertes. Le repérage des références et droits est documentaire; aucune clearance juridique de publication n'a été exécutée. Le test de fusion vérifie le non-écrasement des fichiers protégés, mais aucune publication ou activation réseau n'est effectuée.

## Revue humaine avant toute qualification

1. Enseignant spécialiste CCQ : vérifier niveau d'âge, adéquation des vignettes, charge de lecture et acceptabilité des critères d'autonomie.
2. Réviseur diversité/protection : détecter biais, glissements identitaires, stéréotypes implicites et potentiels déclencheurs; organiser un remplacement de cas si besoin.
3. Deux correcteurs : éprouver l'accord intercorrecteurs sur D1–D4 et les réponses ouvertes; réviser si trop ambigu.
4. Responsable de l'accès : vérifier accessibilité en situation réelle et stockage confidentiel des traces, sans données personnelles dans le canon.
5. Responsable des droits et de l'intégration : autoriser l'usage externe et tester le pipeline réel si publication souhaitée.

## Modifications de structure proposées, sans modifier les bases centrales

- Ajouter ultérieurement au registre central (après décision versionnée) un type de trace d'analyse **sans données identitaires de l'élève** et un statut de revue humaine par item.
- Documenter centralement les remplacements approuvés de vignettes et l'accord intercorrecteurs, sans altérer la famille v1.2 ni les dépendances.
- Prévoir un adaptateur d'accessibilité qui conserve la consigne cognitive mais n'impose pas de captation audio.

## Résultat final vérifié

- **47 groupes de contrôles passés** dans le script local; 800 sélections déterministes de corpus effectuées.
- ZIP : **14/14 fichiers non vides**, première entrée et chemins corrects, manifeste concordant, trois JSON lisibles et CRC valide.
- Fusion simulée par extraction du workspace complet dans un espace temporaire : **8 fichiers protégés inchangés** (SHA-256) et **14 fichiers livrés superposés** octet pour octet.
- Aucune validation humaine réalisée; aucune homologation, certification, publication ou activation.
