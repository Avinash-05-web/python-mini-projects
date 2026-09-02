# 🔐 File Encryption Tool

A secure command-line file encryption and decryption tool built with Python.

This project demonstrates how modern authenticated encryption can be used to protect files using **AES-256-GCM**, with passwords converted into strong encryption keys using **Scrypt**.

The tool is designed as an educational cybersecurity project while following safer design practices such as authenticated encryption, random salts, unique nonces, chunked file processing, atomic output replacement, and secure temporary-file cleanup.

> ⚠️ **Educational Security Project**
>
> This project is intended for learning Python, cryptography, file handling, and cybersecurity fundamentals.
> It should not be considered a replacement for professionally audited encryption software for high-value or production data.

---

## 📌 Project Overview

The File Encryption Tool allows you to:

- 🔒 Encrypt files using a password
- 🔓 Decrypt previously encrypted files
- 🛡️ Protect encrypted data with AES-256-GCM authentication
- 🔑 Derive encryption keys from passwords using Scrypt
- 🧂 Generate a unique random salt for every encrypted file
- 🎲 Generate unique nonce material for encrypted chunks
- 📦 Process files in chunks instead of loading the entire file into memory
- 🚫 Detect incorrect passwords
- 🚫 Detect modified or corrupted encrypted data
- 💾 Preserve the original file
- 🧹 Clean up temporary files if an operation fails
- ⚡ Use atomic file replacement to reduce the chance of leaving partially written output
- ❌ Avoid dangerous operations such as deleting the original file
- ❌ Avoid `eval()`
- ❌ Avoid shell commands
- 🖥️ Run completely from the command line

---

# ✨ Features

## 🔐 File Encryption

Encrypt any file using a password.

Example:

```bash
python file_encryptor.py encrypt secret.txt
````

The encrypted file will normally be created as:

```text
secret.txt.enc
```

The original file remains untouched.

---

## 🔓 File Decryption

Decrypt an encrypted file using the correct password.

Example:

```bash
python file_encryptor.py decrypt secret.txt.enc
```

The decrypted file will normally be created as:

```text
secret.txt
```

If the destination already exists, the tool will not blindly overwrite it unless the output path is explicitly chosen according to the program's behavior.

---

# 🧰 Technologies Used

This project uses:

| Technology                          | Purpose                                |
| ----------------------------------- | -------------------------------------- |
| Python                              | Main programming language              |
| `cryptography`                      | Cryptographic implementation           |
| AES-256-GCM                         | Authenticated encryption               |
| Scrypt                              | Password-based key derivation          |
| `pathlib`                           | File and path handling                 |
| `argparse`                          | Command-line interface                 |
| `getpass`                           | Secure password input                  |
| `secrets`                           | Cryptographically secure random values |
| `struct`                            | Binary header serialization            |
| `os`                                | File operations and permissions        |
| `tempfile`-style temporary workflow | Safe output handling                   |

Most modules come with Python's standard library.

The only external package required is:

```text
cryptography
```

---

# 📋 Requirements

Before running the project, make sure you have:

* Python 3.9 or newer
* `pip`
* A terminal or command prompt
* Basic knowledge of command-line commands

Supported operating systems include:

* Windows
* Linux
* macOS

---

# 🐍 Check Python Installation

Open a terminal.

### Windows

Try:

```bash
python --version
```

If that does not work, try:

```bash
py --version
```

### Linux / macOS

Try:

```bash
python3 --version
```

You should see something similar to:

```text
Python 3.x.x
```

For example:

```text
Python 3.12.4
```

---

# 📁 Project Structure

The project should look like this:

```text
11_file_encryption_tool/
│
├── file_encryptor.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Step 1 — Open the Project Folder

Navigate to the project directory.

Example:

```bash
cd 11_file_encryption_tool
```

You can also open the folder directly in VS Code and use its integrated terminal.

---

# Step 2 — Create a Virtual Environment

A virtual environment is recommended because it keeps project dependencies isolated.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

If using PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

After activation, your terminal may show:

```text
(venv)
```

---

# Step 3 — Upgrade pip

