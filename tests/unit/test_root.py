
def test_get_success(client):
    response = client.get('/')
    data = str(response.data)

    assert response.content_type == 'text/html; charset=utf-8'
    assert response.status_code == 200
    assert "Hello, World" in data
