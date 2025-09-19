import requests
from utils.retry_decorator import retry

@retry(max_attempts=3, delay=1)
def send_get(base_url):
    return requests.get(f"{base_url}/get", params={"test": "value"})

def test_get_request(config):
    resp = send_get(config["api"]["base_url"])
    assert resp.status_code == 200
    data = resp.json()
    assert data["args"]["test"] == "value"
