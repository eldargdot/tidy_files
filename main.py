import subprocess
import time
import shutil
import os
import re
import platform

if platform.system() == "Windows":
    import winsound

def main():

    def beep(freq: int = 1000, duration_s: float = 0.5, volume_pct: int = 50):
        """Cross-platform beep:
        - on Windows uses winsound.Beep
        - on Linux/macOS uses speaker-test + amixer (ALSA)"""
        system = platform.system()

        if system == "Windows":
            winsound.Beep(freq, int(duration_s * 1000))
            return

        if not shutil.which("speaker-test"):
            raise RuntimeError("speaker-test not found; please install alsa-utils")
        if not shutil.which("amixer"):
            raise RuntimeError("amixer not found; please install alsa-utils")

        out = subprocess.check_output(
            ["amixer", "sget", "Master"], stderr=subprocess.DEVNULL
        ).decode()
        m = re.search(r"\[(\d+)%\]", out)
        old_volume = m.group(1) + "%" if m else "100%"

        subprocess.run(
            ["amixer", "sset", "Master", f"{volume_pct}%"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )

        proc = subprocess.Popen(
            ["speaker-test", "-t", "sine", "-f", str(freq)],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        time.sleep(duration_s)
        proc.kill()
        proc.wait()

        subprocess.run(
            ["amixer", "sset", "Master", old_volume],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )

    home_path = os.path.expanduser('~/')

    entries = os.listdir(home_path)

    directories = [
        name
        for name in entries
        if not name.startswith('.') and os.path.isdir(os.path.join(home_path, name))
    ]

    dir_list_str = ", ".join(directories)
    question = (
        "Directories in home (excluding hidden): " + dir_list_str +
        "\nChoose one, or type 'help' for instructions, or 'quit' to exit: "
    )

    
    directories_to_lowercase = [item.lower() for item in directories]

    while True:
        
        answer = input(question).strip()

        if answer.lower() == 'quit':
            confirm = input("Are you sure you want to quit? [y/n]: ").strip().lower()
            if confirm == 'y':
                return
            elif confirm == 'n':
                continue
            else:
                print("Please answer 'y' or 'n'.")
                continue

        help = '''

Help:

This script lists all non-hidden folders in your home directory and asks you to choose one. Once you pick a folder, it scans that folder for files and moves each file into a subfolder named after its extension (all in lowercase). Files without an extension go into a “no_extension” folder. If a file with the same name already exists in the destination, the script appends “_1”, “_2”, etc., to avoid overwriting. After moving each file, it prints a line showing the original name and its new location, and finally reports “Processing finished.”

If you press Enter without typing a name or type a directory that doesn’t exist, the script plays a short beep and asks again.

To run the script, use:
python main.py

On Windows, it uses the built-in winsound module for the beep. On Linux or macOS, it requires the alsa-utils package (amixer and speaker-test) to set volume and play a sine-wave tone. You can customize the beep’s frequency, duration, and (on Linux/macOS) volume by changing the arguments to the beep function in the code.
        
        '''

        if answer.lower() == 'help':
            print(help)
            continue

        if len(answer) == 0:
            beep(3000, 0.3, volume_pct=70)
            print("Please enter the correct directory name.")
            continue

        if answer.lower() not in directories_to_lowercase:
            beep(3000, 0.3, volume_pct=70)
            print('Directory not found.')
            continue

        downloads_folder_path = os.path.expanduser('~/' + answer)

        if not os.path.isdir(downloads_folder_path):
            print('Directory not found.')
            continue

        entries = os.listdir(downloads_folder_path)

        files = [
            name
            for name in entries
            if os.path.isfile(os.path.join(downloads_folder_path, name))
        ]

        if not files:
            print("No files found in the directory.")
            continue

        if entries:
            extensions = [os.path.splitext(f)[1].lstrip('.') for f in entries]

            for ext in extensions:
                dir_path = os.path.join(downloads_folder_path, ext)
                if not os.path.isdir(dir_path):
                    os.makedirs(dir_path, exist_ok=True)

            for name in os.listdir(downloads_folder_path):
                src = os.path.join(downloads_folder_path, name)
                if os.path.isfile(src):
                    root, ext = os.path.splitext(name)
                    ext_clean = ext.lstrip('.').lower() or 'no_extension'
                    target_dir = os.path.join(downloads_folder_path, ext_clean)
                    if not os.path.isdir(target_dir):
                        continue

                    base_name = f"{root}.{ext_clean}" if ext else root
                    dest_path = os.path.join(target_dir, base_name)
                    counter = 1
                    while os.path.exists(dest_path):
                        new_name = f"{root}_{counter}.{ext_clean}" if ext else f"{root}_{counter}"
                        dest_path = os.path.join(target_dir, new_name)
                        counter += 1

                    os.rename(src, dest_path)
                    dir_name = os.path.basename(target_dir)
                    file_name = os.path.basename(dest_path)
                    print(f'Moved "{name}" → "{dir_name}/{file_name}"')
            print("Processing finished.")
        else:
            print('Download directory is empty')

if __name__ == '__main__':
    main()
