def lcm(a, b):
    multiple = max(a, b)
    while True:
        if multiple % a == 0 and multiple % b == 0:
            return multiple
        multiple += 1
num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")
