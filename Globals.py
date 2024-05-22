import random
import subprocess

# Globals
player_id = 1
card_vals = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_suit = ['S','H','C','D'] # spades, hearts, clubs, diamonds
start_cash = 500
min_bet = 25
num_decks = 8
num_players = 8
dealer_stands = 17

# ANSI Escape Sequences (Colors)
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
LIGHTGREY = '\033[37m'
DARKGREY = '\033[90m'
LIGHTRED = '\033[91m'
LIGHTGREEN = '\033[92m'
YELLOW = '\033[93m'
LIGHTBLUE = '\033[94m'
PINK = '\033[95m'
LIGHTCYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[01m'

# Helper methods
is_ace = lambda x: True if x in ['SA','HA','CA','DA'] else False
face_value = lambda x: 10 if x[1] in ['J','Q','K'] else x
can_split = lambda x,y: True if x[1] == y[1] else False
can_double = lambda x,y: True if x + y in [9,10,11] else False

def make_deck():
    deck = []
    global card_suit,card_vals
    for suit in card_suit:
        for card in card_vals:
            deck.append(suit+card)
    return deck

def shuffle_deck(deck):
    return random.shuffle(deck)

def clear_screen():
    subprocess.call(['clear'])
