# Develop a mni calculator with input validation


def add(*args):
    return sum(args)

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
print("Welcome to Calculator App !!")
print("a -> add, s -> subtract, m -> multiply, d -> divide, q -> quit")
while True:
    print('\na/s/m/d/q')
    user_input=input()
    
    if user_input == "q":
        break
    elif user_input in ("a", "s", "m", "d"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "a":
            print("Result:", add(num1, num2))
        elif user_input == "s":
            print("Result:", subtract(num1, num2))
        elif user_input == "m":
            print("Result:", multiply(num1, num2))
        elif user_input == "d":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please try again.")
