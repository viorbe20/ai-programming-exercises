from flask import Flask, request, jsonify, make_response
import pickle
import os

import numpy as np

app = Flask(__name__)

# Obtener la ruta desde el directorio actual
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, 'models', 'wine_model_complete.pkl')
model = pickle.load(open(model_path, 'rb'))


@app.route('/', methods=['GET'])
def predict_wine_quality():
    # Extraer los parámetros del request
    fixed_acidity = request.args.get("fixedacidity", type=float)
    volatile_acidity = request.args.get("volatileacidity", type=float)
    citric_acid = request.args.get("citricacid", type=float)
    residual_sugar = request.args.get("residualsugar", type=float)
    chlorides = request.args.get("chlorides", type=float)
    free_sulfur_dioxide = request.args.get("freesulfurdioxide", type=float)
    total_sulfur_dioxide = request.args.get("totalsulfurdioxide", type=float)
    density = request.args.get("density", type=float)
    ph = request.args.get("ph", type=float)
    sulphates = request.args.get("sulphates", type=float)
    alcohol = request.args.get("alcohol", type=float)

    # Crear un array unidimensional con los valores de las variables
    features = np.array([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, ph, sulphates, alcohol])

    # Convertir el array en una matriz de una fila y 11 columnas
    features = features.reshape(1, -1)

    # Hacer la predicción con el modelo
    quality = int(model.predict(features))

    # Devolver la predicción como respuesta
    return jsonify({'quality': quality})


@app.errorhandler(404)
def not_found(error):
    # Ruta no encontrada
    return make_response(jsonify({'message': 'Recurso no encontrado'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
