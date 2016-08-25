from bs4 import BeautifulSoup
import csv
import json
import requests


def main():
    url = 'http://yahoo.com'
    req = requests.get(url)
    content = req.text
    soup = BeautifulSoup(content, "html.parser")

    headlines = []
    for headline in soup.find_all("h3"):
        raw_headline = headline.get_text()
        headline = raw_headline.strip()
        if len(headline) < 10:
            continue
        headlines.append(headline)

    print(json.dumps(headlines))

    with open("headlines-output.csv", 'w') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        writer.writerow(['headline'])
        for headline in headlines:
            writer.writerow([headline])

if __name__ == '__main__':
    main()
