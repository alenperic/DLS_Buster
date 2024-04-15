import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
from tqdm import tqdm

def fetch_dls_sites():
    url = 'https://raw.githubusercontent.com/joshhighet/ransomwatch/main/docs/INDEX.md'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    df = pd.read_html(str(soup))[0]
    return df[df['status'] == '🟢']

def select_dls_site(dls_sites):
    for idx, row in enumerate(dls_sites.itertuples(), 1):
        print(f"{idx}. {row.title} - {row.location}")
    choice = input("Select DLS site by number or enter a custom onion URL: ")
    if choice.isdigit() and 1 <= int(choice) <= len(dls_sites):
        return dls_sites.iloc[int(choice) - 1]
    return choice

def fetch_files_from_dls(dls_url):
    # Assuming TOR configuration with requests
    print("Fetching files list...")
    response = requests.get(dls_url, proxies={'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'})
    # Process response to extract files list
    return []

def download_file(file_url, output_path):
    response = requests.get(file_url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(output_path, 'wb') as f, tqdm(desc=file_url, total=total_size, unit='iB', unit_scale=True, unit_divisor=1024) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = f.write(data)
            bar.update(size)

def main():
    dls_sites = fetch_dls_sites()
    selected_dls = select_dls_site(dls_sites)
    files = fetch_files_from_dls(selected_dls['location'])
    for file in files:
        download_file(file['url'], os.path.join('downloads', file['name']))

if __name__ == '__main__':
    main()
