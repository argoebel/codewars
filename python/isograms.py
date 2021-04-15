# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# def is_isogram(string):
#   string = string.lower()
#   while len(string) > 0:
#     if string[0] in string[1:]:
#       return False
#     else:
#       string = string[1:]
#   return True

def is_isogram(string):
  return len(string) == len(set(string.lower()))


print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))