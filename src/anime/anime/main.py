#!/usr/bin/env python3
import requests
import pprint
import json
import datetime
from pkg.queries import ANIME
"""
Module Anime
"""

__author__ = "Detik P. Warjaya"
__version__ = "0.1.0"


def main():
    from pyfiglet import Figlet
    f = Figlet(font='slant')
    print(f.renderText('ANIME-CLI'))
    now = datetime.datetime.now()
    variables = {
        'media_season': 'SUMMER',
        'season_year': now.year,
        'sort': 'SCORE_DESC'
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': ANIME, 'variables': variables})
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(response.json()['data']['Page']['media'])

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()