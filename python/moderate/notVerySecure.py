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

def alphanumeric_best(password):
    return password.isalnum()


alphanumeric("PassW0rd")
alphanumeric("Abc@123")
alphanumeric("demo  _")
alphanumeric("  ")