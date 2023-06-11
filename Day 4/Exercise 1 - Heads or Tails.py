# Exercise 1 - Heads or Tails
# "Virtual Coin Toss Program" that randomly tell the user "Heads" or "Tails".

import random

# generate a random number, either 0 or 1
heads_or_tails = random.randint(0, 1)
# Then used the number to print out Heads or Tails.
# e.g. 1 means Heads
if heads_or_tails == 1:
# 0 means Tails
    print("Heads")
elif heads_or_tails == 0:
    print("Tails")
