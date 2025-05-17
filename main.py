import os

downloads_folder_path = os.path.expanduser('~/Downloads')

if os.path.isdir(downloads_folder_path):

    entries = os.listdir(downloads_folder_path)

    if entries:
        
        extensions = [os.path.splitext(f)[1].lstrip('.') for f in entries]

        # print(extensions)

        for ext in extensions:
            # print(ext)
            dir_path = os.path.join(downloads_folder_path, ext)
            # print(dir_path)
            if os.path.isdir(dir_path) == False:
                os.makedirs(dir_path, exist_ok=True)

        # უნდა გავაგრძელო რომ დირექტორიის შექმნიშ შემდეგ გადაიტანოს შესაბამისი გაფართოების ფაილები შექმნილ ფოლდერში.
        # მანდ უნდა გავამახვილო ყურადღება იმაზე რომ როცა ერთი და იგივე დასახელების ფაილია რამე მოვუხერხო 

    else:
        print('Download directory is emptry')


else:
    print('Download directory not found')