def sum_or_triple_sum(a, b, c):
    sum_of_numbers = a + b + c
    if a == b == c:
        return 3 * sum_of_numbers
    else:
        return sum_of_numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = sum_or_triple_sum(num1, num2, num3)

print(f"The result is: {result}")
