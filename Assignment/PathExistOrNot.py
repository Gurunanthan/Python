import os
def check_file_exists(file_path):
    return os.path.isfile(file_path)
file_path = input("Enter the file path: ")
if check_file_exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")
