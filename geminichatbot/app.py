from flask import Flask, render_template, request, jsonify
from utills import generate_response, Load_Model

# Load the model once
model = Load_Model("gemini-1.5-pro")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get("user_input")
    if not user_input:
        return jsonify({"error": "Empty input"}), 400
    
    # Generate response from the model
    response = generate_response(user_input, model=model)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
