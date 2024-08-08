def string_copies(s, n):
    return s * n
input_string = input("Enter a string: ")
n = int(input("Enter the number of copies: "))
if n < 0:
    print("The number of copies must be a non-negative integer.")
else:
    result = string_copies(input_string, n)
    print(f"The result is: {result}")
