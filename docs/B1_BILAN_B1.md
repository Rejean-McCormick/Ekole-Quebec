# Ekole — B1 : audit de couverture pédagogique de la 3e année

**Version B1.1 — 16 octobre 2026 — audit documentaire reproductible**

## Verdict

**Couverture pédagogique intégrale de 3e année : NON démontrée.** Ce rapport ne prétend pas que le programme officiel est couvert à 49/83 ou à 12/83 : ce sont des **indicateurs internes** mesurant les relations entre des fichiers de conception. L'atteinte d'un apprentissage est impossible à inférer de l'existence d'une ressource ou d'une mission.

### Périmètre réellement analysé

- `znapshot_Ekole_10151241.zip` : catalogue de 202 Kristals, affectations candidates par année dans `docs/AUDIT_ACTIVITES_202_V14.json`, plan de transformation V12 et preuves théoriques du catalogue.
- `znapshot_Kontexte_10152150.zip` : 83 objectifs candidats, 60 situations contextualisées, audit interne, 36 semaines, 34 micro-situations.
- Pages du ministère de l'Éducation du Québec : repérage des **sources de référence**, mais **pas extraction et validation exhaustive de chacune des progressions officielles**. Ce travail reste à effectuer avec un enseignant.
- Les artefacts v3 réécrits dans d'autres conversations ne font pas partie de ces deux captures. Les fichiers `cours/*.json` v3, les publications enfant v3 et leur état actuel ne sont donc **pas vérifiés ici**.

Le contenu source des snapshots a été conservé inchangé. Voir les empreintes SHA-256 dans `donnees/05_INDICATEURS_ET_PROVENANCE.json`.

## Résumé chiffré — avec nature exacte de chaque chiffre

| Indicateur | Résultat | Interprétation correcte |
|---|---:|---|
| Cours candidats Ekole, toutes années | 202 | Répertoire historique, non homologué |
| Cours classés *provisoirement* en 3e année | 36 | Affectation interne à valider |
| Cours de 3e avec un outil/activité **candidat** selon V14 | 8 / 36 | Intention ou prototype; ni disponibilité ni qualité confirmée |
| Cours de 3e sans outil candidat recensé dans V14 | 28 / 36 | Manque apparent dans cet ancien inventaire |
| Objectifs candidats indexés par Kontexte | 83 | Référentiel **interne**, pas liste exhaustive officielle |
| Objectifs liés aux 32 scénarios principaux | 49 / 83 | Lien documentaire, **pas maîtrise démontrée** |
| Objectifs sans lien avec ces 32 scénarios | 34 / 83 | Des micro-situations sont proposées pour eux, **non réalisées** |
| Objectifs Kontexte pointant vers un cours classé 3e par Ekole | 12 / 83 | **Désalignement d'index** : les 71 autres pointent vers un cours existant mais classé ailleurs |
| Cours 3e recevant au moins un objectif de Kontexte | 11 / 36 | Ne prouve pas que les 25 autres sont vides |
| Scénarios adaptés catalogués dans Kontexte | 60 | 32 au cœur du parcours annuel; 28 en banque optionnelle |
| Semaines prévues dans Kontexte | 36 | Semaines 9, 18, 27 et 36 sans scénario principal attribué |
| Évaluation d'élèves réellement observée | **Aucune** | Les « preuves attendues » sont des descriptions, pas des travaux d'élève |
| Attestation de conformité PFEQ | **Aucune** | Non revendiquée dans les sources |

## 1. Problème structurel majeur : affectation des cours

Sur les 83 objectifs de Kontexte, **71 renvoient à des Kristals présents dans le catalogue, mais non classés en 3e année** par l'audit Ekole V14. Ce n'est ni 71 erreurs de programme ni 71 sujets à supprimer. C'est un défaut d'alignement **entre deux référentiels internes distincts**. Les affectations de l'un et de l'autre n'ont pas fait l'objet d'une validation commune.

