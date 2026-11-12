# Validation de la livraison — Kristal Sociétés et rencontres

## Environnement

- Validation sur les éléments fournis : *Kristal Authoring Kit*, cadre du cours `qc-pri-us-009`, sources pédagogiques de la v12, ancien visuel de v11.
- Ce n'est ni une publication de collection Kristal v10 ni une qualification institutionnelle.

## Contrôles exécutés

- Contrôle et `build-v9` du modèle `modele-organisation-humaine` : OK, candidat v9 seulement.
- Intégration ciblée du cours historique dans une copie des cadres et contenus existants : OK.
- Second lancement de l'installateur : 0 modification (idempotence).
- Contrôle et `build-v9` du `qc-pri-us-009` enrichi : OK, candidat v9 seulement.
- Tests Python du paquet : OK.
- Validation du corpus : 23 faits sourcés, 22 activités candidates, 6 concepts d'images et aucune image générée : OK.
- JavaScript de l'interface : syntaxe `node --check` OK.
- Contrôles Node du jeu compilé : résolutions des faits/sources, réponses uniques, rétroactions, prompts manquants.
- Anciennes fiches du cours et visuels v10/v11 : préservés dans l'essai d'intégration.

## Limites franches

- Le test d'interaction visuelle dans Chromium n'a **pas réussi à s'exécuter** dans cet environnement (navigation bloquée); l'ergonomie doit être essayée sur Windows/tablette.
- La vérification technique d'une source ne démontre pas que toute interprétation historique ou distracteur est pédagogiquement parfait.
- Une consultation de personnes ressources et des nations concernées est nécessaire avant un usage scolaire institutionnel; les sources comportent perspectives et limitations.
- SemantiK, Konstellation Light et Moodle ne sont pas connectés nativement dans ce greffon. Le jeu local ne requiert ni IA ni réseau.

## Essai local

```powershell
py -3 tools\valider_kristal_histoire.py
py -3 -m unittest discover -s tests -p test_kristal_societes.py
node tests\test_atelier_hors_ligne.mjs
```

Les contenus sur les injustices coloniales sont prévus pour une discussion accompagnée, **sans score automatique**.
