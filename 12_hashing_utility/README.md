# 🔎 Hashing Utility

An advanced command-line file hashing and integrity verification tool built with Python.

This project can generate cryptographic hashes for individual files, verify files against known hashes, create checksum manifests for directories, and verify entire manifests to detect modified, corrupted, or missing files.

The tool is designed to demonstrate practical cybersecurity concepts such as **cryptographic hashing, file integrity, checksums, data verification, chunked file processing, and command-line application design**.

> 🛡️ **Educational Cybersecurity Project**
>
> This project is designed for learning Python and cybersecurity fundamentals. It does not encrypt files or protect their contents. Hashing is primarily used to verify data integrity.

---

# 📌 Project Overview

The Hashing Utility provides four major operations:

```text
Hash
  ↓
Generate a cryptographic hash for a file
````

```text
Verify
  ↓
Compare a file against a known hash
```

```text
Manifest
  ↓
Generate hashes for an entire directory
```

```text
Check Manifest
  ↓
Verify all files against the saved hashes
```

This makes the project useful for learning how file-integrity checking works in real-world systems.

---

# ✨ Features

* 🔎 Generate file hashes
* 🔐 SHA-256 support
* 🔐 SHA-512 support
* 🔐 SHA-1 support
* 🔐 MD5 support
* 📦 Chunked file processing
* ⚡ Efficient handling of large files
* 💾 Does not load the entire file into memory
* ✅ Verify files against expected hashes
* 📁 Generate directory checksum manifests
* 🔍 Verify complete checksum manifests
* 📊 Show hashing progress
* 📂 Recursive directory scanning
* 🚫 Detect modified files
* 🚫 Detect corrupted files
* 🚫 Detect missing files
* 🖥️ Command-line interface
* 🧹 Clean error handling
* 🛡️ Uses Python's standard library
* ❌ No external packages required
* ❌ No `eval()`
* ❌ No shell commands
* ❌ Does not modify files while hashing

---

# 🧰 Technologies Used

| Technology | Purpose                              |
| ---------- | ------------------------------------ |
| Python     | Main programming language            |
| `hashlib`  | Cryptographic hashing                |
| `pathlib`  | File and directory handling          |
| `argparse` | Command-line interface               |
| `sys`      | Program exit codes and errors        |
| Type hints | Code readability and maintainability |

The project uses only Python's standard library.

---

# 📋 Requirements

You need:

* Python 3.9 or newer
* `pip` is not required
* Windows, Linux, or macOS
* Terminal / Command Prompt / PowerShell

No external Python packages are required.

---

# 📁 Project Structure

```text
12_hashing_utility/
│
├── hashing_utility.py
└── README.md
```

---

# ⚙️ Installation & Setup

Because this project uses only Python's standard library, there is no `requirements.txt` file and nothing needs to be installed using `pip`.

---

# 🐍 Step 1 — Check Python

Open your terminal.

## Windows

Run:

```bash
python --version
```

If that does not work:

```bash
py --version
```

## Linux / macOS

Run:

```bash
python3 --version
```

You should see something similar to:

```text
Python 3.12.4
```

---

# 📂 Step 2 — Open the Project Folder

Navigate to the project directory.

For example:

```bash
cd 12_hashing_utility
```

If you cloned the complete repository:

```bash
cd python-mini-projects
cd 12_hashing_utility
```

---

# 🚀 Step 3 — Run the Program

The program does not require installation.

Simply run:

```bash
python hashing_utility.py --help
```

On Linux/macOS:

```bash
python3 hashing_utility.py --help
```

If the help menu appears, the project is ready.

---

# 🆘 Help Command

Run:

```bash
python hashing_utility.py --help
```

The application provides four main commands:

```text
hash
verify
manifest
check-manifest
```

---

# 🔎 Command 1 — Hash a File

The simplest operation is generating a SHA-256 hash.

Run:

```bash
python hashing_utility.py hash test.txt
```

Example output:

```text
File:      test.txt
Algorithm: SHA256
Size:      35.00 B
Hash:      8f3c...example...
```

The generated hash is a fingerprint of the file's contents.

---

# 🔐 Hash Using SHA-256

SHA-256 is the default algorithm.

```bash
python hashing_utility.py hash test.txt
```

You can also explicitly select it:

```bash
python hashing_utility.py hash test.txt --algorithm sha256
```

---

# 🔐 Hash Using SHA-512

Run:

```bash
python hashing_utility.py hash test.txt --algorithm sha512
```

SHA-512 produces a longer digest than SHA-256.

---

# 🔐 Hash Using SHA-1

Run:

```bash
python hashing_utility.py hash test.txt --algorithm sha1
```

SHA-1 is supported mainly for compatibility and educational purposes.

It should not be selected for new security-sensitive integrity designs where collision resistance is important.

---

# 🔐 Hash Using MD5

Run:

```bash
python hashing_utility.py hash test.txt --algorithm md5
```

MD5 is supported for compatibility and learning.

It is not recommended for security-sensitive collision-resistant applications.

---

# 📊 Supported Algorithms

| Algorithm | Digest Size | Recommended for New Security Use? |
| --------- | ----------: | --------------------------------- |
| MD5       |     128-bit | ❌ No                              |
| SHA-1     |     160-bit | ❌ No                              |
| SHA-256   |     256-bit | ✅ Yes                             |
| SHA-512   |     512-bit | ✅ Yes                             |

For normal integrity verification, use:

```text
SHA-256
```

or:

```text
SHA-512
```

---

# 📈 Show Hashing Progress

For large files, you can display progress while calculating the hash.

Run:

```bash
python hashing_utility.py hash large_file.zip --progress
```

Example:

```text
Progress:  25.00% (250.00 MB / 1.00 GB)
Progress:  50.00% (500.00 MB / 1.00 GB)
Progress:  75.00% (750.00 MB / 1.00 GB)
Progress: 100.00% (1.00 GB / 1.00 GB)

