Yep bro 😎 Here is the **complete `README.md` for Project 09**, all in **one single copyable block**.

````markdown
# 🧮 CLI Calculator

A feature-rich command-line calculator built with Python.

This project started as a basic calculator and was developed into a more complete command-line application with multiple mathematical operations, calculation history, history saving, input validation, error handling, and helpful commands.

The project was built as part of my hands-on Python learning journey.

---

## ✨ Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- `%` Modulus
- `//` Floor division
- `**` Power
- √ Square root
- 📊 Percentage calculations
- 📜 Calculation history
- 💾 Save calculation history to a file
- 🧹 Clear calculation history
- 📖 Built-in help system
- 🔄 Continuous calculation loop
- 🛡️ Input validation
- 🚫 Division-by-zero protection
- ⚠️ Error handling
- 🔢 Supports integers and decimal numbers
- ❌ Safe program exit
- 📦 No external packages required

---

## 🛠️ Technologies Used

- Python 3.8+
- `math`
- `datetime`

Both modules are included in Python's standard library.

---

## 📋 Requirements

- Python 3.8 or newer
- No external Python packages required

Check your Python version:

```bash
python --version
````

If your system uses `python3`:

```bash
python3 --version
```

---

## 📥 Installation

### Clone the Repository

Clone the complete Python Mini Projects repository:

```bash
git clone https://github.com/Avinash-05-web/python-mini-projects.git
```

Enter the repository:

```bash
cd python-mini-projects
```

Enter the CLI Calculator project:

```bash
cd 09_cli_calculator
```

No additional packages are required.

---

## ▶️ Run the Calculator

Run:

```bash
python calculator.py
```

On systems using `python3`:

```bash
python3 calculator.py
```

---

## 🧮 Available Operations

The calculator supports the following operations.

### 1. Addition

Adds two numbers.

Example:

```text
10 + 5 = 15
```

---

### 2. Subtraction

Subtracts the second number from the first.

Example:

```text
10 - 5 = 5
```

---

### 3. Multiplication

Multiplies two numbers.

Example:

```text
10 × 5 = 50
```

---

### 4. Division

Divides the first number by the second.

Example:

```text
10 ÷ 5 = 2
```

Division by zero is prevented.

---

### 5. Modulus

Returns the remainder after division.

Example:

```text
10 % 3 = 1
```

---

### 6. Floor Division

Performs division and returns the floor value.

Example:

```text
10 // 3 = 3
```

---

### 7. Power

Raises a number to a specified exponent.

Example:

```text
2 ** 3 = 8
```

---

### 8. Square Root

Calculates the square root of a number.

Example:

```text
√25 = 5
```

Negative numbers are rejected for square-root calculations.

---

### 9. Percentage

Calculates a percentage of a value.

Example:

```text
20% of 500 = 100
```

---

## 📜 Calculation History

The calculator keeps track of calculations performed during the current session.

Type:

```text
history
```

or select:

```text
10
```

Example:

```text
============================================================
📜 CALCULATION HISTORY
============================================================

1. [2026-08-31 18:30:15] 25 + 15 = 40
2. [2026-08-31 18:31:02] 10 × 5 = 50
3. [2026-08-31 18:31:45] 20% of 500 = 100

============================================================
```

---

## 💾 Save History

Calculation history can be saved to a text file.

Type:

```text
save
```

or select:

```text
11
```

The program creates:

```text
calculation_history.txt
```

The file contains the calculations and timestamps from the current session.

---

## 🧹 Clear History

To clear the current calculation history, type:

```text
clear
```

or select:

```text
12
```

The history will be removed from the current session.

---

## 📖 Help

To display the built-in help menu, type:

```text
help
```

or select:

```text
13
```

The help menu explains the available operations and commands.

---

## 🚪 Exit

To exit the calculator, type:

```text
exit
```

You can also use:

```text
quit
```

or select:

```text
0
```

---

## 💻 Example Session

```text
============================================================
                 🧮 CLI CALCULATOR
============================================================

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

