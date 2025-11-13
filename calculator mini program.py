#this is a program to make a calculator.
try:
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))
except:
    print("Enter only numbers!")

def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("Division by zero is not possible!")

def power(num1,num2):
    return num1**num2

def modulus(num1,num2):
    return num1%num2

def floor_division(num1,num2):
    try:
        return num1//num2
    except ZeroDivisionError:
        print("Division by zero is not possible")

while True:

    statement="\nwhat mathematical operation do you want to perform?"
    statement+="\nEnter 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division, and 5 for exponentiation."
    statement+="\nAlso enter -1 to terminate the program: "

    try:
        choice=int(input(statement))
    except ValueError:
        print("Enter integer value!")

    if choice==1:
            print('The sum of two numbers is', add(num1,num2))
        
    elif choice==2:
            print('The difference between the two numbers is:', subtract(num1,num2)) 
        
    elif choice==3:
            print('The product of the two numbers is:', multiply(num1, num2))
        
    elif choice==4:
            print('The answer upon division of both the numbers is:', divide(num1, num2))
            print('The quotient of the division would be: ', floor_division(num1,num2))
            print('The remainder upon division is: ', modulus(num1,num2))

    elif choice==5:
            print('The answer upon exponentiation of both the numbers is: ', power(num1, num2))

    elif choice==-1:
            print("Program terminated!!")
            break
        
    else:
            print("Invalid Choice!!")

        

