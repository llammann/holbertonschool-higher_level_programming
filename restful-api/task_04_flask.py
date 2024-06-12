from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    elif username in users:
        return jsonify({"error": "Username already exists"}), 409
    else:
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201

def test_add_user_duplicate_username():
    response = app.test_client().post('/add_user', json={"username": "john", "name": "John", "age": 30, "city": "New York"})
    assert response.status_code == 409

if __name__ == '__main__':
    app.run(debug=True)

