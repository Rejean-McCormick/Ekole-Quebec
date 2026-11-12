# Contrat du lecteur hors ligne

- Entrées : JSON canonique, JSON de projection publique, index de thèmes, options de pratique.
- Recherche : normalisation d'accents et quelques variantes de dictée vocale; correspondance stricte ou suggestions. **Aucune inférence sémantique libre**.
- Réponse : `reponse_courte`, puis `explication_detaillee`, `precision`, sources et préalables.
- Exercice : trois choix explicites, bon identifiant stable, ordre des boutons mélangé, explication et lien vers une fiche. Un élève peut lire les réponses dans le JSON ; il s'agit d'entraînement formatif.
- Source absente : erreur de validation, aucune correction automatique.
- Image : fichier `<theme>.webp` uniquement après production; `onerror` révèle le texte exact du prompt.
- Mode déconnecté : toutes les données nécessaires sont locales; cliquer sur une référence externe nécessite internet et ne modifie pas la réponse locale.
- Données privées : le lecteur n'enregistre pas d'élève, ne transmet pas de réponses, n'utilise ni cookie ni API IA.
- Publication : le Core enseignant existant n'est pas rendu sécurisé par ce lecteur; publier uniquement un export Élève conforme aux politiques locales.
