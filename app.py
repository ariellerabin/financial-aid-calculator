from flask import Flask, request, jsonify
from flask_cors import CORS
from calculator import financial_aid_calculator

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

calculator = financial_aid_calculator()

@app.route('/', methods=['POST'])
def calculate():
    data = request.json
    membership = int(data['membership'])
    family_size = int(data['family_size'])
    income = int(data['income'])
    result = calculator.perform_calculation(membership, family_size, income)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
