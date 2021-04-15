# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    return int(''.join(sorted(list(str(num)), reverse=1)))


  
print(descending_order(123456789))