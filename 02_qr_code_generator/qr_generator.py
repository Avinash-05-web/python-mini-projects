import qrcode
import os
import tkinter as tk
from tkinter import messagebox, filedialog


def generate_qr():
    url = url_entry.get().strip()

    if not url:
        messagebox.showwarning("Missing URL", "Please enter a URL or text.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=5
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="red",
        back_color="white"
    )

    file_path = filedialog.asksaveasfilename(
        title="Save QR Code",
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")]
    )

    if file_path:
        img.save(file_path)

        messagebox.showinfo(
            "Success",
            f"QR code saved successfully!\n\n{file_path}"
        )


# Create GUI window
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("500x300")
window.resizable(False, False)

# Title
title_label = tk.Label(
    window,
    text="QR Code Generator",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=25)

# URL label
url_label = tk.Label(
    window,
    text="Enter URL or Text:",
    font=("Arial", 12)
)

url_label.pack()

# URL input
url_entry = tk.Entry(
    window,
    width=50,
    font=("Arial", 12)
)

url_entry.pack(pady=10)

# Generate button
generate_button = tk.Button(
    window,
    text="Generate QR Code",
    font=("Arial", 12, "bold"),
    command=generate_qr
)

generate_button.pack(pady=20)

# Status
status_label = tk.Label(
    window,
    text="Enter a URL or text and generate your QR code.",
    font=("Arial", 10)
)

status_label.pack(pady=10)

# Start GUI
window.mainloop()
