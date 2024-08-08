def count_number_in_list(lst, number):
    return lst.count(number)
numbers_list = [1, 4, 2, 4, 3, 4, 5, 4]
count = count_number_in_list(numbers_list, 4)
print(f"The number 4 appears {count} times in the list.")
