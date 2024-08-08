def find_unique_colors(color_list_1, color_list_2):
    unique_colors = color_list_1 - color_list_2
    return unique_colors
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
result = find_unique_colors(color_list_1, color_list_2)
print(result)