Run:

```bash
python -m pip install --upgrade pip
```

On Linux/macOS, if necessary:

```bash
python3 -m pip install --upgrade pip
```

---

# Step 4 — Install Dependencies

The project includes:

```text
cryptography>=46.0
```

Install it with:

```bash
pip install -r requirements.txt
```

Or:

```bash
python -m pip install -r requirements.txt
```

After installation, verify the package:

```bash
pip show cryptography
```

---

# 🚀 Running the Program

The program is controlled using two main commands:

```text
encrypt
decrypt
```

The basic syntax is:

```bash
python file_encryptor.py encrypt <file>
```

or:

```bash
python file_encryptor.py decrypt <encrypted_file>
```

---

# 🔒 Encrypt a File

Create a test file first.

For example:

```text
secret.txt
```

Put some text inside:

```text
This is my secret file.
```

Then run:

```bash
python file_encryptor.py encrypt secret.txt
```

The program will ask for a password.

Example:

```text
Enter password:
Confirm password:
```

After successful encryption, an encrypted file will be created.

Example:

```text
secret.txt.enc
```

---

# 🔑 Password Requirements

The tool requires a password with a minimum length.

The default minimum password length is:

```text
8 characters
```

A stronger password is recommended.

Example of a weak password:

```text
password
```

A stronger example:

```text
River!Cloud#47Moon
```

Do not use the example password for real files.

---

# ⚠️ IMPORTANT: Remember Your Password

The encryption password is **not stored anywhere**.

That means:

```text
Password lost = File cannot be recovered
```

There is no password recovery mechanism built into this project.

Do not forget the password used to encrypt an important file.

---

# 📤 Specify a Custom Output File

You can use the `-o` option to specify where the encrypted file should be created.

Example:

```bash
python file_encryptor.py encrypt secret.txt -o protected.dat
```

The encrypted output will be:

```text
protected.dat
```

---

# 🔓 Decrypt a File

To decrypt an encrypted file:

```bash
python file_encryptor.py decrypt secret.txt.enc
```

The program will ask for the password:

```text
Enter password:
```

Enter the same password that was used during encryption.

If the password and encrypted data are valid, the file will be decrypted.

---

# 📥 Specify a Custom Decryption Output

You can also specify the destination file.

Example:

```bash
python file_encryptor.py decrypt secret.txt.enc -o recovered.txt
```

The decrypted file will be written to:

```text
recovered.txt
```

---

# 🧪 Complete Example

Suppose the folder contains:

```text
11_file_encryption_tool/
│
├── file_encryptor.py
├── requirements.txt
├── README.md
└── secret.txt
```

Run:

```bash
python file_encryptor.py encrypt secret.txt
```

Enter your password.

You should now have:

```text
secret.txt
secret.txt.enc
```

The original file is still present.

Now decrypt:

```bash
python file_encryptor.py decrypt secret.txt.enc
```

You can also choose a different output:

```bash
python file_encryptor.py decrypt secret.txt.enc -o recovered_secret.txt
```

The folder could then contain:

```text
11_file_encryption_tool/
│
├── file_encryptor.py
├── requirements.txt
├── README.md
├── secret.txt
├── secret.txt.enc
└── recovered_secret.txt
```

---

# 🆘 View Help

The CLI provides built-in help.

Run:

```bash
python file_encryptor.py --help
```

You can also check encryption help:

```bash
python file_encryptor.py encrypt --help
```

And decryption help:

```bash
python file_encryptor.py decrypt --help
```

---

# 🧠 How the Encryption Works

The tool uses several security mechanisms together.

The basic process is:

```text
User Password
      │
      ▼
Random Salt
      │
      ▼
     Scrypt
      │
      ▼
32-byte Encryption Key
      │
      ▼
AES-256-GCM
      │
      ▼
Encrypted File
```

---

# 🔑 1. Password

The user provides a password.

Passwords should not be used directly as AES keys because human-created passwords generally do not contain enough random entropy.

Therefore, the password is processed using a password-based key derivation function.

---

# 🧂 2. Random Salt

For every encrypted file, the program generates a random salt.

