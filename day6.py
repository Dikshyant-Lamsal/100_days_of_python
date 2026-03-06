print("Calculator")
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


choice=int(input("Select 1 for sum, 2 for difference, 3 for division, 4 for multiplication. Enter choice: \n"))
num1=float(input("Enter number 1: "))
num2=float(input("Enter number 2: "))

if(choice==1):
    print("Sum: ",addition(num1,num2))
elif(choice==2):
    print("Difference: ",subtraction(num1,num2))
elif(choice==3):
    print("Quotient: ",division(num1,num2))
elif(choice==4):
    print("Product: ",multiplication(num1,num2))
else:
    print("Invalid Choice!")

