# https://www.codewars.com/kata/526dbd6c8c0eb53254000110/train/python
import re

def alphanumeric(password):        
    regular_expression = "[A-Za-z0-9]{1,}\w"
    pattern = re.compile(regular_expression)
    valid = re.search(pattern, password)
    if valid:
        return valid and valid.group() == password
    else:
        return False

pattern = re.compile('^[0-9a-zA-Z]+$')

def alphanumeric_better(string):
    print(pattern.match(string))
    return pattern.match(string) is not None

def alphanumeric_best(password):
    return password.isalnum()


alphanumeric_better("PassW0rd")
alphanumeric_better("Abc@123")
alphanumeric_better("demo  _")
alphanumeric_better("  ")
alphanumeric_better("")