from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
    input_text = request.json.get('text', '')
    # Here, you can put your AI model logic; for now, we just echo
    response = {"classified_text": input_text}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
