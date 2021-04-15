# https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
# expanded_form(12) # Should return '10 + 2'

# def expanded_form(num):
#   exp = 0
#   arr = []
#   while num > 0:
#     if num % 10:
#       arr.insert(0, str((num % 10) * 10 ** exp))
#     num = num // 10
#     exp += 1
#   return ' + '.join(arr)


def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')



print(expanded_form(70304))