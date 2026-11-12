#!/usr/bin/env sh
set -eu
DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
MOTEUR="$DIR/../ekole/launcher.py"
if [ ! -f "$MOTEUR" ]; then echo "Moteur manquant: $MOTEUR" >&2; exit 1; fi
exec python3 "$MOTEUR" --contenu "$DIR" --port 8765 --port-editeur 8766 --ouvrir "$@"
