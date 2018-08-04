#!/usr/bin/env python3

QUERY = '''
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