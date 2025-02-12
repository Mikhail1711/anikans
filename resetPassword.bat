@echo off
cd /d "%~dp0"

call ..\venv\Scripts\activate

echo from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.set_password('admin'); user.save() | python manage.py shell

echo Пароль администратора 'admin' успешно изменен на 'admin'.
pause
