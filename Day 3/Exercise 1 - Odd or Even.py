# Exercise 1 - Odd or Even
# Program that works out whether if a given number is an odd or even number.

number = int(input("Which number do you want to check? "))

# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
remainder = number % 2

# if number % 2 == 0:
if remainder == 0:  # if a number is divided by 2 and remains nothing then, it is an even number.
    print("This is an even number.")
else:   # However, if the number has it's remainder after dividing by 2 then, it is an odd number.
    print("This is an odd number.")
