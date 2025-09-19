
# HTTPBin API Automation Framework

## Quick start (local, using Docker Compose)

1. Build & run all services (httpbin, RabbitMQ, Prometheus, Grafana, test runner):

   docker compose up --build --exit-code-from metrics_exporter --abort-on-container-exit

2. Useful UIs:
   - Grafana: http://localhost:3000 (admin/admin)
   - Prometheus: http://localhost:9090
   - RabbitMQ management: http://localhost:15672 (guest/guest)
   - httpbin: http://localhost:8080

3. After tests finish, Allure results will be in ./allure-results

## Local dev loop (run tests from host)

1. Start infrastructure:
   docker compose up -d httpbin rabbitmq prometheus grafana

2. Wait for services:
   ./scripts/wait-for-service.sh localhost:8080
   ./scripts/wait-for-service.sh localhost:5672

3. Update config.yaml to point to host addresses:
   # For local host runs:
   sed -i 's|https://httpbin.org|http://localhost:8080|g' config.yaml
   sed -i 's|host: "rabbitmq"|host: "localhost"|g' config.yaml

4. Create venv & install:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

5. Run tests:
   pytest -q --maxfail=1 --alluredir=allure-results


