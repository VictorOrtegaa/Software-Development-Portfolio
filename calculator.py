
import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide }


def calculator():
    print(art.logo)
    accumulate = True
    num1 = float(input("Enter the first number: "))

    while accumulate:

        for symbol in operations:
            print(symbol)
        operation2 = input("Enter the operation: ")

        num2 = float(input("Enter the second number: "))
        answer = operations[operation2](num1, num2)
        print(f"{num1} {operation2} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}"
                       f", or type 'n' to start a new calculation: "
                       f", or  Z to turn off the calculator ").lower()
        if choice == "y":
            num1 = answer

        elif choice == "n":
            accumulate = False
            print("\n" * 20)
            calculator()

        else:
            print("--- THANKS FOR USING THE CALCULATOR ---")
            break

calculator()
