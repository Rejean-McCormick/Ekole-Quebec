# Rapport de livraison et limites — qc-pri-fls-010

**Livraison :** `qc-pri-fls-010_livraison_v1.2.zip` (delta de 14 fichiers sous `kristals/qc-pri-fls-010/`).  
**Origine :** frame v1.2 incluse dans l’archive source. **Statut :** production rédactionnelle complète, validation technique automatisée à vérifier avec le script de contrôle de la livraison, **revue humaine requise**.

## Travaux exécutés pendant la rédaction

- Lecture de trois normes v1.2, du graphe, du `PARCOURS.md` initial, du contrat JSON initial, de `ALIGNEMENT.md` et de `BRIEF_REDACTION.md`.
- Conservation des identités canoniques : `obj-1`, `crit-1`, `qc-pri-fls-010-ev-01`, objectif et preuve immuables, préalable `qc-pri-fls-009`, aucun ordre conseillé ou renforcement.
- Rédaction de 12 sections, six fichiers de contenu, banque de 10 items fixes avec solutions, grille à deux preuves dans des contextes distincts et plan d’administration.
- Références externes OQLF consultées pour accords / ponctuation. Tous les scénarios et corrigés sont originaux.

## Contrôles techniques

Les contrôles *effectivement exécutés* et leur résultat sont inscrits dans la section suivante à l’issue de la fabrication; un outil ne garantit pas la validation pédagogique.

**Précontrôle automatisé local** : 65 assertions exécutées avec succès (source originale, identité et graphe, YAML et contrat, JSON, numérotation, schémas, deux corrigés contrôlés par substitutions textuelles, nombre de tâches, droits documentés et chemins). Les assertions ne prouvent pas la correction pédagogique de toutes les variantes.

**Contrôles d’emballage** : intégrité CRC, premier chemin, liste exacte des 14 fichiers, chemins sûrs, identité des octets, JSON parsables et fichiers non vides — **7 assertions d’emballage exécutées avec succès**. Test final après mise à jour du rapport effectué également.



## Revues et limites non résolues

1. **Relecture humaine FLS** : niveaux de vocabulaire, clarté, corrections orthographiques / grammaticales, acceptation des reformulations équivalentes; tester le temps et le seuil proposé.
2. **Essai apprenant et accessibilité du LMS** : aucun test avec enfants, aucun audit réel de compatibilité technologies d’assistance; les adaptations sont décrites mais non observées en situation.
3. **Évaluations** : les dix items portent `validation_status=a_revoir`; aucune certification, qualification officielle, publication ou alignement PFEQ détaillé.
4. **Sources/droits** : scénarios rédigés originaux, liens externes crédités; les conditions de republication des pages externes n’ont pas été utilisées pour incorporer leur contenu; décisions de publication non prises.
5. **Frontière canonique** : aucune modification des registres, gouvernance, données `canon/`, `state/`, `runtime/`, d’autres Kristals ou de `AGENTS.md`.

## Propositions de structure (non appliquées)

- Ajouter ultérieurement, après décision de gouvernance, un champ optionnel de trace par preuve (modalité d’accès / aide corrective / justification observée); **aucun schéma central modifié**.
- Prévoir séparation stricte des supports élève et corrigés au moment de la projection LMS, sans déplacer les fichiers dans ce delta.
- Ajouter un corpus de preuves alternatives approuvées pour les reprises, distinct de q-009 et q-010; ne pas faire fabriquer de nouvelles données librement par IA.

## Fusion

Extraire ce ZIP **depuis la racine du workspace** `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`. Le chemin `kristals/qc-pri-fls-010/` se superpose à la frame et n’introduit aucun dossier englobant. Vérifier les conflits avant fusion; le ZIP ne contient que les 14 chemins du manifeste.
