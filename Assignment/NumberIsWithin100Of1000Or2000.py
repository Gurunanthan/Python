def is_the_number_within_100_of_1000_or_2000(n):
    return abs(1000 - n) <= 100 or abs(2000 - n) <= 100
number = int(input("Enter a number: "))
result = is_the_number_within_100_of_1000_or_2000(number)

if result:
    print(f"The number is within 100 of 1000 or 2000.")
else:
    print(f"The number is not within 100 of 1000 or 2000.")
