#!/usr/bin/env python3

QUERY = '''
    query ($media_season: MediaSeason, $sort: [MediaSort], $season_year: Int) {
        Page (page: 1, perPage: 10) {
            media (season: $media_season, seasonYear: $season_year, sort: $sort ,type: ANIME) {
                id
                title {
                    romaji
                }
            }
        }
    }
'''