def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
