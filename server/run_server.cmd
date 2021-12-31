@ECHO OFF
CLS

SET FLASK_APP=main.py
SET FLASK_ENV=development
SET FLASK_DEBUG=1

flask run --port 5000