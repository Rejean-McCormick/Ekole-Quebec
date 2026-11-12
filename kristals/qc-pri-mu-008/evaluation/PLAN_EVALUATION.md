# Plan d'évaluation — `qc-pri-mu-008`

**Objectif** `obj-1` : Écouter un extrait et en décrire des caractéristiques musicales observables. **Critère** `crit-1` : Présenter une analyse d’écoute justifiée par des moments précis. **Famille** `qc-pri-mu-008-ev-01`; mode privilégié **`observation_ou_production`**, mis en œuvre par 10 items fixes sous le contrat JSON commun. L'enseignant produit les micro-œuvres originales localement à partir de scores exacts; **aucun fichier son préenregistré n'est livré**. Avant toute passation, vérifier la fidélité d'exécution et la perception réelle des élèves.

## Couverture, difficulté, représentation et critères par item

**Chaque ligne lie explicitement** l'item à `obj-1`, `crit-1` et `qc-pri-mu-008-ev-01`; cette liaison est répétée dans le JSON. Les items 001–008 sont formatifs; les items 009–010 sont les deux manifestations nécessaires de maîtrise.

| Item complet | Niveau | Représentation | Observables ciblés | Usage |
|---|---|---|---|---|
| `qc-pri-mu-008-q-001` (`obj-1` / `crit-1` / `qc-pri-mu-008-ev-01`) | initial | 2 groupes T | 2 attaques puis 4, repères 1/3 et 5–8 | formatif |
| `qc-pri-mu-008-q-002` (`obj-1` / `crit-1` / `qc-pri-mu-008-ev-01`) | initial | comparaison T/F | timbre contrasté, positions rythmiques identiques | formatif |
| `qc-pri-mu-008-q-003` (`obj-1` / `crit-1` / `qc-pri-mu-008-ev-01`) | initial | M brefs | densité ≠ accélération, pulsation stable | formatif |
| `qc-pri-mu-008-q-004` (`obj-1` / `crit-1` / `qc-pri-mu-008-ev-01`) | intermediaire | trois groupes T/F | rythme relatif et source à 9 | formatif |
| `qc-pri-mu-008-q-005` (`obj-1` / `crit-1` / `qc-pri-mu-008-ev-01`) | intermediaire | structure F/L/F | retour 1–4 à 9–12, segment B | formatif |
| `qc-pri-mu-008-q-006` (`obj-1` / `crit-1` / `qc-pri-mu-008-ev-01`) | intermediaire | trois groupes F/T | diminution de densité puis timbre | formatif |
| `qc-pri-mu-008-q-007` (`obj-1` / `crit-1` / `qc-pri-mu-008-ev-01`) | intermediaire | quatre groupes M/T | forme AABB et densité 2→3 | formatif |
| `qc-pri-mu-008-q-008` (`obj-1` / `crit-1` / `qc-pri-mu-008-ev-01`) | transfert | alternance T/F | forme ABAB avec indices temporels | prétransfert |
| `qc-pri-mu-008-q-009` (`obj-1` / `crit-1` / `qc-pri-mu-008-ev-01`) | transfert | original A, T/F, 16 pulsations | 3 faits distincts, 2 notions dont structure/contraste, localisation et autonomie | **preuve A** |
| `qc-pri-mu-008-q-010` (`obj-1` / `crit-1` / `qc-pri-mu-008-ev-01`) | transfert | original B, M/L, 16 pulsations | 3 faits distincts, forme AABB, contraste à 9, localisation et autonomie | **preuve B** |

## Progression et conditions d'épreuve

1. Avant chaque écoute, le responsable teste doucement les sources T, F, L, M et l'égalité des **16 pulsations** (c. 1/seconde); avertir en cas de son inattendu. La notation T/F/L/M est **pour l'exécutant**, pas une réponse montrée au candidat pendant sa prestation.
2. Pour la maîtrise A : score `T · T · | T T T T | F F F F | T · T ·`. Pour la maîtrise B : score `M M · · | M M · · | L · L L | L · L L`. Exécuter chaque score intégralement dans l'ordre, avec deux écoutes non directives possibles.
3. Demander une réponse de trois constats observables : au moins deux notions, dont une **structure/contraste**, des pulsations précises, séparation observation/opinion. Consigner la modalité de réponse et les aides effectivement fournies.
4. Coter chaque preuve **indépendamment** selon `GRILLE_MAITRISE.md`. Ni correction en direct, ni imitation d'un modèle, ni « solution » montrée pendant l'épreuve. Arrêter/réaménager si le son ou la modalité d'accès pose un problème.

## Variabilité autorisée et contrôle du corrigé

- **Tous les items sont fixes**, seed et paramètres `null`; aucun tirage paramétrique ni génération contextuelle par IA. Ordre des sons, timbre codé, positions des attaques, comparaisons attendues et grilles sont verrouillés.
- Ajustables sans guider : volume modéré, temps de réponse, nombre de réécoutes entières fixé localement, réponse orale/écrite/pictographique, supports d'accès visuel/tactile synchronisés et installation physique. Ne pas modifier les motifs pour « simplifier » une épreuve de maîtrise; si adaptation plus profonde indispensable, la faire approuver par un évaluateur humain et documenter les limites de comparabilité.
- La **fidélité humaine d'exécution** n'a pas été mesurée par un test automatisé; le score est un contrôleur textuel, pas une preuve d'identité acoustique des performances. La version finale de diffusion doit être approuvée et testée localement.

## Sécurité, équité et droits

Assurer une **accessibilité** auditive et communicationnelle raisonnable et privilégier un volume confortable, court et non surprenant, sans casque imposé, sans évaluation de qualité vocale, d'audition innée ou de goût; sources sonores produites localement. Aucune musique commercialisée ni enregistrement protégé fourni. Ne recueillir aucune voix/photo/vidéo d'élève sans consentement approprié. CAST UDL 3.0 soutient la pluralité de moyens d'expression, mais **ne prouve pas** l'équivalence automatique d'un transcript visuel avec l'écoute observée.

## Couverture et limites

Rythme : 001,003,004,006,007,009,010. Timbre : 002,004,006–010. Structure : 005,007–010. Contraste : 002–010. **Décision** : réussite observée de chacune des preuves 009 et 010, pas de moyenne sur les dix. Tous les items sont `a_revoir`; aucune validation humaine terrain ou homologation n'a été réalisée.
