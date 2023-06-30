# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)