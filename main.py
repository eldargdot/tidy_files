import os

downloads_folder_path = os.path.expanduser('~/Downloads')

if os.path.isdir(downloads_folder_path):

    entries = os.listdir(downloads_folder_path)

    if entries:
        
        extensions = [os.path.splitext(f)[1].lstrip('.') for f in entries]

        for ext in extensions:

            # print(ext)
            
            dir_path = os.path.join(downloads_folder_path, ext)

            # print(dir_path)

            if os.path.isdir(dir_path) == False:
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

    else:
        print('Download directory is emptry')


else:
    print('Download directory not found')

