# ADR Ekole v9 — Mini-environnements pédagogiques réutilisables

Statut : **prototype technique d'entraînement, revue pédagogique humaine requise**. Aucun état Kristal v9 publié, aucun index GitHub v10 qualifié, aucune équivalence déclarée à un item d'examen, aucun résultat personnel enregistré.

## Pourquoi

La v8 proposait deux types de manipulation spécialisés et parfois une zone de texte générique. Les exercices ne doivent pas simuler une correction sur des dessins ou textes libres. Le nouveau MiniLab fournit **9 familles de manipulations à validation déterministe et 18 scénarios de démonstration originaux**.

| Composant | Activité de l'enfant | Vérification exacte | Rétroaction |
| --- | --- | --- | --- |
| Jetons et paniers | Sélectionne et distribue les jetons | Quotient, égalité des groupes, reste inférieur au nombre de groupes | Trop dans une boîte / reste / inégalité |
| Fractions | Colorie des parts *égales* | Nombre de parts sélectionnées et dénominateur donné | Trop / pas assez |
| Droite numérique | Déplace le repère avec boutons ou graduations | Coordonnée entière bornée et pas valide | Trop à gauche/droite |
| Séquences | Déplace les cartes par boutons haut/bas | Permutation ordonnée d'identifiants | Ordre à réviser |
| Associations | Associe deux ensembles | Fonction de correspondance entièrement définie | Omission / association erronée |
| Classement | Place des objets dans des catégories | Classe attendue par élément | Omission / classe incorrecte |
| Grille | Choisit une case par colonne et ligne | Coordonnées exactes et domaines bornés | Bonne/mauvaise case |
| Estimation | Entre une estimation entière | Écart absolu dans une tolérance bornée | Écart trop grand, pas un jugement de maîtrise |
| Suites | Choisit la continuation d'une suite | Suite arithmétique et réponse cohérente | Recherche du pas |

L'affichage utilise HTML + CSS, pas des images IA pour les quantités et la géométrie. Les jetons sont de vrais objets discrets avec identifiants. Les boutons ont des noms accessibles et peuvent être activés au clavier. Tous les changements ont une fonction `apply()` pure; la correction vient de `evaluate()` et d'un scénario approuvé. Il n'y a pas de progression privée, de compte, de micro ni de télémétrie.

## Où le retrouver

- Élève : `/eleve/labo/`, via « 🧩 Mes outils » dans la navigation.
- Élève, cours : étape **Essayer** → « 🧩 Essayer un outil », avec un filtre contextuel quand une association candidate existe.
- Enseignant : onglet **Outils** → bibliothèque de mini-environnements et code d'intégration à copier; point API protégé `/api/labo-catalogue.json` sur le serveur local 8766.

## Contrat de scénario

`site/eleve/labo/data/catalogue.json` est le registre des scénarios; `contracts/EKOLE_MICROLAB_0.1.schema.json` en valide la structure et le moteur valide les contraintes par famille. Chaque entrée comprend `id`, `type`, `title`, `instruction`, `parameters`, `source_kristal_id` (ou `null`), `association_status`, `validation_mode`, `status` et des `hints`. Ajouter un scénario de **type existant** ne demande pas de changer le moteur; vérifier le JSON et faire passer le validateur. Une nouvelle famille d'interaction exige un renderer, un validateur et des tests avant activation. Les réponses programmées en JS servent à entraîner; elles ne sont **pas les corrigés des familles d'évaluation Kristal**.

Les associations `qc-pri-ma-005/009/012` sont **provisoires et non validées pédagogiquement**. Le contrat ne prétend pas à la couverture automatique des 202 cours ni à deux preuves de maîtrise. D'autres cours peuvent utiliser plusieurs mini-environnements si un auteur le justifie.

### Ajouter à volonté

Pour ajouter un défi dans `data/catalogue.json` : dupliquer un item d'un même type, donner un ID inédit, définir `parameters` dans les domaines contrôlés, puis exécuter `python tools/valider_mini_labs.py`. Éviter toute modification des Kristals auteurs. Prévoir une revue humaine de l'énoncé, des droits, des variantes et de la pertinence du lien à un cours.

Un mini-environnement peut être ouvert par lien :

```html
<a href="/eleve/labo/?outil=partage-12">Partager les jetons</a>
```

Ou intégré dans une page dont la provenance est autorisée :

```html
<div id="atelier-partage"></div>
<script src="/eleve/labo/embed.js"></script>
<script>
  EkoleMiniLabEmbed.mount(document.getElementById('atelier-partage'), {
    id: 'partage-12', title: 'Partager 12 jetons dans trois boîtes', height: 700
  });
</script>
```

Ce helper crée une `iframe` d'exploration; il ne transfère aucune note à la page parent ni à un serveur. Les permissions du navigateur restent applicables. Utiliser une URL publique vérifiée au lieu de `127.0.0.1` dans les sites hébergés.

## Générateur/contrôles/UX

`site/eleve/labo/engine.js` est isolé du DOM : `validateSpec`, `initial`, `apply`, `evaluate`. `site/eleve/labo/app.js` est uniquement le renderer. Le registre est public **parce qu'il s'agit de pratique démonstrative**. Aucun examen n'est construit depuis ces réponses.

Validation : `node tests/test_microlab_engine_v9.js .` depuis la racine; `python tools/valider_mini_labs.py` pour JSON et dépendances. `tools/export_ekole_eleve_v8.py` a été étendu pour exporter les fichiers du MiniLab sans sources internes.

## Limites et besoins avant école réelle

- Revue ergonomique avec enfants, test tactile et clavier, lecteurs d'écran, CSS mobile.
- Une réussite répétée dans ces activités ne vaut pas validation des critères `obj-1 / crit-1` d'un Kristal.
- L'estimation utilise des zones de tolérance illustratives, non une règle normative.
- Certaines interprétations historiques, artistiques, orales ou ouvertes ont besoin d'observation humaine; il ne faut pas les convertir de force en association fermée.
- Le lien Konstellation Light conserve le comportement de v8 : pas de fausse publication v10.
- Les futures images IA peuvent ajouter de l'agrément et de la contextualisation, mais les objets évalués restent des formes déterministes avec compte exact.