Exemples concrets :

- Plusieurs objectifs de numération, additions, soustraction, géométrie, mesures et lecture de cartes renvoient à des cours Ekole placés hors du classement de 3e année.
- En univers social, les **8 objectifs** du sous-index Kontexte renvoient à des cours classés hors 3e dans l'ancien audit, alors que le sous-index met précisément en avant la chronologie, le territoire, les sources et certaines sociétés vers 1500.
- En multiplication, `qc3.ma.multiplication` renvoie bien à `qc-pri-ma-008` classé en 3e année : c'est un bon point de départ pour construire un exemple complet et vérifiable.

**Action prioritaire B1 :** faire revoir les 83 liens **objectif → Kristal → année** par discipline. Ne pas réaffecter automatiquement les Kristals à la 3e année; une connaissance peut être transversale, un prérequis ou un approfondissement d'une autre année.

## 2. Scénarios : 49 reliés, 34 à compléter

Les **32 scénarios principaux** mobilisent 49 objectifs candidats sur 83. Les **34 autres** apparaissent dans un plan de micro-situations, mais leur statut indique une **conception à relire et instancier**. Il n'y a pas de preuve de réalisation en classe.

Dans la banque complète de 60 scénarios, **51** objectifs sont référencés au moins une fois, contre 49 dans le plan principal. C'est une banque de contextes additionnels, **pas** l'équivalent d'un enseignement déjà dispensé.

Les quatre semaines 9, 18, 27 et 36 n'ont pas de scénario principal. Elles peuvent être des périodes de bilan, d'ajustement ou d'évaluation : **ne pas les qualifier automatiquement de manquantes**; leur intention et leur contenu doivent être documentés.

## 3. Disciplines — liens avec les scénarios principaux

| Discipline | Objectifs internes | Liés aux scénarios principaux | Cours de 3e correspondant à l'objectif |
|---|---:|---:|---:|
| Français (FR) | 12 | 8 | 4 |
| Mathématique (MA) | 16 | 11 | 4 |
| Anglais langue seconde (ALS) | 5 | 2 | 1 |
| Science et technologie (ST) | 11 | 10 | 1 |
| Univers social (US) | 8 | 3 | 0 |
| Culture et citoyenneté québécoise (CCQ) | 12 | 6 | 1 |
| Éducation physique et santé (EPS) | 6 | 3 | 0 |
| Arts plastiques (AP) | 4 | 3 | 0 |
| Art dramatique (AD) | 3 | 2 | 1 |
| Musique (MU) | 3 | 1 | 0 |
| Danse (DA) | 3 | 0 | 0 |

Ces nombres **ne sont pas des taux de conformité par matière**. Des objectifs internes ont pu être omis, dépassés ou répartis sur d'autres années. L'offre de langues et d'arts varie selon les contextes; ce tableau ne présume pas que les 14 disciplines du catalogue sont obligatoires simultanément dans une école.

## 4. Alertes qualitatives qui exigent une validation humaine

**CCQ :** vérifier explicitement les contenus de 3e année dans la progression officielle, notamment ceux touchant la vie personnelle, les normes sociales, la sécurité, le numérique et la diversité des convictions. Préférer l'enseignement encadré aux missions qui exigeraient une divulgation intime ou une mise en scène de l'identité de l'enfant.

**Univers social :** revoir la progression sur les sociétés étudiées, la chronologie, les territoires et l'usage de sources appropriées, incluant expertise historique et culturelle. Éviter de présenter des reconstitutions stéréotypées comme des faits.

**Arts et langue :** distinguer les disciplines enseignées selon la configuration de l'école de celles conservées comme ressources facultatives; ne pas transformer toute absence de scénario en manque réglementaire.

**Activités et évaluation :** les huit cours de 3e comportant des prototypes dans V14 ne constituent pas huit acquis pédagogiques. Pour chaque objectif, il faut une tâche réalisable par l'enfant, une rétroaction appropriée, une modalité d'observation et des critères pertinents pour l'enseignant.

