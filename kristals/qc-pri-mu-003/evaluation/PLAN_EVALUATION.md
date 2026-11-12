# Plan d'évaluation | `qc-pri-mu-003`

**Objectif commun à tous les items :** `obj-1` — Comparer des motifs mélodiques selon les mouvements de hauteur.  
**Critère commun :** `crit-1` — Chanter ou jouer un motif et décrire ses variations de hauteur.  
**Famille conservée :** `qc-pri-mu-003-ev-01`. Type principal `observation_ou_production`; items **fixes contrôlés** avec `seed=null`, `parametres=null`, pas de génération libre.

## Corpus de repères et corrigé fermé

`do4=60`, `ré4=62`, `mi4=64`, `fa4=65`, `sol4=67` (numéros MIDI pour comparer exactement les rapports dans ce corpus); écart = MIDI(nouvelle) − MIDI(précédente). `>0` = ↑, `<0` = ↓, `=0` = →. Quatre notes produisent trois flèches. Les exemples transposés globalement conservent **tous** les écarts; l'utilisation des syllabes do/ré/mi n'est pas requise des élèves si les sons sont produits sur instrument accessible.

## Carte de couverture : chaque item réfère à `obj-1`, `crit-1`, `qc-pri-mu-003-ev-01`

| ID complet | Niveau | Représentation | Cible et critère observable | Poids de décision |
|---|---|---|---|---|
| `qc-pri-mu-003-q-001` | initial | deux sons + flèche | hauteur plus aiguë; distinction d'intensité | formatif |
| `qc-pri-mu-003-q-002` | initial | même son répété | intervalle nul → | formatif |
| `qc-pri-mu-003-q-003` | initial | motif à 4 notes | performance et ↓ → ↓ | formatif |
| `qc-pri-mu-003-q-004` | intermédiaire | 2 phrases et flèches | distinguer ↑ ↑ ↓ de ↑ ↓ ↓ | formatif |
| `qc-pri-mu-003-q-005` | intermédiaire | paires do/ré et do/mi | 2 contre 4 demi-tons, même direction | formatif |
| `qc-pri-mu-003-q-006` | intermédiaire | son + 4 cartes | produire et analyser ↑ ↓ → | formatif |
| `qc-pri-mu-003-q-007` | intermédiaire | comparaison transposée | mêmes écarts et contour | formatif |
| `qc-pri-mu-003-q-008` | transfert | deux motifs nouveaux | transitions différentes, production autonome formative | entraînement |
| `qc-pri-mu-003-q-009` | transfert | **balise du sentier**, jeu/chant + comparaison | **preuve A** : deux contours identiques mais intervalles distincts | **nécessaire** |
| `qc-pri-mu-003-q-010` | transfert | **signal du jardin**, jeu/chant + comparaison | **preuve B** : changement de direction et phrase différente | **nécessaire** |

## Administration et équité

1. **Avant :** installer instrument accordé ou source de hauteur stable au volume sûr; adopter tessiture confortable ou transposition intégrale uniforme; fournir cartes d'accès à gros caractères, relief ou instrument contrôlable avec commutateur si nécessaire. L'accès ne dicte pas l'ordre musical.
2. **Présenter les deux motifs** sonores au même timbre/volume ou les rendre accessibles par représentation multisensorielle individualisée; aucun exemple de corrigé joué comme indice pendant les preuves. L'élève peut choisir l'un des modes de production **chanter ou jouer**, jamais une obligation de chanter.
3. **Observer séparément** succession de notes, rapports de hauteur, trois flèches et comparaison justifiée; noter la modalité et les aides. Enregistrement d'enfant et application tierce non nécessaires.
4. **Deux preuves** `q-009` et `q-010` : présentées dans deux situations distinctes, idéalement à des moments séparés, sans copier la phrase enseignée. L'une ne remplace pas l'autre. Aucune moyenne ne compense P1/P2/P3/P4 absent.
5. **Qualité des corrigés :** les champs `motif_a` et `motif_b` du JSON contiennent notes, MIDI, deltas et contour. Les vérifications arithmétiques indépendantes sont rapportées dans `livraison/VALIDATION.md`.

## Variabilité permise / interdite

- **Permise :** transposition **identique sur toutes les notes** (même nombre de demi-tons), timbre, tempo confortable, interface adaptée, voix ou instrument, forme de la réponse écrite/gestuelle; mesures relatives inchangées.
- **Interdite :** remplacer une note isolée, substituer un extrait commercial, créer des motifs aléatoires non vérifiés, accepter les flèches sans production lorsque la prestation n'est pas observable, juger la voix naturelle ou le goût artistique.
- **Limite de sécurité :** pause en cas de gêne sonore/vocale; aucune écoute à volume élevé, exercice respiratoire imposé, pression sur la tessiture ni exposition publique obligatoire.
- **Limite probatoire :** une représentation visuelle seule n'établit pas automatiquement la composante chant/jouée; en cas d'obstacle non résolu à la production, consignation non concluante et aménagement de l'épreuve par un spécialiste.

**Statut :** dix tâches rédigées `a_revoir`, aucune certification ou calibration interévaluateurs revendiquée. Une épreuve en situation réelle et une revue musicale humaine restent à mener.
