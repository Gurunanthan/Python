import os
import shutil

source_path = "C:/Users/Gurunanthan/Downloads/Installation and Drivers"
destination_path = "C:/Users/Gurunanthan/Downloads/Installation and Drivers"

# Create destination directories if they don't exist
file_type_folders = {
    ".exe": "exe",
    ".doc": "words",
    ".docx": "words",
    ".zip": "zip",
    ".rar": "rar",
    ".ppt": "ppt",
    ".pptx": "ppt",
    ".xls": "excel",
    ".xlsx": "excel",
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".gif": "images",
    ".bmp": "images",
    ".pdf": "pdf"
}

# Create 'others' folder
others_folder = "others"
others_folder_path = os.path.join(destination_path, others_folder)
os.makedirs(others_folder_path, exist_ok=True)

# Get the list of files in the source directory
files = os.listdir(source_path)

# Iterate through each file in the directory
for file in files:
    # Check if the file has an extension
    if "." in file:
        # Get the file extension
        file_extension = os.path.splitext(file)[1]
        
        # Check if the file extension is in the file_type_folders dictionary
        if file_extension in file_type_folders:
            # Construct the source and destination paths
            source_file_path = os.path.join(source_path, file)
            destination_folder = file_type_folders[file_extension]
            destination_folder_path = os.path.join(destination_path, destination_folder)
            destination_file_path = os.path.join(destination_folder_path, file)
            
            # Move the file to the destination directory
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved {file} to {destination_folder_path}")
        else:
            # If file extension not found in dictionary, move it to 'others' folder
            source_file_path = os.path.join(source_path, file)
            destination_file_path = os.path.join(others_folder_path, file)
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved {file} to {others_folder_path}")
