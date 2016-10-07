from bs4 import BeautifulSoup
import csv
import pprint
import re
import requests
import time


def get_book_data(element):
    """given a BeautifulSoup Tag representing a book,
    extract the book's details and return a dict"""

    title = element.find('div', 'thumbheader').a.text
    by_author = element.find('div', 'AuthorName').text
    authors = [x.strip()
               for x in re.sub("by ", '', by_author, flags=re.IGNORECASE).split(',')
               ]
    # price = element.find('span', 'price').text.strip()

    return {
        'title': title,
        # 'price': price,
        'authors': authors,
    }


def main():
    NUM_PAGES = 31
    books = []

    base_url = 'http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page='

    for page_num in range(1, NUM_PAGES + 1):
        print("souping page", page_num, ",", len(books), " found so far")
        html = requests.get(base_url + str(page_num)).text
        soup = BeautifulSoup(html, 'html5lib')
        books.extend([get_book_data(group) for group in soup('td', 'thumbtext')])

        time.sleep(30)

    with open('books.txt', 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["Title", "Authors"])
        for book in books:
            writer.writerow([book['title'], ', '.join(book['authors'])])

    pprint.pprint(books)


if __name__ == '__main__':
    main()
