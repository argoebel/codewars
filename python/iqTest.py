# https://www.codewars.com/kata/552c028c030765286c00007d/train/python
# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

# ##Examples :

# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd


# my solutions

# only ONE character differs from the rest therefore, you only need to check at most 3 integers to determine if looking
# for odd or even number.

def iq_test(numbers):
    evenOdd = []
    for i in numbers.split(" "):
        evenOdd.append(int(i) % 2)
    if sum(evenOdd) == len(evenOdd)-1:
        return evenOdd.index(0) + 1
    else:
        return evenOdd.index(1) + 1


print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 1 1"))


# other solutions

def iq_test10(numbers):
    nums = [int(n) % 2 for n in numbers.split()]
    if sum(nums) == 1:
        return nums.index(1) + 1
    else:
        return nums.index(0) + 1
