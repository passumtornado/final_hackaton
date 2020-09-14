from flask import Flask, request, jsonify
from joblib import load
import numpy as np
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return 'This is a home'

@app.route('/api/predict/hourly', methods=['POST'])
def hourly_predict():
    model = load('final_model.joblib')
    day = request.json['day']
    hour = request.json['hour']
    month = request.json['month']
    pressure = request.json['pressure']
    temperature = request.json['temperature']
    wind_speed = request.json['wind_speed']

    data= np.array([[month,day, hour, wind_speed,pressure,temperature]])

    return jsonify({'prediction': str(model.predict(data))})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)