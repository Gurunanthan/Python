def height_to_centimeters(feet, inches):
    feet_to_cm = 30.48
    inches_to_cm = 2.54
    total_cm = (feet * feet_to_cm) + (inches * inches_to_cm)
    return total_cm
feet = int(input("Enter height in feet: "))
inches = int(input("Enter height in inches: "))
if inches >= 0 and inches < 12:
    height_cm = height_to_centimeters(feet, inches)
    print(f"Height in centimeters: {height_cm:.2f} cm")
else:
    print("Please enter a valid number of inches (0-11).")
