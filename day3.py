print('''
                    ____...------------...____
               *.-"` /o/*_ ____ ** ** __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   */ \*     <_o#\__/#o_>     */ \*   \\
             \\_________\\####/_________/
              |===\\!/========================\\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \\========|o|===|
              |   | |         \\() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | **/ \\**     '-.\\uuu/.-'    **/ \\** |
              |==== .'.'^'.'.====|
          jgs |  *\\o/   *_  {.' __  '.} *   *\\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island!")
print("Your Mission is to find the treasure!")
choice=input("You are at a cross road. Where do you want to go? \n Type \"Left\" or \"Right\"? \n")

if(choice.upper()!="LEFT"):
    print("Fell into a hole. :( Game Over");
    exit(0);

choice=input("You've come to a lake. There is an island in the middle of the lake. \n Type \"Wait\" to wait for a boat. type \"Swim\" to swim across.\n")
if(choice.upper()!="WAIT"):
    print("Attacked by a trout. :( Game Over");
    exit(0);

choice=input("You have arrived at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which color do you choose? \n")

if(choice.upper()=="RED"):
    print("Burned by fire. :( Game Over ")
    exit(0);
elif(choice.upper()=="BLUE"):
    print("Eaten by Beasts. :( Game Over")
    exit(0);
elif(choice.upper()=="YELLOW"):
    print("You Win!! :D")
    exit(0);
else:
    print("Game Over :(")

