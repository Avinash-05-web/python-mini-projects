# 🐍 Python Mini Projects

A collection of practical Python projects created while learning Python programming, automation, networking, GUI development, CLI applications, cybersecurity, cryptography, and file security.

The goal of this repository is to build small, useful, and practical projects while gradually moving from beginner Python concepts to more advanced real-world applications.

---

## 📂 Projects

| # | Project | Description | Technologies | Status |
|---|---|---|---|---|
| 01 | 🔎 [Port Scanner](./01_port_scanner/) | Scan TCP ports on an authorized target | Python, Socket | ✅ Completed |
| 02 | 📱 [QR Code Generator](./02_qr_code_generator/) | Generate QR codes from text or URLs | Python, qrcode, Pillow, Tkinter | ✅ Completed |
| 03 | 🔐 [Password Generator](./03_password_generator/) | Generate secure customizable passwords | Python, secrets, string | ✅ Completed |
| 04 | 📁 [File Organizer](./04_file_organizer/) | Automatically organize files by extension | Python, os, shutil | ✅ Completed |
| 05 | 💰 [Bill Splitter](./05_bill_splitter/) | Calculate and split bills between people | Python, Tkinter | ✅ Completed |
| 06 | 🌐 [Website Status Checker](./06_website_status_checker/) | Check website availability and HTTP status | Python, urllib, socket, ssl | ✅ Completed |
| 07 | 🔍 [DNS Lookup Tool](./07_dns_lookup_tool/) | Perform IPv4, IPv6 and hostname lookups | Python, Socket, IPAddress | ✅ Completed |
| 08 | 📊 [Log Analyzer](./08_log_analyzer/) | Analyze web server logs and detect suspicious patterns | Python, Regex, Rich, Counter | ✅ Completed |
| 09 | 🧮 [CLI Calculator](./09_cli_calculator/) | Feature-rich command-line calculator with history | Python, argparse, math | ✅ Completed |
| 10 | 🖥️ [System Information Tool](./10_system_information_tool/) | Display useful local system information | Python, platform, socket, shutil | ✅ Completed |
| 11 | 🔐 [File Encryption Tool](./11_file_encryption_tool/) | Encrypt and decrypt files securely | Python, cryptography, Scrypt, AES-GCM | ✅ Completed |
| 12 | 🔎 [Hashing Utility](./12_hashing_utility/) | Generate and verify file hashes and integrity manifests | Python, hashlib, pathlib, argparse | ✅ Completed |
| 13 | 🛡️ Security Tool | Practical security-focused Python utility | Python, Cybersecurity | 🚧 Coming Soon |

---

# 📌 Project Details

## 01 — 🔎 Port Scanner

A TCP port scanner built using Python's `socket` module.

### Features

- Scan individual TCP ports
- Check whether a port is open or closed
- Accept target IP addresses
- Simple command-line interface
- Fast and lightweight

### Technologies

- Python
- Socket

### Security

This project should only be used against systems and networks that you own or have explicit permission to test.

---

## 02 — 📱 QR Code Generator

A QR code generator capable of converting URLs and text into QR codes.

### Features

- Generate QR codes from URLs
- Generate QR codes from text
- High error correction
- Save generated QR codes
- GUI interface
- Simple user interaction

### Technologies

- Python
- `qrcode`
- Pillow
- Tkinter

---

## 03 — 🔐 Password Generator

A customizable password generator designed to create strong random passwords.

### Features

- Secure random password generation
- Custom password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Password strength detection

### Technologies

- Python
- `secrets`
- `string`

### Security

The project uses Python's `secrets` module instead of ordinary pseudo-random functions for password generation.

---

## 04 — 📁 File Organizer

An automation tool that organizes files into folders based on their file extensions.

### Features

- Detect file extensions
- Create folders automatically
- Move files into appropriate folders
- Reduce folder clutter
- Automate repetitive file organization

### Technologies

- Python
- `os`
- `shutil`

### Example

```text
Downloads/
│
├── photo.jpg
├── document.pdf
├── song.mp3
└── video.mp4
````

Becomes:

```text
Downloads/
│
├── Images/
│   └── photo.jpg
│
├── Documents/
│   └── document.pdf
│
├── Audio/
│   └── song.mp3
│
└── Videos/
    └── video.mp4
```

---

## 05 — 💰 Bill Splitter

A graphical bill-splitting application built with Tkinter.

### Features

* Enter food expenses
* Add appetizers
* Add main courses
* Add desserts
* Add drinks
* Calculate tips
* Specify number of people
* Calculate total bill
* Calculate per-person amount
* GUI-based interface

### Technologies

* Python
* Tkinter

---

## 06 — 🌐 Website Status Checker

A Python utility for checking whether websites are reachable and responding correctly.

### Features

* HTTP/HTTPS checking
* URL validation
* HTTP status code detection
* Response time measurement
* Redirect detection
* SSL error handling
* Network error handling

### Technologies

* Python
* `urllib`
* `socket`
* `ssl`

### Example

```text
Website: https://example.com

