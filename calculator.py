operators = ["add", "subtract", "multiply", "divide", "power", "+", "-", "*", "/", "**"]

float_value_1 = float(input("Please enter your first number: "))
float_value_2 = float(input("Please enter your second number: "))
user_operation = input("What would you like to do? ")

while user_operation not in operators:
    print("This operation is not yet available, please choose between addition, multiplaction, subtraction, division, or exponentiation")
    user_operation = input("What would you like to do? ")

def add(num1=0, num2=0):
    return num1+num2

def subtract(num1=0, num2=0):
    return num1-num2

def multiply(num1=0, num2=0):
    return num1*num2

def divide(num1=0, num2=0):
    return num1/num2

def power(num1=1, num2=0):
    return num1**num2

def calculate():
    if user_operation == "add" in operators or user_operation == "+":
        print(add(float_value_1, float_value_2))
    elif user_operation == "subtract" in operators or user_operation == "-":
        print(subtract(float_value_1, float_value_2))
    elif user_operation == "divide" in operators or user_operation == "/":
        print(divide(float_value_1, float_value_2))
    elif user_operation == "multiply" in operators or user_operation == "*":
        print(multiply(float_value_1, float_value_2))
    elif user_operation == "power" in operators or user_operation == "**":
        print(power(float_value_1, float_value_2))
    else:
        print("This calculator does not support this function")

calculate()