The salt prevents the same password from always producing the same derived key.

The salt does not need to be secret.

It is stored inside the encrypted file header.

Conceptually:

```text
Password + Random Salt
        │
        ▼
      Scrypt
        │
        ▼
Encryption Key
```

---

# 🧠 3. Scrypt

The project uses:

```text
Scrypt
```

Scrypt is designed for password-based key derivation and is intentionally expensive in terms of memory and computation.

The configuration used by the project is:

```text
N = 32768
r = 8
p = 1
```

The resulting key size is:

```text
32 bytes
```

which provides a:

```text
256-bit key
```

---

# 🔐 4. AES-256-GCM

The actual file encryption is performed using:

```text
AES-256-GCM
```

AES provides the encryption.

GCM provides authenticated encryption.

This means the tool does not only encrypt the data; it also detects unauthorized modification.

---

# 🛡️ Authentication

AES-GCM generates an authentication tag for each encrypted chunk.

This allows the program to detect:

* Incorrect passwords
* Modified encrypted data
* Corrupted encrypted data
* Invalid authentication data

If authentication fails, the program does not accept the decrypted data as valid.

---

# 🎲 5. Nonces

AES-GCM requires careful nonce management.

The project generates nonce material for the encrypted file and uses a different nonce for each encrypted chunk.

Conceptually:

```text
File
 │
 ├── Chunk 1 → Nonce 1
 │
 ├── Chunk 2 → Nonce 2
 │
 ├── Chunk 3 → Nonce 3
 │
 └── Chunk N → Nonce N
```

Nonce uniqueness is extremely important when using AES-GCM.

---

# 📦 6. Chunked Encryption

Large files should not necessarily be loaded completely into memory.

Instead, the program processes the file in chunks.

The configured chunk size is:

```text
1 MiB
```

The process looks like:

```text
Large File
    │
    ▼
┌─────────────┐
│   Chunk 1   │
├─────────────┤
│   Chunk 2   │
├─────────────┤
│   Chunk 3   │
├─────────────┤
│     ...     │
├─────────────┤
│   Chunk N   │
└─────────────┘
```

Each chunk is encrypted independently.

This makes the tool more suitable for larger files than an implementation that loads the entire file into memory.

---

# 🧾 7. Authenticated Header

The encrypted file contains a custom binary header.

The header stores information needed for decryption, such as:

* File format identifier
* Format version
* Random salt
* Nonce information
* Original file size
* Chunk size

The header is also authenticated as Additional Authenticated Data (AAD).

This helps prevent important encryption metadata from being silently modified.

---

# 🔒 What is AAD?

AAD stands for:

```text
Additional Authenticated Data
```

AAD is data that does not need to be encrypted but should still be authenticated.

In this project, the encrypted file header is used as authenticated data.

Conceptually:

```text
Header ───────────────┐
                      │
                      ▼
                 AES-GCM
                      │
File Chunk ───────────┘
                      │
                      ▼
             Ciphertext + Tag
```

If the authenticated header is modified, authentication can fail.

---

# 💾 8. Temporary Output File

The program does not directly write decrypted or encrypted data to the final destination.

Instead, it first creates a temporary output file.

Conceptually:

```text
Input File
    │
    ▼
Temporary Output
    │
    ├── Success ──► Final Output
    │
    └── Failure ──► Delete Temporary Output
```

This reduces the chance of leaving a partially generated output file after an error.

---

# ⚛️ 9. Atomic File Replacement

Once the encryption/decryption operation finishes successfully, the program uses an atomic replacement operation.

This helps ensure the final output is only replaced after the operation has completed successfully.

This is safer than continuously overwriting the final destination during processing.

---

# 🧹 10. Temporary File Cleanup

If encryption or decryption fails, the temporary output is removed.

For example, if:

```text
Wrong Password
```

is entered during decryption, authentication fails and the incomplete temporary output is discarded.

---

# 🚫 Original Files Are Not Deleted

The program intentionally does **not** delete the original file after encryption.

For example:

```text
secret.txt
```

becomes:

```text
secret.txt
secret.txt.enc
```

