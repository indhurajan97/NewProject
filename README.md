 ⚙️ Setup

1. **Clone repo & create virtual environment:**

```bash
git clone <your-repo-url>
cd AssignThinkPalm
python -m venv .venv
.\.venv\Scripts\activate    #
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



