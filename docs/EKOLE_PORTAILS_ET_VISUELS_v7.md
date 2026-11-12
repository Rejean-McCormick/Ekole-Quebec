# Architecture des trois expériences et couche visuelle

## Couches et données

```
Kristals v1.2 / graphe / catalogue (autorité pédagogique)
           |
  ┌────────┴────────┐
  |                 |
Ekole Core       Ekole Élève (aucun corrigé dans l'export)
organisation     activités, carte Avant/Après, visuels candidats
  |
Ekole Enseignant (serveur local sur 8766, jeton de session)
objectifs, 6 modules, remarques de maîtrise, prompts d'images
  |
   services séparés : SemantiK Architect (phrases), Konstellation Light (v10 public), Médiathèque, Moodle optionnel
```

La couche des visuels ne change pas les énoncés, les faits ou la correction des Kristals. Elle énonce des **intentions d'image** descriptives, identifiables, révisables, générables ultérieurement par un outil image. Les emplacements restent lisibles et compréhensibles sans images, grâce aux alternatives textuelles.

## Intention d'image (`ekole.visual-intent-registry/1.0`)

- `visual_id` : stable, aligné sur cours, accueil, année, matière ou outil.
- `placement` : emplacement exact et audience (`eleve`, `enseignant`).
- `kind` : illustration, décor, symbole ou diagramme.
- `prompt_image` : scène/objet précis, style cohérent, rapport d'image, absence de texte dans l'image et contraintes d'exactitude si utiles.
- `source_ref` : origine de la notion (pour les cours : Kristal et objectif).
- `alt_fr_CA` : alternative écrite; aucune dépendance à la couleur seule.
- `status : non_generee`, `asset_path_actuel : null`, `asset_path_future` : image à injecter une fois validée.
- `negative_constraints` : pas de texte, filigrane, visages réels, stéréotypes.
- `validation_required` : pédagogie, droits/provenance, accessibilité.

## Injection future des fichiers visuels

Créer ultérieurement un script de compilation prenant le registre et un manifeste approuvé des images générées (`visual_id -> file + licence + alt + révision`). Vérifier ratio, dimensions, droits, pertinence, exactitude des diagrams et empreintes SHA-256. Insérer le vrai fichier dans une compilation du site Élève et remplacer le texte de substitution sans changer les identifiants. Aucun injecteur d'images non validées n'est implémenté dans v7.

## Frontières sécurité

Ekole Core a des pages d'administration **non authentifiées** : pour gestion locale seulement. Ekole Enseignant est hors de la racine publique et accessible localement via une session générée au lancement. Un navigateur sur cette même machine avec le jeton peut l'ouvrir; ne pas l'exposer aux réseaux scolaires sans authentification dédiée.

Konstellation Light : URL de démonstration locale `127.0.0.1:4177`; brancher une véritable collection v10 uniquement quand les State Snapshots exacts et l'index public sont qualifiés et publiés. `DIRECTORY ≠ AUTHORITY`.
