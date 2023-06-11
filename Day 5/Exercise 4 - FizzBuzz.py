# Exercise 4 - FizzBuzz
# Program that automatically prints the solution to the FizzBuzz game.
#   Print each number from 1 to 100
#   When the number is divisible by 3, it prints "Fizz".
#   When the number is divisible by 5, it prints "Buzz".
#   if the number is divisible by both 3 and 5, it prints "FizzBuzz"

for number in range(1, 101):
    if (number % 5 == 0) and (number % 3 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