File:      large_file.zip
Algorithm: SHA256
Size:      1.00 GB
Hash:      ...
```

---

# 📦 Chunked File Processing

The program does not read the entire file into memory.

Instead, it reads the file in chunks.

The default chunk size is:

```text
1 MiB
```

Conceptually:

```text
Large File
    │
    ├── Chunk 1
    ├── Chunk 2
    ├── Chunk 3
    ├── Chunk 4
    ├── ...
    └── Chunk N
         │
         ▼
      hashlib
         │
         ▼
       Hash
```

This makes the application more memory-efficient when processing large files.

---

# ⚙️ Custom Chunk Size

You can specify a custom chunk size in bytes.

For example:

```bash
python hashing_utility.py hash large_file.zip --chunk-size 524288
```

This uses:

```text
524288 bytes
```

which is:

```text
512 KiB
```

The default is:

```text
1048576 bytes
```

which is:

```text
1 MiB
```

For most users, the default is recommended.

---

# 📄 Hash Multiple Files

You can provide multiple files in one command.

Example:

```bash
python hashing_utility.py hash file1.txt file2.txt file3.txt
```

The program processes each file individually.

Example:

```text
[1/3] file1.txt
File:      file1.txt
Algorithm: SHA256
Size:      1.25 KB
Hash:      ...

[2/3] file2.txt
File:      file2.txt
Algorithm: SHA256
Size:      4.80 KB
Hash:      ...

