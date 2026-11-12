# Ekole v8 — L'école qui se parcourt : architecture & responsabilités

**Statut : prototype d'expérience, pas une qualification pédagogique ni une publication v10.**

## Architecture des trois espaces

```text
202 Kristals pédagogiques auteurs / registre / graphe
     │ immutable autorité sémantique
     ▼
Ekole Core (site/, administration locale et catalogue)
  ├─ Ekole Élève (site/eleve/, export public filtré)
  │   ├─ Années 1-6 / 3 cycles / 4 étapes pédagogiques
  │   ├─ Quatre moments : Découvrir → Essayer → Expliquer → Explorer
  │   ├─ 202 fiches de découverte basées sur les objectifs sources
  │   ├─ 6 ateliers pilotes distincts (sans évaluation officielle)
  │   ├─ Carte locale Avant/Après, carnet de session sans identité
  │   └─ Images approuvées seulement / descriptions provisoires
  └─ Ekole Enseignant (enseignant-app/, serveur 127.0.0.1:8766)
      ├─ Lecture complète des six modules et de leurs consignes
      ├─ Préparation proposée de séance (durées modifiables)
      ├─ Grille de revue et atelier de prompts d'images
      └─ Consultation locale des 202 références

Konstellation Light (viewer séparé):
  navigation locale Ekole : graphe pédagogique de référence
  viewer v10 : lien seulement quand une collection publique vérifiée existe
SemantiK Architect : phrases en sortie, non paragraphes; non branché.
Médiathèque : droits et attributions des médias à vérifier.
Moodle : éventuel service opérationnel, non modèle de page ni obligation de conversion.
```

## Exigence 8 ans

Un choix à la fois, gros contrôles, consignes courtes, langage direct, pas d'ID technique sur les cartes, priorité au geste et au visuel. L’enfant ne doit pas voir les réponses des diagnostics ou les contenus de la banque d'évaluation. Les réponses d’un atelier pilote déterministe ne sont **pas** celles d’une preuve de maîtrise source.

## Corpus et limites

202 parcours auteurs préservés sans modification. L'affectation à une année/étape reste proposée et est présentée comme telle. Les 4 étapes d'Ekole (Automne 1/2, Hiver 1/2) sont une vue pédagogique configurable, et non les trois étapes officielles des bulletins. Les ateliers `qc-pri-ma-001`, `qc-pri-ma-012`, `qc-pri-ma-009`, `qc-pri-ma-005`, `qc-pri-fr-004`, `qc-pri-ad-001` possèdent une interaction pilote d'auteur originale et non évaluée; les 196 autres ont une fiche de découverte avec consignes générales. Cela n’équivaut pas à 202 cours interactifs complets.

## Frontière du carnet

`sessionStorage` conserve uniquement les ID des activités **essayées** et leurs titres pour l’onglet en cours. Aucune identité, aucun enregistrement audio, aucune note ou suivi serveur. Bouton effacement; fermeture de l'onglet efface les données selon le navigateur. Ne pas assimiler cette exploration à un achèvement de cours.

## Dossier image

`visuels/INTENTIONS_IMAGES.json` conserve 227 intentions non générées. `visuels/SCENES_V8.json` ajoute 17 scénarios génériques. Chaque dessin approuvé est lié à un `visual_id`, une licence, une provenance, un SHA256, un alt et trois revues humaines. Les fractions et quantités exactes doivent être dessinées par des contrôles déterministes, pas par DALL·E. Le compilateur n'invente pas de licence et ne publie rien sur un serveur distant.

## Sécurité

Le Core actuel expose localement des données de cours qui contiennent des corrigés. **Ne pas publier `site/` entier.** Pour un hébergement public, exporter seulement `site/eleve` par `tools/export_ekole_eleve_v8.py`. Le serveur enseignant est une démo locale basée sur cookie temporaire, non une authentification multi-utilisateurs. Aucune identité personnelle d'enfant dans les fichiers.
