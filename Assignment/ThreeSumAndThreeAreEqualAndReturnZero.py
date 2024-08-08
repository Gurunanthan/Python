def sum_of_three(a, b, c):
    if a == b or b == c or a == c:
        return 0
    return a + b + c
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))
result = sum_of_three(a, b, c)
print(f"The result is: {result}")