[3/3] file3.txt
File:      file3.txt
Algorithm: SHA256
Size:      10.20 KB
Hash:      ...
```

---

# ✅ Command 2 — Verify a File

Hash generation tells you what the current file hash is.

Verification allows you to compare that hash with a known expected hash.

The syntax is:

```bash
python hashing_utility.py verify <file> <expected_hash>
```

Example:

```bash
python hashing_utility.py verify test.txt 8f3c...your_hash_here...
```

The program calculates the file's current hash and compares it against the expected value.

---

# 🟢 Successful Verification

If the hashes match:

```text
Result: ✅ HASH MATCHES
Integrity check passed.
```

This means the file currently produces the expected hash.

---

# 🔴 Failed Verification

If the hashes are different:

```text
Result: ❌ HASH DOES NOT MATCH
The file may have been modified or corrupted.
```

This indicates that the file's contents no longer produce the expected hash.

---

# 🔎 How File Verification Works

Suppose the original file produces:

```text
ABC123...
```

You later calculate the hash again.

If you get:

```text
ABC123...
```

then:

```text
Expected Hash == Actual Hash
```

The verification passes.

If you get:

```text
XYZ789...
```

then:

```text
Expected Hash != Actual Hash
```

The verification fails.

---

# 📁 Command 3 — Generate a Directory Manifest

A checksum manifest allows you to record hashes for multiple files.

Suppose you have:

```text
my_folder/
│
├── document.pdf
├── image.jpg
├── notes.txt
└── archive.zip
```

Run:

```bash
python hashing_utility.py manifest my_folder
```

The program hashes every file and creates:

```text
checksums.sha256
```

---

# 📄 Manifest Example

A generated manifest looks conceptually like:

```text
SHA256  hash_of_file_1  document.pdf
SHA256  hash_of_file_2  image.jpg
SHA256  hash_of_file_3  notes.txt
SHA256  hash_of_file_4  archive.zip
```

The manifest stores:

* Hash algorithm
* Hash value
* Relative file path

---

# 💾 Specify Manifest Output

By default, the program creates:

```text
checksums.sha256
```

You can choose another output filename:

```bash
python hashing_utility.py manifest my_folder -o my_checksums.txt
```

---

# 🔐 Generate a SHA-512 Manifest

You can also use SHA-512:

```bash
python hashing_utility.py manifest my_folder --algorithm sha512
```

Or specify a custom output:

```bash
python hashing_utility.py manifest my_folder \
    --algorithm sha512 \
    -o checksums.sha512
```

On Windows Command Prompt, use the command on one line if necessary:

```cmd
python hashing_utility.py manifest my_folder --algorithm sha512 -o checksums.sha512
```

---

# 📂 Recursive Directory Scanning

By default, the manifest command searches recursively.

Example:

```text
my_folder/
│
├── file1.txt
│
├── documents/
│   ├── report.pdf
│   └── notes.txt
│
└── images/
    └── photo.jpg
```

The program will find all regular files, including files inside subdirectories.

---

# 🚫 Disable Recursive Scanning

If you only want files directly inside the specified directory:

```bash
python hashing_utility.py manifest my_folder --no-recursive
```

This will ignore files inside subdirectories.

---

# 🔍 Command 4 — Verify a Manifest

Once you have created:

```text
checksums.sha256
```

you can verify all listed files.

Run:

```bash
python hashing_utility.py check-manifest checksums.sha256
```

The program reads every entry and calculates the current hash of each file.

---

# 🟢 Successful Manifest Verification

Example:

```text
[1/3] document.pdf
    ✅ PASS (SHA256)

[2/3] image.jpg
    ✅ PASS (SHA256)

[3/3] notes.txt
    ✅ PASS (SHA256)

==================================================
Manifest Verification Summary
==================================================
Total:   3
Passed:  3
Failed:  0
Missing: 0

✅ ALL FILES PASSED INTEGRITY CHECK.
```

---

# 🔴 Modified File Detection

Suppose you originally generated a manifest.

Later, someone changes:

```text
notes.txt
```

Run:

```bash
python hashing_utility.py check-manifest checksums.sha256
```

The program can report:

```text
[3/3] notes.txt
    ❌ FAIL (SHA256)
    Expected: abc123...
    Actual:   def456...
```

The summary will show the failure.

---

# ❌ Missing File Detection

If a file listed in the manifest no longer exists:

```text
[2/3] important.pdf
    ❌ MISSING
