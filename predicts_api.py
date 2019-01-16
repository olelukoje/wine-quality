import os
from flask import Flask, request, jsonify
import pickle

from werkzeug.exceptions import BadRequest

app = Flask(__name__)
MODEL_NAME = os.environ.get('MODEL_NAME', default="rf_model.pkl")

property_names = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides",
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
                """Check all properties availability"""
                correct_order_data = []
                for d in json_data:
                    values = []
                    for name in property_names:
                        try:
                            values.append(d[name])
                        except KeyError:
                            raise BadRequest("Missing property(-ies)")
                    correct_order_data.append(values)
        except ValueError:
            raise BadRequest("Invalid json format")

        return jsonify(rf_model.predict(correct_order_data).tolist())


with open("models/" + MODEL_NAME, 'rb') as f:
    rf_model = pickle.load(f)


if __name__ == "__main__":
    app.run(port=4001, host="0.0.0.0")
