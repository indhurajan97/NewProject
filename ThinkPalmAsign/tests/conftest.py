
import pytest
import yaml
import os
from utils.faker_utils import fake
from tests.metrics_server import start_metrics_server
from loguru import logger
from dotenv import load_dotenv
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from utils.config_loader import load_config


CONFIG = load_config()
load_dotenv()

CONFIG_PATH = os.getenv('CONFIG_PATH', 'config.yaml')

with open(CONFIG_PATH) as f:
    CONFIG = yaml.safe_load(f)

@pytest.fixture(scope='session', autouse=True)
def metrics_server():
    port = CONFIG.get('metrics', {}).get('port', 8000)
    logger.info(f"Starting metrics server on port {port}")
    start_metrics_server(port=port)
    yield

@pytest.fixture()
def httpbin_base_url():
    return CONFIG['httpbin']['base_url']

@pytest.fixture()
def faker():
    return fake

@pytest.fixture()
def rabbitmq_config():
    return CONFIG['rabbitmq']

