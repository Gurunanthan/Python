def Name_Reverser_By_Maintaining_Spaces(name):
    def find_spaces(name):
        spaceList = []
        index = 0
        for char in name:
            if char == " ":
                spaceList.append(index)
            index += 1
        return spaceList
    spaceList = find_spaces(name)
    name_no_spaces = name.replace(" ", "")
    reversed_name_with_no_spaces = name_no_spaces[::-1]
    reversed_name_with_spaces = list(reversed_name_with_no_spaces)
    for pos in spaceList:
        reversed_name_with_spaces.insert(pos, " ")
    final_reversed_name = "".join(reversed_name_with_spaces)
    return final_reversed_name
result = Name_Reverser_By_Maintaining_Spaces("hello world")
print(result)
