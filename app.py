from flask import Flask, request, jsonify
import model

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    prediction = model.make_prediction(data)
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
