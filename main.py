def main():

    valid_operations = {'+', '-', '*', '/'}

    while True:
        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Error: please enter valid numbers.")

    while True:
        operation = input("Choose an operation +, -, *, /): ")
        if operation in valid_operations:
            break
        else:
            print("Error: Invalid operation. Please enter +, -, *, or /.")

    if operation == "+":
        result = first_number + second_number
        print(f"{first_number} + {second_number} = {result}")

    elif operation == "-":
        result = first_number - second_number
        print(f"{first_number} - {second_number} = {result}")

    elif operation == "*":
        result = first_number * second_number
        print(f"{first_number} * {second_number} = {result}")

    elif operation == "/":
        if second_number != 0:
            result = first_number / second_number
            print(f"{first_number} / {second_number} = {result}")
        else:
            print("Error: Division by zero is not allowed.")

    else:
        print("error, invalid operation")

if __name__ == "__main__":
    main()