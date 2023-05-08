import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urljoin

def extract_parameters(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params

def fetch_urls(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the URL: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    urls = [urljoin(url, link.get("href")) for link in soup.find_all("a")]
    return urls

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ParamHunter.py [URL]")
        sys.exit(1)

    url = sys.argv[1]
    all_urls = fetch_urls(url)

    for u in all_urls:
        parameters = extract_parameters(u)
        if parameters:
            print(f"URL: {u}")
            print("Parameters found:")
            for key, value in parameters.items():
                print(f"{key}: {value[0]}")
            print()
