# 🖥️ System Information Tool

A lightweight and secure Python command-line tool that displays useful information about the local computer system.

The tool collects basic operating system, CPU, memory, disk, network, Python, and runtime information using Python's standard library.

This project was built as part of my hands-on Python learning journey.

The main goal is to practice system-level Python programming while keeping the application **read-only, safe, lightweight, and beginner-friendly**.

---

## ✨ Features

- 🖥️ Operating system information
- 📦 OS version and release
- 🏗️ System architecture
- ⚙️ CPU information
- 🔢 Logical CPU core count
- 🧠 RAM information
- 💾 Disk usage information
- 🌐 Hostname
- 📡 Local IP address
- 🐍 Python version
- ⏱️ System uptime
- 🕐 Current system time
- 📊 Human-readable disk sizes
- 🛡️ Read-only operation
- ❌ Safe error handling
- ⌨️ Keyboard interrupt handling
- 📦 No external Python packages required
- 💻 Cross-platform design

---

## 🛠️ Technologies Used

- Python 3.8+
- `platform`
- `socket`
- `os`
- `getpass`
- `shutil`
- `ctypes`
- `datetime`

All modules are included in Python's standard library.

No external packages are required.

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

Enter the System Information Tool project:

```bash
cd 10_system_information_tool
```

No additional packages are required.

---

## ▶️ Run the Program

Run:

```bash
python system_info.py
```

On systems using `python3`:

```bash
python3 system_info.py
```

---

## 💻 Example Output

The exact information will depend on the operating system and hardware.

Example:

```text
============================================================
          🖥️ SYSTEM INFORMATION
============================================================

Collecting system information...

============================================================
  🖥️ SYSTEM INFORMATION
============================================================
Operating System   : Windows
OS Version         : 10.0.26100
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

> Actual values will vary depending on your computer.

---

## 🖥️ Information Collected

### Operating System

The tool displays:

* Operating system name
* OS version
* OS release
* System architecture
* Processor information

Example:

```text
Operating System   : Linux
OS Version         : ...
OS Release         : ...
Architecture       : x86_64
Processor          : ...
```

---

### ⚙️ CPU Information

The application reports the number of logical CPU cores available to Python.

Example:

```text
Logical CPU Cores  : 8
```

This can be useful for understanding the processing capacity available to applications.

---

### 🧠 Memory Information

The program attempts to display:

* Total RAM
* Available RAM
* Used RAM
* Memory usage percentage

Example:

```text
Total RAM          : 16.00 GB
Available RAM      : 8.20 GB
Used RAM           : 7.80 GB
Memory Usage       : 48.8%
```

Memory detection uses platform-specific functionality where available and falls back to other supported methods.

---

### 💾 Disk Information

The tool displays disk usage information including:

* Total storage
* Used storage
* Free storage
* Storage usage percentage

Example:

```text
Drive: C:\
  Total : 476.84 GB
  Used  : 245.31 GB
  Free  : 231.53 GB
  Usage : 51.4%
```

The program uses Python's `shutil.disk_usage()` function.

---

### 🌐 Network Information

The program displays basic local network information:

* Hostname
* Local IP address

Example:

```text
Hostname           : MY-PC
Local IP Address   : 192.168.1.10
```

The tool does not perform network scanning.

---

### 🐍 Python Information

The installed Python version is displayed.

Example:

```text
Python Version     : 3.12.5
```

---

### ⏱️ Runtime Information

The tool attempts to display:

* Current local date and time
* System uptime

Example:

```text
Current Time       : 2026-09-01 13:30:00
System Uptime      : 2d 5h 32m 18s
```

Uptime detection depends on the operating system.

---

## 🔒 Security & Privacy

This project is designed to operate locally and in a read-only manner.

The program:

* Does not modify system settings
* Does not modify files
* Does not install software
* Does not execute shell commands
* Does not collect passwords
* Does not collect browser data
* Does not collect private keys
* Does not scan other devices
* Does not upload information to external servers
* Does not require administrator/root privileges

The information displayed is collected from the local operating system.

---

## 🛡️ Safe Design

The application avoids potentially dangerous system operations.

It does not use:

```python
os.system()
```

or:

```python
subprocess
```

to execute arbitrary operating-system commands.

Instead, it uses Python's standard library APIs to retrieve system information.

This makes the application safer and easier to understand.

---

## 🌍 Cross-Platform Support

The program is designed to work across common operating systems.

### Windows

Uses Windows-specific functionality where required, such as:

* RAM detection
* System uptime
* Drive detection

### Linux

Uses Linux system information such as:

```text
/proc/meminfo
/proc/uptime
```

when available.

### macOS

Uses supported Python standard-library functionality for basic system and disk information.

Some fields may display:

```text
Not available
```

depending on the operating system.

This is expected behavior and prevents the application from failing when a particular system API is unavailable.

---

## ❌ Error Handling

The program includes error handling for situations such as:

* Missing system information
* Permission errors
* Unsupported operating-system features
* Invalid system data
* Disk access errors
* Keyboard interruption
* Unexpected runtime errors

The application attempts to continue safely instead of crashing whenever possible.

---

## 📂 Project Structure

```text
10_system_information_tool/
│
├── system_info.py
└── README.md
```

---

## 🧠 Python Concepts Used

This project demonstrates:

* Variables
* Functions
* Dictionaries
* Loops
* Conditional statements
* Exception handling
* String formatting
* File handling
* Operating-system interaction
* System information APIs
* Network information
* Date and time handling
* Cross-platform programming
* Standard-library modules
* Command-line applications

---

## 🔧 How It Works

The program follows this process:

```text
Start Program
      ↓
Collect OS Information
      ↓
Collect CPU Information
      ↓
Collect Memory Information
      ↓
Collect Disk Information
      ↓
Collect Network Information
      ↓
Collect Runtime Information
      ↓
Display Results
      ↓
Exit Safely
```

---

## 🧪 Testing

You can test the program by running:

```bash
python system_info.py
```

Then verify that it displays information for:

```text
✓ Operating System
✓ Architecture
✓ CPU
✓ Memory
✓ Disk
✓ Hostname
✓ Local IP
✓ Python Version
✓ System Uptime
✓ Current Time
```

You can also test the error handling by pressing:

```text
Ctrl + C
```

The program should exit gracefully.

---

## 🚀 Future Improvements

Possible future improvements include:

* [ ] GUI interface
* [ ] Network adapter information
* [ ] Battery information
* [ ] GPU information
* [ ] Running process information
* [ ] Boot time detection
* [ ] Detailed CPU information
* [ ] Temperature monitoring
* [ ] Export system information to TXT
* [ ] Export system information to JSON
* [ ] Export system information to CSV
* [ ] System health summary
* [ ] Interactive menu
* [ ] Cross-platform hardware detection improvements

---

## 🎯 Learning Goals

This project was created to practice:

* Python system programming
* Operating-system information
* Hardware information
* Disk management APIs
* Network information
* Python standard-library modules
* Exception handling
* Cross-platform programming
* Building useful command-line utilities
* Writing safe read-only system tools

---

## ⚠️ Ethical & Legal Disclaimer

This project is intended for educational and legitimate system-information purposes.

Only use system-information tools on computers and systems that you own or have explicit permission to inspect.

The author is not responsible for misuse of this project.

---

## 👨‍💻 Author

**Avinash Das Manikpuri**

GitHub:

[https://github.com/Avinash-05-web](https://github.com/Avinash-05-web)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

More Python and cybersecurity projects coming soon! 🚀
