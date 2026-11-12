# Ports SemantiK et Konstellation

**Entrée SemantiK** : pour chaque obligation de page, `id`, `source_ref`, `kind=utterance`, `language`, `semantic_payload`, `allowed_variation`, `status`. **Sortie attendue** : phrase réalisée, liens de provenance et statut de validation; aucun paragraphe généré. À ce stade, les phrases françaises dans `organisation/pages/` sont des propositions éditoriales, pas des sorties SemantiK.

**Konstellation** : la navigation est un graphe de pages, audiences, disciplines et liens de membres; l'index de découverte GitHub v10 n'est ni une preuve d'autorité, ni le graphe pédagogique. `Konstellation-Light` peut projeter une collection v10 **qualifiée**; le site Ekole ne prétend pas être une collection v10 qualifiée.

**Références externes** : résolution séparée via un registre (`organisation/services_externes.example.json`) où les liens restent désactivés avant vérification de l'URL et des données transmises. Les identifiants de Médiathèque restent opaques.

**Évolution nécessaire** : adaptateurs bidirectionnels et contrats schématisés avec versions explicitement épinglées, tests d'intégration dans un environnement contrôlé, contrôle des langues et de l'accessibilité.
