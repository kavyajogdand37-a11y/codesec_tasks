
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def calculator():
    print("=" * 35)
    print("      SIMPLE CALCULATOR")
    print("=" * 35)

    while True:
        try:
            num1 = float(input("\nEnter First Number: "))
            num2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        print("\nSelect Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            result = add(num1, num2)
            print(f"\nResult: {num1} + {num2} = {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"\nResult: {num1} - {num2} = {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"\nResult: {num1} * {num2} = {result}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"\nResult: {num1} / {num2} = {result}")

        else:
            print("Invalid Choice!")
            continue

        again = input("\nDo you want to perform another calculation? (y/n): ")

        if again.lower() != 'y':
            print("\nThank you for using the Calculator!")
            break


if __name__ == "__main__":
    calculator()