```

The summary will report the missing file.

---

# 📊 Manifest Verification Summary

The program reports:

```text
Total
Passed
Failed
Missing
```

For example:

```text
==================================================
Manifest Verification Summary
==================================================
Total:   10
Passed:  8
Failed:  1
Missing: 1
```

This makes it easy to understand the overall integrity status of a directory.

---

# 📁 Custom Manifest Directory

By default, the program assumes that the files referenced by the manifest are relative to the manifest's directory.

You can specify another base directory using:

```bash
python hashing_utility.py check-manifest checksums.sha256 --directory my_folder
```

This is useful when the manifest is stored separately from the files.

---

# 🧪 Complete Testing Tutorial

Here is a complete test you can perform after setting up the project.

---

## Step 1 — Create a Test File

Create:

```text
test.txt
```

Put this inside:

```text
Hello from the Python Hashing Utility!
```

---

## Step 2 — Generate SHA-256

Run:

```bash
python hashing_utility.py hash test.txt
```

Copy the hash displayed by the program.

---

## Step 3 — Verify the File

Use the hash you copied:

```bash
python hashing_utility.py verify test.txt YOUR_HASH_HERE
```

You should receive:

```text
Result: ✅ HASH MATCHES
Integrity check passed.
```

---

## Step 4 — Modify the File

Change the contents of:

```text
test.txt
```

For example:

```text
Hello from the modified Python Hashing Utility!
```

Now run the verification command again using the **old hash**.

The verification should fail:

```text
Result: ❌ HASH DOES NOT MATCH
```

This demonstrates how hashing can detect changes.

---

# 🧪 Directory Integrity Test

Create:

```text
test_folder/
│
├── file1.txt
├── file2.txt
└── file3.txt
```

Generate a manifest:

```bash
python hashing_utility.py manifest test_folder
```

Then verify it:

```bash
python hashing_utility.py check-manifest checksums.sha256
```

All files should pass.

Now modify one file.

Run:

```bash
python hashing_utility.py check-manifest checksums.sha256
```

The modified file should fail.

---

# 🧠 How Hashing Works

A cryptographic hash function takes input data and produces a fixed-size output called a digest.

Conceptually:

```text
File Contents
      │
      ▼
Hash Function
      │
      ▼
Fixed-Length Hash
```

For SHA-256:

```text
Input:
Any amount of data

Output:
256-bit digest
```

Usually represented as:

```text
64 hexadecimal characters
```

Example format:

```text
e3b0c44298fc1c149afbf4c8996fb924...
```

---

# 🔐 Why Hashes Are Useful

Hashing is useful for detecting whether data has changed.

For example:

```text
Original File
     ↓
SHA-256
     ↓
Hash A
```

Later:

```text
Current File
     ↓
SHA-256
     ↓
Hash B
```

Compare:

```text
Hash A == Hash B
```

If they match, the file has the expected hash.

If they differ, the file contents differ.

---

# 🔄 Hashing vs Encryption

Hashing and encryption are different.

## Encryption

Encryption is designed to protect confidentiality.

```text
Plaintext
   ↓
Encryption
   ↓
Ciphertext
   ↓
Decryption
   ↓
Plaintext
```

Encryption is reversible with the appropriate key.

---

## Hashing

Hashing is designed primarily for fingerprints and integrity checks.

```text
Data
  ↓
Hash Function
  ↓
Hash
```

A cryptographic hash is designed to be computationally infeasible to reverse into the original data.

---

# 🔐 Hashing vs Password Protection

A normal hash by itself should not be treated as a password-storage solution.

For password storage, specialized password hashing / key derivation functions such as:

* Argon2
* scrypt
* bcrypt
* PBKDF2

are appropriate depending on the application.

This project focuses on **file integrity**, not password storage.

---

# 🧠 SHA-256

SHA-256 belongs to the SHA-2 family.

It produces:

```text
256 bits
```

or:

```text
32 bytes
```

or:

```text
64 hexadecimal characters
```

SHA-256 is a strong general-purpose choice for file integrity verification.

---

# 🧠 SHA-512

SHA-512 also belongs to the SHA-2 family.

It produces:

```text
512 bits
```

or:

```text
64 bytes
```

or:

```text
128 hexadecimal characters
```

It is another strong choice for general-purpose integrity checking.

---

# ⚠️ MD5

MD5 produces a:

```text
128-bit
```

digest.

MD5 has known collision weaknesses and should not be used where strong collision resistance is required.

It is included in this project mainly for:

* Learning
* Compatibility
* Legacy checksum verification

---

# ⚠️ SHA-1

SHA-1 produces a:

```text
160-bit
```

digest.

SHA-1 has known collision attacks and should not be selected for new security-sensitive designs requiring collision resistance.

It is included mainly for:

* Learning
* Compatibility
* Legacy systems

---

# ⚡ Performance Optimization

The program is designed to be reasonably efficient for large files.

Instead of doing:

```python
file.read()
```

for an entire file, it uses chunked processing.

Conceptually:

```python
while True:
    chunk = file.read(chunk_size)

    if not chunk:
        break

    hasher.update(chunk)
