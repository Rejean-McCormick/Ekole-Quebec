#!/usr/bin/env sh
set -eu
root="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
python3 "$root/outils/construire_ecole.py"
exec python3 "${EKOLE_MOTEUR:-$root/../ekole}/launcher.py" --contenu "$root" \
    --activites-locales "$root/dist/ecole-locale/catalogue.json" --edition --ouvrir "$@"
