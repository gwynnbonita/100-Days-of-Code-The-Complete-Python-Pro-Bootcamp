# Exercise 3 - Adding Even Numbers
# Program that calculates the sum of all the even numbers from 1 to 100.

total = 0
for even_numbers in range(2, 101, 2):
    total += even_numbers
print(total)
