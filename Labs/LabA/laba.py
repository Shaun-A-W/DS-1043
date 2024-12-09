""" Lab A: Web Scraping

Crawls the website http://books.toscrape.com and creates a spreadsheet of books.
"""
import time
import random
import requests
import json
import csv
from urllib.parse import urljoin
from bs4 import BeautifulSoup as Soup

# User Agent from Chrome Browser on Win 10/11
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

DEFAULT_SLEEP = 3.0 # These may need tuning
SIGMA = 1.0

DOMAIN = 'http://books.toscrape.com' # Ideally, these would be
STATE_FILENAME = 'state.json'        # read in from a configuration
OUTPUT_FILENAME = 'books.csv'        # or commandline, but this is fine


def get(url: str) -> requests.Response:
    """Waits a random amount of time, then send a GET request"""
    time.sleep(random.gauss(DEFAULT_SLEEP, SIGMA))
    return requests.get(url, headers=HEADERS)


# [TODO] Save links left to visit and the data extracted to a JSON file
def save_state(filename: str, links: list[str], data: dict[str, dict]) -> None:
    with open(filename, 'w') as state:
        try:
            to_dump = [links, data]
            json.dump(to_dump, state)
        except FileNotFoundError:
            pass
    

# [TODO] Load links left to visit and collected data from a JSON file
def load_state(filename: str) -> tuple[list[str], dict[str, dict]]:
    with open(filename, 'r') as state:
        load = json.load(state)
        return load['links'], load['data']


# [TODO] Write all data to a CSV file
def write_spreadsheet(filename: str, data: dict[str, dict]) -> None:
    with open (filename, 'w') as sheet:
        writer = csv.DictWriter(sheet, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)


if __name__ == '__main__':
    # [TODO] Load the state file or start fresh if it cannot be read
    to_visit: list = [urljoin(DOMAIN, '/index.html')]
    data: dict[str, dict] = {}
    # Main Loop
    while len(to_visit) > 0:
        try:
            current = to_visit.pop(0)
            if current in data:
                continue
            resp = get(current)
            soup = Soup(resp.text, 'html.parser')
            a_tags = soup.find_all('a')
            for tag in a_tags:
                link = tag.get('href')
                url = urljoin(DOMAIN, link)
                if url not in data and url not in to_visit:
                    to_visit.append(url)
                else: continue

            try:
                # title,
                # category or categories,
                # UPC,
                # price and tax data,
                # availability, and number of reviews.

                temp_dat = {}
                bread_list = []

                for crumb in (breadcrumbs := soup.find_all('ul', class_='breadcrumb')):
                    _title = crumb.find('li', class_='active')
                    _title = _title.text.strip()
                    temp_dat['Title'] = _title

                    for li in crumb.find_all('li'):
                        li = li.text.strip()
                        bread_list.append(li)
                    _category = bread_list[(len(bread_list) - 2)]
                    temp_dat['Category'] = _category

                for row in soup.find_all('tr'):
                    _head = row.find('th')
                    _head = _head.text.strip()
                    _dat = row.find('td')
                    _dat = _dat.text.strip()
                    _dat = _dat.replace('Â', '')
                    temp_dat[_head] = _dat
                data[current] = temp_dat

            except:
                pass

            # [TODO] Process files from to_visit
            #        This requires:
            #        - Popping a link from the list
            #        - Checking to see if it has already been processed
            #        - Downloading the file the link points to
            #          - Link should not be removed from to_visit if it
            #            cannot be downloaded
            #        - Add the current file to data, using the url as the
            #          key, and a dictionary containing book data if present
            #        - Extract links from the HTML
            #          - Use urljoin(full_url_of_current_doc, link_ref)
            #            to create the full url for a link
            #          - Check to see if this full url is already in data
            #          - If not, append to to_visit

        except KeyboardInterrupt:
            save_state(STATE_FILENAME, to_visit, data)
            is_finished = False
            break
    else:
        is_finished = True
    if is_finished:
        write_spreadsheet(OUTPUT_FILENAME, data)