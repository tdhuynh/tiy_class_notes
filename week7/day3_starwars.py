import requests
import time

url = "http://swapi.co/api/people/1/"

json_result = requests.get(url).json()

films = json_result.get("films", "") # the empty string is a default in case it can't find 'films' in the keys

for film in films:
    film_result = requests.get(film).json()
    split_crawl = film_result["opening_crawl"].split("\r\n")
    for line in split_crawl:
        print(line)
        time.sleep(.05)
