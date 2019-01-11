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
                raise InvalidRequestData("Expected json")
            else:
                properties = [list(d.keys()) for d in json_data]
                for name in properties:
                    if name == properties_name:
                        continue
                    else:
                        raise InvalidRequestData("Incorrect properties order")
                data = [list(d.values()) for d in json_data]
        except ValueError:
            raise InvalidRequestData("Invalid json format")

        return jsonify(rf_model.predict(data).tolist())


class InvalidRequestData(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidRequestData)
def handle_invalid_request_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


with open("models/" + MODEL_NAME, 'rb') as f:
    rf_model = pickle.load(f)
