from os import system
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
system("cls")
print(logo)
print("Welcome to the secret auction program.")
bidder_info={
    "name":[],
    "bid":[],
}



def auction():
    go_on=True
    while(go_on):
        bidder_info["name"].append(input("What's your name?: "))
        bidder_info["bid"].append(int(input("What's your bid? $")))
        
        choice_go_on=True
        while(choice_go_on):
            choice=input("Are there any other bidders? Type \'yes\' or \'no\'\n").lower()
            if(choice=="yes"):
                choice_go_on=False
                go_on=True
                system("cls")
            elif(choice=="no"):
                go_on=False
                choice_go_on=False
                select_winner()
            else:
                print("Invalid Input")
                choice_go_on=True

def select_winner():
    winner_name=""
    highest_bid=0
    for value in range(0,len(bidder_info["bid"])):
        if(bidder_info["bid"][value]>highest_bid):
            winner_name=bidder_info["name"][value]
            highest_bid=bidder_info["bid"][value]
    system("cls")
    print(f"The winner is {winner_name} with a bid of ${highest_bid}\n\n\n\n")

auction()

