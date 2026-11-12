# Validation du delta — `qc-pri-ilss-007`

**Périmètre :** production locale de 14 fichiers dans `kristals/qc-pri-ilss-007/` : deux remplacements `authoring/`, 12 ajouts. **État :** rédaction complète, revue pédagogique humaine nécessaire; aucun statut de publication, d'homologation ou de certification.

## Contrôles techniques exécutés

**589 assertions préarchivage ont effectivement réussi** dans le script `verify_ilss007.py` (contrôles YAML/JSON, champs canoniques, graphe, 12 sections, exercices, dix items, réponses factuelles, deux preuves, droits et accessibilité). Aucun échec dans les contrôles de préarchivage finaux.

- **3 JSON analysés** : contrat pédagogique, banque d'items, manifeste; frontmatter YAML valide, inchangé par rapport à la source.
- **Fusion simulée depuis l'archive maîtresse complète** : 2 remplacements `authoring/`, 12 ajouts, **34 fichiers initiaux protégés** préservés byte pour byte et contrôlés par SHA-256; aucun fichier hors du Kristal n'a été empaqueté.
- **Validation d'archive** : contrôle des 14 entrées sous `kristals/qc-pri-ilss-007/`, absence d'évasion/chemin absolu, lecture byte pour byte, cohérence du manifeste et vérification CRC finale, exécutés dans ce même script.
- **Non testés** : essais auprès d'élèves, jugement humain d'accessibilité, fidélité entre correcteurs, réussite pédagogique réelle et qualification institutionnelle.

## Qualité des corrigés et limites

- Chaque item fixe propose une consigne, un contexte entièrement spécifié, un exemple de production recevable, plusieurs dimensions de correction et une rétroaction. Les corrigés dépendent des faits verrouillés dans les stimuli; aucune génération IA libre ni réponse secrète n'est utilisée comme autorité.
- Les fautes mineures non gênantes ne sont pas éliminatoires; les erreurs qui changent l'engagement, le lieu, la date ou le nombre rendent un message partiellement ou totalement inutilisable selon la grille.
- La concordance formelle et les faits écrits sont vérifiables techniquement, **sans démontrer** que les seuils conviennent à tous les élèves. Aucune étude de fidélité interévaluateurs n'a été effectuée.

## Revue humaine obligatoire

1. Spécialiste en intégration linguistique, scolaire et sociale : vérifier les messages naturels, les niveaux de langue et les risques de confusion langue/compétence disciplinaire.
2. Spécialiste en accessibilité : confirmer que clavier, scribe mécanique, dictée vocale révisée et temps adapté préservent les décisions d'écriture de l'élève; trancher les équivalences individuelles sans les présumer.
3. Évaluateurs : valider rubriques, fiabilité du jugement sur les deux contextes, contenu culturellement neutre et durée de passation.
4. Droits et confidentialité : confirmer la procédure locale de traitement des traces; aucune adresse réelle, identité réelle ni envoi de message requis dans les scénarios.

## Limites et propositions sans changer les fichiers centraux

- Aucun enfant n'a été observé; les activités n'ont pas été expérimentées en classe; pas d'estimation statistique de validité, de fiabilité ou de progression.
- L'efficacité des adaptations doit être contrôlée dans le contexte réel, notamment pour les technologies de composition, sans confondre scribe mécanique et aide rédactionnelle.
- **Proposition de schéma, non appliquée :** créer plus tard des champs normalisés décrivant séparément outil d'accès, auteur de la formulation et type d'aide, pour rendre la cotation d'autonomie auditable.
- **Proposition méthodologique, non appliquée :** étalonner la distinction entre « information secondaire absente » et « message inutilisable » sur copies anonymisées et corrigées par plusieurs personnes.
- Aucun fichier `registry/`, `governance/`, `docs/`, `canon/`, `state/`, `runtime/`, `kristal.workspace.json`, `AGENTS.md` ou autre Kristal n'est intégré. Aucun alignement PFEQ détaillé n'est revendiqué.
