# 🐍 Python Mini Projects

A collection of practical Python projects created while learning Python programming, automation, networking, GUI development, and cybersecurity fundamentals.

The goal of this repository is to build small, useful projects while gradually moving from beginner concepts to more advanced applications.

---

## 📂 Projects

| #  | Project                                           | Description                                                    | Technologies                    | Status         |
| -- | ------------------------------------------------- | -------------------------------------------------------------- | ------------------------------- | -------------- |
| 01 | 🔍 [Port Scanner](./01_port_scanner/)             | Scan TCP ports on an authorized device and identify open ports | Python, Socket                  | ✅ Completed    |
| 02 | 📱 [QR Code Generator](./02_qr_code_generator/)   | Generate QR codes from URLs or text                            | Python, qrcode, Tkinter         | ✅ Completed    |
| 03 | 🔐 [Password Generator](./03_password_generator/) | Generate secure random passwords                               | Python, secrets, string         | ✅ Completed    |
| 04 | 📁 [File Organizer](./04_file_organizer/)         | Automatically organize files by extension                      | Python, OS, shutil              | ✅ Completed    |
| 05 | 🌐 Website Status Checker                         | Check whether websites are reachable                           | Python, Requests                | 🔜 Coming Soon |

---

# 🔍 Project 01 — Port Scanner

A simple TCP port scanner built using Python's `socket` module.

### Features

* Scan a target IP address
* Scan a custom range of TCP ports
* Detect open ports
* Configurable connection timeout
* Display scan results

### Technologies

* Python
* Socket Programming
* TCP/IP

[View Port Scanner →](./01_port_scanner/)

---

# 📱 Project 02 — QR Code Generator

A Python application that generates QR codes from URLs or text.

### Features

* Generate QR codes from URLs or text
* High error correction
* PNG output
* Choose a save location
* GUI-based interface
* Beginner-friendly implementation

### Technologies

* Python
* qrcode
* Pillow
* Tkinter

### Installation

Go to the project directory:

