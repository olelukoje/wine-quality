import os
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
MODEL_NAME = os.environ['MODEL_NAME']

properties_name = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides",
                   "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]


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
                # TODO: add a response error code
                return jsonify("Expected json")
            else:
                properties = [list(d.keys()) for d in json_data]
                for name in properties:
                    if name == properties_name:
                        continue
                    else:
                        return jsonify("Incorrect properties order")
                data = [list(d.values()) for d in json_data]
        except ValueError:
            return jsonify("Please check the json format")

        return jsonify(rf_model.predict(data).tolist())


with open("models/" + MODEL_NAME, 'rb') as f:
    rf_model = pickle.load(f)
