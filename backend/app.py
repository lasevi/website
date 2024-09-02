from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

# Temporary test routes
users = {
    1: {'name': 'Mauri', 'age': 25},
    2: {'name': 'Liisa', 'age': 30},
    3: {'name': 'Annikki', 'age': 35}
}

@app.route('/test_users', methods=['GET'])
def test_users():
    return jsonify({'users': users}), 200

@app.route('/test_user/<id>', methods=['GET'])
def test_user(id):
    # Get single user
    id = int(id)
    if id in users:
        return jsonify(users[id]), 200
    else:
        return jsonify(f'User with ID {id} not found'), 404

@app.route('/teapot', methods=['GET'])
def teapot():
    return 'I am a teapot', 418

if __name__ == '__main__':
    app.run()
