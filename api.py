from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://cmongo.dbmongo.svc.cluster.local:27017/')
db = client['mydatabase']
collection = db['users']

@app.route('/api/users', methods=['GET'])
def get_users():
    users = [user['name'] for user in collection.find({}, {'_id': 0, 'name': 1})]
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    if name:
        user = {'name': name}
        collection.insert_one(user)
        return 'Usuario creado exitosamente', 201
    else:
        return 'Error: Se requiere un nombre para crear un usuario', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