## 5. Sources officielles repérées — contrôle de conformité à compléter

Le ministère du Québec présente les **progressions des apprentissages** comme un complément aux programmes disciplinaires, apportant les connaissances à acquérir et à utiliser au fil des années. Une future matrice réglementaire devra référencer **chaque apprentissage précis**, son année, la page/table du PDF applicable, et la compétence à laquelle il se rapporte.

- Cadre des progressions : https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/a-propos
- Français primaire : https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/francais-langue-enseignement
- Mathématique primaire : https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/mathematique
- Science et technologie primaire : https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/science-technologie
- Univers social primaire : https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/geographie-histoire-education-citoyennete
- CCQ primaire : https://www.quebec.ca/education/prescolaire-primaire-et-secondaire/programmes-formations-evaluation/programme-formation-ecole-quebecoise/primaire/culture-citoyennete-quebecoise

**Non fait dans B1.1 :** la lecture ligne par ligne de tous les PDF de progression et cadres d'évaluation, l'attestation officielle par compétence et la revalidation humaine des affectations par année. Des liens vers des pages de programme, même officielles, ne suffisent pas à démontrer une correspondance par objectif.

## 6. Recommandations et priorité d'action

| Niveau | Travail | Justification | Branche intéressée |
|---|---|---|---|
| **P0** | Réconcilier les 83 objectifs avec les années proposées et les exigences applicables | 71 liens hors classement 3e | B1 + B2 + B5 |
| **P0** | Revue experte des 20 objectifs internes CCQ et US, et des contenus sensibles | Sécurité, conformité, sources et pertinence | B1 + B5 |
| **P1** | Passer les 34 micro-situations de « conçues » à activités révisées et vérifiables | Couverture documentaire ≠ pratique | B5 + B4 + B8 |
| **P1** | Examiner les 28 cours sans activité candidate dans V14 | Vérifier si une activité existe dans une version ultérieure avant d'en concevoir une | B1 + B4 |
| **P1** | Formaliser preuve/critères de chacun des 83 objectifs | Aucune trace élève observée dans le corpus | B2 + B8 |
| **P2** | Clarifier semaines 9, 18, 27, 36 | Périodes sans scénario principal, potentiellement de synthèse | B5 |
| **P2** | Distinguer contenus obligatoires, options d'école et soutien linguistique | Éviter une mesure erronée de la couverture | B1 |

## 7. Passage de relais à la consolidation

- **B2** : prendre `01_MATRICE_83_OBJECTIFS.csv` comme référentiel de correspondances candidates, **pas de prescriptions officielles**, et maintenir un champ `validation_humaine_requise`.
- **B5 Kontexte** : se concentrer sur les 34 micro-situations et la clarification des 4 semaines sans scénario; ne pas inventer de missions achevées.
- **B4 Élève** : piloter une multiplication contextualisée; la rendre compréhensible avant de produire en masse 33 autres leçons.
- **B8 QA** : vérifier toutes les correspondances, les actes de publication et le statut des preuves; un test vert de route ne vaut pas une preuve d'apprentissage.
- **Consolidation** : commencer par une comparaison des bases réellement utilisées par chaque branche, notamment Ekole snapshot historique versus paquet v3 découpé.

## Livrables B1

`donnees/01_MATRICE_83_OBJECTIFS.csv|json`, `02_INVENTAIRE_36_COURS.csv|json`, `03_SYNTHESE_DISCIPLINES.csv`, `04_PLAN_36_SEMAINES.csv`, `05_INDICATEURS_ET_PROVENANCE.json`, `auditer_b1.py`, `tests/test_b1.py`, `PROPOSITION.md`, `DEPENDANCES.md`, `TESTS.md`, `MANIFESTE_CHANGEMENTS.json` et un classeur Excel à onglets pour consultation.
