import tkinter as tk
from tkinter import messagebox


def calculate_bill():
    try:
        # Get values from input fields
        people = int(people_entry.get())
        appetizers = float(appetizers_entry.get() or 0)
        main_courses = float(main_courses_entry.get() or 0)
        desserts = float(desserts_entry.get() or 0)
        drinks = float(drinks_entry.get() or 0)
        tip_percentage = float(tip_entry.get() or 0)

        # Validate number of people
        if people <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Number of people must be greater than 0."
            )
            return

        # Validate tip percentage
        if tip_percentage < 0:
            messagebox.showerror(
                "Invalid Input",
                "Tip percentage cannot be negative."
            )
            return

        # Calculate subtotal
        subtotal = (
            appetizers
            + main_courses
            + desserts
            + drinks
        )

        # Calculate tip
        tip_amount = subtotal * (tip_percentage / 100)

        # Calculate final bill
        total_bill = subtotal + tip_amount

        # Calculate amount per person
        per_person = total_bill / people

        # Update result labels
        subtotal_result.config(
            text=f"Subtotal: ₹{subtotal:.2f}"
        )

        tip_result.config(
            text=f"Tip: ₹{tip_amount:.2f}"
        )

        total_result.config(
            text=f"Total Bill: ₹{total_bill:.2f}"
        )

        person_result.config(
            text=f"Per Person: ₹{per_person:.2f}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers in all fields."
        )


def clear_fields():
    people_entry.delete(0, tk.END)
    appetizers_entry.delete(0, tk.END)
    main_courses_entry.delete(0, tk.END)
    desserts_entry.delete(0, tk.END)
    drinks_entry.delete(0, tk.END)
    tip_entry.delete(0, tk.END)

    people_entry.insert(0, "1")
    tip_entry.insert(0, "15")

    subtotal_result.config(text="Subtotal: ₹0.00")
    tip_result.config(text="Tip: ₹0.00")
    total_result.config(text="Total Bill: ₹0.00")
    person_result.config(text="Per Person: ₹0.00")


# Create main window
window = tk.Tk()

window.title("Bill Splitter")
window.geometry("500x650")
window.resizable(False, False)


# -----------------------------
# Title
# -----------------------------

title = tk.Label(
    window,
    text="🧾 Bill Splitter",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)


subtitle = tk.Label(
    window,
    text="Calculate and split your bill easily",
    font=("Arial", 11)
)

subtitle.pack(pady=(0, 20))


# -----------------------------
# Number of People
# -----------------------------

people_frame = tk.Frame(window)
people_frame.pack(pady=5)

people_label = tk.Label(
    people_frame,
    text="Number of People:",
    width=20,
    anchor="w",
    font=("Arial", 11)
)

people_label.pack(side="left")

people_entry = tk.Entry(
    people_frame,
    width=20,
    font=("Arial", 11)
)

people_entry.pack(side="left")

people_entry.insert(0, "1")


# -----------------------------
# Food Inputs
# -----------------------------

def create_input(label_text):
    frame = tk.Frame(window)
    frame.pack(pady=5)

    label = tk.Label(
        frame,
        text=label_text,
        width=20,
        anchor="w",
        font=("Arial", 11)
    )

    label.pack(side="left")

    entry = tk.Entry(
        frame,
        width=20,
        font=("Arial", 11)
    )

    entry.pack(side="left")

    return entry


appetizers_entry = create_input("Appetizers: ₹")

main_courses_entry = create_input("Main Courses: ₹")

desserts_entry = create_input("Desserts: ₹")

drinks_entry = create_input("Drinks: ₹")


# -----------------------------
# Tip
# -----------------------------

tip_entry = create_input("Tip Percentage: %")

tip_entry.insert(0, "15")


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(window)
button_frame.pack(pady=25)

calculate_button = tk.Button(
    button_frame,
    text="Calculate Bill",
    command=calculate_bill,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=8
)

calculate_button.pack(side="left", padx=10)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    font=("Arial", 12),
    padx=20,
    pady=8
)

clear_button.pack(side="left", padx=10)


# -----------------------------
# Results
# -----------------------------

result_title = tk.Label(
    window,
    text="Bill Summary",
    font=("Arial", 16, "bold")
)

result_title.pack(pady=10)


subtotal_result = tk.Label(
    window,
    text="Subtotal: ₹0.00",
    font=("Arial", 12)
)

subtotal_result.pack(pady=5)


tip_result = tk.Label(
    window,
    text="Tip: ₹0.00",
    font=("Arial", 12)
)

tip_result.pack(pady=5)


total_result = tk.Label(
    window,
    text="Total Bill: ₹0.00",
    font=("Arial", 13, "bold")
)

total_result.pack(pady=5)


person_result = tk.Label(
    window,
    text="Per Person: ₹0.00",
    font=("Arial", 15, "bold")
)

person_result.pack(pady=15)


# Start application
window.mainloop()
