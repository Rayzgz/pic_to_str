import curses
from random import randrange, choice
from collections import defaultdict

"""
all user actions:
    up, down, left, right,restart, exit
"""


# finite state machine

# functions that input an action, return a state

def main(stdscr):
    
    def init():
        return 'Game'

    def game():
        if action == 'Win':
            return 'Win'
        if action == 'Game Over':
            return 'Game Over'
        if action == 'Exit':
            return 'Exit'
        if action == 'Restart':
            return 'Restart'
        return 'Game'

    def win():
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'

    def gameover():
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'


    state_actions = {
        'Init': init,
        'Win': lambda: not_game('Win')
        'Gameover':lambda: not_game('Gameover'),
        'Game':game
    }

    state = 'Init'

    while state != 'Exit':
        state = state_actions[state]()
