from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
import brain
import os

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')  # Serve the HTML

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")
        if not user_input:
            return jsonify({"error": "No message provided"}), 400
        response = brain.get_response(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
