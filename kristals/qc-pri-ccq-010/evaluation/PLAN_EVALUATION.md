# Plan d'évaluation — `qc-pri-ccq-010` / famille `qc-pri-ccq-010-ev-01`

## Cadrage verrouillé

- **`obj-1` :** Reconnaître les limites personnelles, le respect et les règles de sécurité dans des situations adaptées à l’âge.
- **`crit-1` :** Choisir une conduite sûre dans une vignette fictive et identifier une ressource adulte.
- **Mode de famille (natif) :** `observation_ou_production`; items en mode **`fixe`** (aucune génération libre ou paramétrisation de scénarios sensibles).
- **Évaluation ciblée :** formulation ou sélection expliquée d'une conduite fictive, justification, adulte-ressource; aucun jugement des croyances, du vécu, de l'identité ou des émotions de l'élève.

## Répartition et traçabilité intégrale

Tous les items portent `objectif_id=obj-1`, `critere_id=crit-1` et `family_id=qc-pri-ccq-010-ev-01` dans `BANQUE_ITEMS.json`.

| Item | Contexte | Difficulté | Représentation | Fonction |
|---|---|---|---|---|
| q-001 | Salutation au camp | initial | dialogue | Respect du corps / limites |
| q-002 | Carnet personnel | initial | récit | Intimité non numérique |
| q-003 | Photo de groupe | initial | avis | Image et consentement |
| q-004 | Message secret | initial | échange écrit | Sécurité et adulte |
| q-005 | Jeu imposé | intermédiaire | règle | Pression de groupe |
| q-006 | Soin du poignet | intermédiaire | situation | Explication et protection, sans refus systématique de soin |
| q-007 | Secret inquiétant | intermédiaire | récit | Recours à un autre adulte |
| q-008 | Mot de passe | intermédiaire | message | Confidentialité |
| q-009 | Localisation dans un groupe | transfert | annonce | Limites et sécurité hors école |
| q-010 | Usage d'un enregistrement | transfert | histoire | Consentement limité à un usage |
| **q-011** | **Vidéo de sortie scolaire** | **transfert** | **vignette** | **Preuve autonome A, intimité/publication** |
| **q-012** | **Contact inconnu en ligne** | **transfert** | **vignette** | **Preuve autonome B, renseignements/secret** |

## Barème identique (0–2 × 4 dimensions)

1. **Repérage** de la limite ou du risque figurant dans le texte.
2. **Conduite** réellement protectrice et respectueuse, sans blâme.
3. **Adulte-ressource** accessible ou voie équivalente permettant de joindre une personne responsable.
4. **Justification** liée à une notion pertinente et aux faits, non à un jugement sur le personnage.

Chaque dimension reçoit 0 = absent ou nocif, 1 = partiellement correct, 2 = correct et adapté. Une conduite alternative peut être pleinement correcte même si elle diffère du corrigé exemple. Pas de correction par mot-clé isolé ni de score sur le style, la conformité aux croyances d'un enseignant, la vie privée ou la divulgation.

**Décision de maîtrise :** au moins deux preuves *indépendantes* `q-011` et `q-012`, réalisées sans indices de solution; chaque preuve doit comporter une conduite protectrice (`dimension 2 = 2`), un adulte-ressource crédible (`dimension 3 = 2`), aucun blâme ni action dangereuse, les autres dimensions ≥ 1, et un ensemble ≥ 7/8. Les notes sont des repères **secondaires** : les deux preuves et la stabilité du raisonnement sont obligatoires. Sinon remédiation ciblée + nouvelle occasion avec scénario revu humainement.

## Variabilité, couverture et contrôle

- **Énoncés, réponses et limites :** fixes; seule la présentation varie (lecture neutre, typographie, aide de communication, pictogrammes neutres). `seed` et `parametres` valent `null`; pas de transformation automatique du contenu, pas de génération IA de cas sensibles.
- **Couverture :** corps (q-001/q-005), intimité (q-002/q-003/q-009/q-010/q-011), consentement (q-001/q-003/q-005/q-010), sécurité (q-004/q-007/q-008/q-009/q-012), aide (les 12 items).
- **Deux contextes de maîtrise :** sortie scolaire physique et communication privée numérique. Ne pas remplacer ces deux situations par deux reformulations d'une seule scène.
- **Équité :** des élèves sans parent sécurisant peuvent identifier du personnel scolaire ou une autre ressource sûre; aucune obligation de nommer une personne réelle.

## Sécurité, accessibilité, confidentialité

- Scènes fictives sobres sans images de nudité, contact simulé, jeu de rôle tactile ni demande de souvenirs ou pratiques familiales.
- Ne jamais exiger de révéler des abus, croyances, identité, orientations, situations familiales ou données de compte; ne pas stocker de divulgations dans les évaluations.
- Accès équivalent par texte lu neutrement, réponse orale, écrit, pointage, dictée ou communication alternative; l'adulte ne fournit pas la conduite attendue.
- Si confidence ou signe de danger : interrompre la passation, répondre selon le protocole institutionnel de protection; distinguer ce protocole de la correction d'un item.
- Revue humaine requise avant usage : clarté selon l'âge, risques de biais, protection de l'enfance, dispositif de signalement local, durée réelle de passation.

## Statut

**Items :** `a_revoir`. Ce plan n'est pas un examen certifié et n'affirme aucune conformité ministérielle détaillée.
