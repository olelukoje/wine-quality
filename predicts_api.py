import os
from flask import Flask, request, jsonify
import pickle

from werkzeug.exceptions import BadRequest

app = Flask(__name__)
try:
    MODEL_NAME = os.environ['MODEL_NAME']
except KeyError:
    MODEL_NAME = "rf_model.pkl"

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
                raise BadRequest("Expected json")
            else:
                """Check input properties order"""
                properties = [list(d.keys()) for d in json_data]
                for name in properties:
                    if name == properties_name:
                        continue
                    else:
                        raise BadRequest("Incorrect properties order")
                data = [list(d.values()) for d in json_data]
        except ValueError:
            raise BadRequest("Invalid json format")

        return jsonify(rf_model.predict(data).tolist())


with open("models/" + MODEL_NAME, 'rb') as f:
    rf_model = pickle.load(f)


if __name__ == "__main__":
    app.run(port=4001, host="0.0.0.0")
