# Exercise 4 - Pizza Order Practice
# Automatic pizza order program
# Based on a user's order, work out their final bill.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":  # Small Pizza: $15
  bill = 15
    if add_pepperoni == "Y":  # Pepperoni for Small Pizza: +$2
      bill += 2
elif size == "M":  # Medium Pizza: $20
  bill = 20
    if add_pepperoni == "Y":  # Pepperoni for Medium or Large Pizza: +$3
      bill += 3
elif size == "L":  # Large Pizza: $25
  bill = 25
    if add_pepperoni == "Y":  # Pepperoni for Medium or Large Pizza: +$3
      bill += 3

if extra_cheese == "Y":  # Extra cheese for any size pizza: + $1
  bill += 1

print(f"Your final bill is: ${bill}.")
