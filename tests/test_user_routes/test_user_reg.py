
from  test.configtest import USER_NAME, USER_EMAIL, USER_PASSWORD

def test_create_user(client):
    data ={
        "username": USERNAME,
        "email address": USER_EMAIL,
        "password": USER_PASSWORD,
    
    }