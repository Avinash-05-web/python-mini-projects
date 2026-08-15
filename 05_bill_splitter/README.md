# 🧾 Bill Splitter

A simple and user-friendly Python GUI application that calculates a restaurant bill, adds a customizable tip, and splits the final bill between multiple people.

This project started as a basic Python bill calculation program and was enhanced with a graphical user interface using Tkinter.

---

## ✨ Features

- 🧾 Calculate the total restaurant bill
- 👥 Split the bill between multiple people
- 🍽️ Enter appetizer costs
- 🍛 Enter main course costs
- 🍰 Enter dessert costs
- 🥤 Enter drink costs
- 💰 Set a custom tip percentage
- 📊 Display subtotal
- 💵 Calculate tip amount
- 🧮 Calculate final bill
- 👤 Calculate bill per person
- 🧹 Clear all inputs
- ❌ Handle invalid input
- 🖥️ Simple graphical user interface
- 📦 No external Python packages required

---

## 🛠️ Technologies Used

- Python 3
- Tkinter

Tkinter is included with most standard Python installations.

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

Enter the Bill Splitter project:

```bash
cd 05_bill_splitter
```

No additional packages are required.

---

## ▶️ Run the Application

Run:

```bash
python bill_splitter.py
```

On systems using `python3`:

```bash
python3 bill_splitter.py
```

A graphical window should open.

---

## 📖 How to Use

When the application opens, enter the required information.

Example:

```text
Number of People: 4
Appetizers: 37.89
Main Courses: 57.34
Desserts: 39.39
Drinks: 64.21
Tip Percentage: 25
```

Then click:

```text
Calculate Bill
```

The application will calculate:

* Subtotal
* Tip amount
* Total bill
* Amount per person

---

## 🧮 Calculation

The application uses the following calculation:

### Subtotal

```text
Subtotal =
Appetizers
+ Main Courses
+ Desserts
+ Drinks
```

### Tip

```text
Tip = Subtotal × (Tip Percentage / 100)
```

### Total Bill

```text
Total Bill = Subtotal + Tip
```

### Bill Per Person

```text
Bill Per Person = Total Bill / Number of People
```

---

## 💻 Example

Using:

```text
Number of People: 4

Appetizers: 37.89
Main Courses: 57.34
Desserts: 39.39
Drinks: 64.21

Tip Percentage: 25%
```

The application calculates approximately:

```text
Subtotal:     ₹198.83
Tip:          ₹49.71
Total Bill:   ₹248.54
Per Person:   ₹62.14
```

---

## 🖥️ Application Interface

The application provides input fields for:

```text
┌─────────────────────────────────┐
│          🧾 Bill Splitter        │
│                                 │
│ Number of People: [ 4       ]   │
│ Appetizers:       [ 37.89   ]   │
│ Main Courses:     [ 57.34   ]   │
│ Desserts:         [ 39.39   ]   │
│ Drinks:           [ 64.21   ]   │
│ Tip Percentage:   [ 25      ]   │
│                                 │
│      [ Calculate Bill ]         │
│           [ Clear ]             │
│                                 │
│          Bill Summary           │
│                                 │
│ Subtotal:     ₹198.83           │
│ Tip:          ₹49.71            │
│ Total Bill:   ₹248.54           │
│ Per Person:   ₹62.14            │
└─────────────────────────────────┘
```

---

## ❌ Input Validation

The application checks for invalid input.

For example, if the user enters text instead of a number:

```text
Number of People: abc
```

The application displays an error message:

```text
Please enter valid numbers in all fields.
```

The application also prevents the number of people from being zero or negative.

Example:

```text
Number of People: 0
```

Result:

```text
Number of people must be greater than 0.
```

Negative tip percentages are also rejected.

---

## 🧹 Clear Button

The **Clear** button removes the entered values and resets the application.

It also restores the default values:

```text
Number of People: 1
Tip Percentage: 15
```

---

## 📂 Project Structure

```text
05_bill_splitter/
│
├── bill_splitter.py
└── README.md
```

---

## 🧠 Python Concepts Used

This project demonstrates:

* Variables
* User input
* Functions
* Conditional statements
* Exception handling
* Arithmetic operations
* Floating-point numbers
* GUI programming
* Tkinter widgets
* Entry fields
* Buttons
* Labels
* Message boxes
* Event-driven programming
* Basic input validation

---

## 🔧 How It Works

The application follows this process:

```text
User enters bill details
        ↓
User enters number of people
        ↓
User enters tip percentage
        ↓
Click "Calculate Bill"
        ↓
Calculate subtotal
        ↓
Calculate tip
        ↓
Calculate total bill
        ↓
Split total between people
        ↓
Display bill summary
```

---

## 🔧 Troubleshooting

### Python is not recognized

If you see:

```text
'python' is not recognized as an internal or external command
```

install Python and make sure Python is added to your system PATH.

Then restart your terminal and run:

```bash
python --version
```

---

### Tkinter is not available

On most Windows and macOS Python installations, Tkinter is included by default.

On Ubuntu/Debian Linux, install it using:

```bash
sudo apt install python3-tk
```

Then run:

```bash
python3 bill_splitter.py
```

---

## 🚀 Future Improvements

Planned improvements include:

* [ ] Custom currency selection
* [ ] Restaurant tax calculation
* [ ] Service charge calculation
* [ ] Individual item entry
* [ ] Item quantity support
* [ ] Bill history
* [ ] Save bill as PDF
* [ ] Export bill as text
* [ ] Copy bill summary
* [ ] Dark mode
* [ ] Better GUI design
* [ ] Receipt-style bill preview
* [ ] Different amounts for different people
* [ ] Equal and custom bill splitting
* [ ] Currency conversion

---

## 🎯 Learning Goals

This project was created to practice:

* Python GUI development
* User input handling
* Functions
* Calculations
* Exception handling
* Tkinter
* Real-world problem solving
* Building useful desktop utilities

---

## ⚠️ Disclaimer

This project is created for educational purposes.

The calculations are intended for general use and should be verified when used for real financial transactions.

---

## 👨‍💻 Author

**Avinash Das Manikpuri**

GitHub:

[https://github.com/Avinash-05-web](https://github.com/Avinash-05-web)

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

More Python projects coming soon! 🚀
