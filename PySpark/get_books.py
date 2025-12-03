import re
import requests

from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def get_links(n: int | list[int] = -1) -> tuple[ list[str], list[str] ]:
    """Gets the urls for books in the Gutenberg project with numbers `n`.

    The books are in txt format under the section frequently downloaded in:
        https://www.gutenberg.org/browse/scores/top.

    The numbers `n` must correspond to those on this list (starting with one).

    Parameters
    ----------
    n : int | list[int], optional
        An integer or list of integers with the desired book numbers. Choose -1
        (default) if all books are desired.

    Returns
    -------
    links : list[str]
        Links to the txt files of the books.
    titles : list[str]
        Book titles.
    """
    assert n == -1 or min(n) > 0, ( "n can only take values greater than zero "
                                    "or -1 if all links are desired" )
    # Get the html of the top books in Gutenberg project
    url = "https://www.gutenberg.org/browse/scores/top"
    try:
        response = requests.get(url)

        # Parse contents with BeautifulSoup
        parser = BeautifulSoup(response.text, 'html.parser')

        # Get links of books
        ordered_list = parser.find('ol')  # get first ordered list
        list_items = ordered_list.find_all('li')  # list items inside
        if(n != -1):
            list_filtered = [list_items[i-1] for i in list(n)]
        else:
            list_filtered = list_items

        prefix = "https://www.gutenberg.org"
        suffix = ".txt.utf-8"
        links, titles = [], []
        for li in list_filtered:
            links.append(prefix + li.find("a").get("href") + suffix)
            # replace whitespaces by underscores
            title = re.sub( r'\s+', '_', li.get_text())
            # remove numbers and parenthesis at end of filename
            title = re.sub(r'_\(\d+\)$', '', title)
            title += r'.txt'  # add file extension
            titles.append(title)
        return links, titles

    except requests.exceptions.RequestException as e:
        print("wrong url for Gutenberg project")

def download_file(url, name):
    response = requests.get(url, stream=True)
    with open(name, mode='wb') as file:
        for chunk in response.iter_content(chunk_size=10 * 1024):  #10kb chunks
            file.write(chunk)
    print(f"Downloaded file: {name}")

def store_files(links, names):
    with ThreadPoolExecutor() as executor:
        executor.map(download_file, links, names)

def store_files_slow(links, names):
    for url, name in zip(links, names):
        download_file(url, name)

def main( n = -1 ):
    links, titles = get_links(n)
    store_files(links, titles)
    print("Done")

n = range(1, 41)
main( n )
