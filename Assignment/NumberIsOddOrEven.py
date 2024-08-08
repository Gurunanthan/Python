def check_even_or_odd(number):
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
number = int(input("Enter a number: "))
check_even_or_odd(number)
