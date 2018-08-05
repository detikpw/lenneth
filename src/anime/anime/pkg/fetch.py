import requests
import datetime
from .queries import ANIME

def get_current_season_top_ten_anime(self):
    now = datetime.datetime.now()
    variables = {
        # TODO Remove this hard code
        'media_season': 'SUMMER',
        'season_year': now.year,
        'sort': 'SCORE_DESC'
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': ANIME, 'variables': variables})
    return response.json()['data']['Page']['media']

