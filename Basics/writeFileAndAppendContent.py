import os
import time

def contentCheck():
    if not os.path.exists("Basics/contentDict.txt"):
        writeNew()
    else:
        with open("Basics/contentDict.txt", "r") as file:
            content = file.read()
            if content.strip():  
                writeContent()
            else:
                writeNew()

def writeNew():
    with open("Basics/contentDict.txt", "w") as file:
        content = input("Enter the content: ")
        file.write(content)

def writeContent():
    with open("Basics/contentDict.txt", "a") as file:
        content = input("Enter the content to be written: ")
        file.write(content)

def readContent():
    with open("Basics/contentDict.txt", "r") as file:
        content = file.read()
        print(content)

while True:
    print("\nMenu:")
    print("1) Write a file")
    print("2) Read the content")
    print("3) Exit")
    try:
        choice = int(input("Enter the choice: "))
        if choice == 1:
            contentCheck()

        elif choice == 2:
            readContent()
        elif choice == 3:
            print("Exiting", end="")
            for _ in range(5):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print("\nGoodbye!")
            break
    except ValueError:
        print("Error: Invalid input.")
