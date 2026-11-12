# Plan d'évaluation — qc-pri-ale-013

**Objectif commun immuable :** `obj-1` — Écouter un échange anglais et en restituer les idées essentielles.  
**Critère commun immuable :** `crit-1` — Résumer un échange et poser une question pertinente de clarification.  
**Famille unique :** `qc-pri-ale-013-ev-01` ; type natif : `réponse_argumentée`.  
**Mode réel :** textes anglais originaux complets, fixes (`fixe`) ou scénarios verrouillés (`scenario_controle`), **aucun tirage IA**.  
**Poids des dimensions par item :** idée centrale 2/8, deux détails 2/8, question de clarification 2/8, fidélité et distinction fait/inférence 2/8.

## Matrice de couverture, difficulté et représentation

Toutes les lignes ci-dessous pointent vers `obj-1`, `crit-1` et `qc-pri-ale-013-ev-01`. Les dialogues sont intégralement dans `evaluation/BANQUE_ITEMS.json`; la réponse attendue comprend un modèle sans imposer de formulation exacte.

| Item | Situation contrôlée / représentation | Difficulté | Compétence particulièrement observée | Statut |
|---|---|---|---|---|
| `qc-pri-ale-013-q-001` | Book swap change; dialogue oral à deux voix → synthèse orale/écrite | initial | correction de date | `a_revoir` |
| `qc-pri-ale-013-q-002` | Snack plan; dialogue oral à deux voix → synthèse orale/écrite | initial | choix final | `a_revoir` |
| `qc-pri-ale-013-q-003` | Missing library book; dialogue oral à deux voix → synthèse orale/écrite | initial | localisation d’un objet | `a_revoir` |
| `qc-pri-ale-013-q-004` | Music club; dialogue oral à deux voix → synthèse orale/écrite | intermediaire | correction d’heure | `a_revoir` |
| `qc-pri-ale-013-q-005` | Indoor games day; dialogue oral à deux voix → synthèse orale/écrite | intermediaire | cause et lieu | `a_revoir` |
| `qc-pri-ale-013-q-006` | Plant observations; dialogue oral à deux voix → synthèse orale/écrite | intermediaire | observation versus supposition | `a_revoir` |
| `qc-pri-ale-013-q-007` | Picnic location; dialogue oral à deux voix → synthèse orale/écrite | intermediaire | choix de lieu | `a_revoir` |
| `qc-pri-ale-013-q-008` | School newsletter; dialogue oral à deux voix → synthèse orale/écrite | intermediaire | échéance avancée | `a_revoir` |
| `qc-pri-ale-013-q-009` | Drama rehearsal; dialogue oral à deux voix → synthèse orale/écrite | intermediaire | lieu et heure | `a_revoir` |
| `qc-pri-ale-013-q-010` | Neighbourhood book drive; dialogue oral à deux voix → synthèse orale/écrite | intermediaire | information hors notice | `a_revoir` |
| `qc-pri-ale-013-q-011` | Reading buddies — autonomous proof A; dialogue oral à deux voix → synthèse orale/écrite | transfert | preuve A : résumé et question sans indices | `a_revoir` |
| `qc-pri-ale-013-q-012` | Museum nature visit — autonomous proof B; dialogue oral à deux voix → synthèse orale/écrite | transfert | preuve B : synthèse transférée sans indices | `a_revoir` |

## Passation et contrôle des faits

1. Fournir la consigne commune en anglais; faire entendre deux fois le dialogue complet à débit naturel raisonnable (en direct ou audio créé à partir du script). À défaut d'enregistrement, deux personnes lisent les rôles à voix distinctes.
2. Ne pas dévoiler le script avant la production. Aucun indice de contenu lors des deux preuves de maîtrise. Réponses orales enregistrées/consignées avec consentement applicable ou retranscrites par un scribe neutre, sans modifier le sens.
3. Réviser manuellement le résumé et les deux détails en comparant aux tours de parole. Accepter des paraphrases exactes; refuser une inversion du projet initial/final, un détail inventé et une question déjà répondue.
4. Les `points_fixes` de la banque établissent les faits et questions modèles. Il existe plusieurs questions valides pour une même situation : n'attribuer aucun score par appariement lexical seul.
5. Pour une épreuve locale, une personne autre que l'autrice de l'item doit relire le script, l'écoute réelle, l'âge cible, la difficulté linguistique et la rubrique avant tout statut supérieur à `a_revoir`.

## Variabilité autorisée et interdite

- **Permise :** lecteur humain différent, accent anglais intelligible, vitesse accessible cohérente entre apprenants, restitution en anglais oral/écrit/dicté, reformulation fidèle de la réponse ou de la question, sans changement des faits.
- **Non permise sans contrôle :** dialogues réécrits automatiquement, inversion de dates/lieux, omission d'une réplique apportant la réponse, nouvelles conditions de réussite ou nouvelle question déjà résolue par le stimulus.
- **Modes fixes :** q-001 à q-003; **scénarios contrôlés :** q-004 à q-012. Pas de variables numériques à résoudre ni seed aléatoire; `seed` et `parametres` restent `null`.

## Deux preuves dans des contextes distincts

- **Preuve A, q-011 :** programme de lecture scolaire; sans indices, résumer qui participe, moment/lieu, une condition, et poser une question sur l'inscription non indiquée.
- **Preuve B, q-012 :** visite d'exposition naturelle au musée; sans indices, restituer visite, lieu/heure et matériel, puis demander l'heure de fin non indiquée.
- Décision : validité des quatre dimensions dans **les deux contextes**, stabilité et autonomie; ne pas réduire à une note unique. Niveau/décision et suivi dans `evaluation/GRILLE_MAITRISE.md`.

## Sécurité, droits et accessibilité

Contenus fictifs sans données personnelles, marques, témoignages ni citations externes. Débit modéré, absence d'effets sonores inutiles, volume confortable, casques ou salle calme selon besoins; consentement et stockage prudent des réponses. Ne pas évaluer l'accent, l'orthographe ou l'écriture hors objectif. Sous-titres/transcriptions avant la réponse modifient l'accès à la tâche auditive : noter la modalité et vérifier le construit, sans discriminer l'élève. Les scripts de la banque sont originaux et peuvent être lus; aucun enregistrement ni autorisation de voix tierce n'est présumé.

## Couverture et limites

Le corpus couvre les indices *actually, but, instead, so, because, no*, main idea, deux détails et questions ouvertes. Aucune revue humaine, étude de biais/équité ni essai élève n'a été exécuté. Un dialogue lu par un seul enseignant qui change de voix peut être utilisé, mais l'intelligibilité et la fidélité à deux locuteurs doivent être vérifiées avant qualification.
