# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
# Description:
# Welcome.

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)


# my solutions


def alphabet_position(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newStr = ''
    strLen = len(text)
    for i in range(len(text)):
        if text[i].lower() in alphabet:
            newStr += str(alphabet.index(text[i].lower())+1)
            if i+1 != strLen:
                newStr += ' '
    return newStr


def alphabet_position1(text):
    return ' '.join(str(ord(i) - ord("a")+1) for i in text.lower() if i.isalpha())

# use ord() to find unicode values. ord("a") is the lowest unicode value so we can
# subtract any value by ord("a") to determine its rank in the alphabet. We add +1
# so our alphabet list starts with index 1 instead of zero. We iterate through a for
# loop consisting of the given string in lowercase and if a character in the string
# is in the alphabet, it's ordinal value joined to the string separated by a space.

    # other solutions:


def alphabet_position10(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


def alphabet_position11(s):
    return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())


print(ord("a") - ord("a") + 1)
print(ord("b"))
print(ord("z"))

print(alphabet_position1("The narwhal bacons at midnight."))
