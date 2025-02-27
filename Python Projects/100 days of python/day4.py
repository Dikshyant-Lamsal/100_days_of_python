import random
user_win_count=0;
comp_win_count=0;
choice = 'y'  

while (choice.lower() == 'y'):
    user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
    comp_choice = random.randint(0, 2)

    if user_choice == 0:
        if comp_choice == 0:
            res = "draw"
        elif comp_choice == 1:
            res = "comp_win"
        else:
            res = "user_win"
    elif user_choice == 1:
        if comp_choice == 1:
            res = "draw"
        elif comp_choice == 2:
            res = "comp_win"
        else:
            res = "user_win"
    elif user_choice == 2:
        if comp_choice == 2:
            res = "draw"
        elif comp_choice == 0:
            res = "comp_win"
        else:
            res = "user_win"
    else:
        print("Invalid Choice!")
        exit(0)

    print("You Chose: ")
    if user_choice == 0:
        print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)
    elif user_choice == 1:
        print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)
    else:
        print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)

    print("Computer Chose: ")
    if comp_choice == 0:
        print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)
    elif comp_choice == 1:
        print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)
    else:
        print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)

    if res.lower() == "draw":
        print("DRAW\n")
    elif res.lower() == "comp_win":
        print("You Lose\n")
        comp_win_count=comp_win_count+1;
    elif res.lower() == "user_win":
        print("You Win\n")
        user_win_count=user_win_count+1;
    else:
        print("Invalid Choice")
    print(f"User wins:{user_win_count} Computer wins:{comp_win_count}\n")
    choice = input("Do you want to continue? (y/n) \n")