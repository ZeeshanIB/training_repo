from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)
class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(80), unique=True, nullable=False)
  content = db.Column(db.String(120), unique=True, nullable=False)

  def __init__(self, title, content):
    self.title = title
    self.content = content
db.create_all()
@app.route('/')
def starting():
  
  return("connecting")

@app.route('/items/<id>', methods=['GET'])
def get_item(id):
  item = Item.query.get(id)
  del item.__dict__['_sa_instance_state']
  return jsonify(item.__dict__)


@app.route('/items', methods=['POST'])
def create_item():
  body = request.get_json()
  db.session.add(Item(body['title'], body['content']))
  db.session.commit()
  return "item created"



if __name__ == '__main__':
    app.run(debug=True)