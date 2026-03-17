from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to my Flask API!"

# Route to get student details
@app.route('/student', methods=['GET'])
def get_student():
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    })

# Route to create/update a student (example)
@app.route('/student', methods=['POST'])
def create_student():
    data = request.get_json()
    # For simplicity, just return the received data
    return jsonify({
        "message": "Student data received successfully!",
        "student": data
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
