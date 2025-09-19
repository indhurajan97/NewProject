
import pika
import time
import json
from loguru import logger
from utils.faker_utils import random_user

def publish_and_consume(rabbit_cfg, message, timeout=5):
    credentials = pika.PlainCredentials(rabbit_cfg['username'], rabbit_cfg['password'])
    parameters = pika.ConnectionParameters(host=rabbit_cfg['host'], port=rabbit_cfg['port'], credentials=credentials)
    conn = pika.BlockingConnection(parameters)
    channel = conn.channel()
    q = rabbit_cfg.get('queue', 'httpbin_test_queue')
    channel.queue_declare(queue=q, durable=False)

    # Publish
    channel.basic_publish(exchange='', routing_key=q, body=json.dumps(message))
    logger.info('Published message to RabbitMQ')

    # Try to consume one message (with timeout)
    method_frame, header_frame, body = channel.basic_get(q, auto_ack=True)
    start = time.time()
    while method_frame is None and (time.time() - start) < timeout:
        time.sleep(0.2)
        method_frame, header_frame, body = channel.basic_get(q, auto_ack=True)

    conn.close()
    if method_frame is None:
        raise AssertionError('No message consumed within timeout')
    return json.loads(body)

def test_rabbitmq_publish_consume(rabbitmq_config):
    payload = random_user()
    received = publish_and_consume(rabbitmq_config, payload)
    assert received == payload

