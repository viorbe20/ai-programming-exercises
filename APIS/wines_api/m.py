# Importar Flask y Flask-Restful
import os
from flask import Flask, request
from flask_restful import Resource, Api
import pickle
import os


# Crear la aplicación Flask y la API Restful
app = Flask(__name__)
api = Api(app)

model = pickle.load(open('C:/Users/vober/Documents/curso-especializacion-bd-ia/PIA/pia-github/apis/wines_api/model/wine_model.pkl', 'rb')) # Importar el archivo

# Definir la clase del recurso
class WineQuality(Resource):
    def get(self):
        # Obtener los parámetros de la petición
        alcohol = request.args.get('alcohol')
        sulphates = request.args.get('sulphates')

        # Validar los parámetros
        if alcohol and sulphates:
            try:
                # Convertir los parámetros a números
                alcohol = float(alcohol)
                sulphates = float(sulphates)

                # Predecir la calidad del vino usando el modelo
                quality = model.predict([[alcohol, sulphates]])[0]

                # Devolver la respuesta en formato JSON
                return {'quality': quality}, 200
            except ValueError:
                # Devolver un mensaje de error si los parámetros no son números
                return {'message': 'Los parámetros deben ser números'}, 400
        else:
            # Devolver un mensaje de error si faltan parámetros
            return {'message': 'Se requieren los parámetros alcohol y sulphates'}, 400

# Añadir el recurso a la API
api.add_resource(WineQuality, '/winequality', 'winequality')

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
