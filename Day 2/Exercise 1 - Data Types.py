# Exercise 1 - Data Types
# Program that adds the digits in a 2 digit number.

two_digit_number = input("Type a two digit number: ")

# originally, the type of tens and ones
# is string, <class 'str'>
# type convertion to int
tens = int(two_digit_number[0])
ones = int(two_digit_number[1])

print(tens + ones)

# Alternative Solution

# tens = two_digit_number[0]
# ones = two_digit_number[1]

# tens_int = int(tens)
# ones_int = int(ones)

# add = tens_int + ones_int
# print(add)


# Dr. Angela Yu's

# first_digit =  two_digit_number[0]
# second_digit = two_digit_number[1]

# result = int(first_digit) + int(second_digit)
# print(result)
