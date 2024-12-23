from flask import Flask, request, jsonify
import os

# Initialize the Flask application
app = Flask(__name__)

@app.route('/message', methods=['POST'])
def respond():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input. Please provide a 'text' field."}), 400

    user_text = data['text']
    return jsonify({"response": "Ok Bro"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