```

This keeps memory usage relatively stable regardless of the total file size.

---

# 💾 Memory Efficiency

Suppose a file is:

```text
10 GB
```

The program does not need to load all 10 GB into RAM.

Instead, it processes approximately:

```text
1 MiB
```

at a time by default.

This makes the design more appropriate for large files.

---

# 🛡️ Security Considerations

The tool is designed around integrity verification.

Important security principles include:

### Use SHA-256 or SHA-512

Prefer:

```text
SHA-256
```

or:

```text
SHA-512
```

for new integrity checks.

---

### Treat Hashes as Verification Values

A hash can tell you whether the data matches an expected value.

It does not automatically prove who created the file or hash.

For stronger authenticity guarantees, digital signatures or authenticated mechanisms are required.

---

### Protect the Expected Hash

If an attacker can replace both:

```text
File
```

and:

```text
Expected Hash
```

then simple hash comparison may not detect the replacement.

For high-security environments, the trusted hash value should be distributed or stored through a trusted mechanism.

---

# 🚫 What This Tool Does NOT Do

This application does not:

* ❌ Encrypt files
* ❌ Decrypt files
* ❌ Delete files
* ❌ Modify file contents
* ❌ Execute shell commands
* ❌ Execute arbitrary Python code
* ❌ Use `eval()`
* ❌ Upload files anywhere
* ❌ Send files over the network
* ❌ Store passwords
* ❌ Hide files
* ❌ Provide digital signatures

It is an integrity and verification utility.

---

# 🧪 Error Handling

The program handles common problems such as:

* File does not exist
* Directory does not exist
* Path is not a regular file
* Permission denied
* Unsupported hashing algorithm
* Invalid hash format
* Invalid manifest entries
* Missing manifest files
* File system errors
* User cancellation

The program also uses appropriate exit codes.

Generally:

```text
0 = Success
1 = Error / Verification Failure
130 = User Cancellation
```

---

# 💻 Windows Usage

Example complete workflow:

```powershell
cd path\to\12_hashing_utility

python hashing_utility.py --help

python hashing_utility.py hash test.txt

python hashing_utility.py hash test.txt --algorithm sha512

python hashing_utility.py verify test.txt YOUR_HASH_HERE

python hashing_utility.py manifest test_folder

python hashing_utility.py check-manifest checksums.sha256
```

---

# 🐧 Linux Usage

```bash
cd ~/python-mini-projects/12_hashing_utility

python3 hashing_utility.py --help

python3 hashing_utility.py hash test.txt

python3 hashing_utility.py hash test.txt --algorithm sha512

python3 hashing_utility.py verify test.txt YOUR_HASH_HERE

python3 hashing_utility.py manifest test_folder

python3 hashing_utility.py check-manifest checksums.sha256
```

---

# 🍎 macOS Usage

```bash
cd ~/python-mini-projects/12_hashing_utility

python3 hashing_utility.py --help

python3 hashing_utility.py hash test.txt

python3 hashing_utility.py hash test.txt --algorithm sha512

python3 hashing_utility.py verify test.txt YOUR_HASH_HERE

python3 hashing_utility.py manifest test_folder

