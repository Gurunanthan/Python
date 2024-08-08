import os
import datetime
def get_file_times(file_path):
    creation_time = os.path.getctime(file_path)
    modification_time = os.path.getmtime(file_path)
    creation_time = datetime.datetime.fromtimestamp(creation_time)
    modification_time = datetime.datetime.fromtimestamp(modification_time)
    return creation_time, modification_time
file_path = input("Enter the file path: ")
if os.path.exists(file_path):
    creation_time, modification_time = get_file_times(file_path)
    print(f"Creation Time: {creation_time}")
    print(f"Last Modified Time: {modification_time}")
else:
    print("File does not exist.")
