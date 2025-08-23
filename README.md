# Gemini CLI Whatsnew Command

This project contains a custom `whatsnew` command for the Gemini CLI. It fetches and summarizes release notes for various Google Cloud products.

The project also includes an automated testing suite to validate the release note URLs.

## Getting Started

### Prerequisites

- Python 3
- `venv` module

### Setup

1.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

To run the URL validation tests, make sure your virtual environment is activated and then run the following command:

```bash
pytest tests/
```

To run the tests in parallel for faster execution, you can use the `pytest-xdist` plugin (which is included in `requirements.txt`):

```bash
pytest -n auto tests/
```
