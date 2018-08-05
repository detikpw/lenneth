#!/usr/bin/env python3
from toolz.curried import pipe
from pkg.title import show_title
from pkg.fetch import get_current_season_top_ten_anime
from pkg.inquiries import show_questions

"""
Module Anime
"""

__author__ = "Detik P. Warjaya"
__version__ = "0.1.0"


def main():
    show_title();
    pipe(
        None,
        get_current_season_top_ten_anime,
        show_questions
    )

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()