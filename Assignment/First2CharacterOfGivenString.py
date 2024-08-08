def get_copies(s, n):
    if len(s) < 2:
        return s * n
    else:
        return s[:2] * n
input_string = input("Enter a string: ")
n = int(input("Enter the number of copies: "))
if n < 0:
    print("The number of copies must be a non-negative integer.")
else:
    result = get_copies(input_string, n)
    print(f"The result is: {result}")
