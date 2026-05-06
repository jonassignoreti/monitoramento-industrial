@echo off 

echo Iniciando API Flask... 
start cmd /k "title [API] Flask && venv\Scripts\activate && cd api && python app.py" 

echo Iniciando Coletor... 
start cmd /k "title [PLC] Coletor && venv\Scripts\activate && cd collector && python plc_reader.py" 

echo Iniciando Django... 
start cmd /k "title [WEB] Django && venv\Scripts\activate && cd dashboard && python manage.py runserver 192.168.0.157:8000" 

echo Tudo iniciado. 
pause