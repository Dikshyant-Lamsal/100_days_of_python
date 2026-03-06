from os import system
logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
system("clear")

a=0.0
b=0.0
def addition(a,b):
    return (a+b)

def subtraction(a,b):
    return (a-b)

def multiplication(a,b):
    return (a*b)

def division(a,b):
    if(b!=0):
        return (a/b)
    else:
        print("Cannot Divide by Zero!!")
        exit(0)

def calculator():
    calculate=True
    print(logo)
    num1=float(input("Enter number 1: "))
    while(calculate):
        choice_1=(input("+\n-\n*\n/\nPick an operation: "))
        num2=float(input("Enter number 2: "))

        if(choice_1=="+"):
            res=addition(num1,num2)
            print("Sum: ",res)
        elif(choice_1=="-"):
            res=subtraction(num1,num2)
            print("Difference: ",res)
        elif(choice_1=="/"):
            res=division(num1,num2)
            print("Quotient: ",res)
        elif(choice_1=="*"):
            res=multiplication(num1,num2)
            print("Product: ",res)
        else:
            print("Invalid Choice!")
            
        choice=input(f"Do you want to continue with {res} or start a new calculation? Type \"y\" to continue \"n\" for new calculation. ")
        
        if (choice.lower()=="y"):
            num1=res
            calculate=True
        else:
            calculate=False
            calculator()

calculator()

