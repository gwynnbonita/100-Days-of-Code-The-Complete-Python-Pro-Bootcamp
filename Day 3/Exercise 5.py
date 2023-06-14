# Exercise 5 - Love Calculator
# Program that tests the compatibility between two people.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# lower() - a function changes all the letters in a string to lowercase.
# count() - a function will give you the number of times a letter occurs in a string.

two_names = name1 + name2
# lower_names = two_names.lower()
# a = lower_names.count("a")

# Take both people's names and check for the number of times the letters in the word TRUE occurs.
t = two_names.lower().count('t')
r = two_names.lower().count('r')
u = two_names.lower().count('u')
e = two_names.lower().count('e')
true = t + r + u + e

# Then check for the number of times the letters in the word LOVE occurs.
l = two_names.lower().count('l')
o = two_names.lower().count('o')
v = two_names.lower().count('v')
e = two_names.lower().count('e')
love = l + o + v + e

# Then combine these numbers to make a 2 digit number.
love_scores = int(str(true) + str(love))

# For Love Scores less than 10 or greater than 90, the message should be:
if (love_scores < 10) or (love_scores > 90):
    print(f"Your score is {love_scores}, you go together like coke and mentos.")
# For Love Scores between 40 and 50, the message should be:
elif (love_scores > 40) and (love_scores < 50):
    print(f"Your score is {love_scores}, you are alright together.")
# Otherwise, the message will just be their score:
else:
    print(f"Your score is {love_scores}.")
