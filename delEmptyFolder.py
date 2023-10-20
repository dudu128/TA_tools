import os

# Specify the directory path from which you want to delete empty folders
directory_path = 'D:/vscode/moveFolder/Module4_Lab1'

def delete_empty_folders(path):
    for folder_name in os.listdir(path):
        folder_path = os.path.join(path, folder_name)

        if os.path.isdir(folder_path):
            # Recursively call the function for subfolders
            delete_empty_folders(folder_path)

            # Check if the folder is empty and delete it
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
                print(f'Deleted empty folder: {folder_path}')

# Start the process from the top-level directory
delete_empty_folders(directory_path)