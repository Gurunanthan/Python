function_name = input("")

function_object = getattr(__builtins__, function_name, None)

if function_object:
    help(function_object)
else:
    print(f"{function_name} is not a valid built-in function.")
