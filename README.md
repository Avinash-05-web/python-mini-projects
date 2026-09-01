# 🐍 Python Mini Projects

A collection of practical Python projects created while learning Python programming, automation, networking, GUI development, and cybersecurity fundamentals.

The goal of this repository is to build small, useful projects while gradually moving from beginner concepts to more advanced applications.

---

## 📂 Projects

| #  | Project                                                   | Description                                                        | Technologies                         | Status         |
| -- | --------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------ | -------------- |
| 01 | 🔍 [Port Scanner](./01_port_scanner/)                     | Scan TCP ports on an authorized device and identify open ports     | Python, Socket                       | ✅ Completed    |
| 02 | 📱 [QR Code Generator](./02_qr_code_generator/)           | Generate QR codes from URLs or text                               | Python, qrcode, Pillow, Tkinter      | ✅ Completed    |
| 03 | 🔐 [Password Generator](./03_password_generator/)         | Generate secure random passwords                                  | Python, secrets, string              | ✅ Completed    |
| 04 | 📁 [File Organizer](./04_file_organizer/)                 | Automatically organize files by extension                         | Python, OS, shutil                   | ✅ Completed    |
| 05 | 🧾 [Bill Splitter](./05_bill_splitter/)                   | Calculate and split bills between multiple people                 | Python, Tkinter                      | ✅ Completed    |
| 06 | 🌐 [Website Status Checker](./06_website_status_checker/) | Check whether websites are reachable                              | Python, urllib, SSL                  | ✅ Completed    |
| 07 | 🔎 [DNS Lookup Tool](./07_dns_lookup_tool/)               | Look up DNS information for a domain                              | Python, Socket, IP Address           | ✅ Completed    |
| 08 | 📊 [Log Analyzer](./08_log_analyzer/)                     | Analyze logs and identify useful information and security indicators | Python, Rich, Regex                | ✅ Completed    |
| 09 | 🧮 [CLI Calculator](./09_cli_calculator/)                 | Perform mathematical calculations from the command line            | Python, math, datetime               | ✅ Completed    |
| 10 | 🖥️ [System Information Tool](./10_system_information_tool/) | Display useful local system information                         | Python, platform, socket, shutil      | ✅ Completed    |
| 11 | 🔐 File Encryption Tool                                    | Encrypt and decrypt files securely                                 | Python                               | 🔜 Coming Soon |

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

### Run

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
* `secrets`
* `string`

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

A Python automation tool that automatically organizes files into separate folders based on their file extensions.

### Features

* Automatically organize files
* Sort images
* Sort videos
* Sort documents
* Sort audio files
* Sort archives
* Sort programming files
* Create category folders automatically
* Move unknown file types into an `Others` folder
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

The program will ask for the folder path you want to organize.

Example:

```text
Enter the folder path to organize: C:\Users\YourName\Downloads
```

[View File Organizer →](./04_file_organizer/)

---

# 🧾 Project 05 — Bill Splitter

A simple and user-friendly Python GUI application that calculates a restaurant bill, adds a customizable tip, and splits the final bill between multiple people.

### Features

* Calculate total restaurant bill
* Split the bill between multiple people
* Enter appetizer costs
* Enter main course costs
* Enter dessert costs
* Enter drink costs
* Set a custom tip percentage
* Display subtotal
* Calculate tip amount
* Calculate final bill
* Calculate amount per person
* Clear all inputs
* Handle invalid input
* GUI-based interface
* No external packages required

### Technologies

* Python
* Tkinter

### Installation

Go to the project directory:

```bash
cd 05_bill_splitter
```

No additional packages are required.

### Run

```bash
python bill_splitter.py
```

The application will open a graphical window where you can enter the bill details.

### Example

```text
Number of People: 4
Appetizers: 37.89
Main Courses: 57.34
Desserts: 39.39
Drinks: 64.21
Tip Percentage: 25
```

The application calculates:

```text
Subtotal:     ₹198.83
Tip:          ₹49.71
Total Bill:   ₹248.54
Per Person:   ₹62.14
```

[View Bill Splitter →](./05_bill_splitter/)

---

# 🌐 Project 06 — Website Status Checker

A secure and beginner-friendly Python command-line tool that checks whether websites are reachable over HTTP/HTTPS.

The program validates URLs, checks website connectivity, displays HTTP status codes, measures response time, handles redirects, and safely handles common network and SSL errors.

### Features

* Check whether a website is reachable
* Support HTTP and HTTPS
* Validate website URLs
* Automatically add HTTPS when needed
* Display HTTP status codes
* Measure response time
* Handle redirects
* Request timeout protection
* Handle connection errors
* Handle SSL/TLS errors
* No external packages required

