# Exercise 2 - Banker Roulette
# Program that select a random name from a list of names.

# Import the random module here
import random

# Split string method
#   given string
names_string = input("Give me everybody's names, separated by a comma. ")
#   gives us the type of string1
# print(type(names_string))     <class 'str'>

# Convert a String to a List
names = names_string.split(", ")
# print(type(names))            <class 'list'>

# used the len() function, to find the number of elements in the list "names"
b = len(names)      # stored in variable b

# variable b as "maximum inclusive" or "higher range"
# in the Python random Module Method, random.randint(a, b)
index = random.randint(0, b-1)
# print(index)

payer = names[index]
# print(payer)
print(f"{payer} is going to buy the meal today!")
