import os
import shutil
from datetime import datetime
import zipfile

new_dir = input('Name of new directory: ')

pre_path = 'C:\\Users\\johannes.falnes\\PycharmProjects\\NoroffVC\\Module 5\\M5L1\\folder'
new_path = f'C:\\Users\\johannes.falnes\\PycharmProjects\\NoroffVC\\Module 5\\M5L1\\{new_dir}'

os.mkdir(new_path)

def copy_files(PRE_PATH, PATH):

    time_now = datetime.now()
    time_now = str(time_now)

    for current, subdirectories, files in os.walk(PRE_PATH):
        print("Current directory:",current)
        for current_subdir in subdirectories:
            print("Subdirectory:", current_subdir)
            
        for current_file in files:
            print("File:", current_file)

            split_file = current_file.split('.')
            new_name = f'{split_file[0]}{time_now[:10]}.{split_file[1]}'
            os_path = os.path.join(PRE_PATH, current_file)

            shutil.copy(os_path, f'{PATH}\{new_name}')


def list_dir(PATH):
    for current, subdirectories, files in os.walk(PATH):
        print("Current directory:",current)
    for current_subdir in subdirectories:
        print("Subdirectory:", current_subdir)

    for current_file in files:
        print("File:", current_file)
        
    print()

def zip_dir(PATH):

    with zipfile.ZipFile('noroff.zip', 'w') as zip:
        for current, subdirectories, files in os.walk(PATH):
            print("Current directory:",current)
        for current_subdir in subdirectories:
            print("Subdirectory:", current_subdir)

        for current_file in files:
            print("File:", current_file)
            zip.write(f'{PATH}\{current_file}')

copy_files(pre_path, new_path)
list_dir(new_path)
zip_dir(new_path)