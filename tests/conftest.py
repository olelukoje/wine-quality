import pytest
from predicts_api import app


@pytest.fixture(scope='module')
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    return client
