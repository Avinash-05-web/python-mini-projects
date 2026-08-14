import os
import shutil


# Folder that we want to organize
folder_path = input("Enter the folder path to organize: ").strip()

# Check if the folder exists
if not os.path.isdir(folder_path):
    print("Error: Folder does not exist.")
    exit()


# File extension categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".py", ".js", ".java", ".cpp", ".c", ".html", ".css"],
}


# Go through every item in the folder
for filename in os.listdir(folder_path):

    file_path = os.path.join(folder_path, filename)

    # Ignore folders
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    extension = os.path.splitext(filename)[1].lower()

    # Find the correct category
    category_found = False

    for category, extensions in categories.items():

        if extension in extensions:

            category_path = os.path.join(folder_path, category)

            # Create category folder if it doesn't exist
            os.makedirs(category_path, exist_ok=True)

            # Move the file
            shutil.move(
                file_path,
                os.path.join(category_path, filename)
            )

            print(f"Moved: {filename} → {category}/")

            category_found = True
            break

    # Files with unknown extensions
    if not category_found:

        other_path = os.path.join(folder_path, "Others")

        os.makedirs(other_path, exist_ok=True)

        shutil.move(
            file_path,
            os.path.join(other_path, filename)
        )

        print(f"Moved: {filename} → Others/")


print("\n========================================")
print("       FILE ORGANIZATION COMPLETE")
print("========================================")