Status: Online
HTTP Status: 200
Response Time: ...
```

---

## 07 — 🔍 DNS Lookup Tool

A DNS lookup utility for retrieving basic domain and hostname information.

### Features

* IPv4 lookup
* IPv6 lookup
* Canonical hostname lookup
* Hostname resolution
* IP address validation
* Error handling

### Technologies

* Python
* `socket`
* `ipaddress`

---

## 08 — 📊 Log Analyzer

An Apache/Nginx-style web server log analyzer designed to help understand server activity and identify suspicious request patterns.

### Features

* Analyze web server logs
* Count total requests
* Identify HTTP status codes
* Analyze IP addresses
* Detect suspicious request patterns
* Detect common attack indicators
* Command-line interface
* Rich terminal output
* Logging support
* Regular expression-based parsing

### Technologies

* Python
* Regex
* `pathlib`
* `Counter`
* `argparse`
* `logging`
* Rich

### Security Concepts

* Log analysis
* Threat detection
* Suspicious request detection
* HTTP status analysis
* Basic security monitoring

---

## 09 — 🧮 CLI Calculator

A feature-rich command-line calculator built using Python.

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
* Save history
* Clear history
* Help menu
* Input validation
* Error handling

### Security

The calculator intentionally avoids:

```python
eval()
```

User input is processed using controlled operations instead of executing arbitrary Python expressions.

### Technologies

* Python
* `argparse`
* `math`
* File handling

---

## 10 — 🖥️ System Information Tool

A read-only local system information utility that displays useful information about the current computer.

### Features

* Operating system information
* OS version
* Hostname
* CPU information
* RAM information
* Disk information
* Network information
* Python version
* User information
* System uptime
* Current date and time

### Technologies

* Python
* `platform`
* `socket`
* `os`
* `getpass`
* `shutil`
* `ctypes`
* `datetime`

### Security

The tool is designed to be read-only.

It does not:

* Modify system configuration
* Execute shell commands
* Require administrator privileges
* Install software
* Delete files

---

# 11 — 🔐 File Encryption Tool

A command-line file encryption and decryption tool using modern authenticated cryptography.

This project represents a major step into cybersecurity and cryptography.

### Features

* 🔒 Encrypt files
* 🔓 Decrypt files
* 🔑 Password-based encryption
* 🧂 Random salts
* 🧠 Scrypt key derivation
* 🔐 AES-256-GCM encryption
* 🛡️ Authentication tags
* 🎲 Unique nonce material per encrypted chunk
* 📦 Chunked file processing
* 💾 Atomic output replacement
* 🧹 Temporary file cleanup
* ❌ Does not delete original files
* ❌ Does not store passwords
* ❌ Does not use `eval()`
* ❌ Does not execute shell commands

### Technologies

* Python
* `cryptography`
* AES-256-GCM
* Scrypt
* `argparse`
* `getpass`
* `secrets`
* `pathlib`

### Basic Usage

Encrypt:

```bash
python file_encryptor.py encrypt secret.txt
```

Decrypt:

```bash
python file_encryptor.py decrypt secret.txt.enc
```

Custom output:

```bash
python file_encryptor.py encrypt secret.txt -o protected.enc
```

```bash
python file_encryptor.py decrypt protected.enc -o recovered.txt
```

### Security Note

The password is not stored.

If the password is lost, there is no password recovery mechanism.

This project is intended for educational purposes and has not undergone a formal security audit.

---

# 12 — 🔎 Hashing Utility

An advanced command-line file hashing and integrity verification utility.

The project goes beyond simply generating a hash by supporting file verification and directory-wide checksum manifests.

### Features

* 🔎 Generate file hashes
* 🔐 SHA-256
* 🔐 SHA-512
* 🔐 SHA-1
* 🔐 MD5
* 📦 Chunked file processing
* ⚡ Large-file support
* 📊 Hashing progress
* 📁 Directory scanning
* 📝 Checksum manifest generation
* ✅ Individual file verification
* 🔍 Manifest verification
* 🚫 Detect modified files
* 🚫 Detect missing files
* 🖥️ Command-line interface
* ❌ No external dependencies
* ❌ No shell commands
* ❌ No `eval()`

### Technologies

* Python
* `hashlib`
* `pathlib`
* `argparse`
* `sys`
* Type hints

### Basic Usage

Generate SHA-256:

```bash
python hashing_utility.py hash test.txt
```

Generate SHA-512:

```bash
python hashing_utility.py hash test.txt --algorithm sha512
```

Show progress:

```bash
python hashing_utility.py hash large_file.zip --progress
```

Verify a file:

```bash
python hashing_utility.py verify test.txt YOUR_HASH_HERE
```

Generate a directory manifest:

```bash
python hashing_utility.py manifest test_folder
```

Verify a manifest:

```bash
python hashing_utility.py check-manifest checksums.sha256
```

### Integrity Workflow

```text
File
 ↓
