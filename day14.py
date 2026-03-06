from game_data_day14 import data
import random
from os import system
play_game=True
score=0
logo_1='''

 ██░ ██  ██▓ ▄████  ██░ ██ ▓█████  ██▀███      ██▓     ▒█████   █     █░▓█████  ██▀███  
▓██░ ██▒▓██▒██▒ ▀█▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒   ▓██▒    ▒██▒  ██▒▓█░ █ ░█░▓█   ▀ ▓██ ▒ ██▒
▒██▀▀██░▒██▒██░▄▄▄░▒██▀▀██░▒███   ▓██ ░▄█ ▒   ▒██░    ▒██░  ██▒▒█░ █ ░█ ▒███   ▓██ ░▄█ ▒
░▓█ ░██ ░██░▓█  ██▓░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄     ▒██░    ▒██   ██░░█░ █ ░█ ▒▓█  ▄ ▒██▀▀█▄  
░▓█▒░██▓░██░▒▓███▀▒░▓█▒░██▓░▒████▒░██▓ ▒██▒   ░██████▒░ ████▓▒░░░██▒██▓ ░▒████▒░██▓ ▒██▒
 ▒ ░░▒░▒░▓  ░▒   ▒  ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▓░▒ ▒  ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░ ▒ ░ ░   ░  ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░   ░ ░ ▒  ░  ░ ▒ ▒░   ▒ ░ ░   ░ ░  ░  ░▒ ░ ▒░
 ░  ░░ ░ ▒ ░ ░   ░  ░  ░░ ░   ░     ░░   ░      ░ ░   ░ ░ ░ ▒    ░   ░     ░     ░░   ░ 
 ░  ░  ░ ░       ░  ░  ░  ░   ░  ░   ░            ░  ░    ░ ░      ░       ░  ░   ░     
                                                                                        
'''
logo_2='''

 ██▒   █▓ ██████      
▓██░   █▒██    ▒      
 ▓██  █▒░ ▓██▄        
  ▒██ █░░ ▒   ██▒     
   ▒▀█░ ▒██████▒▒ ██▓ 
   ░ ▐░ ▒ ▒▓▒ ▒ ░ ▒▓▒ 
   ░ ░░ ░ ░▒  ░ ░ ░▒  
     ░░ ░  ░  ░   ░   
      ░       ░    ░  
     ░             ░  
'''
def check_game(guess):
    global score
    global first
    if guess== 'a' and first['follower_count']>second['follower_count']:
            score+=1
            display_score()
            print(f"You're right! Current Score: {score}")
            first=first
            return True
    elif guess == 'b' and first['follower_count']<second['follower_count']:
            score+=1
            display_score()
            print(f"You're right! Current Score: {score}")
            first=second
            return True
    else:
        display_score()
        print(f"Sorry that's Wrong! Final score: {score}")
        return False

def display_score():
    system("cls")
    print(logo_1)

display_score()
first=random.choice(data)

while play_game:
    print(f"Compare A: {first["name"]}, a {first["description"]}, from {first['country']} ")
    print(logo_2)
    second = random.choice(data)
    while second==first:
        second = random.choice(data)

    print(f"Against B: {second["name"]}, a {second["description"]}, from {second['country']} ")
    guess=input("Who has more followers? Input \'A\' or \'B\' ").lower()
    play_game=check_game(guess)

