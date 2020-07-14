# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then - 1 should be returned. You may assume the parameter is positive.

# Examples:

# findNextSquare(121) - -> returns 144
# findNextSquare(625) - -> returns 676
# findNextSquare(114) - -> returns - 1 since 114 is not a perfect

# my solutions


def find_next_square(sq):
    counter = 1
    squared = 1
    while squared <= sq:
        squared = counter ** 2
        if squared == sq:
            return (counter + 1)**2
        counter += 1
    return -1


# other solutions
def find_next_square10(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1


print(find_next_square(144))
print(find_next_square(319225))
