# Validation du delta `qc-pri-fls-006` v1.2

**Statut :** contenu rédigé; revue et essais pédagogiques à réaliser. Le rapport sera renseigné automatiquement par les tests de préarchivage puis archivé dans ce même lot. Aucune homologation, certification ni conformité PFEQ revendiquée.

## Périmètre protégé

Exactement 14 fichiers dans `kristals/qc-pri-fls-006/` : les deux fichiers `authoring/` sont remplacés et douze fichiers sont ajoutés. Le workspace `AGENTS.md`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, le registre, la gouvernance, les dossiers `docs/`, `canon/`, `state/`, `runtime/`, et les autres Kristals ne sont pas empaquetés ni modifiés.

## Tests réellement exécutés

**498 assertions préarchivage vérifiées sans échec**, via un script réellement exécuté le 8 octobre 2026. Contrôles : 14 fichiers non vides, YAML strictement préservé et 12 sections, JSON analysables, invariants de contrat et de famille, dix items séquentiels avec corrections, deux stimuli indépendants, liens et plan, critères, sécurité/accessibilité et droits. Les réponses factuelles de la banque ont été testées contre 31 sous-chaînes de faits présentes dans les stimuli originaux.

Le diff de fusion a été simulé par superposition de tous les chemins du lot sur les **7322 fichiers** du workspace de départ : exactement 2 recouvrements autorisés et 12 nouveaux chemins, sans modification ni suppression des autres entrées. Le script vérifie l'identité des deux vrais remplacements et la présence des deux liens de préalables/ordre dans le maître.

L'archive ZIP finale a été ensuite soumise à des contrôles supplémentaires (CRC, arborescence exacte, absence de chemins dangereux, 14 fichiers non vides et décodage des JSON).

## Limites non résolues et contrôle humain exigé

- Vérifier la difficulté réelle des mots, textes et questions avec plusieurs apprenants FLS de parcours différents; aucune étude d'étalonnage réalisée.
- Revoir la pertinence et l'équité des seuils sur deux textes inconnus ainsi que la fidélité entre correcteurs; les corrélations avec le programme scolaire n'ont pas été évaluées.
- Valider les adaptations d'accès qui permettent bien de mesurer la lecture et non la compréhension orale seulement. Les variations de voix, de syntaxe orale ou de réponse écrite ne sont pas des erreurs si le sens est exact.
- Vérifier les exigences locales de droits, consentement et conservation des traces, bien qu'aucun média externe ni donnée personnelle ne soit livré.
- La maîtrise d'un apprenant n'a pas été observée; la banque reste `a_revoir`.

## Propositions de structure uniquement, sans changement central

- Ajouter ultérieurement au schéma commun une distinction explicite `modalite_source` (texte lu / texte entendu) et `modalite_reponse` (oral, écrit, pointage).
- Ajouter un journal formel des accommodations ayant modifié ou non le construit évalué pour les épreuves de lecture.
- Définir en gouvernance une version de schéma de rubriques acceptant les paraphrases littérales et les preuves d'indice textuel; aucune de ces propositions n'est appliquée dans ce delta.
