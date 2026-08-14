# 📁 File Organizer

A simple Python automation tool that automatically organizes files into separate folders based on their file extensions.

This project is designed to make messy folders easier to manage by automatically sorting files into categories such as Images, Videos, Documents, Audio, Archives, Programs, and Others.

---

## ✨ Features

- 📂 Organize files automatically
- 🖼️ Sort image files
- 🎬 Sort video files
- 📄 Sort documents
- 🎵 Sort audio files
- 📦 Sort archive files
- 💻 Sort programming files
- 📁 Create category folders automatically
- ❓ Place unknown file types into an `Others` folder
- 🛡️ Check whether the selected folder exists
- 🚫 Ignore existing folders
- ⚡ Simple command-line interface
- 📦 No external Python packages required

---

## 🛠️ Technologies Used

- Python 3
- `os`
- `shutil`

Both `os` and `shutil` are included in Python's standard library.

---

## 📋 Requirements

- Python 3.8 or newer
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

Clone the complete repository:

```bash
git clone https://github.com/Avinash-05-web/python-mini-projects.git
```

Enter the repository:

```bash
cd python-mini-projects
```

Enter the File Organizer project:

```bash
cd 04_file_organizer
```

No additional packages are required.

---

## ▶️ Run the Program

Run:

```bash
python file_organizer.py
```

On systems using `python3`:

```bash
python3 file_organizer.py
```

---

## 📖 How to Use

When the program starts, it asks for the folder path you want to organize.

Example:

```text
Enter the folder path to organize: C:\Users\YourName\Downloads
```

The program will scan the selected folder and move files into appropriate category folders.

---

## 📂 Supported Categories

### 🖼️ Images

Supported extensions:

```text
.jpg
.jpeg
.png
.gif
.bmp
.webp
```

Files are moved into:

```text
Images/
```

### 🎬 Videos

Supported extensions:

```text
.mp4
.mkv
.avi
.mov
.wmv
```

Files are moved into:

```text
Videos/
```

### 📄 Documents

Supported extensions:

```text
.pdf
.doc
.docx
.txt
.xlsx
.xls
.ppt
.pptx
```

Files are moved into:

```text
Documents/
```

### 🎵 Audio

Supported extensions:

```text
.mp3
.wav
.flac
.aac
.ogg
```

Files are moved into:

```text
Audio/
```

### 📦 Archives

Supported extensions:

```text
.zip
.rar
.7z
.tar
.gz
```

Files are moved into:

```text
Archives/
```

### 💻 Programs

Supported extensions:

```text
.py
.js
.java
.cpp
.c
.html
.css
```

Files are moved into:

```text
Programs/
```

### ❓ Unknown Files

Files with extensions that are not included in the categories above are moved into:

```text
Others/
```

---

## 🧪 Example

Before running the program:

```text
PythonTest/
│
├── photo.jpg
├── song.mp3
├── movie.mp4
├── resume.pdf
├── project.py
└── archive.zip
```

After running the program:

```text
PythonTest/
│
├── Images/
│   └── photo.jpg
│
├── Audio/
│   └── song.mp3
│
├── Videos/
│   └── movie.mp4
│
├── Documents/
│   └── resume.pdf
│
├── Programs/
│   └── project.py
│
└── Archives/
    └── archive.zip
```

---

## 💻 Example Output

```text
Enter the folder path to organize: C:\PythonTest

Moved: photo.jpg → Images/
Moved: song.mp3 → Audio/
Moved: movie.mp4 → Videos/
Moved: resume.pdf → Documents/
Moved: project.py → Programs/
Moved: archive.zip → Archives/

========================================
       FILE ORGANIZATION COMPLETE
========================================
```

---

## 📂 Project Structure

```text
04_file_organizer/
│
├── file_organizer.py
└── README.md
```

---

## 🧠 Python Concepts Used

This project demonstrates:

* Variables
* User input
* Conditional statements
* Loops
* Dictionaries
* Functions and modules
* File paths
* File extensions
* Directory handling
* File movement
* Automation
* Error checking
* Python standard library

---

## 🔧 How It Works

The program follows these basic steps:

```text
User selects a folder
        ↓
Check whether the folder exists
        ↓
Scan files inside the folder
        ↓
Read each file's extension
        ↓
Identify the correct category
        ↓
Create the category folder
        ↓
Move the file
        ↓
Display the result
```

---

## ⚠️ Important Safety Note

Always test the program on a **temporary folder first**.

For example:

```text
PythonTest/
```

Do not initially run it against important folders such as:

```text
C:\Windows
C:\Program Files
Desktop
Documents
```

unless you understand exactly which files the program will move.

The program moves files rather than deleting them, but you should still make a backup of important data before using automation tools on real folders.

---

## 🔧 Troubleshooting

### Folder does not exist

If you enter an invalid path, the program will display:

```text
Error: Folder does not exist.
```

Make sure the folder path is correct.

### Windows Path

You can enter a Windows path such as:

```text
C:\Users\YourName\Downloads
```

### Linux/macOS Path

You can use:

```text
/home/username/Downloads
```

or:

```text
/Users/username/Downloads
```

---

## 🚀 Future Improvements

Planned improvements include:

* [ ] Duplicate filename protection
* [ ] Preview files before moving them
* [ ] Dry-run mode
* [ ] Custom categories
* [ ] Custom file extensions
* [ ] GUI interface
* [ ] Progress indicator
* [ ] Organization summary
* [ ] Undo functionality
* [ ] Logging
* [ ] Recursive subfolder organization
* [ ] Configuration file
* [ ] Ignore selected folders

---

## ⚠️ Disclaimer

This project is created for educational and automation purposes.

Always verify the target folder before running the program. The author is not responsible for unintended file organization or data loss resulting from misuse of the software.

---

## 👨‍💻 Author

**Avinash Das Manikpuri**

GitHub:

[https://github.com/Avinash-05-web](https://github.com/Avinash-05-web)

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

More Python projects coming soon! 🚀

