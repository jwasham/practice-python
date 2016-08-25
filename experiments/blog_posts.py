from bs4 import BeautifulSoup
import requests


def main():
    url = 'https://googleyasheck.com'

    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        html = req.text

        soup = BeautifulSoup(html, 'html.parser')
        for page in soup.find_all('article', 'post'):
            href = page.h2.a['href']
            title = page.h2.text.strip()
            date = page.footer.time.text.strip()

            print('{title} ({date}): {domain}{url}'.format(title=title, url=href, date=date, domain=url))


if __name__ == '__main__':
    main()
