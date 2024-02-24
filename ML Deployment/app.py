from flask import Flask, jsonify
from ml_cancer import load_model, prepare_new_data
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    new_data = {
        'radius_mean': 15.0,
        'perimeter_mean': 100.0,
        'area_mean': 700.0,
        'symmetry_mean': 0.2,
        'compactness_mean': 0.3,
        'concave_points_mean': 0.1
    }
    prepared_new_data = prepare_new_data(new_data)
    loaded_model = load_model('models/model.pkl')
    prediction = loaded_model.predict(prepared_new_data)

    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)