### Technologies

* Python
* `urllib`
* `urlparse`
* `ssl`
* `time`

### Installation

Go to the project directory:

```bash
cd 06_website_status_checker
```

No additional packages are required.

### Run

```bash
python website_status_checker.py
```

Example:

```text
Enter website URL: example.com

Checking website...
-------------------------------------------------------
Website : https://example.com
Status  : ONLINE
HTTP Code: 200
Response: 123.45 ms
-------------------------------------------------------
✅ Website is reachable.
=======================================================
```

[View Website Status Checker →](./06_website_status_checker/)

---

# 🔎 Project 07 — DNS Lookup Tool

A simple and secure Python command-line tool that looks up DNS information for a domain.

The program can find IPv4 addresses, IPv6 addresses, and the canonical hostname of a domain using Python's built-in networking modules.

### Features

* Look up DNS information
* Find IPv4 addresses
* Find IPv6 addresses
* Find canonical hostname
* Accept domains with or without HTTP/HTTPS
* Basic domain validation
* Handle invalid domains safely
* No external packages required
* Simple command-line interface

### Technologies

* Python
* `socket`
* `ipaddress`

### Installation

Go to the project directory:

```bash
cd 07_dns_lookup_tool
```

No additional packages are required.

### Run

```bash
python dns_lookup.py
```

Example:

```text
Enter a domain name: google.com

Looking up DNS information for: google.com
Please wait...

============================================================
              DNS LOOKUP RESULTS
============================================================

Domain: google.com

IPv4 Addresses:
  • 142.250.x.x

IPv6 Addresses:
  • 2a00:1450:xxxx::xxxx

Canonical Hostname:
  • google.com

============================================================
```

[View DNS Lookup Tool →](./07_dns_lookup_tool/)

---

# 📊 Project 08 — Log Analyzer

A lightweight Python tool for analyzing Apache/Nginx-style access logs and extracting useful information.

The project analyzes log entries and provides statistics such as IP addresses, HTTP status codes, request methods, requested paths, failed requests, errors, warnings, and basic suspicious request indicators.

### Features

* Analyze Apache/Nginx-style access logs
* Count total log entries
* Identify unique IP addresses
* Find the most active IP addresses
* Analyze HTTP status codes
* Analyze HTTP request methods
* Find frequently requested paths
* Count failed requests
* Detect errors and warnings
* Identify basic suspicious request patterns
* Display suspicious IP addresses
* Clean terminal output using Rich
* Application-level logging
* Read-only log analysis
* Lightweight implementation

### Technologies

* Python 3.8+
* Rich
* Regular Expressions
* `pathlib`
* `collections.Counter`
* `argparse`
* `logging`

### Installation

Go to the project directory:

```bash
cd 08_log_analyzer
```

Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

### Run

Analyze the included sample log:

```bash
python log_analyzer.py sample.log
```

You can also analyze another log file:

```bash
python log_analyzer.py access.log
```

For help:

```bash
python log_analyzer.py --help
```

### Security Analysis

The analyzer can identify basic suspicious request patterns such as:

```text
/admin
/wp-admin
/wp-login
/phpmyadmin
/.env
/etc/passwd
/config
/login
```

These patterns can help identify potentially interesting activity, but a matching request **does not automatically mean that an attack occurred**.

### Security & Privacy

The analyzer processes log files locally and does not upload log contents anywhere.

Real production logs may contain sensitive information such as IP addresses, usernames, URLs, session identifiers, and internal paths.

**Do not upload private production logs to a public GitHub repository.**

Use synthetic or sanitized logs for testing and demonstrations.

[View Log Analyzer →](./08_log_analyzer/)

---

# 🧮 Project 09 — CLI Calculator

A feature-rich command-line calculator built with Python.

The calculator supports multiple mathematical operations, calculation history, saving history to a file, input validation, error handling, and built-in help commands.

### Features

* Addition
* Subtraction
* Multiplication
* Division
* Modulus
* Floor division
* Power
* Square root
* Percentage calculations
* Calculation history
* Save history to a text file
* Clear calculation history
* Built-in help system
* Continuous calculation loop
* Input validation
* Division-by-zero protection
* Supports integers and decimal numbers
* No external packages required

### Technologies

* Python
* `math`
* `datetime`

### Installation

Go to the project directory:

```bash
cd 09_cli_calculator
```

No additional packages are required.

### Run

```bash
python calculator.py
```

### Example

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

### Security

The calculator intentionally does **not** use Python's `eval()` function to process user input.

