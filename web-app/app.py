from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    experience = db.Column(db.Integer)

    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

@app.route('/', methods=['POST'])
def create_user():
    name = request.json['name']
    experience = request.json['experience']
    user = User(name=name, experience=experience)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'name': user.name, 'experience': user.experience}), 201

@app.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append({'id': user.id, 'name': user.name, 'experience': user.experience})
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
