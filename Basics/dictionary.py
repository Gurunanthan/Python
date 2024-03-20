dicts = {}
def display():
    for key, value in dicts.items():
        print("{}={}".format(key, value))
while True:
    choice = int(input("Enter the choice: "))
    if choice!=0:
        keys = int(input("enter the key"))
        values = str(input("Enter the value"))
        dicts[keys] = values
    else:
        display()
        break