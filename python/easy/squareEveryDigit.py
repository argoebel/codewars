def square_digits(num):
    return int("".join(str(int(char) * int(char)) for char in str(num)))

def square_digits_BEST(num):
    return int(''.join(str(int(char)**2) for char in str(num)))

print(square_digits(9119))