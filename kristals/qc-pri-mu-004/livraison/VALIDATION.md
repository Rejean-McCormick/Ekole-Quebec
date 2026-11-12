# Validation de livraison — `qc-pri-mu-004`

**État :** rédaction complète, validation documentaire et technique à effectuer par script; toutes les évaluations musicales exigent encore une revue humaine et des essais auditifs avec instruments réels. Ni publié, ni homologué, ni certifié.

## Périmètre de livraison

Un seul ID et quatorze fichiers sous `kristals/qc-pri-mu-004/` (deux remplacements authoring existants, douze ajouts). Aucun autre Kristal, registre, gouvernance, canon, state, runtime, docs, `ALIGNEMENT.md`, `BRIEF_REDACTION.md`, `AGENTS.md` ou `kristal.workspace.json` n'est livré.

## Tests techniques effectivement exécutés

**7834 assertions techniques préarchivage réussies**, sans échec : 14 chemins non vides, sécurité des chemins, parse YAML des deux parcours et conservation de leurs clés immuables, trois JSON stricts sans clés dupliquées, métadonnées v1.2 du contrat préservées, famille enrichie, liens du graphe, 10 IDs et énoncés uniques, rubriques, présence des réponses de sources, absence de génération audio libre, deux preuves indépendantes A et B, couverture du plan, références et accessibilité.

**Fusion réellement simulée dans un dossier temporaire** : décompression des fichiers du workspace v1.2, écrasement des seuls 2 `authoring/` existants et ajout de 12 nouveaux fichiers; **7320 fichiers maîtres protégés comparés SHA-256 avant/après**, inchangés. Aucun fichier protégé inclus dans le delta.

**Qualité des corrigés contrôlée structurellement** : noms des instruments et séquences codées vérifiés; critères et feedback présents. **Non contrôlé par écoute** : la qualité réelle des sons, leurs indices acoustiques et leur discrimination avec du matériel scolaire; l'enseignant doit prévalider les stimuli avant usage. Aucune présence de média protégé dans le ZIP.

**Après écriture du ZIP**, le script vérifie à nouveau les 14 entrées, les 3 JSON à l'intérieur de l'archive, l'intégrité CRC (`testzip()`), l'ordre et le manifeste (résultat dans la sortie console).

## Limites non résolues et points de revue humaine

1. **Absence de sources audio binaires dans le ZIP** : les sons T/M/D doivent être joués en direct, selon protocole P0; les items ne sont pas utilisables comme QCM audio hors ligne sans matériel. Leur audibilité et leur différenciabilité ne sont pas testées par ce contrôle documentaire.
2. **Préparation** : adulte et trois instruments en bon état, salle calme, volume sûr, contrôle du matériel avant épreuve. À vérifier physiquement en classe.
3. **Accessibilité et équivalence** : adaptation de l'écoute en cas de surdité ou d'hypersensibilité; une preuve purement visuelle ne suffit pas à établir la compétence de reconnaissance des sons. Décision humaine nécessaire.
4. **Rubriques et seuils** : C1–C5 non étalonnés, corrigeabilité des adjectifs et concordance interévaluateurs à vérifier avec des performances sonores effectives. Deux contextes ne peuvent remplacer cette vérification.
5. **Provenance et droits** : aucun son protégé ou morceau inclus; vérifier toute licence ou consentement si une captation est ajoutée ultérieurement. Aucune autorisation externe présumée.

## Propositions de structure, sans changement du workspace central

- Un registre d'**actifs de stimulus auditif** pourrait relier l'ID d'une prise sonore validée, son niveau cible, l'instrument et les droits d'enregistrement. Non créé ici car le ZIP est limité aux 14 fichiers et aucune captation n'a été fournie.
- Une matrice d'**adaptations accessibles contrôlées** et une procédure d'étalonnage interévaluateurs seraient utiles dans la gouvernance future; simple recommandation, pas modification des fichiers centraux.
- Distinguer formellement dans le moteur un item « structurellement complet, mais matériel live non passé » d'un item dont le média audio a été juridiquement et acoustiquement vérifié.
