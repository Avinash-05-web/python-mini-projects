# 📊 Log Analyzer

A lightweight Python tool for analyzing log files and extracting useful information such as IP addresses, HTTP status codes, request methods, requested paths, errors, warnings, and basic security indicators.

This project was built as part of my hands-on Python and cybersecurity learning journey.

The goal is to keep the tool **simple, readable, useful, and easy to extend** while using Python's standard library together with the `Rich` library for a cleaner terminal interface.

---

## ✨ Features

- 📄 Analyze Apache/Nginx-style access logs
- 📊 Count total log entries
- 🌐 Identify unique IP addresses
- 🔝 Find the most active IP addresses
- 📈 Analyze HTTP status codes
- 🔧 Analyze HTTP request methods
- 🔗 Find frequently requested paths
- ❌ Count failed requests
- ⚠️ Detect errors and warnings
- 🛡️ Identify basic suspicious request patterns
- 🔎 Display suspicious IP addresses
- 🎨 Clean and readable terminal output
- 📝 Application-level logging
- 🔒 Read-only log analysis
- ⚡ Lightweight implementation
- 🧩 Uses Python standard-library modules where possible

---

## 🛠️ Technologies Used

- Python 3.8+
- Rich
- Regular Expressions (`re`)
- `pathlib`
- `collections.Counter`
- `argparse`
- `logging`

---

## 📁 Project Structure

```text
06_log_analyzer/
│
├── log_analyzer.py
├── sample.log
├── requirements.txt
├── log_analyzer.log
└── README.md
````

### File Description

| File               | Purpose                        |
| ------------------ | ------------------------------ |
| `log_analyzer.py`  | Main log analysis program      |
| `sample.log`       | Example log file for testing   |
| `requirements.txt` | Python dependency list         |
| `log_analyzer.log` | Application activity/error log |
| `README.md`        | Project documentation          |

> `log_analyzer.log` is generated automatically when the program runs.

---

## ⚙️ Requirements

* Python 3.8 or newer
* pip

Check your Python version:

```bash
python --version
```

Check pip:

```bash
python -m pip --version
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Avinash-05-web/python-mini-projects.git
```

### 2. Enter the project directory

```bash
cd python-mini-projects/06_log_analyzer
```

### 3. Install the required dependency

```bash
python -m pip install -r requirements.txt
```

Or install Rich directly:

```bash
python -m pip install rich
```

---

## 🚀 Usage

The program requires a log file as a command-line argument.

Analyze the included sample log:

```bash
python log_analyzer.py sample.log
```

You can also analyze another log file:

```bash
python log_analyzer.py access.log
```

Or provide a complete file path:

```bash
python log_analyzer.py "C:\path\to\access.log"
```

### Help

To see the available command-line options:

```bash
python log_analyzer.py --help
```

---

## 📊 Example Output

Running:

```bash
python log_analyzer.py sample.log
```

produces a readable report containing sections similar to:

```text
╭──────────────────────────────────────╮
│           📊 LOG ANALYZER            │
│       Security & Log Analysis        │
╰──────────────────────────────────────╯

File: sample.log

       📈 General Statistics
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Metric                ┃ Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ Total Log Entries     │ 15    │
│ Unique IP Addresses   │ 9     │
│ Failed Requests       │ 5     │
│ Errors                │ 1     │
│ Warnings              │ 3     │
└───────────────────────┴───────┘
```

The terminal also displays:

* 🌐 Top IP addresses
* 📊 HTTP status codes
* 🔧 HTTP methods
* 🔗 Most requested paths
* 🛡️ Security indicators
* ⚠️ Suspicious IP addresses

The exact appearance may vary depending on your terminal and Rich version.

---

## 🛡️ Security Analysis

The analyzer performs basic checks for potentially interesting request paths.

Examples include:

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

These requests may sometimes indicate:

* Directory or endpoint enumeration
* Automated scanning
* Attempts to access sensitive files
* Unauthorized access attempts

### ⚠️ Important

A matching request **does not automatically mean that an attack occurred**.

For example:

```text
GET /login
```

is completely normal for many websites.

The suspicious-request detection in this project is intentionally simple and is meant for **learning and basic log analysis**, not professional threat detection.

---

## 🔒 Security & Privacy

The analyzer is designed to process logs locally and in a read-only manner.

It:

* Does not modify the analyzed log file
* Does not upload logs anywhere
* Does not send log contents over the network
* Processes the selected file locally
* Handles invalid text safely using replacement characters
* Records application errors separately

### Protect Sensitive Logs

Real production logs may contain sensitive information such as:

* IP addresses
* Usernames
* URLs
* Session identifiers
* Internal paths
* Application information

**Do not upload private production logs to a public GitHub repository.**

Use synthetic or sanitized logs when testing or demonstrating the project publicly.

---

## 🧠 What I Learned

This project helped me practice:

* Python file handling
* Regular expressions
* Command-line arguments
* Python classes
* `Counter`
* Log parsing
* Error handling
* Application logging
* Data aggregation
* Basic security analysis
* Terminal interfaces
* Writing reusable Python code

---

## 🔮 Future Improvements

Possible future versions may include:

* [ ] CSV report generation
* [ ] JSON report generation
* [ ] Date and time filtering
* [ ] Custom status-code filtering
* [ ] Configurable suspicious patterns
* [ ] Failed-login detection
* [ ] Request-rate analysis
* [ ] Multiple log-format support
* [ ] Exportable security reports
* [ ] Interactive charts
* [ ] GUI interface

---

## ⚠️ Ethical & Legal Disclaimer

This project is intended for:

* 🎓 Educational purposes
* 🐍 Python learning
* 🔐 Cybersecurity education
* 📊 Log analysis
* 🧪 Authorized security testing
* 💻 Personal development

Only analyze log files that you own or have explicit permission to access.

The author is not responsible for misuse of this project.

---

## 👨‍💻 Author

**Avinash Das Manikpuri**

GitHub: [@Avinash-05-web](https://github.com/Avinash-05-web)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

More Python and cybersecurity projects coming soon! 🚀
