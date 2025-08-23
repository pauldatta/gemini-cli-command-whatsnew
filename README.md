# Gemini CLI Whatsnew Command

This project contains a custom `whatsnew` command for the Gemini CLI. It fetches and summarizes release notes for various Google Cloud products.

## Installation

To install the `whatsnew` command, run the following in your terminal:

```bash
mkdir -p ~/.gemini/commands && curl -sSL https://raw.githubusercontent.com/pauldatta/gemini-cli-command-whatsnew/main/.gemini/commands/whatsnew.toml -o ~/.gemini/commands/whatsnew.toml
```

## Usage

Once installed, you can use the command like this:

```bash
gemini whatsnew <product_name> <another_product_name>
```

For example, to get the latest updates for Cloud Run and GKE, you would run:

```bash
gemini whatsnew cloudrun gke
```

## Development

The project also includes an automated testing suite to validate the release note URLs.

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

### Running Tests

To run the URL validation tests, make sure your virtual environment is activated and then run the following command:

```bash
pytest tests/
```

To run the tests in parallel for faster execution, you can use the `pytest-xdist` plugin (which is included in `requirements.txt`):

```bash
pytest -n auto tests/
```
