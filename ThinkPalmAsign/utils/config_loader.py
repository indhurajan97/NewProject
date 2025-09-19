import os
import yaml

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        config = yaml.safe_load(f)

    # Override RabbitMQ host if env variable is set
    rabbitmq_host = os.getenv("RABBITMQ_HOST")
    if rabbitmq_host:
        config["rabbitmq"]["host"] = rabbitmq_host

    return config
