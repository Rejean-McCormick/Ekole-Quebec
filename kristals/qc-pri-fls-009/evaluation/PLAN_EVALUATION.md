# Plan d'évaluation — `qc-pri-fls-009`

**Objet (`obj-1`, immuable) :** Rédiger un court texte en français répondant à une consigne précise.  
**Critère (`crit-1`, immuable) :** Produire un texte bref avec début, information et clôture.  
**Famille (`family_id`) :** `qc-pri-fls-009-ev-01`; type privilégié `observation_ou_production`. **Statut de chaque item :** `a_revoir`.

## Architecture de la banque

**Dix items fixes**, déterminés manuellement; `mode=fixe`, `seed=null`, `parametres=null` pour chaque item. Les tâches de rédaction restent ouvertes quant à la formulation et requièrent une grille et une lecture humaine. Aucun tirage libre de texte, de nombres, de dates ou de corrigé par IA; la variation éventuelle des formulations **par l'élève** n'est pas une génération paramétrique.

| Item | Difficulté | Représentation / activité | Lien immuable | Indicateurs ciblés | Variation recevable |
|---|---|---|---|---|---|
| `qc-pri-fls-009-q-001` | initial | Repérage écrit sur invitation à Malo | `obj-1` / `crit-1` / `qc-pri-fls-009-ev-01` | Début, faits, clôture; expliquer le rôle de la fin | Formulation de l'explication; pas le découpage essentiel |
| `qc-pri-fls-009-q-002` | initial | Deux phrases à partir d'une fiche factuelle | `obj-1` / `crit-1` / `qc-pri-fls-009-ev-01` | Deux unités de sens, activité, lieu, moment | Synonymes et ordre des phrases sans changer les faits |
| `qc-pri-fls-009-q-003` | initial | Réparation d'une contradiction de jour | `obj-1` / `crit-1` / `qc-pri-fls-009-ev-01` | Cohérence et correction du jeudi | Réécriture de l'invitation, sans altérer jeudi/11 h/hall |
| `qc-pri-fls-009-q-004` | initial | Remise en ordre d'une annonce en segments | `obj-1` / `crit-1` / `qc-pri-fls-009-ev-01` | Organisation B–A–C, raison fonctionnelle | Explication en mots personnels; ordre fixé |
| `qc-pri-fls-009-q-005` | intermédiaire | Message personnel à Rosa | `obj-1` / `crit-1` / `qc-pri-fls-009-ev-01` | Destinataire, tous les faits, D-I-C, cohérence | Lexique et salutations adaptées; pas les faits |
| `qc-pri-fls-009-q-006` | intermédiaire | Demande à un adulte fictif | `obj-1` / `crit-1` / `qc-pri-fls-009-ev-01` | Question réelle, politesse, fait non inventé | Plusieurs formes de question correctes |
| `qc-pri-fls-009-q-007` | intermédiaire | Note de restitution d'un ballon | `obj-1` / `crit-1` / `qc-pri-fls-009-ev-01` | Situation, moment, lieu, fin | Choix des phrases non imposé |
| `qc-pri-fls-009-q-008` | intermédiaire | Annonce publique depuis notes en désordre | `obj-1` / `crit-1` / `qc-pri-fls-009-ev-01` | Renseignements complets, nuance « si possible » | Style personnel mais pas de nouvelle obligation |
| `qc-pri-fls-009-q-009` | transfert | **Preuve A** : invitation individuelle au jardinage | `obj-1` / `crit-1` / `qc-pri-fls-009-ev-01` | C1–C4 : tous faits, D-I-C, cohérence, phrases | Variantes libres de phrases, faits verrouillés |
| `qc-pri-fls-009-q-010` | transfert | **Preuve B** : annonce publique d'une collecte de livres | `obj-1` / `crit-1` / `qc-pri-fls-009-ev-01` | C1–C4 et adaptation à un autre genre | Variantes libres de phrases, faits verrouillés |

## Couverture / mode / poids

- **Organisation début–information–clôture :** items 001, 004, 005–010; **cohérence** : 002, 003, 005–010; **phrases intelligibles** : 002, 005–010; **réponse à des consignes précises** : 001–010. Les exercices initiaux sont des jalons, non des raccourcis de certification.
- **Pondération pour les deux preuves finales :** chacune est appréciée séparément selon **C1–C4, 0–2 par dimension**. Pas d'agrégation compensatoire entre A et B. Les items 001–008 sont formatifs et ne décident pas seuls de la maîtrise.
- **Deux contextes** : le message individuel `q-009` et l'annonce collective `q-010` ont des publics, intentions communicatives et situations différents. Ils sont prévus sans canevas ni rappel de formulations modèles pendant l'épreuve.
- **Seuil opérationnel proposé, non étalonné :** pour chacune des preuves, C1=2, C2=2, C3≥1 et C4≥1; documenter autonomie, possibilité de communiquer un choix d'organisation, conditions de passation. Seule une double réussite permet de proposer la maîtrise; échec d'une dimension → remédiation ciblée et nouvelle preuve.

## Règles de correction et variabilité

- Le corrigé des items 001, 003 et 004 comporte des segments/faits fixés contrôlables; leur interprétation est argumentée dans `reponse_attendue` et `criteres`. Pour les **productions ouvertes**, les exemples sont des modèles **non exclusifs**, pas des réponses uniques ni des sorties IA fiables.
- Les faits des scénarios fixes (dates relatives, lieux, matériel demandé) ne peuvent être substitués automatiquement; toute nouvelle variante exigerait un **nouvel item contrôlé**, une comparaison de difficulté et une revue humaine. Ne pas supposer qu'une graine fournit un générateur : `seed=null`, aucune variable.
- Contrôler les omissions et incohérences avant les détails d'orthographe. Les erreurs de surface mineures n'annulent pas une communication intelligible; une date contradictoire, en revanche, peut invalider C1 ou C3. Consigner la justification selon le cas, non un simple score.

## Conditions, accessibilité, sécurité et équité

Consignes et aide de compréhension disponibles à l'oral; vocabulaire factuel simple, police lisible, temps adaptable, clavier ou transcripteur neutre **qui ne reformule pas** lorsque nécessaire. Le produit reste un **texte français choisi par l'apprenant**. Pour les preuves A/B, tout conseil du correcteur sur les phrases, le plan ou les faits invalide l'autonomie et nécessite une reprise. Aucun accent, identité, vécu privé ou préférence culturelle n'est évalué. Tous les prénoms et événements sont fictifs; aucune collecte de nom réel, adresse, photo ou voix. Aucun matériel dangereux requis. Comparer l'effet de ces accommodements en revue humaine.

## Révision préalable à l'usage sommative

Une personne compétente en FLS doit vérifier la naturalité des messages en français québécois, les attentes d'âge et de compétence, la différence de difficulté des preuves, l'absence de biais et la durée réelle; faire ensuite un essai accessible avec apprenants, revoir les rubriques et la stabilité intercorrecteurs. **Aucun test élève, contrôle interjuges ou homologation PFEQ n'est prétendu.** Voir [grille](GRILLE_MAITRISE.md), [banque](BANQUE_ITEMS.json) et [références](../sources/REFERENCES_CONTENU.md).
