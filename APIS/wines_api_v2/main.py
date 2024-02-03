import os
import pickle
from flask import Flask, request, jsonify, make_response
import numpy as np

app = Flask(__name__)

# Get path
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, 'models', 'wine_model_complete.pkl')
model = pickle.load(open(model_path, 'rb'))

def validate_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

@app.route('/', methods=['GET'])
def predict_wine_quality():
    # Define parameters
    input_params = {
        'fixedacidity': None,
        'volatileacidity': None,
        'citricacid': None,
        'residualsugar': None,
        'chlorides': None,
        'freesulfurdioxide': None,
        'totalsulfurdioxide': None,
        'density': None,
        'ph': None,
        'sulphates': None,
        'alcohol': None,
    }

    # Iterates through key-value from input_params dictionary. 
    # Each iteration: if there is not value or cannot be float, the key keeps the default value (None)
    for param, default_value in input_params.items():
        input_params[param] = request.args.get(param, type=validate_float, default=default_value)

    # If case a value is None
    if None in input_params.values():
        return make_response(jsonify({'message': 'Parámetros de entrada inválidos'}), 400)

    # Creates a one dimension array, that is, what the model is expecting
    features = np.array(list(input_params.values()))

    # Reshape the array into a matrix with one row and n columns, where n is the number of features
    # From 1 dimension to 2 dimensions
    features = features.reshape(1, -1)

    # Prediction
    quality = int(model.predict(features)[0])

    return jsonify({'quality': quality})


@app.errorhandler(404)
def not_found(error):
    # Ruta no encontrada
    return make_response(jsonify({'message': 'Recurso no encontrado'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
