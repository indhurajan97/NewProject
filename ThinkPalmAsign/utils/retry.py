
import time
import functools
from loguru import logger
from prometheus_client import Counter, Histogram

# Prometheus metrics
RETRY_COUNTER = Counter(
    'test_retries_total',
    'Total retry attempts across tests',
    ['function']
)
RETRY_HIST = Histogram(
    'test_retry_duration_seconds',
    'Duration of retry attempts (s)',
    ['function']
)


def retry(max_attempts=3, backoff_seconds=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            name = func.__name__
            attempt = 0
            last_exc = None
            start = time.time()

            while attempt < max_attempts:
                try:
                    attempt += 1
                    logger.debug(f"Attempt {attempt}/{max_attempts} for {name}")
                    result = func(*args, **kwargs)

                    duration = time.time() - start
                    RETRY_HIST.labels(function=name).observe(duration)

                    if attempt > 1:
                        # count only retries (attempts after first)
                        RETRY_COUNTER.labels(function=name).inc(attempt - 1)

                    return result

                except Exception as e:
                    last_exc = e
                    logger.warning(f"Attempt {attempt} for {name} failed: {e}")

                    if attempt < max_attempts:
                        sleep = backoff_seconds * attempt
                        logger.info(f"Backing off for {sleep}s before next attempt")
                        time.sleep(sleep)
                    else:
                        logger.error(f"All {max_attempts} attempts failed for {name}")
                        raise

            raise last_exc

        return wrapper
    return decorator

