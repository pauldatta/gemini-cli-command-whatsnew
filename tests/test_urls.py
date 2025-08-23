import re
import os
import pytest
import requests

# Get the absolute path to the project root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
MARKDOWN_FILE = os.path.join(ROOT_DIR, 'release_notes_whatsnew.md')

def extract_urls_from_markdown(file_path):
    """Extracts all URLs from a markdown file."""
    with open(file_path, 'r') as f:
        content = f.read()
    # Regex to find URLs in plain text
    urls = re.findall(r'https?://[^\s]+', content)
    return sorted(list(set(urls)))

@pytest.mark.parametrize("url", extract_urls_from_markdown(MARKDOWN_FILE))
def test_url_is_valid(url):
    """Tests if a given URL is valid."""
    try:
        response = requests.get(url, timeout=10, stream=True)
        assert response.ok, f"URL {url} returned status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"URL {url} failed to load: {e}")