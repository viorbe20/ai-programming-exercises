'''
Uso del framework Flask para crear una API web,
la cual predice la calidad de un vino 
utilizando un modelo de clasificación de machine learning 
cargado desde un archivo pickle.

author: Virginia Ordoño Bernier
date: January 2024
'''
from flask import Flask, request, jsonify, make_response
import pickle
import os

app = Flask(__name__)

# Get path from current dir
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, 'model', 'wine_model.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/', methods=['GET'])
def home():
    return "PREDICCIÓN DE LA CALIDAD DE UN VINO"

@app.route('/winequality', methods=['GET'])
def wine_quality():
    
    # get parameters
    alcohol = request.args.get('alcohol')
    sulphates = request.args.get('sulphates')

    # validate parameters
    if alcohol and sulphates:
        try:
            alcohol = float(alcohol)
            sulphates = float(sulphates)

            # model prediction
            quality = int(model.predict([[alcohol, sulphates]])[0])
            return jsonify({'quality': quality}), 200
        
        except ValueError:
            # Exception if parameters != digits
            return jsonify({'message': 'Los parámetros deben ser números'}), 400
    else:
        # Not enough parameters
        return jsonify({'message': 'Se requieren los parámetros alcohol y sulphates'}), 400

@app.errorhandler(404)
def not_found():
    # Non existing route
    return make_response(jsonify({'message': 'Recurso no encontrado'}), 404)

if __name__ == '__main__':
    app.run(debug=True)