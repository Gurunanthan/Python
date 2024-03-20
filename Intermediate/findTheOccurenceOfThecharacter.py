string = str(input("Enter the string: "))
dicts = {}
for character in string:
    if character in dicts:
        dicts[character] += 1
    else:
        dicts[character] = 1

# Print the dictionary
for key, value in dicts.items():
    print(key, ":", value)

# Find the maximum occurring element
max_occurrence_key, max_occurrence_value = max(dicts.items(), key=lambda x: x[1])
print("Maximum occurring element:", max_occurrence_key)
print("Occurrence count:", max_occurrence_value)
