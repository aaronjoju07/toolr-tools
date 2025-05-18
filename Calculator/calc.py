import sys

def main():
    if len(sys.argv) < 4:
        print("Usage: python calc.py [add|sub|mul|div] num1 num2")
        return

    operation = sys.argv[1]
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Invalid numbers.")
        return

    if operation == "add":
        print(f"Result: {num1 + num2}")
    elif operation == "sub":
        print(f"Result: {num1 - num2}")
    elif operation == "mul":
        print(f"Result: {num1 * num2}")
    elif operation == "div":
        if num2 == 0:
            print("Division by zero error.")
        else:
            print(f"Result: {num1 / num2}")
    else:
        print("Unknown operation.")

if __name__ == "__main__":
    main()
