import random
word_list=["Hello","Word","Onomotopoeia","Hangman","Einstein","Oppenheimer","Gracilis","Momentum","Ballerina"]
chosen_word=(random.choice(word_list)).lower()

print(chosen_word)
placeholder=""

    
for i in range(len(chosen_word)):
    placeholder+="_"



display_list=list(placeholder)
correct=""
length=len(placeholder)


while(length>0):
    i=-1
    j=-1
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        i+=1
        if letter == guess:
            display_list[i] = letter
            length-=1
        elif display_list[i]!=letter:
            display_list[i] = "_"

    print("".join(display_list))


