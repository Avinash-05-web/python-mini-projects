# 📱 QR Code Generator

A simple Python application that generates QR codes from URLs or text and saves them as PNG images.

## ✨ Features

* Generate QR codes from URLs or text
* High error correction
* PNG image output
* Choose where to save the generated QR code
* Simple graphical interface using Tkinter
* Lightweight and beginner-friendly

## 🛠️ Technologies Used

* **Python 3**
* **qrcode**
* **Pillow**
* **Tkinter**

## 📋 Requirements

Before running the project, make sure you have:

* Python 3.8 or newer
* pip
* Windows, Linux, or macOS

Check your Python installation:

```bash
python --version
```

or on some systems:

```bash
python3 --version
```

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Avinash-05-web/python-mini-projects.git
```

### 2. Open the project directory

```bash
cd python-mini-projects/02_qr_code_generator
```

### 3. Install the required package

```bash
pip install qrcode[pil]
```

If your system uses `python3`:

```bash
pip3 install qrcode[pil]
```

> **Note:** Tkinter is included with most standard Python installations. On some Linux distributions, you may need to install it separately.

For Ubuntu/Debian:

```bash
sudo apt install python3-tk
```

## ▶️ Run the Application

Run:

```bash
python qr_generator.py
```

or:

```bash
python3 qr_generator.py
```

A graphical window should open.

## 📖 How to Use

1. Enter a URL or text into the input field.
2. Click **Generate QR Code**.
3. Select where you want to save the QR code.
4. Save the image as a `.png` file.
5. Scan the generated QR code using your phone or another QR scanner.

### Example Input

```text
https://github.com/Avinash-05-web
```

The application will generate a QR code containing that URL.

## 📂 Project Structure

```text
02_qr_code_generator/
│
├── qr_generator.py
└── README.md
```

## 🖼️ Output

The generated QR code is saved as a PNG image.

Example:

```text
QR_Code.png
```

## 🔧 Troubleshooting

### `ModuleNotFoundError: No module named 'qrcode'`

Install the required package:

```bash
pip install qrcode[pil]
```

### `No module named tkinter`

On Ubuntu/Debian:

```bash
sudo apt install python3-tk
```

On Windows and macOS, Tkinter is normally included with the standard Python installation.

### `python is not recognized`

Make sure Python is installed and added to your system PATH.

Check with:

```bash
python --version
```

## ⚠️ Disclaimer

This project is created for **educational purposes**.

The QR code generator does not verify or validate the safety of URLs entered by the user. Always check a URL before opening or sharing it.

## 🚀 Future Improvements

Planned improvements include:

* [ ] Custom QR code colors
* [ ] Logo/image inside QR code
* [ ] QR code preview inside the application
* [ ] Batch QR code generation
* [ ] Dark mode
* [ ] Export options
* [ ] Better GUI design

## 👨‍💻 Author

**Avinash Das Manikpuri**

GitHub: [@Avinash-05-web](https://github.com/Avinash-05-web)

---

⭐ If you found this project useful, consider giving the repository a star!