python3 hashing_utility.py check-manifest checksums.sha256
```

---

# 🔧 Troubleshooting

## Python is not recognized

Windows:

```bash
py --version
```

Then use:

```bash
py hashing_utility.py hash test.txt
```

Linux/macOS:

```bash
python3 --version
```

---

## File Not Found

If you see:

```text
File not found
```

make sure the file exists and that you are running the program from the correct directory.

You can also provide a full or relative path.

Example:

```bash
python hashing_utility.py hash ./files/test.txt
```

---

## Permission Denied

If the program cannot read a file:

```text
Permission denied
```

make sure your user account has permission to read that file.

---

## Invalid Hash Format

A hash must contain the correct number of hexadecimal characters for the selected algorithm.

For SHA-256:

```text
64 hexadecimal characters
```

For SHA-512:

```text
128 hexadecimal characters
```

For SHA-1:

```text
40 hexadecimal characters
```

For MD5:

```text
32 hexadecimal characters
```

---

# 📊 Exit Codes

The program uses exit codes so it can also be used in scripts or automation.

```text
0
```

means successful execution.

```text
1
```

means an error or failed integrity check.

```text
130
```

means the operation was interrupted by the user.

This allows other programs or scripts to detect whether verification succeeded.

---

# 🧑‍💻 Learning Objectives

This project helps practice:

## Python

* Functions
* Modules
* Exception handling
* File I/O
* Binary file processing
* Command-line arguments
* Type hints
* Path handling
* Iteration
* Error reporting
* Program exit codes

## Cybersecurity

* Cryptographic hashing
* File integrity
* Checksum verification
* Hash comparison
* Collision concepts
* Integrity monitoring
* Trusted verification values

## Software Engineering

* CLI architecture
* Subcommands
* Input validation
* Error handling
* Modular functions
* Efficient memory usage
* User-friendly terminal output

---

# 📚 Important Concepts Learned

## Hash

A fixed-size digest generated from input data.

---

## Digest

The output produced by a hashing algorithm.

---

## Checksum

A value used to detect changes or corruption in data.

---

## Integrity

The property that data has not been unexpectedly modified.

---

## Collision

A situation where two different inputs produce the same hash.

Strong cryptographic hash functions are designed to make finding useful collisions computationally difficult.

---

## Avalanche Effect

A small change in the input should cause a large and unpredictable change in the resulting hash.

For example:

```text
Hello
```

and:

```text
hello
```

produce completely different hashes.

---

# 🔐 Real-World Uses

File hashing is commonly useful for:

* Software downloads
* File integrity monitoring
* Backup verification
* Digital forensics
* Malware analysis
* Incident response
* Data synchronization
* Package verification
* Archive verification
* Detecting accidental corruption
* Detecting unexpected modifications

---

# 🧪 Recommended Testing Checklist

Before considering the project complete, test:

```text
[x] Hash a normal text file
[x] Hash a binary file
[x] Hash a large file
[x] Use SHA-256
[x] Use SHA-512
[x] Use SHA-1
[x] Use MD5
[x] Verify a correct hash
[x] Verify an incorrect hash
[x] Modify a file and verify again
[x] Generate a directory manifest
[x] Verify a manifest
[x] Modify a manifest-listed file
[x] Delete a manifest-listed file
[x] Test a missing file
[x] Test an invalid hash
[x] Test invalid paths
[x] Test user cancellation
```

---

# 🔮 Future Improvements

Possible future versions could add:

* 📊 Rich terminal interface
* 🎨 Colored status output
* 📈 Detailed progress bars
* 🗂️ Ignore patterns
* 📄 JSON manifest support
* 📄 CSV report generation
* 🔐 Digital signature verification
* 🔑 HMAC verification
* 📋 Exportable integrity reports
* 🧪 Automated unit tests
* 🧪 Benchmark mode
* 🔄 Continuous directory monitoring
* 📝 Logging
* ⚙️ Configuration files
* 🖥️ Optional GUI
* 📊 Hash performance comparison
* 🔍 Duplicate-file detection
* 📦 Parallel hashing for suitable workloads

---

# ⚠️ Ethical & Legal Disclaimer

This project is intended for:

* Educational purposes
* Python programming practice
* Cybersecurity learning
* File integrity testing
* Personal systems
* Authorized environments

Do not use this project to interfere with systems or files that you do not own or have permission to access.

You are responsible for following applicable laws, regulations, and organizational policies.

---

# 🔒 Security Notice

Never treat a hash as a secret password.

Do not commit sensitive information to GitHub.

Avoid uploading:

```text
Passwords
API Keys
Access Tokens
Private Keys
SSH Keys
Credentials
Personal Secrets
```

A hash is not automatically proof of authenticity. If authenticity matters, use a trusted distribution channel or an appropriate digital-signature mechanism.

---

# 📦 Dependencies

This project has:

```text
No external dependencies
```

It uses Python's built-in standard library:

```text
hashlib
pathlib
argparse
sys
typing
```

Therefore, you do not need:

```bash
pip install ...
```

---

# 🗂️ File Description

## `hashing_utility.py`

Contains:

* Hashing engine
* Hash verification
* Directory scanning
* Manifest generation
* Manifest verification
* CLI argument parser
* Progress display
* Error handling

---

## `README.md`

Contains:

* Installation instructions
* Usage instructions
* Security concepts
* Command examples
* Testing instructions
* Troubleshooting
* Project documentation

---

# 🏗️ Architecture

The application can be viewed as four major components:

```text
                 Hashing Utility
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
      Hash           Verify        Manifest
        │              │              │
        │              │              ▼
        │              │        Check Manifest
        │              │              │
        └──────────────┴──────────────┘
                       │
                       ▼
                    hashlib
                       │
                       ▼
                 File Integrity
