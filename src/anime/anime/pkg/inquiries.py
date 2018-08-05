import pprint
from PyInquirer import prompt, style_from_dict, Token, Separator

def show_questions(anime_titles):
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

