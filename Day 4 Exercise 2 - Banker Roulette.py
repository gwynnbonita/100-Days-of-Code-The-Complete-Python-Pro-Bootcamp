# Exercise 2 - Banker Roulette
# Program that select a random name from a list of names.

# Import the random module here
import random

# Split string method

names_string = input("Give me everybody's names, separated by a comma. ")
# print(type(names_string)) <class 'str'>

# Convert a String to a List
names = names_string.split(", ")
# print(type(names))        <class 'list'>

b = len(names)
index = random.randint(1, b)
# print(index)

payer = names[index]
# print(payer)
print(f"{payer} is going to buy the meal today!")
