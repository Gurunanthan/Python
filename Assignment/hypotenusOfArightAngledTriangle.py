import math

def calculate_hypotenuse(a, b):
    # Calculate the hypotenuse using the Pythagorean theorem
    c = math.sqrt(a**2 + b**2)
    return c

# Example usage
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))

# Calculate the hypotenuse
hypotenuse = calculate_hypotenuse(a, b)
print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
