def add_if_integer(obj1, obj2):
    if isinstance(obj1, int) and isinstance(obj2, int):
        return obj1 + obj2
    return "Both objects must be integers."
obj1 = input("Enter the first object: ")
obj2 = input("Enter the second object: ")
try:
    obj1 = int(obj1)
    obj2 = int(obj2)
except ValueError:
    print("Invalid input. Please enter valid integers.")
else:
    result = add_if_integer(obj1, obj2)
    print(f"Result: {result}")
