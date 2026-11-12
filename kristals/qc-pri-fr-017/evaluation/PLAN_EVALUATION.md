# Plan d'évaluation — qc-pri-fr-017

**Identité verrouillée :** objectif `obj-1` — **Accorder le verbe avec son sujet dans des phrases simples puis enrichies.** Critère `crit-1` — **Repérer le sujet et justifier l’accord dans six phrases différentes.** Famille `qc-pri-fr-017-ev-01`; type *réponse_argumentée*. Tout item ci-dessous lie explicitement les trois identifiants dans `BANQUE_ITEMS.json`.

## Conception et correction

- **Corpus fermé**, dix items en mode **fixe**, aucun algorithme paramétrique, `seed: null` et `parametres: null` (absence de tirage à reproduire). Corrigés écrits et structures d'analyse associées aux stimuli; **aucune génération IA libre** admise pour décider du vrai/faux.
- **Temps/forme :** phrases écrites en français, infinitif entre parenthèses, expression justifiée courte. Écrit de la forme verbale obligatoire, justification oralement dictée/transcrite possible si le contenu est conservé. Les graphies *-e* / *-ent* ne sont pas interchangeables même lorsqu'elles se prononcent pareil.
- **Rubrique par phrase :** S = sujet entier correctement délimité (et noyau d'un groupe nominal lorsqu'il sert au choix); PN = personne ET nombre exacts; V = forme écrite exacte au présent; J = explication reliant traits du sujet à cette forme. Une phrase n'est complète que si S, PN, V et J sont présents et exacts. Une justification paraphrasée est acceptable si le raisonnement reste explicite.
- **Variabilité :** ordre, verbes, phrase et réponse ne peuvent être changés automatiquement. Pas de variation non documentée : pour tout nouveau contexte, produire un nouvel item avec corrigé revu. Seule la formulation de la justification est ouverte.

## Matrice de couverture (tous : `obj-1`, `crit-1`, `qc-pri-fr-017-ev-01`)

| Item | Complexité | Représentation | Cible grammaticale | Rôle |
|---|---|---|---|---|
| q-001 | initial | phrase à compléter + justification | GN simple, 3e singulier | sonde |
| q-002 | initial | phrase + justification | tu, 2e singulier | sonde |
| q-003 | initial | phrase + justification | nous, 1re pluriel | sonde |
| q-004 | initial | phrase + justification | vous, 2e pluriel | sonde |
| q-005 | intermédiaire | GN enrichi | noyau singulier, complément pluriel | sonde |
| q-006 | intermédiaire | GN enrichi | noyau pluriel, complément singulier | sonde |
| q-007 | intermédiaire | coordination de deux sujets | deux noms reliés par *et* | sonde |
| q-008 | transfert | sujet après le verbe | sujet postposé pluriel | sonde |
| q-009 | transfert | **six phrases**, contexte bibliothèque scolaire | mélange des sujets et des formes au présent | **manifestation A** |
| q-010 | transfert | **six phrases**, contexte jardin communautaire | mélange + sujet postposé | **manifestation B** |

**Couverture des notions :** sujet (simple, enrichi, coordonné, inversé); personne (1re, 2e, 3e); nombre (singulier/pluriel); verbe (présent régulier en -er, marques -e/-es/-ons/-ez/-ent). Le tableau de progression et les notions sont enseignés dans `contenu/01_NOTIONS_ET_EXEMPLES.md` et travaillés avant la banque. Les items q-001 à q-008 sont **sondes** et ne remplacent jamais A/B.

## Deux preuves non interchangeables

**A — q-009** : six phrases sur la bibliothèque et une activité en classe. Réponse indépendante complète sans consulter la correction; toutes les six lignes S/PN/V/J exactes. **B — q-010** : six nouvelles phrases, autre lieu et autre usage du français, au jardin de quartier; administrer sur une séance distincte et idéalement après une pause/rappel différé, sans montrer les corrections de A pendant B. Toutes les six lignes S/PN/V/J exactes.

**Règle de décision :** A valide + B valide + autonomie observable ⇒ maîtrise de `crit-1` selon `GRILLE_MAITRISE.md`. Si A ou B manque, ou si une erreur essentielle subsiste, ne pas attribuer la maîtrise; remédier et construire une **nouvelle** épreuve de six phrases contrôlées (hors de ce delta, soumise à revue) avant de requalifier. La moyenne, le hasard et un quiz unique ne sont jamais substituts.

## Correction, fiabilité, risques et limites

- Comparer la **forme écrite** au corrigé déterminé; juger la justification avec la grille et garder la trace, pas par appariement de mots-clés seulement. Ne pas confondre erreur de langue avec variation de vocabulaire dans la justification.
- Les dix corrigés ont été relus sur leurs règles et testés pour champs/structures dans la validation locale; **pas de revue humaine indépendante ni d'essai avec apprenants**. Statut des dix items : **`a_revoir`**, non certifié.
- Accessibilité : phrases présentées en clair, une par ligne; taille de caractères ajustable; consignes audibles si nécessaire, mais **stimulus écrit et orthographe finale conservés**; saisie clavier, temps souple ou transcription contrôlée. Noter toute aide qui fournit la règle : cela invalide le critère d'autonomie sans disqualifier la personne.
- Sécurité/équité : contextes fictifs, sans enquête sur la vie privée, les croyances ou l'identité; prénoms fictifs diversifiés et situations courantes; aucun risque physique et aucune mise en compétition publique.
- Liens internes : `evaluation/BANQUE_ITEMS.json`, `evaluation/GRILLE_MAITRISE.md`, `contenu/06_REMEDIATION_ET_TRANSFERT.md`, `sources/REFERENCES_CONTENU.md`. Aucune dépendance ajoutée au graphe.
