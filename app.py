from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://calculator-app-dun-three.vercel.app"}})  # Enable CORS for all routes

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    result = num1 + num2
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
