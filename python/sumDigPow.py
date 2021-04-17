# https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python
# The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

# def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
#   final = []
#   for i in range(a,b+1):
#     splitNum = list(str(i))
#     count = 0
#     for j in range(len(splitNum)):
#       count += int(splitNum[j]) ** (j+1)
#     if count == i:
#       final.append(i)
#   return final


def sum_dig_pow(a, b):
  return list(filter(myFilter, range(a,b+1)))

def myFilter(num):
  return sum(int(y) ** (x+1) for x,y in enumerate(str(num))) == num
  



print(sum_dig_pow(1, 100))