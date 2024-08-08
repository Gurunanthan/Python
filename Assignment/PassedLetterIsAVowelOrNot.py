def is_vowel(letter):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return letter.lower() in vowels
letter = input("Enter a letter: ")
if len(letter) != 1 or not letter.isalpha():
    print("Please enter a single alphabetical character.")
else:
    if is_vowel(letter):
        print(f"The letter '{letter}' is a vowel.")
    else:
        print(f"The letter '{letter}' is not a vowel.")
