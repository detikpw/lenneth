#!/usr/bin/env python3
import requests
import pprint
import json

"""
Module Docstring
"""

__author__ = "Detik P. Warjaya"
__version__ = "0.1.0"


def main():
    """ Main entry point of the app """
    print("hello world")
    # Here we define our query as a multi-line string
    query = '''
    query ($media_season: MediaSeason) {
        Page (page: 1, perPage: 10) {
            media (season: $media_season, seasonYear: 2018, sort: SCORE_DESC ,type: ANIME) {
                id
                title {
                    romaji
                }
            }
        }
    }
    '''

    # Define our query variables and values that will be used in the query request
    variables = {
        'media_season': 'SUMMER'
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.loads(response.content))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()