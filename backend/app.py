from flask import Flask, jsonify, request
from db_config import get_db
from bson.json_util import dumps

app = Flask(__name__)
db = get_db()

@app.route('/api/students', methods=['GET'])
def get_students():
    students = list(db.quiz_scores.find({}, {'_id': 0}))
    return dumps(students)

@app.route('/api/add_score', methods=['POST'])
def add_score():
    data = request.get_json()
    db.quiz_scores.insert_one(data)
    return jsonify({'message': 'Score added successfully!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
