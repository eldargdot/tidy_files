# File Organizer Script

**About:** A simple Python tool that automatically sorts files into extension-based folders, keeping your chosen directory neat and organized.

This Python script automatically organizes files in your **Downloads** directory (or any specified folder) by grouping them into subdirectories based on their file extensions.

## Features

* Scans the target directory for all files.
* Extracts each file’s extension (normalized to lowercase).
* Creates a subfolder named after each extension if it doesn’t already exist.
* Moves each file into its corresponding extension-named subfolder.
* Resolves naming conflicts by appending an incremental suffix (e.g., `_1`, `_2`) to duplicate filenames.
* Prints a log for each move in the format:

  ```
  Moved "original_name.ext" → "ext/clean_name.ext"
  ```

## Prerequisites

* Python 3.x installed on your Linux system.

## Installation and Setup

1. Clone or download this repository to your local machine.
2. Navigate to the project folder:

   ```bash
   cd path/to/project
   ```
3. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux
   ```
4. No external dependencies are required; the script uses only the Python standard library.

## Usage

1. Open `main.py` in a text editor and verify that the `downloads_folder_path` variable points to your desired directory (default: `~/Downloads`).

   ```python
   downloads_folder_path = os.path.expanduser('~/Downloads')
   ```

2. Run the script:

   ```bash
   python3 main.py
   ```

3. Watch the console output to see each file being moved. On completion, all files in the target directory will be sorted into extension-based subfolders.

## How It Works

1. **Directory Check**: Verifies that the target directory exists; otherwise prints an error and exits.
2. **Scan Entries**: Lists all entries (`os.listdir`) in the directory.
3. **Create Subfolders**:

   * Extracts extensions from each filename.
   * Uses `os.makedirs(..., exist_ok=True)` to create a folder for each extension.
4. **Move Files**:

   * Iterates over the entries again, checks `os.path.isfile` to skip subdirectories.
   * Builds a lowercase extension (`ext_clean`) and determines the destination subfolder.
   * Reconstructs the filename to match the cleaned extension.
   * If a file with the same name already exists in the destination, appends `_1`, `_2`, etc., until a unique name is found.
   * Moves the file using `os.rename`.
5. **Logging**: Prints each move in the console for easy tracking.

## Notes

* Hidden files (or files without extensions) are grouped under `no_extension`.
* The script can be adapted to any folder by changing the `downloads_folder_path` variable.
* For large directories, consider adding progress indicators or dry-run mode for safety.

---

Feel free to customize and extend this script to fit your workflow!
