# Plan d'évaluation — `qc-pri-fr-002`

## Traçabilité des invariants

- `obj-1` : **Associer les graphèmes courants aux phonèmes et effectuer la conversion dans les deux sens.**
- `crit-1` : **Lire et écrire une série de syllabes et de mots réguliers nouveaux.**
- Famille native `qc-pri-fr-002-ev-01` ; type natif **réponse_argumentée**, opérationnalisé par lecture à voix haute, encodage écrit et pointage/justification de graphèmes. La prononciation n'a pas à imiter un accent externe.
- 10 items fixes, aucun moteur génératif ni seed aléatoire. Variabilité de réalisation phonétique et adaptations de support explicitement bornées.

## Matrice item par item (liens complets)

| Item | Objectif | Critère | Famille | Difficulté | Représentation / compétence visée | Variabilité permise |
|---|---|---|---|---|---|---|
| `qc-pri-fr-002-q-001` | `obj-1` | `crit-1` | `qc-pri-fr-002-ev-01` | initial | syllabes en lecture | fixe ; oral / écrit séparés |
| `qc-pri-fr-002-q-002` | `obj-1` | `crit-1` | `qc-pri-fr-002-ev-01` | initial | syllabes sous dictée | fixe ; oral / écrit séparés |
| `qc-pri-fr-002-q-003` | `obj-1` | `crit-1` | `qc-pri-fr-002-ev-01` | initial | mots en lecture | fixe ; oral / écrit séparés |
| `qc-pri-fr-002-q-004` | `obj-1` | `crit-1` | `qc-pri-fr-002-ev-01` | intermediaire | mots sous dictée | fixe ; oral / écrit séparés |
| `qc-pri-fr-002-q-005` | `obj-1` | `crit-1` | `qc-pri-fr-002-ev-01` | intermediaire | digrammes ch/ou | fixe ; oral / écrit séparés |
| `qc-pri-fr-002-q-006` | `obj-1` | `crit-1` | `qc-pri-fr-002-ev-01` | intermediaire | contraste u/ou bidirectionnel | fixe ; oral / écrit séparés |
| `qc-pri-fr-002-q-007` | `obj-1` | `crit-1` | `qc-pri-fr-002-ev-01` | intermediaire | pseudo-mot et fusion | fixe ; oral / écrit séparés |
| `qc-pri-fr-002-q-008` | `obj-1` | `crit-1` | `qc-pri-fr-002-ev-01` | transfert | lecture/dictée, extension | fixe ; oral / écrit séparés |
| `qc-pri-fr-002-q-009` | `obj-1` | `crit-1` | `qc-pri-fr-002-ev-01` | transfert | preuve A : 3+3 lecture, 3+3 dictée | fixe ; oral / écrit séparés |
| `qc-pri-fr-002-q-010` | `obj-1` | `crit-1` | `qc-pri-fr-002-ev-01` | transfert | preuve B : 3+3 lecture, 3+3 dictée | fixe ; oral / écrit séparés |

## Couverture, complexité et instrumentation

- **Initial** 001–003 : règles simples en syllabes et mots; **intermédiaire** 004–007 : encodage sous dictée, digrammes et fusion; **transfert** 008–010 : deux directions dans des listes indépendantes et nouvelles.
- Deux contextes de maîtrise **réservés** : q-009 **atelier d’étiquettes** (lecture de cartes + dictée des commandes) et q-010 **station des messages** (lecture de messages + dictée d’annonces), avec ensembles de syllabes et de mots disjoints et distincts des démonstrations.
- Par contexte : 3 syllabes et 3 mots *lus* + 3 syllabes et 3 mots *écrits*. Les éléments écrits sont prélevés d'un lexique fermé, expliqué oralement à l'apprenant sans lui montrer les graphies. Les quatre sous-dimensions sont consignées séparément. Si une réponse phonologique correcte diverge d’une graphie possible en français mais non retenue dans le corpus, une personne doit constater l'ambiguïté et documenter ce qui est et n’est pas attesté; ne pas noter une conversion fautive par simple comparaison aveugle de chaînes.
- Chaque item est documenté par consigne, stimulus, corrigé/rubrique, feedback, difficulté, représentation et variabilité limitée. Le mode `fixe` est utilisé partout; **pas** de génération IA libre ni de certification automatique.

## Procédure de passation

1. **Lecture** : présenter seulement les unités imprimées réservées à la lecture, avec grosse police et sans image devinette; demander une lecture orale. La personne responsable marque résultat et procédure; réécoute de l’enfant ou enregistrement uniquement si consentement.
2. Retirer **toutes** les cartes de lecture. **Dictée** : une personne lit les unités de la colonne destinée à l'adulte, naturellement, sans exposer la graphie; elle peut répéter identiquement l'énoncé, donner un indice de sens non orthographique convenu et préciser la banque fermée, sans segmenter la réponse.
3. Comparer à la transcription de référence, vérifier son–graphème et contexte lexical. Admettre variantes d’accent ne détruisant pas l'identité du phonème. Ne pas traiter une difficulté d'écriture motrice comme une erreur orthographique si la sélection des graphèmes est indépendante sur clavier/lettres mobiles.
4. Demander après la tentative une courte justification ou un pointage de deux unités choisies; ne pas souffler le corrigé avant que la preuve soit complète.
5. Appliquer `GRILLE_MAITRISE.md` sur **les deux contextes**; une note globale, même élevée, ne compense pas l’absence de lecture ou de dictée.

## Accessibilité, sécurité, limites

- Aucun volume sonore excessif. Soutien visuel en **lecture** et aide motrice neutre en **écriture**; une dictée ne doit pas être transformée en lecture de l’orthographe cible, sinon ce n’est plus la même preuve.
- Pour troubles de l'audition/parole, convenir avec spécialiste d'une modalité réellement équivalente; ne pas déclarer attestée une correspondance auditivo-graphique non observée.
- Ne pas noter l'accent québécois, les variantes non distinctives ou la vitesse; conserver un relevé des réalisations et une trace du soutien.
- Revue humaine requise pour lexique de dictée, homophones, script acoustique, durée et fidélité intercorrecteurs. Aucun audio externe ou propriété de licence sonore n'est fourni.
