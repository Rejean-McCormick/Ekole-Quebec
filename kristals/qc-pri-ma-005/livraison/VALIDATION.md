# Validation de livraison — qc-pri-ma-005 (v1.2)

## Périmètre et source
Delta **fusionnable** dans `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`; 14 fichiers sous `kristals/qc-pri-ma-005/`, aucun fichier de registre, canon, state, runtime, governance, AGENTS ou autre Kristal. Source : archive maîtresse à sous-arbre v1.2 fournie dans la conversation.

## Contrôles réellement exécutés par script
- Lecture des **trois documents de gouvernance** demandés, du graphe v1.2, des deux `PARCOURS.md`, deux contrats JSON, deux ALIGNEMENT et deux BRIEF_REDACTION.
- Conservation à l’identique du frontmatter YAML source et vérification de son analyse; 12 sections numérotées dans l’ordre pour ce Kristal; champs initiaux du contrat JSON conservés avec famille native et champs supplémentaires de gouvernance.
- Identifiants `obj-1`, `crit-1`, famille `qc-pri-ma-005-ev-01`, préalable qc-pri-ma-003, banque JSON parsable, ID d’items séquentiels, champs exigés et minimum 8 items.
- Vérification de deux contextes de preuve de maîtrise, de la présence de rubriques et références, de l’absence d’autres IDs que l’ID courant et le lien de préalable.
- Six familles d’items paramétriques (cas finis) : **32 cas** vérifiés exhaustivement avec un oracle indépendant Python `decimal.Decimal(..., ROUND_HALF_UP)` pour rang, estimation, exact, différence signée et écart absolu, dont contrôle de sélection par seed.
- Six corrigés fixes (`q-007` à `q-012`) recalculés indépendamment; deux preuves autonomes (`q-011`, `q-012`) dans des contextes différents.
- 50 assertions structurelles, de banque et de contenu exécutées et réussies **avant empaquetage**, puis vérification indépendante du ZIP créé (nombre d’entrées, chemins, non-vacuité, JSON, fichier manifeste, absence de traversée de répertoire, CRC).

## Limites non résolues
- Aucune revue par enseignante ou enseignant indépendant, aucun essai avec des élèves, aucune équivalence psychométrique des contextes attestée, aucun alignement PFEQ revendiqué, aucune certification d’items ou publication.
- **Lecture** : observation orale humaine et équité d’accent nécessaire; ce script ne peut pas certifier exactitude/prosodie de prestations réelles. **Mathématique** : les variantes testées sont seulement celles des **catalogues finis**; interdiction d'extrapoler une génération libre en dehors de ces domaines.
- Droits : créations originales, aucune citation d’œuvre tierce; vérifier la politique de l'organisation sur les traces d'élèves avant mise en production.
- Accessibilité : suggestions documentées, aménagements à évaluer humainement selon les besoins.

## Revue humaine attendue
1. Vérifier difficulté des textes et activités, clarté des consignes, équité linguistique ou mathématique.
2. Vérifier l’adéquation de chaque rubrique, les deux preuves et le seuil de maîtrise; essayer auprès d’élèves avec consentement approprié.
3. Approuver l’accessibilité et les droits/traces avant diffusion; la banque reste `a_revoir`.

## Propositions, sans modification des bases centrales
- Harmoniser ultérieurement le schéma des critères de famille (`critere: crit-1`) et le manifeste dans une décision de gouvernance distincte.
- Formaliser un test de performances orales humaines ou un validateur de variantes numériques finies au niveau du Kit; **non appliqué** au registre central dans cette livraison.

**Statut :** contrôles techniques locaux effectués; révision pédagogique humaine requise, aucun statut « publié », « certifié » ou « homologué ».
