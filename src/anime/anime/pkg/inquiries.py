import pprint
from toolz import curry
from toolz.curried import map, filter, pipe
from PyInquirer import prompt, style_from_dict, Token, Separator

_get_title = lambda anime: anime['title']['romaji']

def _get_anime_by_title(anime_list):
    return lambda selected_title: list(
        filter(lambda anime: anime['title']['romaji'] == selected_title)(anime_list)
    )

def show_questions(anime_list):
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
            'choices': map(_get_title)(anime_list)
        },
    ]
    answers = prompt(questions, style=style)
    pp = pprint.PrettyPrinter(indent=1)
    pipe(
        answers,
        lambda answers: answers['anime_title'],
        _get_anime_by_title(anime_list),
        pp.pprint
    )

