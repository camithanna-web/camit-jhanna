from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to my Flask API!",
        "status": "API is running"
    })

# Student information
@app.route('/student', methods=['GET'])
def get_student():
    student = {
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    }
    return jsonify(student)

# Add student using POST
@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()

    new_student = {
        "name": data.get("name"),
        "grade": data.get("grade"),
        "section": data.get("section")
    }

    return jsonify({
        "message": "Student added successfully",
        "student": new_student
    })

if __name__ == "__main__":
    app.run(debug=True)
