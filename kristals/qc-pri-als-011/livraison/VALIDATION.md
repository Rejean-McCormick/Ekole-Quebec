# Validation de livraison — `qc-pri-als-011`

## Périmètre et origine

Delta de **14 fichiers sous `kristals/qc-pri-als-011/`** pour le workspace `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`, récupéré dans l'archive fournie `Prompts_202_Kristals_Primaire_Qc_v1.2_boutons_gris.zip`. Seul le Kristal `qc-pri-als-011` est touché. `authoring/PARCOURS.md` conserve intégralement son frontmatter YAML original; `authoring/CONTRAT_PEDAGOGIQUE.json` conserve les clés et valeurs canoniques natives ainsi que les structures des familles, avec champs de gouvernance ajoutés et statut de rédaction actualisé. Aucun registre global ni fichier de gouvernance n'est livré.

## Contrôles effectivement exécutés dans cette livraison

Le script local de vérification a validé **70 assertions avant empaquetage**, notamment :

- lecture réelle des sources v1.2 et vérification de la relation `requires` du graphe; pas d'autre relation sortante;
- comparaison textuelle du frontmatter YAML avec la source, parsing YAML, sections 1 à 12, identités et objectif/critère;
- comparaison des champs originaux du contrat et validation JSON, présence des 13 champs requis de la famille;
- existence des deux exemples résolus, des deux contre-exemples, des deux diagnostics, de G1–G3, A1–A4 et des deux transferts;
- 10 items JSON complets, séquence sans doublon, identifiants `obj-1`/`crit-1`/`qc-pri-als-011-ev-01`, modes fixes et statut `a_revoir`;
- **10 corrections vérifiées** : pour chaque stimulus, application indépendante des deux remplacements ciblés et comparaison exacte à la version corrigée déclarée; ceci n'évalue pas toutes les variantes idiomatiques;
- deux contextes distincts `q-009` (pair) et `q-010` (bibliothécaire), autonomie et décision non compensatoire documentées;
- mentions des droits, de la sécurité, de l'accessibilité; références locales et liens de fichiers recherchés.

## Conditions de validation de l'archive ZIP

Le script effectue **après sa création** un contrôle exhaustif des 14 chemins et contenus : préfixe unique, premier chemin correct, manifeste identique à la liste ordonnée des 14 fichiers, tailles strictement positives, aucune entrée parent/absolue, absence de dossier englobant, extraction JSON valable et intégrité CRC. Les résultats de ce contrôle apparaissent dans le journal d'exécution de la livraison. Aucune simulation de fusion dans un workspace de production n'a été faite.

## Limites non résolues et revue humaine requise

1. **Relecture linguistique bilingue** : idiomaticité des dix mini-messages, cohérence du niveau d'anglais, acceptation de variantes et explications proposées. Le test de substitutions ne remplace pas cette revue.
2. **Essai en situation réelle** : longueur, durée, intelligibilité, accessibilité avec lecteur d'écran/scribe et discrimination réelle des deux contextes.
3. **Droits** : les exemples sont rédigés pour ce lot et les sources externes sont liées (non recopiées); confirmer les conditions de diffusion du workspace entier avant publication.
4. **Implantation** : aucune exécution dans le LMS, aucun test du moteur d'évaluation, de l'interface ou de l'archivage des traces; les descriptions d'accessibilité et de sécurité ont été inspectées mais non testées en dispositif réel.
5. **Statuts** : famille et chaque item sont `a_revoir`; aucune qualification « certifié », « publié », « homologué » ou conformité détaillée au PFEQ.

## Propositions de changements structurels (non appliquées)

- Prévoir au niveau central un champ optionnel pour *preuves indépendantes par contexte* (ID, date, aide reçue, décision par dimension) sans changer les identifiants du graphe.
- Prévoir un protocole de revue des paraphrases/variantes idiomatiques et l'enregistrement de la validation humaine séparément du simple parsing JSON.
- Prévoir une distinction technique entre aide d'accès neutre et aide suggérant une correction lors des évaluations autonomes.

**Fusion recommandée :** entrer dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/` après extraction de l'archive maîtresse, puis extraire directement `qc-pri-als-011_livraison_v1.2.zip` à cet emplacement. Aucun préfixe `Frames_202.../` n'est présent dans ce delta.
