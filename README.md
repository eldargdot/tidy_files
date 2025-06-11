# Interactive File Organizer

**About:**
A Python script that interactively organizes files in any home subdirectory you choose, sorting them into extension-based folders for a tidier workspace.

This tool prompts you to pick a directory from your home folder, then automatically groups and moves all files inside into subfolders named after each file’s extension.

---

## Features

* **Interactive prompt:** Lists all visible directories in your home and asks you to select one.
* **Flexible directory selection:** Works on any subfolder (e.g., `Downloads`, `Desktop`, etc.), not just `Downloads`.
* **Automatic sorting:** Detects each file’s extension (lowercase), creates corresponding folders if needed, and moves files accordingly.
* **Duplicate handling:** Renames files with suffixes like `_1`, `_2`, etc. if a filename conflict is detected.
* **Logging:** Prints a log for every file moved, e.g.:

  ```
  Moved "example.docx" → "docx/example.docx"
  ```
* **Cross-platform:** Works on Linux, macOS, and Windows.

---

## Prerequisites

* Python 3.x installed (works on Linux, Windows, and macOS)
* No external libraries required (standard library only)

---

## Installation and Setup

1. **Clone or download** this repository to your machine.
2. Navigate to the project folder:

   ```bash
   cd path/to/project
   ```
3. *(Optional)* Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On Linux/macOS
   .\venv\Scripts\activate      # On Windows
   ```
4. **No further dependencies** are needed.

---

## Usage

1. **Run the script**:

   ```bash
   python3 main.py
   ```
2. **Follow the prompt** to select a directory (e.g., Downloads, Documents, Desktop, etc.).
3. The script will:

   * Sort all files in the chosen folder into extension-based subfolders
   * Print a log for every file moved

---

## How It Works

1. **Prompts for directory:** Lists home subdirectories (excluding hidden ones) and asks you to choose.
2. **Validates input:** Asks again if the directory does not exist or is empty.
3. **Scans files:** Identifies all files in the selected directory.
4. **Creates subfolders:** For each file extension (in lowercase), creates a folder if it doesn’t already exist.
5. **Moves files:** Transfers each file into its corresponding extension folder, appending suffixes for duplicates as needed.
6. **Prints a move log** for every action taken.

---

## Notes

* Hidden files and files without extensions are placed in a `no_extension` folder.
* Works with any user-accessible directory inside your home folder.
* For very large directories, you can adapt the script to add a progress bar or dry-run mode.

---

Feel free to modify and expand the script to suit your needs! Pull requests and suggestions are always welcome.

---
