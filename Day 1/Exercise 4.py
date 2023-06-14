# Exercise 4 - Variables
# Program that switches the values stored in the variables a and b.

a = input("a: ")
b = input("b: ")

c = a               # Alternative Solution:
d = b               #   c = a
a = d               #   a = b
b = c               #   b = c

print("a: " + a)
print("b: " + b)
