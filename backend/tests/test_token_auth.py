import requests

domain = "http://localhost:8000/"
path_requiring_permission = "libraries/"
token_path = "token/"
login_credential = {
    "username": "park",
    "password": "1234",
}


def test_token_auth():
    assert requests.get(domain + path_requiring_permission).status_code == 401

    token = "Bearer " + requests.post(domain + token_path, data=login_credential).json()["access"]
    headers = {"Authorization": token}
    assert requests.get(domain + path_requiring_permission, headers=headers).status_code == 200
