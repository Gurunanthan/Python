import os
def list_files_in_directory(directory):
    try:
        entries = os.listdir(directory)
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]
        if files:
            print("Files in the directory:")
            for file in files:
                print(file)
        else:
            print("No files found in the directory.")
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {directory}.")
directory = input("Enter the directory path: ")
list_files_in_directory(directory)
