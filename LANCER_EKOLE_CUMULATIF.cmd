@echo off
setlocal
set "CONTENU=%~dp0"
if not defined EKOLE_MOTEUR set "EKOLE_MOTEUR=%CONTENU%..\ekole"
set "PY=python"
where py >nul 2>nul && set "PY=py -3"
%PY% "%CONTENU%outils\construire_ecole.py"
if errorlevel 1 exit /b 1
%PY% "%EKOLE_MOTEUR%\launcher.py" --contenu "%CONTENU%." --activites-locales "%CONTENU%dist\ecole-locale\catalogue.json" --edition --ouvrir %*
