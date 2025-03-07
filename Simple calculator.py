# Simple Calculator
def calculator():
    operation = input("Choose an operation (+, -, *, /): ").strip()

    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation! Please choose +, -, *, or /")
        return

    try:
        numbers = input("Enter two numbers: ").split()
        
        if len(numbers) != 2:
            print("Please enter exactly two numbers separated by space.")
            return
        
        num1, num2 = float(numbers[0]), float(numbers[1])

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
                return
            result = num1 / num2

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

calculator()