Instead, supported mathematical operations are handled through dedicated functions, keeping input processing controlled and predictable.

[View CLI Calculator →](./09_cli_calculator/)

---

# 🖥️ Project 10 — System Information Tool

A lightweight and secure Python command-line tool that displays useful information about the local computer system.

The tool collects basic operating system, CPU, memory, disk, network, Python, and runtime information using Python's standard library.

### Features

* Operating system information
* OS version and release
* System architecture
* CPU information
* Logical CPU core count
* RAM information
* Disk usage information
* Hostname
* Local IP address
* Python version
* System uptime
* Current system time
* Human-readable disk sizes
* Read-only operation
* Safe error handling
* Cross-platform design
* No external packages required

### Technologies

* Python
* `platform`
* `socket`
* `os`
* `getpass`
* `shutil`
* `ctypes`
* `datetime`

### Installation

Go to the project directory:

```bash
cd 10_system_information_tool
```

No additional packages are required.

### Run

```bash
python system_info.py
```

Example:

```text
============================================================
          🖥️ SYSTEM INFORMATION TOOL
============================================================

Collecting system information...

============================================================
  🖥️ SYSTEM INFORMATION
============================================================
Operating System   : Windows
OS Version         : ...
OS Release         : 11
Architecture       : AMD64
Processor          : ...
Hostname           : MY-PC
Username           : User
Python Version     : 3.12.5

============================================================
  ⚙️ CPU INFORMATION
============================================================
Logical CPU Cores  : 12

============================================================
  🧠 MEMORY INFORMATION
============================================================
Total RAM          : 15.87 GB
Available RAM      : 7.42 GB
Used RAM           : 8.45 GB
Memory Usage       : 53%

============================================================
  💾 DISK INFORMATION
============================================================

Drive: C:\
  Total : 476.84 GB
  Used  : 245.31 GB
  Free  : 231.53 GB
  Usage : 51.4%

============================================================
  🌐 NETWORK INFORMATION
============================================================
Hostname           : MY-PC
Local IP Address   : 192.168.1.10

============================================================
  ⏱️ RUNTIME INFORMATION
============================================================
Current Time       : 2026-09-01 13:30:00
System Uptime      : 2d 5h 32m 18s

============================================================
✅ Information collection completed.
============================================================
```

### Security & Privacy

The tool operates locally and in a read-only manner.

It does not:

* Modify system settings
* Modify files
* Install software
* Execute shell commands
* Collect passwords
* Collect browser data
* Collect private keys
* Scan other devices
* Upload system information to external servers
* Require administrator/root privileges

[View System Information Tool →](./10_system_information_tool/)

---

# 📈 Learning Progress

This repository represents my hands-on Python learning journey.

## 🐍 Python Fundamentals

* [x] Variables and data types
* [x] User input
* [x] Conditional statements
* [x] Loops
* [x] Lists
* [x] Dictionaries
* [x] Functions
* [x] Modules
* [x] File paths
* [x] Exception handling
* [x] Arithmetic operations
* [x] URL parsing
* [x] Basic HTTP requests
* [x] DNS resolution
* [x] IPv4 and IPv6
* [x] Regular expressions
* [x] Command-line arguments
* [x] File handling
* [x] Data aggregation
* [x] Application logging
* [x] Mathematical operations
* [x] System information APIs
* [x] Cross-platform programming
* [x] Input validation
* [x] Error handling
* [ ] Object-oriented programming
* [ ] APIs
* [ ] Multithreading
* [ ] Advanced Python

## 🌐 Networking & Cybersecurity

* [x] Basic TCP socket programming
* [x] Port scanning fundamentals
* [x] Secure random generation
* [x] Password generation
* [x] HTTP/HTTPS fundamentals
* [x] URL validation
* [x] SSL/TLS basics
* [x] Response-time measurement
* [x] DNS fundamentals
* [x] DNS resolution
* [x] IPv4 and IPv6
* [x] Log analysis
* [x] Basic security indicators
* [x] Suspicious request detection
* [ ] Service detection
* [ ] Banner grabbing
* [ ] DNS record enumeration
* [ ] Network automation
* [ ] Advanced log analysis
* [ ] Security automation
* [ ] Cryptography fundamentals
* [ ] Hashing
* [ ] Encryption

## 🖥️ GUI Development

* [x] Basic Tkinter
* [x] User input fields
* [x] Buttons
* [x] Labels
* [x] Message boxes
* [x] File dialogs
* [x] Event-driven programming
* [ ] Advanced GUI layouts
* [ ] Custom themes
* [ ] GUI application packaging

