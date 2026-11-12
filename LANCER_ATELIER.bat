@echo off
setlocal
REM Atelier Enseignant : l'edition locale doit etre activee volontairement.
echo [EKOLE] Arretez toute autre instance sur les ports 8765 / 8766.
echo [EKOLE] Le navigateur Enseignant sera ouvert avec une session privee.
call "%~dp0LANCER_EKOLE_QUEBEC.bat" --edition
