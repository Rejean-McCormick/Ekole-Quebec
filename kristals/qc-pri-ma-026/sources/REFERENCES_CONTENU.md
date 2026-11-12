# Sources, traçabilité, production originale — `qc-pri-ma-026`

## A. Sources internes effectivement consultées (vérifiées dans l'archive source)

Les fichiers ci-dessous ont été **lus depuis** `initbundle(1).zip` → `Frames_202_Kristals_Primaire_Qc_v1.2_Enrichis/`; « vérifié » signifie présence et lecture effective dans cette archive, **non** une validation externe ou une homologation.

1. `governance/Norme_Pedagogique_Autonome_v1.2/CONTRAT_PEDAGOGIQUE_V1.2.md` — cadre autonome, deux manifestations d'autonomie, absence d'obligation PFEQ.
2. `governance/Norme_Pedagogique_Autonome_v1.2/GENERATEUR_ET_EXAMENS.md` — paramètres minimaux des familles et contrôles indépendants des solutions.
3. `governance/Norme_Pedagogique_Autonome_v1.2/CHARTE_CONVERSION_QC.md` — discipline appelée **Mathématique**, sans attribution d'année/cycle officielle au Kristal.
4. `registry/GRAPHE_PEDAGOGIQUE_202.json` — `qc-pri-ma-026` : aucune sortie `requires`, `recommends_before`, `reinforces`; une arête entrante `reinforces` **non bloquante**. Aucun contenu du Kristal voisin n'a été copié.
5. `kristals/qc-pri-ma-026/authoring/PARCOURS.md`, `CONTRAT_PEDAGOGIQUE.json`, `ALIGNEMENT.md`, `BRIEF_REDACTION.md` — identité, objectif, critère, famille, forme YAML/JSON et périmètre natifs v1.2.
6. `governance/Norme_Pedagogique_Autonome_v1.2/REFERENCES_EVIDENCE.md` — références de méthode référencées par le workspace (IES/WWC, EEF, CAST). Les **pages externes elles-mêmes n'ont pas été vérifiées ni consultées** pour cette livraison; les avantages invoqués y figurent comme principes de design du workspace, non comme preuves d'efficacité du module.

## B. Faits mathématiques et raisonnements dérivés

- Une heure de durée = 60 min, une minute = 60 secondes; 24 h uniformes = 1440 min dans les problèmes fictifs sans ajustement légal de l'heure.
- Même date : `durée = (60×h_fin + m_fin) − (60×h_début + m_début)`; dates différentes : ajouter `1440×écart de jours` déterminé par le calendrier grégorien (dates ISO).
- Vérification inverse : `début + durée = fin`; vérification de l'horaire : `marge = prochain début/fermeture − fin`, positive ou nulle selon l'énoncé.
- Calendrier grégorien : année bissextile si divisible par 4, sauf siècles non divisibles par 400; février 2024 = 29 jours; février 2025 = 28 jours. Ces règles sont déterministes; des tests calendaires locaux ont été exécutés avec les bibliothèques Python `datetime` et un calcul indépendant par date ordinale.
- **Choix de modélisation explicite, pas fait sur tous les horaires réels :** on exclut heure d'été/hiver, fuseaux horaires et seconde intercalaire. Un jour peut avoir une durée civile réelle différente lors des transitions légales; le module n'enseigne pas ces cas.

## C. Textes et scénarios originaux

Les explications, exemples, contre-exemples, diagnostics, séances, exercices, horaires fictifs, cas de transfert, grilles, données de banques, templates de variables et rétroactions ont été rédigés **pour cette livraison**. Aucun texte, photo, illustration, donnée utilisateur, horaire d'entreprise réel, œuvre protégée ou extrait de site externe n'a été reproduit. Pas de revendication de droits sur les textes de gouvernance du workspace; ces textes ne sont **pas inclus** dans le ZIP.

## D. Droits et limites de vérification

Le ZIP ne contient que des fichiers de texte/JSON originaux dans le Kristal cible, sans média tiers ni police ou image. Aucun registre de licences externe ni vérification juridique formelle n'a été effectuée. Les références externes citées dans le workspace restent des **pistes** à consulter si une publication demande un audit des preuves. Les calculs ont été testés par code, mais les stratégies pédagogiques, la compréhension des élèves et la langue finale requièrent une revue humaine et des essais de passation.
