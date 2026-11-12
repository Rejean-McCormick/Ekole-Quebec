"""Stage a Québec character overlay from reviewed Kolor Studio role exports."""
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse
import hashlib
import os
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(os.environ.get('EKOLE_MOTEUR', ROOT.parent / 'ekole')).resolve()))

from personnages import safe_file, validate
from kolor_roles import export_png, export_rows, verify_png


def prepare(manifest, target, selected):
    if target.exists() or target.is_symlink():
        raise ValueError('Choisir un nouveau dossier pour préparer cet overlay')
    rows = export_rows(manifest)
    source_root = ROOT / 'personnages'
    catalogue = validate(json.loads((source_root / 'catalogue.json').read_bytes()))
    roles = {asset['id']: asset for asset in catalogue['assets'] if asset['type'] == 'role'}
    wanted = selected or sorted(key for key in roles if rows.get(key, {}).get('statut') == 'pret')
    if not wanted:
        raise ValueError('Aucun rôle prêt dans le manifeste Kolor Studio')
    target.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix='kolor-', dir=target.parent) as temporary:
        stage = Path(temporary) / 'overlay'
        for role in dict.fromkeys(wanted):
            entry = rows.get(role, {})
            if role not in roles or entry.get('statut') != 'pret':
                raise ValueError(f'{role} : statut prêt et rôle Québec requis')
            raw = export_png(manifest, entry)
            verify_png(raw)
            asset = roles[role]
            current = safe_file(source_root, asset['fichier'])
            if current.exists() and current.read_bytes() != raw:
                raise ValueError(f'{role} : un média différent existe déjà dans Ekole Québec')
            output = stage / 'personnages' / asset['fichier']
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(raw)
            asset['statut'] = 'pret'
            asset['sha256'] = 'sha256:' + hashlib.sha256(raw).hexdigest()
        (stage / 'personnages/catalogue.json').write_text(
            json.dumps(catalogue, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        stage.rename(target)
    print(f'{len(set(wanted))} rôles dans {target}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    select = parser.add_mutually_exclusive_group(required=True)
    select.add_argument('--role', action='append', help='Identifiant de rôle, répétable')
    select.add_argument('--tous-prets', action='store_true')
    args = parser.parse_args()
    prepare(args.manifest.absolute(), args.out.absolute(), args.role)


if __name__ == '__main__':
    main()
