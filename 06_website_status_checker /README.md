# 🌐 Website Status Checker

A secure and beginner-friendly Python command-line tool that checks whether websites are reachable over HTTP/HTTPS.

The tool validates the URL, checks the website connection, displays the HTTP status code, measures response time, and safely handles common network and SSL errors.

---

## ✨ Features

- 🌐 Check whether a website is reachable
- 🔗 Supports HTTP and HTTPS
- 🔒 Secure HTTPS certificate verification
- ⏱️ Measure website response time
- 📊 Display HTTP status codes
- 🔄 Handle website redirects
- 🛡️ Validate URLs before making requests
- ⏰ Request timeout protection
- ❌ Handle connection errors safely
- 🔐 Handle SSL/TLS errors
- 💻 Simple command-line interface
- 📦 No external Python packages required

---

## 🛠️ Technologies Used

- Python 3
- `urllib`
- `urlparse`
- `ssl`
- `time`

All modules used by this project are included in Python's standard library.

---

## 📋 Requirements

- Python 3.8 or newer
- No external Python packages required
- Internet connection

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

Enter the Website Status Checker project:

```bash
cd 06_website_status_checker
```

No additional packages are required.

---

## ▶️ Run the Program

Run:

```bash
python website_status_checker.py
```

On systems using `python3`:

```bash
python3 website_status_checker.py
```

---

## 📖 How to Use

When the program starts, enter the website you want to check.

You can enter a complete URL:

```text
https://example.com
```

Or simply enter a domain:

```text
example.com
```

The program automatically adds `https://` when a scheme is not provided.

---

## 💻 Example

Run the program:

```text
=======================================================
          🌐 WEBSITE STATUS CHECKER
=======================================================

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

---

## 📊 Status Types

The program can report different statuses depending on the result.

### 🟢 ONLINE

The website responded successfully.

Example:

```text
Status: ONLINE
HTTP Code: 200
```

### 🟡 REACHABLE

The server was reached but returned an HTTP error status.

For example:

```text
Status: REACHABLE
HTTP Code: 404
```

A `404` does not necessarily mean the entire website is offline. It means the requested resource was not found.

### 🔴 UNREACHABLE

The program could not establish a connection to the website.

### ⏱️ TIMEOUT

The website did not respond within the configured timeout period.

The current timeout is:

```text
10 seconds
```

### 🔒 SSL ERROR

The HTTPS connection encountered an SSL/TLS certificate or connection problem.

### ❌ ERROR

An unexpected error occurred while checking the website.

---

## 📈 HTTP Status Codes

The program displays the HTTP response status code when available.

Common examples include:

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 301  | Permanent Redirect    |
| 302  | Temporary Redirect    |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 500  | Internal Server Error |
| 502  | Bad Gateway           |
| 503  | Service Unavailable   |

An HTTP error code does not automatically mean that a website is completely offline.

---

## ⏱️ Response Time

The program measures approximately how long it takes to receive a response.

Example:

```text
Response: 123.45 ms
```

Lower response times generally indicate a faster response from the server, although response time can vary depending on:

* Internet connection
* Geographic location
* Server load
* Network congestion
* DNS resolution
* Routing

---

## 🔒 Security

This project is designed with basic security considerations.

### URL Validation

The program only accepts:

```text
http://
https://
```

Other protocols are rejected.

### HTTPS Verification

HTTPS connections use Python's default SSL context, which performs normal certificate verification.

### Timeout Protection

Requests have a timeout of:

```text
10 seconds
```

This prevents the program from waiting indefinitely for a server response.

### No Downloaded Code Execution

The program only checks the HTTP/HTTPS response. It does not execute JavaScript, downloaded programs, or webpage code.

---

## 🧠 Python Concepts Used

This project demonstrates:

* Variables
* Functions
* User input
* Conditional statements
* Exception handling
* Dictionaries
* String manipulation
* URL parsing
* HTTP requests
* SSL/TLS concepts
* Response timing
* Error handling
* Python standard library
* Network programming fundamentals

---

## 🔧 How It Works

The program follows this process:

```text
User enters website
        ↓
Validate URL
        ↓
Add HTTPS if needed
        ↓
Create HTTP request
        ↓
Establish secure connection
        ↓
Wait for server response
        ↓
Measure response time
        ↓
Read HTTP status code
        ↓
Display result
```

---

## 📂 Project Structure

```text
06_website_status_checker/
│
├── website_status_checker.py
└── README.md
```

---

## 🧪 Example Tests

You can safely test the program with websites you are authorized to access.

Examples:

```text
https://example.com
https://github.com
https://google.com
```

You can also test without specifying the protocol:

```text
example.com
github.com
google.com
```

The program will automatically add:

```text
https://
```

---

## 🔧 Troubleshooting

### Python is not recognized

If you see:

```text
'python' is not recognized as an internal or external command
```

install Python and make sure it is added to your system PATH.

Then restart the terminal and check:

```bash
python --version
```

---

### No Internet Connection

The program requires an active internet connection to check external websites.

If your computer is offline, websites will generally be reported as unreachable.

---

### Website Returns 403

A website may return:

```text
HTTP Code: 403
```

This means the server understood the request but refused access.

It does not necessarily mean the website is offline.

---

### Website Returns 404

A response such as:

```text
HTTP Code: 404
```

means the requested resource was not found.

The server itself may still be online.

---

## 🚀 Future Improvements

Planned improvements include:

* [ ] Check multiple websites at once
* [ ] Read websites from a text file
* [ ] Generate a status summary
* [ ] Add response-time ratings
* [ ] Add colored terminal output
* [ ] Save results to a file
* [ ] Export results as CSV
* [ ] Continuous website monitoring
* [ ] Automatic retry system
* [ ] GUI interface
* [ ] Website uptime tracking
* [ ] Response history
* [ ] Notification system

---

## 🎯 Learning Goals

This project was created to practice:

* HTTP/HTTPS fundamentals
* Python networking
* URL validation
* Exception handling
* SSL/TLS basics
* Response-time measurement
* Python standard-library modules
* Building practical command-line tools

---

## ⚠️ Ethical & Legal Disclaimer

This tool is intended for educational and legitimate website monitoring purposes.

Only check websites and systems that you are authorized to interact with.

Do not use this tool to perform abusive, excessive, or disruptive requests against websites or services.

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
