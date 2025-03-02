import random
word_list=["Hello","Word","Onomotopoeia","Hangman","Einstein","Oppenheimer","Gracilis","Momentum","Ballerina"]
chosen_word=(random.choice(word_list)).lower()

print(chosen_word)
placeholder=""

    
for i in range(len(chosen_word)):
    placeholder+="_"



display_list=list(placeholder)

game_over=False
false_guess=0

while(not game_over):
    i=-1
    j=-1
    guess = input("Guess a letter: ").lower()
    

    for letter in chosen_word:
        # display_list_prev=display_list
        i+=1
        if letter == guess:
            display_list[i] = letter
        elif display_list[i]!=letter:
            display_list[i] = "_"
        
    # if(display_list_prev==display_list):
    #     false_guess+=1        
    #     print(f"False Guess: {false_guess}")

    print("".join(display_list))

    if("_" not in display_list):
        print("YOU WIN!")
        game_over=True
    elif(false_guess==5):
        game_over=True

    


