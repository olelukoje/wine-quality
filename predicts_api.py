from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=['GET'])
def start():
    if request.method == 'GET':
        return "Hello, World"


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            json_data = request.get_json()
            df = pd.DataFrame({0: json_data}).transpose()
            rf_model = pickle.load(open("./rf_model.pkl", 'rb'))
        except ValueError:
            return jsonify("Please check the json file.")

        return jsonify(rf_model.predict(df).tolist())


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)

