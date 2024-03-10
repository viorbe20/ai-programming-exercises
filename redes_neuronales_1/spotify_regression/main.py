import numpy as np
from keras.models import Sequential, model_from_json
from keras.layers import Dense
from flask import Flask, render_template, request, jsonify, make_response
import pickle
import os
import pandas as pd

app = Flask(__name__)

# Obtener ruta desde el directorio actual
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, 'models', 'spotify.pkl')

# Obtener el modelo y el preprocesador desde el pickle
try:
    model, preprocessor = pickle.load(open(model_path, 'rb'))
except Exception as e:
    app.logger.error(f"Error al cargar el modelo: {e}")



@app.route('/', methods=['GET'])
def home():

    return ('API de predicción de calidad de vino', 200)

@app.route('/prediction', methods=['GET'])
def prediction():
    
    # ejemplo de petición
    #http://localhost:5000/prediction?track_id=3kgKVcBpBGuSeaEC0AZGlb&track_name=Old+Town+Road+-+Diplo+Remix&track_artist=Lil+Nas+X&track_album_id=66FxETmTBazRMZNbvGtGQl&track_album_name=Old+Town+Road+(Diplo+Remix)&track_album_release_date=2019-04-29&playlist_name=Pop+Remix&playlist_id=37i9dQZF1DXcZDD7cfEKhW&playlist_genre=pop&playlist_subgenre=dance+pop&danceability=0.766&energy=0.771&key=6&loudness=-9.108&mode=1&speechiness=0.0576&acousticness=0.00407&instrumentalness=0.000004&liveness=0.113&valence=0.297&tempo=140.036&duration_ms=204027
    
    # Obtener parámetros
    track_id = request.args.get('track_id')
    track_name = request.args.get('track_name')
    track_artist = request.args.get('track_artist')
    track_album_id = request.args.get('track_album_id')
    track_album_name = request.args.get('track_album_name')
    track_album_release_date = request.args.get('track_album_release_date')
    playlist_name = request.args.get('playlist_name')
    playlist_id = request.args.get('playlist_id')
    playlist_genre = request.args.get('playlist_genre')
    playlist_subgenre = request.args.get('playlist_subgenre')
    danceability = request.args.get('danceability')
    energy = request.args.get('energy')
    key = float(request.args.get('key'))
    loudness = float(request.args.get('loudness'))
    mode = float(request.args.get('mode'))
    speechiness = float(request.args.get('speechiness'))
    acousticness = float(request.args.get('acousticness'))
    instrumentalness = float(request.args.get('instrumentalness'))
    liveness = float(request.args.get('liveness'))
    valence = float(request.args.get('valence'))
    tempo = float(request.args.get('tempo'))
    duration_ms = float(request.args.get('duration_ms'))
    
    
    data = {
        'track_id': track_id,
        'track_name': track_name,
        'track_artist': track_artist,
        'track_album_id': track_album_id,
        'track_album_name': track_album_name,
        'track_album_release_date': track_album_release_date,
        'playlist_name': playlist_name,
        'playlist_id': playlist_id,
        'playlist_genre': playlist_genre,
        'playlist_subgenre': playlist_subgenre,
        'danceability': danceability,
        'energy': energy,
        'key': key,
        'loudness': loudness,
        'mode': mode,
        'speechiness': speechiness,
        'acousticness': acousticness,
        'instrumentalness': instrumentalness,
        'liveness': liveness,
        'valence': valence,
        'tempo': tempo,
        'duration_ms': duration_ms,
        
    }
    
    data_df = pd.DataFrame([data])

    # Preprocessing
    X = preprocessor.transform(data_df) 

    # Prediction
    prediction = model.predict(X)

    return make_response(jsonify({'prediction': prediction.tolist()}), 200)
        


@app.errorhandler(404)
def not_found(error):
    # Ruta no existente
    return make_response(jsonify({'message': 'Recurso no encontrado'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