```

---

# 🎯 Project Goal

The main goal of this project is to understand how cryptographic hashing can be used in practical software.

Instead of simply calculating a hash, the project demonstrates a complete workflow:

```text
File
 ↓
Hash
 ↓
Store / Compare
 ↓
Verify
 ↓
Detect Changes
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

---

# 📈 Project Status

**Project:** 12 - Hashing Utility

**Status:** ✅ Completed

**Difficulty:** Advanced

**Category:** Cybersecurity / Cryptography / File Integrity

**Language:** Python

**External Dependencies:** None

**Default Algorithm:** SHA-256

**Large File Support:** ✅

**Chunked Processing:** ✅

**Directory Manifest:** ✅

**Integrity Verification:** ✅

**Progress Display:** ✅

**Recursive Scanning:** ✅

**Original Files Modified:** ❌ No

**Files Uploaded:** ❌ No

**Shell Commands:** ❌ No

**`eval()` Used:** ❌ No

---

# 🐍 Part of Python Mini Projects

This project is part of the **Python Mini Projects** repository.

The repository is a hands-on learning journey that gradually moves from basic Python programming to networking, automation, CLI development, cybersecurity, and cryptography.

Current progression:

```text
01 🔎 Port Scanner
       ↓
02 📱 QR Code Generator
       ↓
03 🔐 Password Generator
       ↓
04 📁 File Organizer
       ↓
05 💰 Bill Splitter
       ↓
06 🌐 Website Status Checker
       ↓
07 🔍 DNS Lookup Tool
       ↓
08 📊 Log Analyzer
       ↓
09 🧮 CLI Calculator
       ↓
10 🖥️ System Information Tool
       ↓
11 🔐 File Encryption Tool
       ↓
12 🔎 Hashing Utility
```

---

# 👨‍💻 Author

**Avinash Das Manikpuri**

GitHub:

[https://github.com/Avinash-05-web](https://github.com/Avinash-05-web)

Repository:

[https://github.com/Avinash-05-web/python-mini-projects](https://github.com/Avinash-05-web/python-mini-projects)

---

# ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 🍴 Fork the repository
* 📚 Explore the other projects
* 💡 Suggest improvements
* 🧑‍💻 Use the project for learning

---

# 🏁 Quick Start

If Python is already installed:

```bash
cd 12_hashing_utility
```

Run:

```bash
python hashing_utility.py --help
```

Hash a file:

```bash
python hashing_utility.py hash test.txt
```

Verify a file:

```bash
python hashing_utility.py verify test.txt YOUR_HASH_HERE
```

Generate a directory manifest:

```bash
python hashing_utility.py manifest test_folder
```

Verify the manifest:

```bash
python hashing_utility.py check-manifest checksums.sha256
```

No additional packages are required.

---

# 🐍 Build. Learn. Secure. Repeat.

This project adds another important cybersecurity concept to the Python Mini Projects journey:

```text
Encryption protects confidentiality.
Hashing helps verify integrity.
```

**Project 12 — Hashing Utility 🔎**

**12 projects completed. 🚀**
