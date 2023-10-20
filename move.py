import shutil
import os


# path = 'D:/vscode/moveFolder/Module1-3'
# dirname = os.path.dirname(path) 
# print(dirname) 

main_folder = 'D:/vscode/moveFolder/Module4_Lab1'
subfolders = os.listdir(main_folder)


# for subfolder in subfolders:
#     print(subfolder)


for subfolder in subfolders:
    print(subfolder)
    subfolder_path = os.path.join(main_folder, subfolder)
    # print(subfolder_path)
    for root, dirs, files in os.walk(subfolder_path):
        print(files)
        for file in files:
            
            # Get the full path of the file in the subfolder
            source_path = os.path.join(root, file)
            
            # Construct the destination path in the main folder
            destination_path = os.path.join(main_folder, file)
            
            try:
                # Move the file to the main folder
                shutil.move(source_path, destination_path)
                print(f"Moved {file} from {subfolder} to {main_folder}")
            except shutil.Error as e:
                print(f"Error moving {file}: {e}")
            except IOError as e:
                print(f"Error: {e}")

