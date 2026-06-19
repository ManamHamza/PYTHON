def calculator():
    print("Simple Calculator")
    print("The available operators are: +, -, /, *")

    while True:
        try:
            num1 = float(input("\nEnter number 1: "))
            operator = input("Enter the operation you want to perform: ").strip()
            num2 = float(input("Enter number 2: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("INVALID OPERATOR USED!")
                continue

            # Show result
            print(f"{num1} {operator} {num2} = {result}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

        again = input("\nDo another calculation? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    calculator()