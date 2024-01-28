from flask import Flask, render_template, request, jsonify, make_response
import pickle
import os

app = Flask(__name__)

# Get path from current dir
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, 'model', 'wine_model.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        # get parameters from form
        alcohol = request.form['alcohol']
        sulphates = request.form['sulphates']

        # validate parameters
        if alcohol and sulphates:
            try:
                alcohol = float(alcohol)
                sulphates = float(sulphates)

                # model prediction
                quality = int(model.predict([[alcohol, sulphates]])[0])
                return render_template('prediction.html', alcohol=alcohol, sulphates=sulphates, quality=quality)

            except ValueError:
                # Exception if parameters != digits
                return render_template('home.html', message='Los parámetros deben ser números')
        else:
            # Not enough parameters
            return render_template('home.html', message='Se requieren los parámetros alcohol y sulphates')

    return render_template('home.html')

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
def not_found(error):
    # Non existing route
    return make_response(jsonify({'message': 'Recurso no encontrado'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
