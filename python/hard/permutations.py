# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python

def permutations(s):
    results = []
    if len(s) <= 2:
        return set([s,s[::-1]])
    else:
        for x in range(len(s)):
            results += [s[x] + temp for temp in permutations(s[0:x]+s[x+1:])]
    return set(results)


print(permutations('abc'))
