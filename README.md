# Data Quality Validation Framework

## Overview

This project provides a simple and reusable framework to validate data from APIs using Python and pytest.

It demonstrates how to ensure **data quality, correctness, and structure validation** in real-world data pipelines.

---

## Features

- API data extraction
- Data validation (schema + quality checks)
- Pytest-based testing
- Parameterized test execution
- Logging (file + console)
- HTML test reports
- GitHub Actions CI integration

---

## Project Structure

```
data-quality-framework/
│
├── src/
│   ├── api_client.py        # API call logic
│   ├── validations.py       # Data validation rules
│   └── logger.py            # Logging setup
│
├── tests/
│   └── test_api.py          # Test cases
│
├── reports/                 # HTML reports (ignored)
├── logs/                    # Logs (ignored)
│
├── requirements.txt
├── README.md
└── .github/workflows/test.yml
```

---

## How It Works

1. Fetch data from API
2. Apply validation rules:
   - User count validation
   - Required field validation
   - Email format validation

3. Execute tests using pytest
4. Generate HTML report

---

## Run Tests

```bash
pytest -v
```

Generate HTML report:

```bash
pytest --html=reports/report.html
```

---

## Validation Scenarios

- Ensure API returns data
- Validate required fields exist
- Validate email format correctness

---

## Tech Stack

- Python
- Pytest
- Requests
- Logging
- GitHub Actions

---

## CI/CD

GitHub Actions automatically:

- Installs dependencies
- Runs tests
- Generates reports

---
