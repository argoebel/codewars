# https://www.codewars.com/kata/52e864d1ffb6ac25db00017f/train/python

def to_postfix (infix):
    queue = []
    stack = []

    for i in infix:
        if i.isnumeric():
            queue.append(i)
        else:
            stack.append(i)
    
    return queue