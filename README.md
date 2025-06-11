# File Organizer Script

**About:**
A simple Python tool for Linux that interactively sorts files into extension-based folders, keeping your chosen directory neat and organized.

Instead of hard-coding a target folder, this script prompts you to pick any visible subdirectory in your home folder. It then automatically groups all files inside into subdirectories named after each file’s extension.

---

## Features

* **Interactive directory selection:**

  * Lists all non-hidden folders in your home directory
  * Prompts you to choose one
  * Re-asks until you enter a valid, non-empty name
* **Flexible target folder:** Works on any home subdirectory (e.g., `Downloads`, `Documents`, `Desktop`, etc.)
* **Automatic sorting:**

  * Scans the chosen directory for all files
  * Extracts each file’s extension (normalized to lowercase)
  * Creates a subfolder for each extension if it doesn’t already exist
  * Moves each file into the matching subfolder
* **Duplicate handling:** Appends incremental suffixes (`_1`, `_2`, …) when a file name conflict occurs
* **Clear feedback:**

  * Prints “Directory not found” or “No files found” and re-prompts as needed
  * Logs every move in the format:

    ```
    Moved "original_name.ext" → "ext/clean_name.ext"
    ```
* **Processing complete message:** Informs you when sorting has finished
* **Linux only:** Uses standard Python libraries and `~/` paths suited for Linux home folders

---

## Prerequisites

* Python 3.x installed on your Linux system
* No external dependencies (standard library only)

---

## Installation and Setup

1. **Clone or download** this repository.
2. Open a terminal and navigate to the project folder:

   ```bash
   cd path/to/project
   ```
3. *(Optional)* Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

---

## Usage

1. Run the script:

   ```bash
   python3 main.py
   ```
2. When prompted, select one of the listed directories (e.g., `Downloads`, `Documents`, `Desktop`).
3. The script will:

   * Validate your input and re-prompt on errors
   * Sort all files in the chosen directory into extension-named subfolders
   * Print a log line for each moved file
   * Show **Processing finished.** when done

---

## How It Works

1. **Directory prompt & validation:**

   * Lists `~/` subfolders (excludes hidden)
   * Loops until you provide a non-empty, existing directory name
2. **File scan:** Uses `os.listdir` and `os.path.isfile` to identify files
3. **Folder creation:**

   * Extracts lowercase extensions via `os.path.splitext`
   * Creates each extension folder with `os.makedirs(..., exist_ok=True)`
4. **File moves:**

   * Builds a unique destination path, resolving duplicates with `_1`, `_2`, etc.
   * Renames/moves files using `os.rename`
   * Prints a log entry for every move
5. **Completion:** Prints “Processing finished.” and then re-prompts if you run it again

---

## Notes

* Files without an extension are placed in `no_extension`.
* Hidden files/folders (starting with `.`) are ignored in the initial prompt.
* Designed and tested on Linux; paths use `~/`.

---

Feel free to customize, extend, or contribute enhancements!
