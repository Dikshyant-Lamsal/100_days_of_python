import random
from os import system
logo='''
   _____                       _______ _            _   _ _    _ __  __ ____  ______ _____  _ _ _ _ 
  / ____|                     |__   __| |          | \ | | |  | |  \/  |  _ \|  ____|  __ \| | | | |
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| | |  | | \  / | |_) | |__  | |__) | | | | |
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | |  | | |\/| |  _ <|  __| |  _  /| | | | |
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |__| | |  | | |_) | |____| | \ \|_|_|_|_|
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\____/|_|  |_|____/|______|_|  \_(_|_|_|_)
'''                                                                                                   

system("cls")
print(logo)
print("Welcome to the number guessing game! \nI'm thinking of a number between 1 and 100\n")
difficulty=input("Choose a difficulty. Type \'easy\' or \'hard\': ").lower()
num = random.randint(1,100)

def guesser(level):
    if(level=="easy"):
        return 10
    else:
        return 5

attempts=guesser(difficulty)


while(attempts>0):
    print(f"You have {attempts} attempts remaining to guess the number")
    user_num=int(input("Make a guess: "))
    if(attempts==0):
        print("You have run out of guesses! You Lose :(")
    elif(user_num==num):
        print(f"You got it! The answer was {num}!")
        attempts=0
    elif(user_num>num):
        print("Too high!")
        attempts-=1
    else:
        print("Too low!")
        attempts-=1

