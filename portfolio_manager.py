from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/portfolio', methods=['GET'])
def portfolio():
    sample_data = {
        "assets": [
            {"symbol": "AAPL", "quantity": 10, "price": 150.75},
            {"symbol": "GOOGL", "quantity": 5, "price": 2800.25}
        ]
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8004)
