# Ekole — Kristal : sociétés autochtones et établissements français

Ce ZIP contient **un modèle Kristal des organisations humaines**, un **enrichissement du Kristal existant `qc-pri-us-009`**, un **micro-monde Élève autonome** et des outils hors ligne.

**Il n’ajoute pas un 203e cours et n’écrase aucun Kristal existant à l’extraction.**

## Installation à la racine d’Ekole

Extraire ce ZIP à la racine du dépôt, au même niveau que `site/`, `tools/` et `kristals/`.

1. Si le cadre `qc-pri-us-009/kristal.workspace.json` manque, restaurer uniquement ses fichiers absents : `py -3 tools\integrer_kristal_histoire.py --root . --restore-missing-frame --apply`. (Sinon, sauter cette étape.)
2. Prévisualiser l’enrichissement du cours : `py -3 tools\integrer_kristal_histoire.py --root .`.
3. Appliquer si tu valides les modifications et si le Kristal `qc-pri-us-009` existe : `py -3 tools\integrer_kristal_histoire.py --root . --apply`.
4. Compiler les données publiques Élève : `py -3 tools\compiler_atelier_histoire.py --root . --prefer-installed`.
5. Ouvrir `site/eleve/ateliers/rencontres-quebec/index.html` par double-clic, **même hors ligne**, ou par le serveur local Ekole : `http://127.0.0.1:8765/eleve/ateliers/rencontres-quebec/`.
6. Valider : `py -3 tools\valider_kristal_histoire.py`, puis `py -3 -m unittest discover -s tests -p 'test_kristal_societes.py'`.

L’intégrateur n’écrase pas les fichiers pédagogiques existants. Il fait un patch contrôlé de `kristal.workspace.json`, `canon/state.index.json` et `sources/source-catalog.json`, sauvegarde les versions modifiées, et refuse les collisions avec des fichiers locaux personnalisés.

## Important

- 23 faits historico-pédagogiques contextualisés, 22 activités candidates, 6 prompts visuels; **zéro image générée**.
- Les faits sont tirés de sources documentaires listées, dont plusieurs institutionnelles ou coloniales. Il faut une **revue des nations concernées** avant tout usage institutionnel.
- Les tests établissent la cohérence des données et du fonctionnement logiciel, pas la validité de toutes les activités ni une homologation du cours.
- Les réponses se vérifient sans IA à l’exécution. Les productions ouvertes ne reçoivent pas de score automatique.
- SemantiK n’est pas intégré nativement ici : le moteur réalise les phrases françaises préparées depuis des faits structurés. Le raccord de génération de phrases multilingues reste une étape d’intégration.
- Konstellation Light n’a pas reçu de fausse URL de collection publiée. Le Kristal modèle est au statut `building`, pas `published`.

## Architecture rapide

`kristals/modele-organisation-humaine/` : modèle polymorphe canonique v9, source des types.

`modules/qc-pri-us-009/` : greffon historique, sources, séquence, activités et prompts, prêt à intégrer dans le Kristal existant.

`site/eleve/ateliers/rencontres-quebec/` : exercice autonome avec boutons, associations, chronologie, questions proposées et prompts affichés si image absente.

`tools/` : validation, installation prudente, compilation déterministe.

L’enrichissement est rangé sous `experience/histoire-rencontres/` pour **préserver les intentions visuelles v10** déjà présentes dans `experience/RESSOURCES_VISUELLES.json`.
