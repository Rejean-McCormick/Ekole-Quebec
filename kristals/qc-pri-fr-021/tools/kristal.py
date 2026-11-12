#!/usr/bin/env python3
# ekole.shared-kristal/1 — point d’entrée conservé, outil partagé épinglé 3.2.3.
from pathlib import Path
import runpy

if __name__ == '__main__':
    for parent in Path(__file__).resolve().parents:
        dispatcher = parent / 'outils' / 'kristal_local.py'
        if (parent / 'pack.json').is_file() and dispatcher.is_file():
            runpy.run_path(str(dispatcher))['run']()
            break
    else:
        raise SystemExit('Outil partagé absent. Pour exporter un Kristal autonome, utiliser la commande pack depuis le dépôt complet.')
