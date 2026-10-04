from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('get_clima'))

@app.route('/sensores/clima', methods=['GET'])
def get_clima():
    return jsonify({
        "status": "operacional",
        "temperatura": 25.3,
        "umidade": 65
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)