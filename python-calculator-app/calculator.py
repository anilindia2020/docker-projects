# calculator.py

def main():
    """Runs the main calculator loop."""
    print("--- Simple Python Calculator ---")
    print("Enter 'q' at any time to quit.")
    print("-" * 30)

    while True:
        # 1. Get the first number
        try:
            num1_input = input("Enter the first number: ")
            if num1_input.lower() == 'q':
                break
            num1 = float(num1_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # 2. Get the operator
        operator = input("Enter an operator (+, -, *, /): ")
        if operator.lower() == 'q':
            break
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator. Please use +, -, *, or /.")
            continue

        # 3. Get the second number
        try:
            num2_input = input("Enter the second number: ")
            if num2_input.lower() == 'q':
                break
            num2 = float(num2_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # 4. Perform calculation and print result
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = num1 / num2
        
        print(f"\n✅ Result: {num1} {operator} {num2} = {result}\n")

    print("\nCalculator exiting. Goodbye!")

if __name__ == "__main__":
    main()
