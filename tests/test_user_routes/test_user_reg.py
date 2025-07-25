

from tests.configtest import USER_NAME, USER_EMAIL, USER_PASSWORD


def test_create_user(client):
    data ={
        "name": USER_NAME,
        "email address": USER_EMAIL,
        "password": USER_PASSWORD
    }
    response = client.post ('/users', json=data)
    assert response.status_code == 201
    
    assert "password" not in response.json()
    