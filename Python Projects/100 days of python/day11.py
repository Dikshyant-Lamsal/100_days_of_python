import random
from os import system

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_deck=[]
comp_deck=[]
user_score=0
comp_score=0


def deal_card():
    return random.choice(cards)

def calculate_score(deck):
    if len(deck)==2:
        if sum(deck)==21:
            return 0
    if 11 in deck:
        if sum(deck)>21:
            deck.remove(11)
            deck.append(1)
    score=sum(deck)
    return score

def compare(deck1, deck2):

    score1 = calculate_score(deck1)
    score2 = calculate_score(deck2)

    print("USER's cards:", deck1)
    print("USER's score:", score1)
    print("COMP's cards:", deck2)
    print("COMP's score:", score2)

    if score1 == score2:
        print("DRAW!")
    elif score1 == 0 or score2 > 21 or score1==21:
        print("USER WINS!")
    elif score2 == 0 or score1 > 21 or score2==21:
        print("COMP WINS")
    elif score1 > score2:
        print("USER WINS")
    else:
        print("COMP WINS")

start_game=True
choice_start=input("Do you want to play a game of Blackjack? Type \'y\' or \'n\' ").lower()
if choice_start== 'n':
    start_game=False

while start_game:
    user_deck=[]
    comp_deck=[]
    user_score=0
    comp_score=0
    system("cls")
    user_deck.append(deal_card())
    user_deck.append(deal_card())
    comp_deck.append(deal_card())
    comp_deck.append(deal_card())
    play=True

    while play:
        print(logo)
        print("USER's cards:", user_deck)
        print("USER's score:", calculate_score(user_deck))
        print("COMP's 1st card:", comp_deck[0])

        if calculate_score(user_deck)>21 or calculate_score(comp_deck)>21 or calculate_score(user_deck)==0 or calculate_score(comp_deck)==0:
            compare(user_deck,comp_deck)
            play=False
        else:
            choice=input("Do you want to draw another card? Type \'y\' or \'n\': ").lower()
            if choice== 'y':
                user_deck.append(deal_card())
                play=True
            else:
                while calculate_score(comp_deck)<17:
                    comp_deck.append(deal_card())
                compare(user_deck, comp_deck)
                play=False

    choice_start = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\' ").lower()
    if choice_start == 'n':
        start_game = False