import struct
def check_python_architecture():
    architecture = struct.calcsize("P") * 8
    print(f"Python is running in {architecture}-bit mode.")
check_python_architecture()
