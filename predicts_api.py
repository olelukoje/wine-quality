import os
from flask import Flask, request, jsonify
import pickle

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
            json_data = request.get_json()
            if json_data is None:
                return jsonify("Expected json")
            else:
                data = [list(d.values()) for d in json_data]
        except ValueError:
            return jsonify("Please check the json format")

        return jsonify(rf_model.predict(data).tolist())


with open("models/" + MODEL_NAME, 'rb') as f:
    rf_model = pickle.load(f)
