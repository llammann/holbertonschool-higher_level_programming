from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for users
users = {}

# Welcome message for the root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to return all usernames
@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

# Endpoint to check API status
@app.route('/status')
def get_status():
    return "OK"

# Endpoint to get user details by username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    elif username in users:
        return jsonify({"error": "Username already exists"}), 400
    else:
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201

if __name__ == '__main__':
    app.run(debug=True)

