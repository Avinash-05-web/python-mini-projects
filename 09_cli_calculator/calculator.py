import math
from datetime import datetime


HISTORY_FILE = "calculation_history.txt"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot use modulus with zero.")
    return a % b


def floor_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a // b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(a)


def percentage(value, percent):
    return value * (percent / 100)


def format_number(value):
    """Make calculator output easier to read."""

    if isinstance(value, float) and value.is_integer():
        return str(int(value))

    return f"{value:.10g}"


def add_history(history, expression, result):
    """Add a calculation to the session history."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    history.append({
        "time": timestamp,
        "expression": expression,
        "result": result
    })


def show_history(history):
    """Display calculation history."""

    if not history:
        print("\n📜 No calculations in history.")
        return

    print("\n" + "=" * 60)
    print("📜 CALCULATION HISTORY")
    print("=" * 60)

    for index, item in enumerate(history, start=1):
        print(
            f"{index}. "
            f"[{item['time']}] "
            f"{item['expression']} = {format_number(item['result'])}"
        )

    print("=" * 60)


def save_history(history):
    """Save calculation history to a text file."""

    if not history:
        print("\n📜 No history to save.")
        return

    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:

            file.write("CLI CALCULATOR - CALCULATION HISTORY\n")
            file.write("=" * 60 + "\n\n")

            for item in history:
                file.write(
                    f"[{item['time']}] "
                    f"{item['expression']} = "
                    f"{format_number(item['result'])}\n"
                )

        print(f"\n💾 History saved to: {HISTORY_FILE}")

    except OSError as error:
        print(f"\n❌ Could not save history: {error}")


def clear_history(history):
    """Clear the current session history."""

    history.clear()
    print("\n🧹 Calculation history cleared.")


def get_number(prompt):
    """Safely get a number from the user."""

    while True:
        value = input(prompt).strip()

        try:
            return float(value)

        except ValueError:
            print("❌ Invalid number. Please enter a valid number.")


def show_menu():
    """Display the calculator menu."""

    print("\n" + "=" * 60)
    print("                 🧮 CLI CALCULATOR")
    print("=" * 60)

    print("""
Choose an operation:

1.  Addition (+)
2.  Subtraction (-)
3.  Multiplication (*)
4.  Division (/)
5.  Modulus (%)
6.  Floor Division (//)
7.  Power (**)
8.  Square Root (√)
9.  Percentage (%)
10. Calculation History
11. Save History
12. Clear History
13. Help
0.  Exit
""")


def show_help():
    """Display calculator instructions."""

    print("\n" + "=" * 60)
    print("                 📖 CALCULATOR HELP")
    print("=" * 60)

    print("""
Basic Operations:

1. Addition
   Example: 10 + 5 = 15

2. Subtraction
   Example: 10 - 5 = 5

3. Multiplication
   Example: 10 * 5 = 50

4. Division
   Example: 10 / 5 = 2

5. Modulus
   Example: 10 % 3 = 1

6. Floor Division
   Example: 10 // 3 = 3

7. Power
   Example: 2 ** 3 = 8

8. Square Root
   Example: √25 = 5

9. Percentage
   Example: 20% of 500 = 100

Commands:

history  → Show calculation history
save     → Save history to a text file
clear    → Clear calculation history
help     → Show this help menu
exit     → Exit the calculator
""")


def perform_operation(choice, history):
    """Perform the selected calculator operation."""

    if choice == "1":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        result = add(a, b)
        expression = f"{format_number(a)} + {format_number(b)}"

    elif choice == "2":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        result = subtract(a, b)
        expression = f"{format_number(a)} - {format_number(b)}"

    elif choice == "3":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        result = multiply(a, b)
        expression = f"{format_number(a)} × {format_number(b)}"

    elif choice == "4":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        result = divide(a, b)
        expression = f"{format_number(a)} ÷ {format_number(b)}"

    elif choice == "5":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        result = modulus(a, b)
        expression = f"{format_number(a)} % {format_number(b)}"

    elif choice == "6":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        result = floor_divide(a, b)
        expression = f"{format_number(a)} // {format_number(b)}"

    elif choice == "7":
        a = get_number("Enter base number: ")
        b = get_number("Enter exponent: ")

        result = power(a, b)
        expression = f"{format_number(a)} ** {format_number(b)}"

    elif choice == "8":
        a = get_number("Enter number: ")

        result = square_root(a)
        expression = f"√{format_number(a)}"

    elif choice == "9":
        percent = get_number("Enter percentage: ")
        value = get_number("Enter value: ")

        result = percentage(value, percent)
        expression = (
            f"{format_number(percent)}% of "
            f"{format_number(value)}"
        )

    else:
        return

    print(
        f"\n✅ Result: "
        f"{expression} = {format_number(result)}"
    )

    add_history(history, expression, result)


def main():
    """Main calculator application."""

    history = []

    print("\n🧮 Welcome to the CLI Calculator!")
    print("Type 'help' for instructions or 'exit' to quit.")

    while True:

        show_menu()

        choice = input("Enter your choice: ").strip().lower()

        # Exit
        if choice in ("0", "exit", "quit"):
            print("\n👋 Thanks for using the CLI Calculator!")
            break

        # Help
        if choice == "help" or choice == "13":
            show_help()
            continue

        # History
        if choice == "history" or choice == "10":
            show_history(history)
            continue

        # Save history
        if choice == "save" or choice == "11":
            save_history(history)
            continue

        # Clear history
        if choice == "clear" or choice == "12":
            clear_history(history)
            continue

        # Operations
        if choice in {
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9"
        }:

            try:
                perform_operation(choice, history)

            except ZeroDivisionError as error:
                print(f"\n❌ Error: {error}")

            except ValueError as error:
                print(f"\n❌ Error: {error}")

            except OverflowError:
                print("\n❌ Error: The calculation result is too large.")

            except Exception as error:
                print(f"\n❌ Unexpected error: {error}")

            continue

        print("\n❌ Invalid choice.")
        print("Please select an option from the menu.")


if __name__ == "__main__":
    main()
