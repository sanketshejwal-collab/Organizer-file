import os
import shutil

# Change this path to the folder you want to clean up
target_folder = r"your_folder_path_here"

if os.path.exists(target_folder):
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)
        
        # Skip directories, look only at files
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower()
            new_subfolder = os.path.join(target_folder, f"{file_extension}_files")
            
            # Create subfolder if it doesn't exist
            os.makedirs(new_subfolder, exist_ok=True)
            
            # Move file
            shutil.move(file_path, os.path.join(new_subfolder, filename))
    print("Folder organized successfully!")
else:
    print("Folder path not found.")
#just give the folder path and run. it will automatically organize the files in that folder in to subfolders based on their file extensions.
# like .jpg files will go into jpg_files folder, 
# .txt files will go into txt_files folder and so on.
#etc
#make sure to change the target_folder variable to the path of the folder you want to organize before running the script.
#and target_folder should contain files that you want to organize.
# then it will automatically create subfolders based on file extensions and move the files into their respective subfolders.