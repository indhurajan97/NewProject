import os
import yaml
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def load_config():
    config_path = os.path.join(BASE_DIR, "config", "config.yaml")
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    # load .env variables
    load_dotenv(os.path.join(BASE_DIR, "config", ".env"))
    config["api"]["api_key"] = os.getenv("API_KEY")

    return config
