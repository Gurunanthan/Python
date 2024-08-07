CommaSeparatedString = input("")
numbers_in_list = []
numbers_set = set()

for i in CommaSeparatedString:
    if i.isdigit():
        numbers_in_list.append(i)

numbers_in_tuples = tuple(numbers_in_list)

print("Numbers in list:", numbers_in_list)
print("Numbers in tuples:", numbers_in_tuples)
