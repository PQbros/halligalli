import os

fileName = "main.py"

os.environ['FLASK_APP'] = fileName
os.system("flask run")
