# Plan d'évaluation — `qc-pri-ad-003` (v1.2)

**Objectif `obj-1` (immuable) :** Improviser une interaction en respectant les propositions des partenaires.  
**Critère `crit-1` (immuable) :** Soutenir une improvisation avec cohérence et prise en compte d’autrui.  
**Famille `qc-pri-ad-003-ev-01` :** `observation_ou_production`, dix items `fixe`, sources et corrigés/rubriques verrouillés. Le **texte des offres est fourni à l'administrateur, pas dévoilé d'avance à l'apprenant**. Aucun générateur IA libre ni pseudo-hasard.

## Couverture explicite des dix items

**Chaque ligne ci-dessous relève de `obj-1`, de `crit-1` et de `qc-pri-ad-003-ev-01`**, et ces identifiants sont également inscrits dans les objets JSON. Les items 001–008 vérifient chacun une composante de la preuve, sans prétendre à eux seuls établir l'ensemble de la maîtrise.

| Item complet | Difficulté | Situation / représentation | Critère prioritaire et usage |
|---|---|---|---|
| `qc-pri-ad-003-q-001` | initial | exposition, court dialogue ou geste | écouter une offre, y relier sa contribution; diagnostic formatif |
| `qc-pri-ad-003-q-002` | initial | coffre à histoires, duo | relancer et attendre une réponse réelle |
| `qc-pri-ad-003-q-003` | initial | affiche au sol, jeu gestuel ou verbal | créer une action pertinente observable |
| `qc-pri-ad-003-q-004` | intermediaire | jardin de papier, nouveauté | intégrer l'imprévu dans la scène |
| `qc-pri-ad-003-q-005` | intermediaire | atelier, règle de sécurité | poser une limite et conserver la possibilité d'une suite sûre |
| `qc-pri-ad-003-q-006` | intermediaire | script dialogué annoté + courte réponse | identifier offre, action et relance possible |
| `qc-pri-ad-003-q-007` | intermediaire | changement de rôles | partager l'initiative et les tours |
| `qc-pri-ad-003-q-008` | transfert | cabine à histoires, trois offres | former une mini-scène cohérente, préparation formative |
| `qc-pri-ad-003-q-009` | transfert | **affiche d'un festival fictif**, duo à trois offres | **preuve autonome A complète**, M1–M4 |
| `qc-pri-ad-003-q-010` | transfert | **gare de voyages imaginaires**, duo à trois offres | **preuve autonome B complète**, M1–M4 |

## Administration et fiabilité de l'observation

1. Délimiter un espace neutre et sûr; convenir d'un signe d'arrêt. Le partenaire évaluateur lit exactement les **trois offres successives**, sans commentaire approbateur qui donne une solution; il attend la réponse. Il peut répéter mot pour mot une offre à la demande.
2. Offrir avant l'épreuve les modalités accessibles (parole, signes, gestes, communication assistée, poste assis, repères de tours sans répliques, temps de traitement). Ne pas noter accent, expression de visage imposée, volume de voix, personnalité, aisance sociale supposée ou humour.
3. Noter pour chaque tour l'offre, la proposition de l'élève et la place donnée au partenaire. Évaluer **M1 écoute et accueil**, **M2 action/relance**, **M3 cohérence/imprévu**, **M4 autonomie/respect** sur niveaux 0–2.
4. Administrer les preuves A et B dans des moments distincts lorsque possible; ne pas révéler les deux dialogues complets en préparation. Une performance apprise mot pour mot n'est pas une improvisation autonome.
5. **Maîtrise :** résultats suffisants indépendamment pour A et B. Le partenaire ne doit ni inventer d'obstacles plus difficiles pour un élève ni accepter l'insécurité au nom de l'« esprit d'équipe ».

## Variabilité et corrigés contrôlés

- **Mode des dix items : `fixe` ; `seed=null`, `parametres=null`.** Les répliques du partenaire et les deux surprises de maîtrise sont dans `BANQUE_ITEMS.json`; les réponses possibles sont *multiples* mais soumises à des critères **observables stables** et à des exemples commentés.
- **Autorisés :** posture, volume, délai nécessaire, supports de communication non directifs, taille des cartes, partenaire professionnel préparé, simple répétition exacte de l'offre.
- **Interdits :** souffler la réponse, modifier la difficulté ou la surprise par élève, changer les critères après coup, pousser les participants à un contact, improviser des provocations et générer librement un corrigé avec l'IA.
- L'item 005 sur les limites n'impose pas la relance lorsqu'un élève choisit légitimement d'interrompre une action risquée. Ne pas utiliser un refus de contact comme preuve d'incapacité à improviser.

## Sécurité, équité et couverture

Scénarios fictifs, culturellement non exclusifs, aucune histoire vécue obligatoire, pas de moquerie ni de captation vidéo requise. Modes d'expression diversifiés et consentement aux rôles. Si une modalité empêche réellement d'observer l'interaction, l'équivalence doit être déterminée par une revue humaine, pas inventée. Prévoir un observateur formé et une seconde cote possible si jugement incertain. Les critères de maîtrise sont éditoriaux et non étalonnés; **révision humaine avant usage sommative**.
