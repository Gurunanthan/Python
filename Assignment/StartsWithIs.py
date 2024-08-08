def add_is_prefix(s):
    if s.startswith("Is"):
        return s
    else:
        return "Is" + s
input_string = input("Enter a string: ")
result = add_is_prefix(input_string)

print(f"{result}")
