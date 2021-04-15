# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
# The tests will always use some integral number, so don't worry about that in dynamic typed languages.
import math

def is_square(n):
  if n >=0 and math.sqrt(n) % 1 == 0:
    return True
  return False

print(is_square(25))