## ⚙️ Automation

* [x] File organization
* [x] File extension detection
* [x] Directory creation
* [x] File movement
* [ ] Duplicate file detection
* [ ] Automated file monitoring
* [ ] Advanced automation workflows

## 🧮 CLI Applications

* [x] Command-line interfaces
* [x] Menu-driven applications
* [x] Input validation
* [x] Calculation processing
* [x] Error handling
* [x] File-based history
* [x] Built-in help systems
* [x] System information display
* [x] Command-line utilities

---

# 🚀 Upcoming Projects

Some projects planned for this repository:

* 🔐 File Encryption Tool
* 🌐 HTTP Header Checker
* 📊 Password Strength Analyzer
* 📂 Duplicate File Finder
* 🧹 File Cleanup Utility
* 📋 Expense Tracker
* 📊 System Resource Monitor
* 📡 Network Monitoring Tool
* 🔐 Hashing Utility
* 📝 Text Processing Tool
* 🔎 Advanced DNS Lookup Tool
* 🛡️ Security Log Monitor

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

Some projects may require additional Python packages.

Each project contains its own `README.md` with installation and usage instructions.

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
├── 04_file_organizer/
│   ├── file_organizer.py
│   └── README.md
│
├── 05_bill_splitter/
│   ├── bill_splitter.py
│   └── README.md
│
├── 06_website_status_checker/
│   ├── website_status_checker.py
│   └── README.md
│
├── 07_dns_lookup_tool/
│   ├── dns_lookup.py
│   └── README.md
│
├── 08_log_analyzer/
│   ├── log_analyzer.py
│   ├── sample.log
│   ├── requirements.txt
│   └── README.md
│
└── 09_cli_calculator/
    ├── calculator.py
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
* HTTP/HTTPS communication
* DNS resolution
* Log analysis
* Command-line tools
* Mathematical programming
* System programming
* Error handling
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

### Project 05 — Bill Splitter

**Focus:** GUI development, calculations, and user input

**Status:** ✅ Completed

### Project 06 — Website Status Checker

**Focus:** HTTP/HTTPS communication, URL validation, networking, and error handling

**Status:** ✅ Completed

### Project 07 — DNS Lookup Tool

**Focus:** DNS resolution, domain validation, IPv4, IPv6, and networking fundamentals

**Status:** ✅ Completed

### Project 08 — Log Analyzer

**Focus:** Log parsing, data aggregation, command-line tools, and basic security analysis

**Status:** ✅ Completed

### Project 09 — CLI Calculator

**Focus:** Mathematical operations, command-line applications, input validation, and error handling

**Status:** ✅ Completed

### Project 10 — System Information Tool

**Focus:** System information, hardware details, operating system information, networking, and Python system utilities

**Status:** ✅ Completed

### Project 11 — File Encryption Tool

**Focus:** File encryption, cryptography fundamentals, secure file handling, and Python security programming

**Status:** 🔜 Coming Soon

---

# ⚠️ Ethical & Legal Disclaimer

Some projects in this repository involve networking and cybersecurity concepts.

**Only use these tools on systems, devices, networks, applications, and log files that you own or have explicit permission to test or analyze.**

The projects are provided for:

* Educational purposes
* Learning Python
* Cybersecurity education
* Personal development
* Authorized security testing
* Authorized log analysis

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
* Private production logs
* Sensitive system information
* Encryption keys

If a project requires credentials or API keys, use environment variables or another secure configuration method.

---

# 👨‍💻 Author

**Avinash Das Manikpuri**

GitHub: [@Avinash-05-web](https://github.com/Avinash-05-web)

---

## ⭐ Support

If you find this repository useful, consider giving it a ⭐ on GitHub.

More Python and cybersecurity projects coming soon! 🚀

---

## 📌 Current Progress

```text
🐍 Python Mini Projects

01 🔍 Port Scanner
   └── ✅ Completed

02 📱 QR Code Generator
   └── ✅ Completed

03 🔐 Secure Password Generator
   └── ✅ Completed

04 📁 File Organizer
   └── ✅ Completed

05 🧾 Bill Splitter
   └── ✅ Completed

06 🌐 Website Status Checker
   └── ✅ Completed

07 🔎 DNS Lookup Tool
   └── ✅ Completed

08 📊 Log Analyzer
   └── ✅ Completed

09 🧮 CLI Calculator
   └── ✅ Completed

10 🖥️ System Information Tool
   └── ✅ Completed

11 🔐 File Encryption Tool
   └── 🔜 Coming Soon
```

**Keep building. Keep learning. Keep improving. 🚀**
