import requests
import json


# "fixed acidity";"volatile acidity";"citric acid";"residual sugar";"chlorides";"free sulfur dioxide";
# "total sulfur dioxide";"density";"pH";"sulphates";"alcohol";"quality"
# 7;0.27;0.36;20.7;0.045;45;170;1.001;3;0.45;8.8;6

PORT = 4001
BASE_URL = "http://127.0.0.1:" + str(PORT)

with open("./wine_inputs.json", "r") as f:
        json_data = json.load(f)
print(json_data)

response = requests.post("{}/predict".format(BASE_URL), json=json_data)

print('model response: {0}'.format(response.json()))
