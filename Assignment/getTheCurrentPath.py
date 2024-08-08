import os
def get_current_file_info():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    print(f"Full Path: {file_path}")
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
get_current_file_info()
