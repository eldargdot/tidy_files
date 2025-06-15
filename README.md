# File Organizer Script

**About**
A cross-platform Python tool that interactively sorts files into extension-based folders and provides audible feedback for invalid input. **Supports Windows, Linux, and macOS**.

---

## Features

* **Interactive directory selection**

  * Lists all non-hidden folders in your home directory
  * Prompts you to choose one (case-insensitive)
  * Supports special commands:

    * Type **help** to display usage instructions
    * Type **quit** to exit the script

* **Cross-platform beep**

  * Windows: uses `winsound.Beep(freq, duration_ms)`
  * Linux/macOS: temporarily sets ALSA Master volume, plays a sine-wave tone, then restores volume
  * Default beep: 3000 Hz for 0.3 s at 70% volume

* **Automatic sorting**

  * Scans the chosen folder for files (ignores subfolders)
  * Extracts each file’s extension (lowercased) or uses `no_extension` if none
  * Creates one subfolder per extension if needed
  * Moves each file into the matching subfolder

* **Duplicate handling**

  * Appends `_1`, `_2`, … to the filename when a conflict occurs

* **Clear feedback**

  * For invalid or empty input: beep + error message + re-prompt
  * Logs every move as:

    ```
    Moved "original_name.ext" → "ext/clean_name.ext"  
    ```
  * Prints **“Processing finished.”** when done

---

## Prerequisites

* **Python 3.x** on your system
* **Windows**: no extra packages needed
* **Linux/macOS**: install `alsa-utils` (provides `amixer` + `speaker-test`)

---

## Installation

1. Save the script as `main.py` (or another name of your choice).
2. On Linux/macOS, if needed:

   ```bash
   sudo apt install alsa-utils  
   ```

---

## Usage

```bash
python main.py  
```

---

## Interactive Flow

1. The script scans `~/` and lists all non-hidden subfolders.

2. It displays a prompt, for example:

   ```
   Directories in home (excluding hidden): Documents, Downloads, Music  
   Choose one, or type 'help' for instructions, or 'quit' to exit:  
   ```

3. **Commands**:

   * **help**: prints this usage summary and re-prompts
   * **quit**: asks “Are you sure you want to quit? \[y/n]: ”

     * `y`: exits the script
     * `n`: returns to the directory prompt

4. If you enter a valid folder name, the script proceeds to sort its files.

---

## How It Works

1. **Beep function**

   * Detects `platform.system()`
   * On Windows: calls `winsound.Beep()`
   * On Linux/macOS:

     1. Checks for `speaker-test` + `amixer`
     2. Reads current Master volume
     3. Sets volume to the desired level
     4. Runs `speaker-test -t sine -f <freq>`
     5. Sleeps for `<duration_s>`
     6. Kills the tone process and restores original volume

2. **Directory prompt & validation**

   * Loops until the user types a non-empty, existing directory name or `quit`

3. **File scan & folder creation**

   * Builds a set of lowercase extensions from files only
   * Creates one subfolder per extension with `os.makedirs(..., exist_ok=True)`

4. **File moves**

   * Constructs a unique destination path, resolving duplicates with `_1`, `_2`, etc.
   * Renames/moves files via `os.rename()`
   * Prints a log entry for each move

5. **Completion**

   * Prints **“Processing finished.”** and exits (unless re-run manually)

---

## Example Session

```bash
$ python main.py  
Directories in home (excluding hidden): Desktop, Documents, Downloads, Music  
Choose one, or type 'help' for instructions, or 'quit' to exit: Downloads  

Moved "report.pdf" → "pdf/report.pdf"  
Moved "photo.JPG" → "jpg/photo.jpg"  
Moved "README" → "no_extension/README"  
Processing finished.  
```

---

Feel free to adjust beep frequency, duration, or volume in the `beep()` call at the top of `main.py`!