SHA-256
 ↓
Known Hash
 ↓
Compare Later
 ↓
Integrity Verification
```

For directories:

```text
Directory
     ↓
Hash Every File
     ↓
Generate Manifest
     ↓
Store Hashes
     ↓
Verify Later
     ↓
Detect Changes
```

### Security Note

SHA-256 and SHA-512 are recommended for new general-purpose integrity checks.

MD5 and SHA-1 are included mainly for compatibility and educational purposes because they have known collision weaknesses.

---

# 13 — 🛡️ Security Tool

🚧 **Coming Soon**

The next project will continue expanding the cybersecurity side of the repository.

The exact project will be selected based on the learning progression and will introduce additional practical security concepts.

Possible areas include:

* Network security
* File integrity
* HTTP security
* Password security
* System monitoring
* Security automation
* Defensive analysis

---

# 🧠 Learning Progress

## 🐍 Python Fundamentals

* [x] Variables and data types
* [x] Conditions
* [x] Loops
* [x] Functions
* [x] Exception handling
* [x] File handling
* [x] Modules
* [x] Command-line arguments
* [x] Working with paths
* [x] Data structures
* [x] Regular expressions
* [x] Binary data handling
* [x] Type hints
* [x] CLI architecture
* [x] Exit codes

---

## 🌐 Networking & Cybersecurity

* [x] TCP connections
* [x] Port scanning
* [x] DNS resolution
* [x] HTTP status checking
* [x] SSL/TLS error handling
* [x] Web server log analysis
* [x] Suspicious request detection
* [x] Password generation
* [x] Password security concepts
* [x] Cryptographic key derivation
* [x] Authenticated encryption
* [x] AES-256-GCM
* [x] Scrypt
* [x] File encryption
* [x] Cryptographic hashing
* [x] SHA-256
* [x] SHA-512
* [x] File integrity verification
* [x] Checksum manifests

---

## 🖥️ GUI Development

* [x] Tkinter basics
* [x] GUI forms
* [x] User input handling
* [x] Buttons and events
* [x] GUI calculations
* [x] QR code generation GUI
* [x] Bill splitting GUI

---

## ⚙️ Automation

* [x] File organization
* [x] File system operations
* [x] Automated folder creation
* [x] File movement
* [x] Log processing
* [x] System information collection
* [x] Automated integrity checking

---

## 💻 CLI Applications

* [x] Command-line input
* [x] `argparse`
* [x] Subcommands
* [x] Command-line validation
* [x] CLI error handling
* [x] Help menus
* [x] Calculation history
* [x] File hashing commands
* [x] File verification commands
* [x] Directory manifest commands
* [x] Manifest verification

---

## 🔐 Cryptography & Data Security

* [x] Secure random generation
* [x] Password security
* [x] Salts
* [x] Key derivation
* [x] Scrypt
* [x] AES-256
* [x] AES-GCM
* [x] Authentication tags
* [x] Nonce management
* [x] Encrypted file formats
* [x] Cryptographic hashing
* [x] SHA-256
* [x] SHA-512
* [x] File integrity
* [x] Checksum verification

---

# 🚀 Upcoming Projects

The repository will continue expanding with progressively more advanced projects.

Possible future projects include:

* 🛡️ Security-focused Python utility
* 🌐 HTTP Header Security Checker
* 🔐 Secure Notes Application
* 📡 Network Service Checker
* 🛡️ Password Strength Analyzer
* 📋 System Resource Monitor
* 📊 Security Log Dashboard
* 🔍 File Integrity Monitor
* 🌐 Network Monitoring Tool
* 🔑 Security Automation Tools

The exact order may change as the learning path develops.

---

# 📦 General Requirements

Most projects require:

* Python 3.9+
* Windows, Linux, or macOS

Some projects require additional Python packages.

Always check the individual project's `README.md` and `requirements.txt`.

Project 12 currently requires **no external packages**.

---

# 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/Avinash-05-web/python-mini-projects.git
```

Enter the repository:

```bash
cd python-mini-projects
```

Each project is independent.

For example:

```bash
cd 12_hashing_utility
```

Then run:

```bash
python hashing_utility.py --help
```

---

# 📂 Repository Structure

