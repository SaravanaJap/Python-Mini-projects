def arithmetic(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        if second == 0:
            return "Error! Division by zero."
        return first / second
    else:
        return "Invalid operation!"

def calculator():
    new_calculation = 'y'

    while new_calculation == 'y':
        first_number = float(input("What's the first number: "))  # Using float for decimal support
        calculation_continue = 'y'

        while calculation_continue == 'y':
            print("+\n-\n*\n/")
            user_choice = input("Pick an operation: ")
            second_number = float(input("What's the next number: "))
            result = arithmetic(first_number, second_number, user_choice)

            print(f"{first_number} {user_choice} {second_number} = {result}")

            calculation_continue = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower()
            if calculation_continue == 'y':
                first_number = result

        new_calculation = input("Type 'y' to start a new calculation or 'n' to exit: ").lower()

print("Welcome to the Calculator")
calculator()
