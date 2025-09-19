
import requests
import time
from utils.retry import retry
from utils.faker_utils import random_user
from loguru import logger
from prometheus_client import Summary

TEST_SUMMARY = Summary('test_duration_summary_seconds', 'Time spent in tests', ['test'])

@retry(max_attempts=3, backoff_seconds=1)
def call_get(url):
    r = requests.get(url)
    r.raise_for_status()
    return r

def test_get_root(httpbin_base_url):
    start = time.time()
    r = call_get(f"{httpbin_base_url}/get")
    assert r.status_code == 200
    data = r.json()
    assert 'url' in data
    duration = time.time() - start
    TEST_SUMMARY.labels(test='test_get_root').observe(duration)

def test_post_inspect_request(httpbin_base_url, faker):
    payload = random_user()
    r = requests.post(f"{httpbin_base_url}/post", json=payload)
    assert r.status_code == 200
    resp = r.json()
    assert resp['json'] == payload

def test_dynamic_delay(httpbin_base_url):
    r = requests.get(f"{httpbin_base_url}/delay/1", timeout=5)
    assert r.status_code == 200

