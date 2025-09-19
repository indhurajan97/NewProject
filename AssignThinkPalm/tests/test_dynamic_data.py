import requests
from utils.retry_decorator import retry
from utils.data_generator import random_user

@retry(max_attempts=3, delay=1)
def post_data(base_url, payload):
    return requests.post(f"{base_url}/post", json=payload)

def test_dynamic_user_post(config):
    user = random_user()
    resp = post_data(config["api"]["base_url"], user)
    assert resp.status_code == 200
    data = resp.json()
    assert data["json"]["email"] == user["email"]
