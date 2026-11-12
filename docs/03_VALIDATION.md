# Portées de validation

`py -3 tools\ekole.py verify` teste : présence des 202 membres du registre, identité de chaque contrat/bank, 14 fichiers de livraison par membre, référentiel de liens du graphe, unicité des items, analyse JSON, couverture des pages et absence de doublons.

Il **ne teste pas** l'efficacité pédagogique, les droits sur tous médias, les scénarios de SemantiK en production, le site Moodle réel, la publication v10, l'intégrité de tout dépôt distant ou la sécurité d'un serveur déployé.

Tous les items pédagogiques doivent être revus par une personne qualifiée avant exploitation en classe. Les profils linguistiques autres que `fr-CA` ne sont pas publiables sans réalisation contrôlée et validation des sorties SemantiK.

L'audit précédent avait relevé des anomalies de normalisation de familles et manifestes; elles ne sont pas silencieusement corrigées ici. `kristals/` conserve les livraisons originales.