```text
python-mini-projects/
│
├── 01_port_scanner/
│   ├── port_scanner.py
│   └── README.md
│
├── 02_qr_code_generator/
│   ├── qr_code_generator.py
│   ├── requirements.txt
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
│   ├── requirements.txt
│   └── README.md
│
├── 09_cli_calculator/
│   ├── calculator.py
│   └── README.md
│
├── 10_system_information_tool/
│   ├── system_information.py
│   └── README.md
│
├── 11_file_encryption_tool/
│   ├── file_encryptor.py
│   ├── requirements.txt
│   └── README.md
│
├── 12_hashing_utility/
│   ├── hashing_utility.py
│   └── README.md
│
├── 13_security_tool/
│   └── Coming Soon
│
└── README.md
```

---

# 🎯 Repository Purpose

The purpose of this repository is to learn Python by building practical projects instead of only studying theory.

Each project focuses on a specific set of programming concepts.

The difficulty gradually increases as new projects are added.

```text
Beginner
   │
   ▼
Python Fundamentals
   │
   ▼
Automation
   │
   ▼
Networking
   │
   ▼
GUI Applications
   │
   ▼
CLI Applications
   │
   ▼
Cybersecurity
   │
   ▼
Cryptography
   │
   ▼
File Security
   │
   ▼
Advanced Python Projects
```

---

# 🧪 Development Workflow

Each project follows a practical learning workflow:

```text
1. Choose a practical problem
        ↓
2. Learn the required concepts
        ↓
3. Build the project
        ↓
4. Test the project
        ↓
5. Handle errors
        ↓
6. Improve security and usability
        ↓
7. Document the project
        ↓
8. Add it to GitHub
        ↓
9. Move to the next project
```

---

# 🔐 Security Philosophy

As the projects become more advanced, security is treated as an important part of development.

The projects aim to practice:

* Input validation
* Error handling
* Safe file operations
* Secure random generation
* Password security
* Authentication
* Encryption
* Data integrity
* Hashing
* Safe command-line handling
* Avoiding dangerous dynamic execution

Security features are introduced gradually as the repository progresses.

---

# ⚠️ Ethical & Legal Disclaimer

Some projects in this repository involve networking and cybersecurity concepts.

These projects are intended for:

* Education
* Personal learning
* Authorized security testing
* Defensive security research
* Local lab environments
* Systems you own or have permission to test

Do **not** use these tools against systems, networks, accounts, or data without authorization.

You are responsible for following applicable laws, regulations, and organizational policies.

---

# 🛡️ Security Notice

Never commit sensitive information to this repository.

Do not upload:

```text
Passwords
API Keys
Access Tokens
Private Keys
SSH Keys
Credentials
Personal Secrets
Production Configuration Files
```

Before committing code, check that no secrets are included.

If a credential is accidentally exposed, revoke or rotate it immediately.

---

# 🤝 Contributing

This repository is primarily a personal learning project, but suggestions and educational improvements are welcome.

If you find:

* A bug
* A security issue
* A documentation problem
* A possible improvement
* A better implementation approach

Feel free to open an issue or submit a pull request.

---

# ⭐ Support

If you find this repository useful:

* ⭐ Star the repository
* 🍴 Fork the repository
* 📚 Explore the projects
* 💡 Suggest improvements
* 🧑‍💻 Use the projects for learning

---

# 👨‍💻 Author

**Avinash Das Manikpuri**

GitHub:

[https://github.com/Avinash-05-web](https://github.com/Avinash-05-web)

Repository:

[https://github.com/Avinash-05-web/python-mini-projects](https://github.com/Avinash-05-web/python-mini-projects)

---

# 📈 Current Learning Journey

This repository represents a continuous learning journey through Python.

Starting from simple projects such as:

```text
Port Scanner
QR Code Generator
Password Generator
```

and progressing toward:

```text
Networking
Automation
System Information
Log Analysis
CLI Applications
Cryptography
File Encryption
File Hashing
Integrity Verification
```

The goal is to keep improving one project at a time.

---

# 📊 Project Progress

Current progress:

```text
Completed Projects: 12
Next Project: 13
```

Progress:

```text
01 ✅
02 ✅
03 ✅
04 ✅
05 ✅
06 ✅
07 ✅
08 ✅
09 ✅
10 ✅
11 ✅
12 ✅
13 🚧
```

---

# 🏆 Current Milestone

## 12 Projects Completed 🎉

```text
🐍 Python
      +
⚙️ Automation
      +
🌐 Networking
      +
🖥️ GUI Development
      +
💻 CLI Applications
      +
📊 Log Analysis
      +
🔐 Cybersecurity
      +
🛡️ Cryptography
      +
🔎 File Integrity
```

**12 projects completed.**

**Project 13 is next.** 🚀

---

# 🐍 Build. Learn. Improve. Repeat.

> "The best way to learn programming is to build."

This repository is built one project at a time, with each project introducing new concepts and improving practical Python skills.

**Project 12 — Hashing Utility 🔎**

**Next → Project 13 — Security Tool 🛡️**
