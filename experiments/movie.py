import json
import requests


def do_search(search_term):
    req = requests.get('http://www.omdbapi.com/', params={'s': search_term, 'type': 'movie'})
    if req.status_code == requests.codes.ok:
        movies = json.loads(req.text)  # not using req.json in order to sort
        if 'Search' in movies:
            lines = sorted(movies['Search'], key=lambda m: m['Year'], reverse=True)

            for movie in lines:
                print("{} - {}".format(movie['Year'], movie['Title']))
        else:
            print('Nothing found')


def main():
    keep_going = True
    while keep_going:
        search = input('Search for a movie [enter to stop]: ')
        if search.strip():
            do_search(search)
        else:
            keep_going = False


if __name__ == '__main__':
    main()