The original remains available.

This is an important safety decision for an educational encryption project.

---

# 🛑 Incorrect Password Behavior

If you attempt to decrypt a file with the wrong password, AES-GCM authentication should fail.

The program should report an error instead of treating the resulting data as valid plaintext.

This is an important difference between authenticated encryption and simple encryption-only schemes.

---

# 🛡️ Security Design

The project follows several security principles:

### Password-Based Key Derivation

```text
Password → Scrypt → 256-bit Key
```

### Authenticated Encryption

```text
AES-256-GCM
```

### Random Salt

Every encrypted file receives a new random salt.

### Unique Nonces

Each encrypted chunk receives nonce material designed to avoid reuse within the file.

### Authentication

Encrypted chunks contain authentication tags.

### Chunked Processing

Large files are processed in manageable chunks.

### Atomic Output

Final files are only replaced after successful processing.

### Temporary Cleanup

Failed operations clean up temporary output.

### No Password Storage

The password is never written to disk by the program.

### No Original File Deletion

The original file remains untouched.

### No `eval()`

The application never evaluates user input as Python code.

### No Shell Commands

The program does not execute shell commands.

---

# 📊 Encryption Architecture

The overall architecture can be represented as:

```text
                    ┌───────────────┐
                    │ User Password │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Random Salt   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    Scrypt     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  AES-256 Key  │
                    └───────┬───────┘
                            │
                            ▼
              ┌─────────────────────────┐
              │      File Chunks        │
              └────────────┬────────────┘
                           │
                           ▼
                  ┌────────────────┐
                  │   AES-256-GCM  │
                  └───────┬────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Ciphertext + Tags  │
                └─────────┬──────────┘
                          │
                          ▼
                  Encrypted File
```

---

# 📁 Encrypted File Format

The project uses a custom binary format.

The file contains a header followed by encrypted chunks.

Conceptually:

```text
┌───────────────────────────────┐
│ Magic / Format Identifier     │
├───────────────────────────────┤
│ Version                       │
├───────────────────────────────┤
│ Random Salt                   │
├───────────────────────────────┤
│ Base Nonce Information        │
├───────────────────────────────┤
│ Original File Size            │
├───────────────────────────────┤
│ Chunk Size                    │
├───────────────────────────────┤
│ Encrypted Chunk 1 + Tag       │
├───────────────────────────────┤
│ Encrypted Chunk 2 + Tag       │
├───────────────────────────────┤
│ Encrypted Chunk 3 + Tag       │
├───────────────────────────────┤
│             ...               │
└───────────────────────────────┘
```

The password is **not stored** in the encrypted file.

---

# 🧪 Testing the Project

It is recommended to test the program with a small test file before using it with important data.

## Step 1 — Create a Test File

Create:

```text
test.txt
```

Put:

```text
Hello, this is a file encryption test.
```

inside it.

---

## Step 2 — Encrypt It

Run:

```bash
python file_encryptor.py encrypt test.txt
```

You should receive an encrypted file.

---

## Step 3 — Decrypt It

Run:

```bash
python file_encryptor.py decrypt test.txt.enc
```

---

## Step 4 — Compare the Files

Verify that the recovered file contains exactly the original content.

For a simple text test:

```text
Original:
Hello, this is a file encryption test.

Recovered:
Hello, this is a file encryption test.
```

---

# 🧪 Test With Different File Types

You can test the tool with different types of files.

Examples:

```text
.txt
.jpg
.png
.pdf
.zip
.csv
.docx
.mp3
.mp4
```

Example:

```bash
python file_encryptor.py encrypt photo.jpg
```

Then:

```bash
python file_encryptor.py decrypt photo.jpg.enc
```

Always test with copies of important files rather than your only copy.

---

# 🧪 Test Wrong Password

Encrypt a file:

```bash
python file_encryptor.py encrypt secret.txt
```

Then try decrypting it using an incorrect password.

The authentication check should fail.

The program should not produce a valid decrypted file.

---

# 🧪 Test File Modification

You can also test whether authentication detects modified encrypted data.

For example:

