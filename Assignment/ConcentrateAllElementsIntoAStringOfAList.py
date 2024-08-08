def concatenate_list_elements_in_the_list(lst):
    str_elements = map(str, lst)
    concatenated_string = ''.join(str_elements)
    return concatenated_string
sample_list = ['Hello', ' ', 'World', 'hi', ' How', ' are', ' you?']
result = concatenate_list_elements_in_the_list(sample_list)
print(f"The concatenated string is: '{result}'")
