# 🛡️ Security Audit Tool

A practical **read-only security auditing tool written in Python** that checks a local system for common security issues and provides a security score with detailed findings.

The tool is designed as an educational cybersecurity project to help understand how Python can be used to perform basic system security checks.

---

## 🚀 Features

### 🖥️ System Information
Collects basic local system information:

- Operating system
- OS version
- Hostname
- CPU information
- Python version
- Disk usage
- Current user
- Privilege status

### 🔥 Firewall Audit

Performs a best-effort check of the system firewall.

Supported platforms:

- Windows
- Linux
- macOS

The tool checks whether the firewall appears to be enabled and reports the result.

### 🌐 Listening Port Detection

Scans locally listening TCP ports using native system utilities.

It can identify ports that are currently listening on the machine.

Common security-sensitive ports are highlighted, including:

| Port | Service | Security Concern |
|---:|---|---|
| 21 | FTP | Unencrypted file transfer |
| 23 | Telnet | Unencrypted remote access |
| 25 | SMTP | Mail service exposure |
| 110 | POP3 | Unencrypted email access |
| 139 | NetBIOS | Windows network exposure |
| 445 | SMB | File-sharing exposure |
| 3389 | RDP | Remote desktop exposure |
| 5900 | VNC | Remote desktop exposure |

> A listening port is not automatically a vulnerability. The purpose of this check is to identify services that may deserve further investigation.

### 🔐 Sensitive File Permission Checks

On Unix-like systems, the tool checks permissions of security-sensitive files such as:

- `/etc/passwd`
- `/etc/shadow`
- `/etc/group`
- `/etc/sudoers`
- `/etc/ssh/sshd_config`

It looks for potentially unsafe permissions such as:

- World-writable files
- Group-writable sensitive files
- World-readable password files

### 🔑 SSH Configuration Audit

Checks basic SSH configuration settings, including:

- `PermitRootLogin`
- `PasswordAuthentication`

Potentially risky configurations are reported as warnings.

### 🌱 Environment Variable Audit

Checks environment variable names for potentially sensitive values.

Examples include variables containing:

- `PASSWORD`
- `SECRET`
- `PRIVATE_KEY`
- `ACCESS_TOKEN`
- `API_KEY`

It also checks for empty entries in the system `PATH`.

> The tool checks variable names only. It does not display or collect the actual secret values.

### 📁 Sensitive File Detection

Searches the current directory for commonly sensitive filenames such as:

- `.env`
- `.git-credentials`
- `id_rsa`
- `id_ed25519`
- `id_ecdsa`
- `credentials`
- `credentials.json`
- `config.json`

This can help identify files that may accidentally contain credentials or private configuration.

### 💾 Disk Usage Check

Reports:

- Total disk space
- Used disk space
- Free disk space
- Disk usage percentage

### 🏆 Security Score

The tool calculates an educational security score from:

**0 → 100**

Findings affect the score based on their severity.

| Severity | Score Impact |
|---|---:|
| INFO | 0 |
| PASS | 0 |
| WARNING | -10 |
| CRITICAL | -25 |

The final score is categorized as:

| Score | Rating |
|---:|---|
| 90–100 | Excellent |
| 75–89 | Good |
| 50–74 | Needs Attention |
| 0–49 | High Risk |

> The score is intended for learning and demonstration purposes. It is not a professional security assessment.

### 📊 JSON Report

Audit results can be exported to a JSON file for later analysis.

Example:

```bash
python security_audit.py audit --report security_report.json
````

---

## 🛠️ Technologies Used

This project uses only Python's standard library.

Main modules include:

* `argparse`
* `platform`
* `socket`
* `os`
* `getpass`
* `shutil`
* `subprocess`
* `pathlib`
* `re`
* `json`
* `datetime`

No external Python packages are required.

---

## 📂 Project Structure

```text
13_security_tool/
│
├── security_audit.py
└── README.md
```

---

## ⚙️ Requirements

* Python 3.9+
* Windows, Linux, or macOS
* No external dependencies

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## ▶️ Installation

No package installation is required.

Navigate into the project directory:

```bash
cd 13_security_tool
```

Then run the tool.

---

## 💻 Usage

### Show Help

```bash
python security_audit.py --help
```

This displays all available commands and options.

---

### Run Full Security Audit

```bash
python security_audit.py audit
```

The tool performs the available security checks and displays the results.

Example workflow:

```text
============================================================
              SECURITY AUDIT TOOL
============================================================

