import random
word_list=["Hello","Word","Onomotopoeia","Hangman","Einstein","Oppenheimer","Gracilis","Momentum","Ballerina"]
chosen_word=(random.choice(word_list)).lower()

print(chosen_word)
placeholder=""

    
for i in range(len(chosen_word)):
    placeholder+="_"

guess = input("Guess a letter: ").lower()

display=""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
