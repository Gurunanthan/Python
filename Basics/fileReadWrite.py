def fileWrite():
    with open("Example.txt",'w') as file:
        content = input("Enter the content for the file")
        file.write(content)
        file.close()
        fileRead()


def fileRead():
    with open("Example.txt",'r') as file:
        content = file.read().split(' ')
        print(content)

fileWrite()