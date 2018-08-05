#!/usr/bin/env python3
import requests
import pprint
import json
import datetime
from PyInquirer import prompt, style_from_dict, Token, Separator
from toolz.curried import map
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

    get_title = lambda anime: anime['title']['romaji']
    anime_titles = map(get_title)(response.json()['data']['Page']['media'])

    style = style_from_dict({
        Token.Separator: '#6C6C6C',
        Token.QuestionMark: '#FF9D00 bold',
        #Token.Selected: '',  # default
        Token.Selected: '#5F819D',
        Token.Pointer: '#FF9D00 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#5F819D bold',
        Token.Question: '',
    })
    questions = [
        {
            'type': 'list',
            'name': 'anime_title',
            # TODO remove this hard code
            'message': 'This is top ten anime in summer 2018, which anime that you want to see detail?',
            'choices': anime_titles
        },
    ]

    answers = prompt(questions, style=style)
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(answers)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()