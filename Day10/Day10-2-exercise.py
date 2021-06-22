from art import logo
print(logo)

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operands = {}

operands["+"] = add
operands["-"] = subtract
operands["*"] = multiply
operands["/"] = divide 

def calculator():
    num1 = float(input("\nWhat's the first number? : "))
    looping = True
    while looping:

        num2 = float(input("\nWhat's the next number? : "))

        for key in operands:
            print(f".... {key} ....")
        sel_operation = input("Please select the operation from above : ")
        calculation_func = operands[sel_operation] 
        answer = calculation_func(num1, num2)

        print(f" {num1} {sel_operation} {num2} = {answer}")
        num1 = answer
        choice = input(f"\nType y to continue calculations with {answer}, n to quit or c to start a new calculation: ")
        if choice == "n":
            looping = False
        elif choice == "c":
            print("\n**New Calculation**")
            calculator()

calculator()