Enter your choice: 1

Enter first number: 25
Enter second number: 15

✅ Result: 25 + 15 = 40
```

---

## 🛡️ Error Handling

The calculator includes protection against common input and calculation errors.

### Invalid Number

If the user enters:

```text
Enter first number: hello
```

The program displays:

```text
❌ Invalid number. Please enter a valid number.
```

---

### Division by Zero

Example:

```text
Enter first number: 10
Enter second number: 0
```

The calculator prevents the operation and displays:

```text
❌ Error: Cannot divide by zero.
```

---

### Negative Square Root

Example:

```text
Enter number: -25
```

The program displays:

```text
❌ Error: Cannot calculate the square root of a negative number.
```

---

### Invalid Menu Choice

If an invalid option is entered:

```text
Enter your choice: 99
```

The program displays:

```text
❌ Invalid choice.
Please select an option from the menu.
```

---

## 🔐 Security Considerations

This calculator intentionally does **not** use Python's `eval()` function to process mathematical expressions.

Using `eval()` with uncontrolled user input can potentially execute arbitrary Python code.

Instead, the calculator performs each supported mathematical operation through dedicated Python functions.

This keeps the calculator's input handling more controlled and predictable.

---

## 🧠 Python Concepts Used

This project demonstrates:

* Variables
* Functions
* User input
* Conditional statements
* Loops
* Exception handling
* Dictionaries
* Lists
* Arithmetic operations
* Floating-point numbers
* Modules
* File handling
* Timestamps
* Command-line interfaces
* Input validation
* Error handling
* Functions with parameters
* Return values
* Python standard library

---

## 🔧 How It Works

The application follows this general process:

```text
Start Calculator
       ↓
Display Menu
       ↓
User Selects Operation
       ↓
Get User Input
       ↓
Validate Input
       ↓
Perform Calculation
       ↓
Display Result
       ↓
Save Result to History
       ↓
Return to Menu
       ↓
Continue or Exit
```

---

## 📂 Project Structure

```text
09_cli_calculator/
│
├── calculator.py
├── calculation_history.txt
└── README.md
```

> `calculation_history.txt` is generated automatically when the user chooses to save calculation history.

If you do not want the generated history file tracked by Git, add it to `.gitignore`.

Example:

```text
calculation_history.txt
```

---

## 🧪 Testing

The calculator can be tested using different types of input.

### Basic calculations

```text
10 + 5
20 - 7
8 * 9
100 / 4
10 % 3
10 // 3
2 ** 8
√144
25% of 200
```

### Error testing

Try:

```text
10 / 0
```

```text
√-25
```

```text
abc + 10
```

```text
Invalid menu option
```

The application should handle these cases without crashing.

---

## 🚀 Future Improvements

Possible future improvements include:

* [ ] Full expression input
* [ ] Scientific calculator mode
* [ ] Trigonometric functions
* [ ] Logarithmic functions
* [ ] Factorial calculations
* [ ] Absolute value
* [ ] Advanced mathematical functions
* [ ] Persistent calculation history
* [ ] Export history to CSV
* [ ] Export history to JSON
* [ ] Custom history file location
* [ ] Calculator themes
* [ ] GUI version
* [ ] Unit conversion
* [ ] Currency conversion
* [ ] More advanced input parsing

---

## 🎯 Learning Goals

This project was created to practice:

* Python fundamentals
* Mathematical operations
* Functions
* Error handling
* Input validation
* File handling
* Command-line applications
* Python modules
* Building reusable code
* Writing safer user-input handling
* Creating practical Python utilities

---

## ⚠️ Disclaimer

This calculator is intended for educational and general-purpose calculations.

Results should be independently verified when used for important financial, scientific, engineering, or other high-stakes calculations.

The author is not responsible for errors or misuse of the application.

---

## 👨‍💻 Author

**Avinash Das Manikpuri**

GitHub:

[https://github.com/Avinash-05-web](https://github.com/Avinash-05-web)

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

More Python and cybersecurity projects coming soon! 🚀
