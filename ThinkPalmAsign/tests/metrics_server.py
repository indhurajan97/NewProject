
from prometheus_client import start_http_server
from prometheus_client import Gauge
import threading

# Example gauge; tests update these metrics
TEST_DURATION_GAUGE = Gauge('test_duration_seconds', 'Duration for tests (s)', ['test'])

def start_metrics_server(port=8000):
    thread = threading.Thread(target=start_http_server, args=(port,), daemon=True)
    thread.start()
    return thread

