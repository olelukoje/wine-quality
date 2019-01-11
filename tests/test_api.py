import pytest
import json
from predicts_api import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    return client


def test_success(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype
    }
    data = [{"fixed acidity": 8.1,
             "volatile acidity": 0.27,
             "citric acid": 0.41,
             "residual sugar": 1.45,
             "chlorides": 0.033,
             "free sulfur dioxide": 11,
             "total sulfur dioxide": 63,
             "density": 0.9908,
             "pH": 2.99,
             "sulphates": 0.56,
             "alcohol": 12
             }]
    response = client.post('/predict', data=json.dumps(data), headers=headers)
    data = json.loads(response.data)

    assert response.content_type == mimetype
    assert response.status_code == 200
    assert type(data) == list
    assert len(data) == 1


def test_not_json_type(client):

    mimetype = 'text/plain'
    headers = {
        'Content-Type': mimetype
    }
    data = [{"fixed acidity": 8.1,
             "volatile acidity": 0.27,
             "citric acid": 0.41,
             "residual sugar": 1.45,
             "chlorides": 0.033,
             "free sulfur dioxide": 11,
             "total sulfur dioxide": 63,
             "density": 0.9908,
             "pH": 2.99,
             "sulphates": 0.56,
             "alcohol": 12
             }]
    response = client.post('/predict', data=json.dumps(data), headers=headers)

    assert response.content_type == "text/html"
    assert response.status_code == 400
    assert b'<p>Expected json</p>' in response.data


def test_incorrect_order(client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype
    }
    data = [{"fixed acidity": 8.1,
             "volatile acidity": 0.27,
             "citric acid": 0.41,
             "residual sugar": 1.45,
             "chlorides": 0.033,
             "free sulfur dioxide": 11,
             "total sulfur dioxide": 63,
             "density": 0.9908,
             "pH": 2.99,
             "sulphates": 0.56
             }]
    response = client.post('/predict', data=json.dumps(data), headers=headers)

    assert response.content_type == "text/html"
    assert response.status_code == 400
    assert b'<p>Incorrect properties order</p>' in response.data
