def parse_string(s):
    try:
        value = int(s)
        return value
    except ValueError:
        try:
            value = float(s)
            return value
        except ValueError:
            return "The string is not a valid number."
input_string = input("Enter a string to parse: ")
result = parse_string(input_string)
print(f"Parsed value: {result}")
