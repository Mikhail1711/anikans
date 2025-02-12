@echo off
cd /d "%~dp0"

call ..\venv\Scripts\activate

start python manage.py runserver

start http://127.0.0.1:8000


(
echo [.ShellClassInfo]
echo IconResource=${%~dp0\static\favicon\favicon.ico},0
) > "%~f0..::%~nx0.lnk"
