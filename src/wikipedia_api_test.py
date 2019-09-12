#!/usr/bin/python3

"""
    search.py

    MediaWiki API Demos
    Demo of `Search` module: Search for a text or title

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

TOPIC = "Izone"
SEARCHPAGE = "Izone Category: K-pop music groups"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srsearch": SEARCHPAGE
}

R = S.get(url=URL, params=PARAMS)

DATA = R.json()
print(DATA)

if DATA['query']['search'][0]['title'] == TOPIC:
    print("Your search page '" + SEARCHPAGE + "' exists on English Wikipedia")