1. Encrypt a test file.
2. Make a copy of the encrypted file.
3. Modify the encrypted data.
4. Try to decrypt the modified file.

The authentication mechanism should reject the modified data.

Do not perform this test on your only encrypted copy.

---

# 🧪 Test Large Files

The project supports chunked processing.

You can test it with a larger file to observe how the program handles data without reading the entire file into memory at once.

Example:

```bash
python file_encryptor.py encrypt large_file.zip
```

Then:

```bash
python file_encryptor.py decrypt large_file.zip.enc
```

---

# 🖥️ Windows Example

A complete Windows workflow could look like:

```powershell
cd path\to\11_file_encryption_tool

python -m venv venv

venv\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

python file_encryptor.py --help

python file_encryptor.py encrypt secret.txt

python file_encryptor.py decrypt secret.txt.enc
```

---

# 🐧 Linux Example

```bash
cd ~/python-mini-projects/11_file_encryption_tool

python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt

python3 file_encryptor.py --help

python3 file_encryptor.py encrypt secret.txt

python3 file_encryptor.py decrypt secret.txt.enc
```

---

# 🍎 macOS Example

```bash
cd ~/python-mini-projects/11_file_encryption_tool

python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements.txt

python3 file_encryptor.py --help

python3 file_encryptor.py encrypt secret.txt

python3 file_encryptor.py decrypt secret.txt.enc
```

---

# 🔧 Troubleshooting

## `python` is not recognized

On Windows, try:

```bash
py --version
```

If that works, use:

```bash
py file_encryptor.py encrypt secret.txt
```

instead of:

```bash
python file_encryptor.py encrypt secret.txt
```

---

## `pip` is not recognized

Try:

```bash
python -m pip install -r requirements.txt
```

or:

```bash
py -m pip install -r requirements.txt
```

---

## `cryptography` is missing

If you see an error similar to:

```text
ModuleNotFoundError: No module named 'cryptography'
```

install the dependency:

```bash
pip install cryptography
```

or:

```bash
python -m pip install cryptography
```

---

## Virtual Environment Is Not Activated

If your terminal does not show:

```text
(venv)
```

activate it again.

Windows:

```powershell
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

---

## PowerShell Does Not Allow Activation

If PowerShell blocks the activation script because of execution policy, you can use Command Prompt instead:

```cmd
venv\Scripts\activate
```

Alternatively, run Python directly from the virtual environment without activating it.

---

## Wrong Password

If the password is incorrect, decryption will fail authentication.

Use the exact password that was originally used to encrypt the file.

There is no password recovery mechanism.

---

## Encrypted File Is Corrupted

If the encrypted file has been damaged or modified, authentication may fail.

Do not assume a corrupted encrypted file can be repaired.

Always keep backups of important encrypted data.

---

# 🔒 Security Best Practices

## 1. Use a Strong Password

Avoid:

```text
12345678
password
qwerty123
mypassword
```

Prefer a long, unique passphrase.

For example:

```text
Mountain!River!Coffee!47
```

Do not use this example password for actual security.

---

## 2. Never Share Your Password

Anyone with the encrypted file and password may be able to decrypt the data.

Keep the password private.

---

## 3. Keep Backups

Encryption does not protect against:

* Disk failure
* Accidental deletion
* Lost passwords
* Hardware damage
* File corruption

Maintain secure backups of important files.

---

## 4. Do Not Lose the Password

The project intentionally does not provide a password recovery mechanism.

If the password is lost:

```text
Encrypted file + lost password
             =
     Potential permanent loss
```

---

## 5. Test Before Encrypting Important Data

Always test the application first.

Recommended workflow:

```text
Test File
   ↓
Encrypt
   ↓
Decrypt
   ↓
Verify Contents
   ↓
