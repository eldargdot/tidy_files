import os

def main():
    home_path = os.path.expanduser('~/')

    entries = os.listdir(home_path)

    directories = [
        name
        for name in entries
        if not name.startswith('.') and os.path.isdir(os.path.join(home_path, name))
    ]

    dir_list_str = ", ".join(directories)
    question = "Directories in home (excluding hidden): " + dir_list_str + "\nChoose: "
    
    directories_to_lowercase = [item.lower() for item in directories]

    while True:
        answer = input(question).strip()

        if len(answer) == 0:
            print("Please enter the correct directory name.")
            continue

        if answer.lower() not in directories_to_lowercase:
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
