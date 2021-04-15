# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python

# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
# Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?
# Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

def tickets(people):
  register = {100: 0, 50: 0, 25: 0}
  for i in people:
    if (i == 25):
      register[25] += 1
    elif (i / 25 == 2) and (register[25] >= 1):
      register[50] += 1
      register[25] -= 1
    elif (i / 25 == 4):
      if (register[50] >= 1) and (register[25] >= 1):
        register[50] -= 1
        register[25] -= 1
      elif (register[25] >= 3):
        register[25] -= 3
      else:
        return 'NO'
    else:
      return 'NO'
  return 'YES'

print(tickets([25, 25, 50]))
print(tickets([25, 25, 50, 50, 100]))