Use With Important Data
```

---

# ⚠️ Important Security Limitations

Although this project uses modern cryptographic primitives, it is still a **learning project**.

Important limitations include:

### Custom Encryption Format

This project implements its own encrypted-file format.

Custom cryptographic formats should not automatically be considered production-ready.

---

### No Professional Security Audit

The project has not undergone a formal cryptographic security audit.

For extremely sensitive or critical information, use established, professionally reviewed encryption software.

---

### Password Security Depends on the Password

Scrypt makes password guessing more expensive, but it cannot make a weak password strong.

A weak password can still be vulnerable to guessing attacks.

---

### Metadata Is Not Completely Hidden

Encrypting file contents does not necessarily hide all information surrounding the file.

For example, the encrypted filename may still reveal information about the original file depending on how the output is named.

---

### Password Recovery Is Not Available

If the password is lost, the application does not provide a recovery mechanism.

---

# 🚫 What This Project Does NOT Do

This tool intentionally does not include:

* ❌ Ransomware behavior
* ❌ Automatic deletion of originals
* ❌ Mass encryption of directories
* ❌ Persistence mechanisms
* ❌ Stealth mechanisms
* ❌ Privilege escalation
* ❌ Credential theft
* ❌ Network propagation
* ❌ Remote command execution
* ❌ Shell command execution
* ❌ Password storage
* ❌ `eval()`-based input execution

The project focuses on defensive and educational file protection.

---

# 🧑‍💻 Learning Objectives

This project helps practice:

### Python

* Functions
* Classes/modules
* Exception handling
* File I/O
* Binary data handling
* Command-line arguments
* Password input
* Path handling
* Temporary files

### Cybersecurity

* Encryption
* Authenticated encryption
* Key derivation
* Password security
* Salts
* Nonces
* Authentication tags
* Data integrity
* Secure file handling

### Cryptography

* AES-256-GCM
* Scrypt
* Random cryptographic values
* Authenticated data
* Key derivation
* Nonce management

---

# 📚 Important Concepts Learned

## Encryption

Encryption transforms readable plaintext into ciphertext.

```text
Plaintext
    ↓
Encryption Key
    ↓
Encryption Algorithm
    ↓
Ciphertext
```

---

## Decryption

Decryption reverses the process when the correct key is available.

```text
Ciphertext
    ↓
Encryption Key
    ↓
Decryption Algorithm
    ↓
Plaintext
```

---

## Salt

A random value used during password-based key derivation.

It does not need to remain secret.

---

## Nonce

A value used with an encryption operation.

For AES-GCM, nonce reuse with the same key can seriously compromise security, so nonce management is critical.

---

## Authentication Tag

A cryptographic value used to verify that authenticated encrypted data has not been modified.

---

## Key Derivation Function

A KDF converts a password into cryptographic key material.

This project uses:

```text
Scrypt
```

---

# 🧱 Project Structure Explained

```text
11_file_encryption_tool/
│
├── file_encryptor.py
│
├── requirements.txt
│
└── README.md
```

### `file_encryptor.py`

Contains the complete encryption/decryption implementation and command-line interface.

### `requirements.txt`

Contains the external Python dependency:

```text
cryptography>=46.0
```

### `README.md`

Contains project documentation, installation instructions, usage examples, security information, and troubleshooting.

---

# 📦 Requirements File

The project's `requirements.txt` contains:

```text
cryptography>=46.0
```

Install it with:

```bash
pip install -r requirements.txt
```

---

# 🔍 Useful Commands

Display help:

```bash
python file_encryptor.py --help
```

Encrypt:

```bash
python file_encryptor.py encrypt file.txt
```

Encrypt with custom output:

```bash
python file_encryptor.py encrypt file.txt -o protected.enc
```

Decrypt:

```bash
python file_encryptor.py decrypt file.txt.enc
```

Decrypt with custom output:

```bash
python file_encryptor.py decrypt file.txt.enc -o recovered.txt
```

---

# 🛠️ Development Notes

The implementation intentionally uses the high-level `AESGCM` interface from the `cryptography` library rather than implementing AES manually.

This is important because cryptographic algorithms should generally be provided by well-tested cryptographic libraries rather than implemented from scratch.

The project also uses Scrypt for password-based key derivation rather than directly converting a password into an AES key.

---

# 🔐 Why AES-GCM?

AES-GCM provides:

```text
Confidentiality
        +
Integrity
        +
