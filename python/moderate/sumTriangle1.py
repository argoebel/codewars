# https://www.codewars.com/kata/6357825a00fba284e0189798/train/python
def get_sum(n):
    # solutions = []
    total = 0
    for i in range(n+1):
        for j in range(i+1):
            total += 2*j + i + 1
    return total


get_sum(2)
get_sum(3)

        