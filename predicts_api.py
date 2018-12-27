from flask import Flask, request, jsonify
import pickle
import pandas as pd
import json

app = Flask(__name__)


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


if __name__ == '__main__':
    with open("./rf_model.pkl", 'rb') as f:
        rf_model = pickle.load(f)
    app.run(host='0.0.0.0', port=80)

