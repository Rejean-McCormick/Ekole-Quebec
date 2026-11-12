#!/usr/bin/env python3
"""Point d'entrée partagé; le moteur Kristal 3.2.3 est conservé octet pour octet.
Les exports pack réintègrent outil et modèles pour rester autonomes.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import sys
import zipfile

SOURCE = Path(__file__).resolve().parent/'vendor/kristal-local/3.2.3/tools/kristal.py'
TEMPLATES = SOURCE.parent/'_templates'
MARKER = b'# ekole.shared-kristal/1'


def load():
    spec=importlib.util.spec_from_file_location('_ekole_kristal_3_2_3',SOURCE)
    if spec is None or spec.loader is None:raise SystemExit('Outil Kristal partagé introuvable')
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module


def pack_portable(args):
    """Même format ZIP déterministe; rétablit les dépendances du point d'entrée."""
    root=Path(args.path).resolve()
    if not root.is_dir():raise SystemExit('Dossier Kristal absent : '+str(root))
    output=Path(args.output).resolve() if args.output else root.with_suffix('.zip')
    output.parent.mkdir(parents=True,exist_ok=True)
    local=root/'tools/kristal.py'
    shared=local.is_file() and MARKER in local.read_bytes()[:200]
    files={}
    for p in sorted(root.rglob('*')):
        if not p.is_file() or p.resolve()==output:continue
        rel=p.relative_to(root)
        if '.git' in rel.parts or '__pycache__' in rel.parts or p.suffix=='.pyc':continue
        files[rel.as_posix()]=(p.read_bytes(),p.stat().st_mode)
    if shared:
        files['tools/kristal.py']=(SOURCE.read_bytes(),SOURCE.stat().st_mode)
        for p in sorted(TEMPLATES.rglob('*')):
            if p.is_file():files.setdefault('tools/_templates/'+p.relative_to(TEMPLATES).as_posix(),(p.read_bytes(),p.stat().st_mode))
    with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for rel,(data,mode) in sorted(files.items()):
            entry=zipfile.ZipInfo(root.name+'/'+rel,(2020,1,1,0,0,0))
            entry.compress_type=zipfile.ZIP_DEFLATED;entry.external_attr=(mode&0xffff)<<16
            archive.writestr(entry,data)
    print('Packed deterministic standalone archive:',output)


def run(argv=None):
    module=load()
    args=module.build_parser().parse_args(argv)
    if args.cmd=='pack':pack_portable(args)
    else:args.func(args)

if __name__=='__main__':run()
