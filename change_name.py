import os

# Specify the directory path where you want to change folder names
main_folder = 'D:/vscode/moveFolder/Module4_Lab1'
subfolders = os.listdir(main_folder)

def is_numeric(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

for folder_name in os.listdir(main_folder):
    if not is_numeric(folder_name):
        new_folder_name = ''.join(filter(str.isdigit, folder_name))
        new_folder_path = os.path.join(main_folder, new_folder_name)
        old_folder_path = os.path.join(main_folder, folder_name)
        
        try:
            os.rename(old_folder_path, new_folder_path)
            print(f'Renamed folder "{folder_name}" to "{new_folder_name}"')
        except OSError as e:
            print(f'Error renaming folder "{folder_name}": {e}')