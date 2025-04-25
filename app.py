from flask import Flask, request, jsonify
import brain
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Chatbot API is running!"

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
    app.run(host='0.0.0.0', port=3000)

