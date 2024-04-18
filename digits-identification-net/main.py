import numpy as np
from flask import Flask, render_template, request, jsonify, make_response
import pickle
import os
import pandas as pd
import cv2

app = Flask(__name__)

# Obtener ruta desde el directorio actual
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, 'model', 'digits-mnist.pkl')

# Obtener el modelo 
try:
    model = pickle.load(open(model_path, 'rb'))
except Exception as e:
    app.logger.error(f"Error al cargar el modelo: {e}")

# Ruta para guardar imágenes
UPLOAD_FOLDER = os.path.join(script_dir, 'static', 'img')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No se ha seleccionado ningún archivo"

    file = request.files['file']
    if file.filename == '':
        return "No se ha seleccionado ningún archivo"

    # Guardar la imagen en la carpeta UPLOAD_FOLDER
    filename = 'number-pic.' + file.filename.rsplit('.', 1)[1]  # Conserva la extensión del archivo original
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename) 
    file.save(filepath)

    # Cargar la imagen con OpenCV
    # cv2.imdecode decodifica la imagen en un array de numpy
    # np.fromstring convierte el contenido del archivo en un string
    # np.uint8 es el tipo de dato de los elementos del array
    # cv2.IMREAD_COLOR indica que la imagen se cargará en color 
    #img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
    img = cv2.imread(filepath, cv2.IMREAD_COLOR)

    # Escalar la imagen a 28x28 píxeles
    img_resized = cv2.resize(img, (28, 28))

    # Convertir la imagen a escala de grises
    img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

    # Normalizar los valores de píxeles
    img_normalized = img_gray / 255.0

    # Ajustar la forma de la imagen para que coincida con la entrada del modelo
    img_reshaped = img_normalized.reshape(1, 28, 28)

    # Realizar la predicción con el modelo
    prediction = model.predict(img_reshaped)
    predicted_class = np.argmax(prediction)

    # Devolver la predicción como un string
    numbers_dict = {0:'cero', 1:'uno', 2:'dos', 3:'tres', 4:'cuatro', 5:'cinco', 6:'seis', 7:'siete', 8:'ocho', 9:'nueve'}
        
    prediction_str = numbers_dict[predicted_class]

    return render_template('prediction.html', prediction=prediction_str)

@app.errorhandler(404)
def not_found(error):
    # Ruta no existente
    return make_response(jsonify({'message': 'Recurso no encontrado'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
