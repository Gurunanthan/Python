import os

filename = input("Enter the filename: ")

file_name, file_extension = os.path.splitext(filename)

print("The extension of the file is:", file_extension)
