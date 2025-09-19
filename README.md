# httpbin Pytest Framework

A full-fledged Python test framework targeting [httpbin.org](https://httpbin.org/) that demonstrates:

* ✅ Configuration via `.yaml` and `.env`
* ✅ Custom retry decorator with detailed logging
* ✅ Test data generation using Faker and utilities
* ✅ Pytest-based test suite covering response formats, request inspection, and dynamic data
* ✅ HTML reports generated automatically (`pytest-html`)
* ✅ CI workflow to publish reports as artifacts in GitHub Actions



## ⚙️ Setup

1. **Clone repo & create virtual environment:**

```bash
git clone <your-repo-url>
cd httpbin_pytest_framework
python -m venv .venv
source .venv/bin/activate   # Linux/MacOS
.\.venv\Scripts\activate    # Windows
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configuration (optional):**

Copy and adjust configs if needed:

```bash
cp .env.example .env
cp config.yaml.example config.yaml
```

Values in `.env` override values in `config.yaml`.

4. **Run tests:**

```bash
pytest
```

5. **View HTML report:**

Open `reports/report.html` in a browser.

---

## 🧪 What is Tested

* **Response formats:**

  * `GET /get`
  * `GET /json`
  * `GET /delay/{n}`
* **Request inspection:**

  * `POST /post`
  * `PUT /put`
* **Dynamic data:**

  * Faker-generated payloads for POST/PUT
* **Retries:**

  * Custom decorator with exponential backoff & logging



