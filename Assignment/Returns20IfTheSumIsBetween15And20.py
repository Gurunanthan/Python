def sum_with_condition(a, b):
    total = a + b
    if 15 <= total <= 20:
        return 20
    return total
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
result = sum_with_condition(a, b)
print(f"The result is: {result}")
