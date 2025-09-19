import requests
from utils.retry_decorator import retry

@retry(max_attempts=3, delay=1)
def fetch_json(base_url):
    return requests.get(f"{base_url}/json")

def test_json_response(config):
    resp = fetch_json(config["api"]["base_url"])
    assert resp.status_code == 200
    assert "slideshow" in resp.json()
