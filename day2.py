print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
percent=float(input("How much tip would you like to give? 10,12 or 15? "))
num=float(input("How many people to split the bill? "))
per_person=(bill+((percent*bill)/100))/num
print(f"Each person should pay: ${round(per_person,2)}")
