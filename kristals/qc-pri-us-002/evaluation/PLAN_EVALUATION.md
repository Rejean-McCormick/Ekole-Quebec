# Plan d’évaluation — qc-pri-us-002

## Invariants et principe

- Objectif `obj-1` (immuable) : **Lire une carte à l’aide de son titre, sa légende et ses repères.**
- Critère `crit-1` (preuve immuable) : **Localiser des lieux et justifier le parcours entre eux sur une carte.**
- Famille : `qc-pri-us-002-ev-01` ; type du contrat v1.2 : `generee_sous_contraintes`.
- Progression : repérer titre/lieux/symboles → orientation/échelle → proposer/vérifier un chemin → comparer/justifier → deux **preuves autonomes** de contexte différent.

## Correspondance des items

| Item | Liens obligatoires | Difficulté | Représentation | Variation |
|---|---|---|---|---|
| `qc-pri-us-002-q-001` | `obj-1` / `crit-1` / `qc-pri-us-002-ev-01` | initial | carte à quadrillage + légende | variations contrôlées |
| `qc-pri-us-002-q-002` | `obj-1` / `crit-1` / `qc-pri-us-002-ev-01` | initial | carte + flèche nord | variations contrôlées |
| `qc-pri-us-002-q-003` | `obj-1` / `crit-1` / `qc-pri-us-002-ev-01` | intermediaire | échelle simple + parcours | variations contrôlées |
| `qc-pri-us-002-q-004` | `obj-1` / `crit-1` / `qc-pri-us-002-ev-01` | intermediaire | carte + comparaison de deux trajets | variations contrôlées |
| `qc-pri-us-002-q-005` | `obj-1` / `crit-1` / `qc-pri-us-002-ev-01` | initial | carte + texte argumenté | fixe |
| `qc-pri-us-002-q-006` | `obj-1` / `crit-1` / `qc-pri-us-002-ev-01` | intermediaire | schéma de parcours + échelle | fixe |
| `qc-pri-us-002-q-007` | `obj-1` / `crit-1` / `qc-pri-us-002-ev-01` | intermediaire | carte + argumentation de trajet | variations contrôlées |
| `qc-pri-us-002-q-008` | `obj-1` / `crit-1` / `qc-pri-us-002-ev-01` | transfert | comparaison chiffrée + carte | variations contrôlées |
| `qc-pri-us-002-q-009` | `obj-1` / `crit-1` / `qc-pri-us-002-ev-01` | transfert | plan scientifique fictif + solution écrite ou orale transcrite | preuve 1 — centre scientifique |
| `qc-pri-us-002-q-010` | `obj-1` / `crit-1` / `qc-pri-us-002-ev-01` | transfert | plan sportif fictif + parcours justifié | preuve 2 — centre sportif |

## Conditions et couverture

**C1 Lecture** : titre adapté à la situation, légende décodée sans devinette, repères cellule-colonne/ligne exacts. **C2 Orientation** : direction appuyée par la flèche N. **C3 Parcours et échelle** : suite de cases contiguës par un côté, aucun obstacle franchi; longueur égale à `(nombre_de_cases−1) × k m`. **C4 Justification et limites** : au moins un argument lié à une indication précise du plan et une limite du document quand demandée. La grille comporte quatre dimensions (voir `GRILLE_MAITRISE.md`), appréciées séparément.

- **Items 1–2** : reconnaître la fonction des titres/légendes, localiser, orienter.
- **Items 3–4** : appliquer l’échelle et vérifier l’existence d’un trajet.
- **Items 5–6** : expliciter les limites et distinguer une longueur de trajet d’une autre mesure.
- **Items 7–8** : construire et comparer des itinéraires justifiés.
- **Item 9** : première manifestation autonome — centre des Sciences (T→A).
- **Item 10** : seconde manifestation autonome — centre sportif du Ruisseau (R→G). **Si cette épreuve a déjà été montrée ou corrigée**, présenter un autre plan de même difficulté, contrôlé par un humain.

**Variabilité permise :** q-001–004, q-007–008 possèdent chacun exactement deux variantes écrites dans `BANQUE_ITEMS.json`; sélection `indice=seed%2`, sans génération IA ouverte ni insertion de symboles inconnus. q-005–006 et q-009–010 sont fixes. Chaque variation possède carte complète, consigne spécifique, corrigé et contraintes; aucun changement libre des valeurs. Les alternatives correctes de trajet de longueur minimale sont acceptées si vérifiées selon les règles.

## Barème, maîtrise et indépendance

Pour chaque épreuve autonome, juger quatre dimensions : (1) lecture précise titre/légende et coordonnées, (2) trajet valide et conforme, (3) direction/échelle exactes, (4) justification vérifiable et limites. **Réussite d’une manifestation** si les dimensions indispensables (lecture + trajet + explication) sont satisfaites sans aide de fond, calcul ou justification d’échelle corrects, et aucune case fermée traversée. **Décision de maîtrise** : réussite de deux manifestations **dans des contextes différents**, à des moments séparés si possible, jamais simple seuil total. Si entraînement préalable sur la même carte, la preuve est contaminée et doit être remplacée par une épreuve équivalente revue.

## Sécurité, équité et accessibilité

Plans et parcours exclusivement fictifs, aucun déplacement demandé; aucun besoin de révéler son quartier, une adresse, son identité ou ses convictions. Les plans ASCII ont colonnes/lignes lisibles et **description textuelle** de la légende et de la flèche N. Proposer grands caractères, maquette tactile ou écoute orale des positions; accepter une suite de cases dictée à un scribe neutre. Ne pas noter graphisme, vitesse, vision des couleurs ou récit d’expérience personnelle. Vérifier les rubriques par relecteur humain avant épreuve certificative : banque `a_revoir`.
