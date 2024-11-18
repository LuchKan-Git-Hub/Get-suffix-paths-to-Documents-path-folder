import os
import shutil
import time
import colorama

def main(doc_path, suffix):
    #Paths
    downloads_folder = os.path.expanduser('~/Downloads')
    document_folder = os.path.expanduser(f"~/Documents/{doc_path}")

    # create if not exist
    if not os.path.exists(document_folder):
        os.makedirs(document_folder)
        print(f'created path named {document_folder}')
        time.sleep(1)

    #   monitors print
    print(f'Monitoring {downloads_folder} tp {document_folder}')

    while True:
        try:
            # List all files in the Downloads folder
            for filename in os.listdir(downloads_folder):
                # Full path to the file
                full_file_path = os.path.join(downloads_folder, filename)

                # Check if the file ends with the suffix
                if filename.endswith(suffix):
                    # Move the file to the Images folder
                    shutil.move(full_file_path, document_folder)
                    print(f"Moved: {filename} to {document_folder}")
        except Exception as e:
            colorama.init()
            print(colorama.Fore.RED + f"Error: {e}")

# get data from user
print('Will add a path or identity which one you need')
choose = input('Type here:  ')
print('Choose suffix like .png .iso and more')
choose_2 = input('Type here:   ')

# run main
main(choose, choose_2)