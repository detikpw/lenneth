#!/usr/bin/env python3
import requests
import pprint
import json
from pkg.queries import QUERY
"""
Module Anime
"""

__author__ = "Detik P. Warjaya"
__version__ = "0.1.0"


def main():
    # Here we define our query as a multi-line string

    # Define our query variables and values that will be used in the query request
    variables = {
        'media_season': 'SUMMER'
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': QUERY, 'variables': variables})
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(response.json())

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()