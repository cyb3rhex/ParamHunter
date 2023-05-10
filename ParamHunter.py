import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urljoin


def print_header():
    header = r"""
 .___                                __  __               .                
 /   \   ___  .___    ___  , _ , _   |   |  ,   . , __   _/_     ___  .___ 
 |,_-'  /   ` /   \  /   ` |' `|' `. |___|  |   | |'  `.  |    .'   ` /   \
 |     |    | |   ' |    | |   |   | |   |  |   | |    |  |    |----' |   '
 /     `.__/| /     `.__/| /   '   / /   /  `._/| /    |  \__/ `.___, /    
                                                                           

Developer: LSDeep
"""
    print(header)


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


def main():
    print_header()
    print("Ex: https://www.website.com")
    url = input("Please enter the URL to scan with (http/https): ")
    
    all_urls = fetch_urls(url)

    for u in all_urls:
        parameters = extract_parameters(u)
        if parameters:
            print(f"URL: {u}")
            print("Parameters found:")
            for key, value in parameters.items():
                print(f"{key}: {value[0]}")
            print()


if __name__ == "__main__":
    main()
