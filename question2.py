# Simple Calculator Functions

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print ("Can not divide a number by zero, try again!")
        main_function()
    

def main_function():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = None
        print("Choose operation: ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        operation = input("Enter choice (1-4): ")
        if(operation not in ["1", "2","3", "4"] ):
            print("The operation has to be selected from 1 to 4, try again! ")
            main_function()
        else:
            if operation == "1":
                result = add(num1, num2)
                operation_sign = "+"
            elif operation == "2":
                result = subtract(num1, num2)
                operation_sign = "-"
            elif operation == "3":
                result = multiply(num1,num2)
                operation_sign = "*"
            else:
                result = divide(num1, num2)
                operation_sign = "/"
        if result != None:
            print(f"{num1} {operation_sign} {num2} = {result:.3f}")
        
    except ValueError:
        print("Enter a valid number! Try again!")
        main_function()
    except Exception as e :
        print(f"An Error has occurred: {e}!! Try again!")
        main_function()

main_function()