Сайт создан на фреймворке Django (ибо мне так комфортнее и понятнее). 
Для запуска сайта (что логично) нужно в venv установить django с помощью команды
```
pip install django
```
Для запуска сайта нужно прописать команду: 
```
python manage.py runserver
```
(или python3 manage.py runserver)

Основая страница не прописана, поэтому перейдите на http://127.0.0.1:8000/index/

Для изменения статуса в терминале нужно в PowerShell ввести команду:
```
iwr -UseBasicParsing http://127.0.0.1:8000/on
```
или
```
iwr -UseBasicParsing http://127.0.0.1:8000/off
```
