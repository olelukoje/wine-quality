import os
from flask import Flask, request, jsonify
import pickle
import pandas as pd
import json

app = Flask(__name__)
MODEL_NAME = os.environ['MODEL_NAME']


@app.route("/", methods=['GET'])
def start():
    if request.method == 'GET':
        return "Hello, World"


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            json_path = request.get_data()
            with open(json_path, "r") as f:
                json_data = json.load(f)
            df = pd.DataFrame({0: json_data}).transpose()
        except ValueError:
            return jsonify("Please check the json file.")

        return jsonify(rf_model.predict(df).tolist())


with open("models/" + MODEL_NAME, 'rb') as f:
    rf_model = pickle.load(f)



