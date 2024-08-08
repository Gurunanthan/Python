def check_conditions(a, b):
    return a == b or abs(a + b) == 5 or abs(a - b) == 5
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
result = check_conditions(a, b)
print(f"Result: {result}")
