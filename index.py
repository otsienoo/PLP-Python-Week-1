# Basic Calculator App
def calculator():
    # Ask for user input
    try:
        num1 = float(input("Enter The First Number:"))
        num2 = float(input("Enter The Second Number:"))
        operation = input("Enter The Operation(+, -, *, /):")

        # Perform the operation and print the result
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")

        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")    

        elif operation == '/':
            if num2 != 0:
             result = num1 / num2
             print(f"{num1} / {num2} = {result}")

            else:
                print("Error: Division By Zero Is Not Allowed.")

        else:
            print("Invalid Operation. Please Enter +, -, *, or /.")

    except ValueError:
        print("Invalid Input. Please Enter Numbers Only.")

# Run the calculator function
calculator()