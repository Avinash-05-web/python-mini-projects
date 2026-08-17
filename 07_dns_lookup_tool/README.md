# 🔎 DNS Lookup Tool

A simple and secure Python command-line tool that looks up DNS information for a domain.

The project uses Python's built-in `socket` module to resolve IPv4 and IPv6 addresses and retrieve the canonical hostname of a domain.

---

## ✨ Features

- 🔎 Look up DNS information for a domain
- 🌐 Find IPv4 addresses
- 🌐 Find IPv6 addresses
- 🖥️ Find the canonical hostname
- 🔗 Accept domains with or without `http://` or `https://`
- 🛡️ Basic domain validation
- ❌ Handle invalid domains safely
- ⚡ Fast DNS resolution using Python's standard library
- 📦 No external Python packages required
- 💻 Simple command-line interface
- ⌨️ Handle interrupted lookups safely

---

## 🛠️ Technologies Used

- Python 3
- `socket`
- `ipaddress`

Both modules are included in Python's standard library.

---

## 📋 Requirements

- Python 3.8 or newer
- Internet connection
- No external packages required

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

Enter the DNS Lookup Tool project:

```bash
cd 07_dns_lookup_tool
```

No additional packages are required.

---

## ▶️ Run the Program

Run:

```bash
python dns_lookup.py
```

On systems using `python3`:

```bash
python3 dns_lookup.py
```

---

## 📖 How to Use

When the program starts, enter the domain you want to look up.

Example:

```text
Enter a domain name: google.com
```

The program will perform a DNS lookup and display available information.

You can also enter a URL:

```text
Enter a domain name: https://github.com
```

The program will remove the protocol and perform the lookup for:

```text
github.com
```

---

## 💻 Example Output

```text
============================================================
                 🔎 DNS LOOKUP TOOL
============================================================

Enter a domain name: example.com

Looking up DNS information for: example.com
Please wait...

============================================================
              DNS LOOKUP RESULTS
============================================================

Domain: example.com

IPv4 Addresses:
  • 93.184.216.34

IPv6 Addresses:
  No IPv6 address found.

Canonical Hostname:
  • example.com

============================================================
```

Actual IP addresses may differ depending on the domain and DNS configuration.

---

## 🌐 DNS Information

### IPv4 Addresses

The tool looks for IPv4 addresses associated with the domain.

Example:

```text
IPv4 Addresses:
  • 142.250.x.x
  • 142.251.x.x
```

IPv4 addresses use the familiar format:

```text
192.168.1.1
```

---

### IPv6 Addresses

The tool also checks for IPv6 addresses.

Example:

```text
IPv6 Addresses:
  • 2607:f8b0:xxxx::xxxx
```

IPv6 addresses are longer than IPv4 addresses and use hexadecimal notation.

---

### Canonical Hostname

The program attempts to retrieve the canonical hostname associated with the domain.

Example:

```text
Canonical Hostname:
  • example.com
```

---

## 🧠 How It Works

The program follows this process:

```text
User enters domain
        ↓
Validate domain
        ↓
Remove HTTP/HTTPS if provided
        ↓
Check for invalid input
        ↓
Perform IPv4 lookup
        ↓
Perform IPv6 lookup
        ↓
Find canonical hostname
        ↓
Display DNS information
```

---

## 🔒 Security Considerations

The project includes basic security and input-validation measures.

### Domain Validation

The program checks that:

* The input is not empty
* The domain does not contain spaces
* The domain is not excessively long
* The input contains a domain separator
* Direct IP addresses are rejected

### No External Packages

The project only uses Python's standard library.

This reduces unnecessary third-party dependencies.

### No DNS Record Modification

The program only performs DNS resolution.

It does not:

* Modify DNS records
* Change DNS settings
* Perform DNS attacks
* Attempt unauthorized access
* Enumerate private DNS zones

---

## 🧪 Example Domains

You can test the program with publicly available domains such as:

```text
example.com
google.com
github.com
python.org
```

---

## ❌ Invalid Input Examples

The program rejects invalid input such as:

```text
192.168.1.1
```

because the project is designed to look up domain names rather than directly resolve IP addresses.

It also rejects:

```text
hello world
```

because spaces are not valid in a normal domain name.

---

## 🔧 Troubleshooting

### Python is not recognized

If you see:

```text
'python' is not recognized as an internal or external command
```

install Python and make sure it is added to your system PATH.

Then restart your terminal and run:

```bash
python --version
```

---

### No DNS information found

If the program cannot resolve a domain, check:

* Your internet connection
* Your DNS configuration
* Whether the domain exists
* Whether the domain is temporarily unavailable

Try another domain:

```text
example.com
```

---

### DNS Resolution Error

DNS resolution can fail for several reasons, including:

* No internet connection
* DNS server problems
* Invalid domain
* Network restrictions
* Temporary DNS failures

The program handles these situations without crashing.

---

## 📂 Project Structure

```text
07_dns_lookup_tool/
│
├── dns_lookup.py
└── README.md
```

---

## 🧠 Python Concepts Used

This project demonstrates:

* Variables
* Functions
* User input
* Conditional statements
* Exception handling
* Lists
* Sets
* String manipulation
* URL processing
* IP address validation
* DNS resolution
* IPv4
* IPv6
* Socket programming
* Python standard library

---

## 🚀 Future Improvements

Planned improvements include:

* [ ] MX record lookup
* [ ] NS record lookup
* [ ] TXT record lookup
* [ ] CNAME lookup
* [ ] SOA record lookup
* [ ] Reverse DNS lookup
* [ ] Multiple domain lookup
* [ ] Save results to a file
* [ ] Export results to CSV
* [ ] GUI interface
* [ ] Custom DNS server selection
* [ ] DNS lookup history
* [ ] Better formatted output

---

## 🎯 Learning Goals

This project was created to practice:

* DNS fundamentals
* Network programming
* Domain validation
* IPv4 and IPv6
* Python's `socket` module
* Exception handling
* Secure input handling
* Building practical command-line networking tools

---

## ⚠️ Ethical & Legal Disclaimer

This tool is intended for educational and legitimate DNS troubleshooting purposes.

Only use networking and DNS tools in accordance with applicable laws, network policies, and terms of service.

The author is not responsible for misuse of this software.

---

## 👨‍💻 Author

**Avinash Das Manikpuri**

GitHub:

[https://github.com/Avinash-05-web](https://github.com/Avinash-05-web)

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

More Python projects coming soon! 🚀