[+] System Information
[+] Privilege Check
[+] Firewall Audit
[+] Listening Port Audit
[+] Sensitive File Audit
[+] SSH Configuration Audit
[+] Environment Variable Audit
[+] Sensitive Filename Audit
[+] Disk Usage Check

Security Score: 85/100
Rating: Good
```

The exact results depend on the operating system and current system configuration.

---

### Generate JSON Report

```bash
python security_audit.py audit --report security_report.json
```

This performs the audit and saves the results to:

```text
security_report.json
```

The report can be useful for:

* Keeping audit records
* Comparing results
* Learning JSON handling
* Further analysis
* Building future security dashboards

---

### Run Quick Check

```bash
python security_audit.py quick
```

The quick check performs a smaller set of security checks for a faster overview.

---

### Show Version

```bash
python security_audit.py version
```

---

## 🧪 Example Commands

```bash
# Display help
python security_audit.py --help

# Full audit
python security_audit.py audit

# Full audit + JSON report
python security_audit.py audit --report security_report.json

# Quick security check
python security_audit.py quick

# Show version
python security_audit.py version
```

---

## 🔍 What I Learned

This project helped me practice:

* Python system administration
* Operating system detection
* File permission analysis
* Network port inspection
* Firewall status detection
* SSH security configuration checks
* Environment variable analysis
* Recursive file searching
* Regular expressions
* Command-line interfaces
* JSON report generation
* Error handling
* Cross-platform Python development
* Basic cybersecurity auditing

---

## 🔐 Security & Privacy

This tool is designed to be **read-only**.

It does not:

* Modify firewall settings
* Change system configuration
* Delete files
* Exploit vulnerabilities
* Execute arbitrary user commands
* Collect passwords
* Display environment variable secret values
* Install software
* Require administrator/root privileges for normal operation

The tool may use native operating-system commands such as `netstat`, `ss`, `ufw`, or firewall utilities to retrieve information.

These commands are executed with fixed arguments and are used only for local information gathering.

---

## ⚠️ Limitations

This project is an educational security auditing tool and should not be considered a replacement for professional security software.

Some checks are **best-effort** because operating systems expose security information differently.

Possible limitations include:

* Firewall detection may vary by distribution and configuration.
* Some commands may not exist on every system.
* Some security checks require elevated privileges to provide complete information.
* Listening port detection depends on available system utilities.
* Sensitive filename detection only searches the selected directory.
* SSH configuration checks focus on a small number of settings.
* The security score is a simplified educational metric.

---

## 🧠 Security Concepts

This project demonstrates several important cybersecurity concepts.

### Attack Surface

Every exposed service or listening network port can potentially increase a system's attack surface.

The tool helps identify services that may need investigation.

### Least Privilege

Running systems with unnecessary administrative privileges can increase security risk.

The tool therefore checks the current privilege level.

### Secure Configuration

Security depends not only on software vulnerabilities but also on system configuration.

Examples include:

* Firewall settings
* SSH configuration
* File permissions
* Exposed services

### Secret Management

Credentials and API keys should not be stored carelessly in:

```text
.env
credentials.json
config.json
.git-credentials
```

The tool demonstrates how automated checks can help identify potentially sensitive files.

---

## 🎯 Future Improvements

Possible future improvements include:

* [ ] More detailed firewall detection
* [ ] UDP listening port detection
* [ ] Process-to-port mapping
* [ ] More SSH security checks
* [ ] Windows-specific security checks
* [ ] Linux service auditing
* [ ] macOS security checks
* [ ] Configurable audit rules
* [ ] HTML security reports
* [ ] Security report comparison
* [ ] CVE integration
* [ ] More advanced risk scoring
* [ ] Interactive terminal dashboard

---

## ⚖️ Ethical & Legal Disclaimer

This project is intended for **educational and defensive security purposes only**.

Only use this tool on systems that you own or have explicit permission to audit.

Do not use it to access, inspect, or interfere with systems without authorization.

Understanding cybersecurity also means understanding responsible and ethical use.

---

## 📌 Project Status

**Status:** ✅ Completed

**Project Number:** 13

**Category:** Cybersecurity / System Security

**Difficulty:** Intermediate

---

## 👨‍💻 Author

**Avinash Das Manikpuri**

GitHub:

```text
https://github.com/Avinash-05-web
```

---

## 🐍 Part of Python Mini Projects

This project is part of my **Python Mini Projects** repository, where I build practical projects to improve my Python programming, automation, networking, cybersecurity, and software development skills.

Repository:

```text
https://github.com/Avinash-05-web/python-mini-projects
```

---

⭐ If you find this project useful, consider giving the repository a star!

**Build. Learn. Improve. Repeat. 🚀**
