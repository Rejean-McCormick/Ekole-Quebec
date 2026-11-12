# MA-005 — Plan d'évaluation, famille `qc-pri-ma-005-ev-01`

**Identification de tous les items :** `objectif_id=obj-1`, `critere_id=crit-1`, famille `qc-pri-ma-005-ev-01`, objectif « Produire une estimation défendable et arrondir selon un rang annoncé », preuve « Estimer puis vérifier une quantité en signalant l’écart observé ».

| Items | Complexité | Représentations | Couverture |
|---|---|---|---|
| 001–002 | initial | nombres et droite graduée | arrondi d'une quantité et cas de milieu |
| 003–006 | intermédiaire | deux termes, tableaux | somme, soustraction, quantités; vérifier l'écart |
| 007–009 | initial/intermédiaire | inventaire, cahiers, réserve | corrigés fixes vérifiés et interprétation |
| 010 | transfert | livraison de livres | changement de contexte |
| **011** | transfert | deux types de boîtes | **M-A** : addition autonome, stratégie et écart |
| **012** | transfert | distribution de trousses | **M-B** : soustraction autonome, stratégie et écart |

## Variables paramétriques contrôlées
Les six premiers items utilisent **des catalogues finis de cas explicités dans `parametres.domaines.cas_finis`**, sans tirage libre. `index = seed % len(cas_finis)`; `seed` est un entier stable. Variables : `n`, `a`, `b` et `rang r` parmi {10,100,1000}. Chaque cas respecte les contraintes `n>=0`, `a>=b` en soustraction et `r>0`. La convention est le milieu vers le haut sur entiers non négatifs. La formule `R(n,r)=r*floor((2n+r)/(2r))` arrondit à un multiple de r. Pour somme et différence, arrondir **chaque terme** avant l'opération, calculer aussi le résultat exact, la différence `E−T` et l'écart `|E−T|`. Les exemples fournis ne justifient pas une génération infinie hors des domaines.

## Barème critérié
Quatre dimensions, évaluées sur chaque tâche : (1) rang et stratégie annoncés; (2) approximation mathématiquement cohérente; (3) quantité exacte calculée avec unité; (4) différence signée et écart absolu correctement calculés et interprétés. Niveau `établi / en développement / à reprendre` par dimension, sans transformer un pourcentage unique en maîtrise. M-A et M-B doivent être réussies séparément et **sans indice**.

## Accessibilité et sécurité
Grands caractères, lecture orale de la consigne, droite graduée, paquets ou justification orale possibles. Une calculatrice pour la **vérification** du calcul exact seulement doit être documentée et ne peut effectuer les arrondis à la place de l'élève. Scénarios fictifs; aucune donnée personnelle ou argent réel. Faire revoir choix des nombres et faisabilité par un pédagogue, et les adaptations particulières.

## Statut et limites
`validation_status=a_revoir` sur les 12 items. L'exactitude des variantes finies peut être testée automatiquement; **ni adéquation au niveau, ni qualité de l'expérience élève** n'est certifiée sans revue humaine et essai terrain.