```bash
cd 02_qr_code_generator
````

Install the required package:

```bash
pip install qrcode[pil]
```

Run:

```bash
python qr_generator.py
```

[View QR Code Generator →](./02_qr_code_generator/)

---

# 🔐 Project 03 — Secure Password Generator

A secure and customizable password generator built using Python's `secrets` module.

The project generates strong random passwords with support for uppercase letters, lowercase letters, numbers, optional symbols, and password strength detection.

### Features

* Custom password length
* Lowercase letters
* Uppercase letters
* Numbers
* Optional symbols
* Password strength detection
* Input validation
* Secure character shuffling
* Uses Python's `secrets` module
* No external packages required

### Technologies

* Python
* secrets
* string

### Installation

Go to the project directory:

```bash
cd 03_password_generator
```

No additional packages are required.

### Run

```bash
python password_generator.py
```

[View Password Generator →](./03_password_generator/)

---

# 📁 Project 04 — File Organizer

A Python automation tool that automatically organizes files into folders based on their file extensions.

The program can sort images, videos, documents, audio files, archives, programming files, and unknown file types.

### Features

* Automatically organize files
* Sort images
* Sort videos
* Sort documents
* Sort audio files
* Sort archives
* Sort programming files
* Create category folders automatically
* Move unknown file types to an `Others` folder
* Check whether the selected folder exists
* Ignore existing folders
* No external packages required

### Technologies

* Python
* `os`
* `shutil`

### Installation

Go to the project directory:

```bash
cd 04_file_organizer
```

No additional packages are required.

### Run

```bash
python file_organizer.py
```

The program will ask for the folder you want to organize.

Example:

```text
Enter the folder path to organize: C:\Users\YourName\Downloads
```

[View File Organizer →](./04_file_organizer/)

---

# 📈 Learning Progress

This repository represents my hands-on Python learning journey.

## Python Fundamentals

* [x] Variables and data types
* [x] User input
* [x] Conditional statements
* [x] Loops
* [x] Lists
* [x] Functions
* [x] Modules
* [x] File paths
* [x] Exception handling
* [ ] Object-oriented programming
* [ ] APIs
* [ ] Multithreading
* [ ] Advanced Python

## Networking & Cybersecurity

* [x] Basic TCP socket programming
* [x] Port scanning fundamentals
* [x] Secure random generation
* [x] Password generation
* [ ] Service detection
* [ ] Banner grabbing
* [ ] DNS tools
* [ ] Network automation
* [ ] Log analysis
* [ ] Security automation
* [ ] Cryptography fundamentals
* [ ] Hashing
* [ ] Encryption

## GUI Development

* [x] Basic Tkinter
* [x] User input fields
* [x] Buttons
* [x] Message boxes
* [x] File dialogs
* [ ] Advanced GUI layouts
* [ ] Custom themes

## Automation

* [x] File organization
* [x] File extension detection
* [x] Directory creation
* [x] File movement
* [ ] Duplicate file detection
* [ ] Automated file monitoring
* [ ] Advanced automation workflows

---

# 🚀 Upcoming Projects

Some projects planned for this repository:

* 🌐 Website Status Checker
* 🔎 DNS Lookup Tool
* 📊 Log Analyzer
* 🧮 CLI Calculator
* 📝 Text Analyzer
* 🖥️ System Information Tool
* 🔗 URL Utilities
* 📡 Network Utilities
* 🔐 File Encryption Tool
* 📊 Password Strength Analyzer
* 🌐 HTTP Header Checker
* 📂 Duplicate File Finder
* 🧹 File Cleanup Utility

More projects will be added as I continue learning.

---

# 🛠️ General Requirements

Most projects require:

* Python 3.8+
* pip

Check your Python version:

```bash
python --version
```

If your system uses `python3`:

```bash
python3 --version
```

Some projects may require additional Python packages. Each project contains its own `README.md` with installation and usage instructions.

---

# 📥 Clone the Repository

To download the complete collection:

```bash
git clone https://github.com/Avinash-05-web/python-mini-projects.git
```

Then enter the repository:

```bash
cd python-mini-projects
```

Choose a project and follow its individual README.

---

# 📁 Repository Structure

```text
python-mini-projects/
│
├── README.md
│
├── 01_port_scanner/
│   ├── port_scanner.py
│   └── README.md
│
├── 02_qr_code_generator/
│   ├── qr_generator.py
│   └── README.md
│
├── 03_password_generator/
│   ├── password_generator.py
│   └── README.md
│
└── 04_file_organizer/
    ├── file_organizer.py
    └── README.md
```

---

# 🎯 Purpose of This Repository

This repository is being developed as a practical Python learning portfolio.

Instead of only learning Python through tutorials and theory, I am building small projects to practice:

* Programming fundamentals
* Problem solving
* Automation
* Networking
* GUI development
* Security programming
* Python modules
* File handling
* Real-world application development

Each project is added as I learn a new concept.

---

# 📚 Project Progress

### Project 01 — Port Scanner

**Focus:** Networking and socket programming

**Status:** ✅ Completed

### Project 02 — QR Code Generator

**Focus:** Python libraries and GUI development

**Status:** ✅ Completed

### Project 03 — Secure Password Generator

**Focus:** Secure random generation and basic security programming

**Status:** ✅ Completed

### Project 04 — File Organizer

**Focus:** File handling and automation

**Status:** ✅ Completed

### Project 05 — Website Status Checker

**Focus:** HTTP requests and network automation

**Status:** 🔜 Coming Soon

---

# ⚠️ Ethical & Legal Disclaimer

Some projects in this repository involve networking and cybersecurity concepts.

**Only use these tools on systems, devices, networks, and applications that you own or have explicit permission to test.**

The projects are provided for:

* Educational purposes
* Learning Python
* Cybersecurity education
* Personal development
* Authorized security testing

The author is not responsible for misuse of these projects.

---

# 🔐 Security Notice

Never commit sensitive information to this repository.

Do not upload:

* Passwords
* API keys
* Access tokens
* Private keys
* Authentication credentials
* Personal secrets
* `.env` files containing secrets

If a project requires credentials or API keys, use environment variables or another secure configuration method.

---

# 👨‍💻 Author

**Avinash Das Manikpuri**

GitHub: [@Avinash-05-web](https://github.com/Avinash-05-web)

---

## ⭐ Support

If you find this repository useful, consider giving it a ⭐ on GitHub.

More projects coming soon! 🚀
