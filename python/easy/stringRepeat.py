def repeat_str(repeat, string):
    return "".join(string for i in range(repeat))

def repeat_str_best(repeat, string):
    return repeat * string


print(repeat_str(5, "Hello"))
print(repeat_str_best(5, "Hello"))