class RomanNumerals:

    def to_roman(number):
        vals = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        numerals = ""
        for key in vals.keys():
            if number // key > 0:
                numerals += (number // key) * vals.get(key)
                number -= (number // key) * key
        
        return numerals

    def from_roman(roman_num):
        vals = { "M": 1000,  "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1  }
        total = 0
        for index, char in enumerate(roman_num):
            total += vals[char]
            if index-1 >= 0 and vals[roman_num[index-1]] < vals[char]:
                total -= 2 * vals[roman_num[index-1]]
        return total


# print(RomanNumerals.from_roman('XXI'))
# print(RomanNumerals.from_roman('MMVIII'))
# print(RomanNumerals.from_roman('IV'))

print(RomanNumerals.to_roman(1000))
print(RomanNumerals.to_roman(4))
print(RomanNumerals.to_roman(1))
print(RomanNumerals.to_roman(1990))
print(RomanNumerals.to_roman(2008))
