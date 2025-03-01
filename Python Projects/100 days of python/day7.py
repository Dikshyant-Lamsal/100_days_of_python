import random
word_list=["Hello","Word","Onomotopoeia","Hangman","Einstein","Oppenheimer","Gracilis","Momentum","Ballerina"]
chosen_word=(random.choice(word_list)).lower()

print(chosen_word)


guess=input("Guess a Letter: ").lower()

for letter in chosen_word:
    if guess==letter:
        print("Right")
    else:
        print("Wrong")
        life = life - 1