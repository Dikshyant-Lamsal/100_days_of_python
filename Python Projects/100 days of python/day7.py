import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list=["Hello","Word","Onomotopoeia","Hangman","Einstein","Oppenheimer","Gracilis","Momentum","Ballerina"]
chosen_word=(random.choice(word_list)).lower()

print(chosen_word)

game_over=False
false_guess=0
correct_guess=[]
lives=6

while(not game_over):
    
    guess = input("Guess a letter: ").lower()
    display=""    

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guess.append(letter)
        elif letter in correct_guess:
            display += letter
        else:
            display += "_"

    if(guess in chosen_word):
        print(stages[lives]) 
        print(display)   
    else:
        lives-=1
        print(f"Incorrect Guess, Lives Remaining: {lives}")
        print(display)
        print(stages[lives])

    if("_" not in list(display)):
        print("YOU WIN!")
        game_over=True
    elif(lives==0):
        print("You Lose")
        print(stages[0])
        game_over=True
