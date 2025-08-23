import re
import pytest
import requests

def extract_urls_from_markdown(file_path):
    """Extracts all URLs from a markdown file."""
    with open(file_path, 'r') as f:
        content = f.read()
    # Regex to find URLs in markdown format
    urls = re.findall(r'\[.*?\]\(`(.*?)`\)', content)
    # Regex to find URLs in plain text
    urls.extend(re.findall(r'https?://[^\s`]+', content))
    return sorted(list(set(urls)))

@pytest.mark.parametrize("url", extract_urls_from_markdown('../release_notes_whatsnew.md'))
def test_url_is_valid(url):
    """Tests if a given URL is valid."""
    try:
        response = requests.get(url, timeout=10, stream=True)
        assert response.ok, f"URL {url} returned status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"URL {url} failed to load: {e}")
