# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python
# The Fibonacci numbers are the numbers in the following integer sequence (Fn):



# def productFib(prod):
#   x = 0
#   y = 1
#   while x*y < prod:
#     temp = y
#     y += x
#     x = temp
#   return [x, y, x*y == prod]

def productFib(prod):
  x,y = 0,1
  while x*y < prod:
    x,y = y, y+x
  return [x,y, y*x == prod]

print(productFib(4895))
print(productFib(5895))