Authentication
```

This is preferable to using encryption without an integrity/authentication mechanism.

If encrypted data is modified, authentication can detect the change.

---

# 🔐 Why Scrypt?

A password is not automatically a suitable cryptographic key.

Scrypt is designed specifically for password-based key derivation and is intentionally resource-intensive.

The workflow is:

```text
Human Password
      ↓
     Salt
      ↓
    Scrypt
      ↓
256-bit Key
      ↓
 AES-256-GCM
```

---

# 📈 Future Improvements

Possible future improvements include:

* 🔑 Password strength estimation
* 🗂️ Directory encryption support
* 📊 More detailed progress reporting
* 🧪 Automated unit tests
* 🧪 Automated encryption/decryption test suite
* 📝 Better structured logging
* 🔄 Key rotation support
* 🖥️ Optional graphical interface
* 🔐 Additional secure key management options
* 📦 Improved encrypted-file format versioning
* 🧾 File integrity verification commands
* ⚙️ Configuration options
* 📚 Formal security documentation
* 🔍 More extensive error handling
* 🧪 Fuzz testing of the encrypted file format

---

# ⚠️ Ethical & Legal Disclaimer

This project is created for:

* Educational purposes
* Cybersecurity learning
* Personal file protection
* Python programming practice
* Understanding modern encryption concepts

Use it only on files and systems you are authorized to access.

Do not use encryption tools to facilitate:

* Extortion
* Ransomware
* Unauthorized access
* Destruction of data
* Concealment of malicious activity
* Attacks against other users or systems

Always follow applicable laws and organizational policies.

---

# 📖 References

The project uses the Python `cryptography` library.

For official documentation and detailed information about the cryptographic primitives used by this project, refer to the official documentation:

[https://cryptography.io/](https://cryptography.io/)

Important topics to study include:

* AES-GCM
* Scrypt
* AEAD encryption
* Password-based key derivation
* Nonce management

---

# 🎯 Project Goal

The main goal of this project is not simply to encrypt a file.

It is to understand how several security concepts work together:

```text
Password
   ↓
Scrypt
   ↓
Encryption Key
   ↓
AES-256-GCM
   ↓
Authenticated Encryption
   ↓
Encrypted File
```

At the same time, the project demonstrates safe Python file handling through:

```text
Chunked Processing
       ↓
Temporary Output
       ↓
Authentication
       ↓
Successful Completion
       ↓
Atomic Replacement
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

If you find this project useful for learning Python or cybersecurity:

* ⭐ Star the repository
* 🍴 Fork the repository
* 🧑‍💻 Explore the other Python mini projects
* 📚 Use the projects as learning references
* 💡 Suggest improvements

---

# 🏁 Quick Start

If you already have Python installed, the shortest setup is:

```bash
cd 11_file_encryption_tool

python -m venv venv
```

Activate the environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Encrypt a file:

```bash
python file_encryptor.py encrypt secret.txt
```

Decrypt it:

```bash
python file_encryptor.py decrypt secret.txt.enc
```

That's it. 🔐🐍

---

# 📊 Project Status

**Project:** 11 - File Encryption Tool

**Status:** ✅ Completed

**Difficulty:** Advanced

**Category:** Cybersecurity / Cryptography / File Handling

**Language:** Python

**Encryption:** AES-256-GCM

**Key Derivation:** Scrypt

**Processing:** Chunked

**Interface:** Command Line

**Original File Deleted:** ❌ No

**Password Stored:** ❌ No

**Shell Commands:** ❌ No

**`eval()` Used:** ❌ No

---

# 🐍 Part of Python Mini Projects

This project is part of the **Python Mini Projects** repository, where each project focuses on building practical programming skills through hands-on development.

The projects gradually progress from basic Python programming to:

```text
Python Fundamentals
        ↓
File Handling
        ↓
Automation
        ↓
Networking
        ↓
GUI Development
        ↓
CLI Applications
        ↓
Cybersecurity
        ↓
Cryptography
```

**Project 11 — File Encryption Tool** 🔐

Built with Python. Built for learning. Built one project at a time.
