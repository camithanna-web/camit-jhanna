app.py
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
return "Welcome to my Flask API!"

@app.route('/student')
def get_student():
return jsonify({
"name": "Your Name",
"grade": 10,
"section": "Zechariah"
})

Procfile
web: gunicorn app:app --bind 0.0.0.0:$PORT
requirements.txt
Flask==3.1.2
gunicorn==23.0.0
runtime.txt
python-3.12.0
