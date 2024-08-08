def is_value_in_group(value, group):
    return value in group
test_values = [3, -1]
group_values = [1, 5, 8, 3]
for test_value in test_values:
    result = is_value_in_group(test_value, group_values)
    print(f"{test_value} -> {group_values} : {result}")
