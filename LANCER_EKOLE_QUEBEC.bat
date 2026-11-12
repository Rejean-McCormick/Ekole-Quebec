@echo off
setlocal
set "CONTENU=%~dp0"
set "MOTEUR=%CONTENU%..\ekole\launcher.py"
if not exist "%MOTEUR%" (
  echo [ERREUR] Moteur Ekole absent : "%MOTEUR%"
  echo Placez ekole au meme niveau que ce repertoire.
  pause
  exit /b 1
)
echo [EKOLE] Ecole Quebec : portail http://127.0.0.1:8765/
where py >nul 2>nul
if not errorlevel 1 (
  py -3 "%MOTEUR%" --contenu "%CONTENU%." --port 8765 --port-editeur 8766 --ouvrir %*
) else (
  python "%MOTEUR%" --contenu "%CONTENU%." --port 8765 --port-editeur 8766 --ouvrir %*
)
if errorlevel 1 (
  echo [ERREUR] Impossible de demarrer. Python 3.10 ou plus recent est requis.
  pause
)
