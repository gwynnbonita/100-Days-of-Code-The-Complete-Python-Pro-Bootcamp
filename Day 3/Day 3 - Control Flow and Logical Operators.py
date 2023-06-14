# Day 3 - Conditional Statements, Logical Operators, Code Blocks and Scope
# 29. Control Flow with if / else and Conditional Operators  7
# 31. Nested if statements and elif statements               62
# 34. Multiple If Statements in Succession                   137
# 36. Logical Operators                                      175

print("\n29. Control Flow with if / else and Conditional Operators\n")
# 29. Control Flow with if / else and Conditional Operators

# Conditional
# if / else

# if condition:
#   do this
# else:
#   do this

water_level = 50
if water_level > 80:
  print("Drain water")
else:
  print("Continue")

# > 120cm


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
# Variable = Assignment

if height > 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

print("\nSecond Condition:")

if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

# Comparison Operators
# Operator  Meaning
#    >    Greater than
#    <    Less than
#   >=    Greater than or equal to
#   <=    Less than or equal to
#   ==    Equal to
#   !=    Not equal to

print("\nThird Condition:")

if height == 120:  # Check Equality
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

# % - Modulo Opeerator
# remainder of the division

print("\n31. Nested if statements and elif statements\n")
# 31. Nested if statements and elif statements

# > 120 cm
# <= 18 $ 7
# > 18 $ 12

# if condition:
#   do this
# else:
#   do this

# Nested if / else
# if condition:
#   if another condition:
#     do this
#    else:
#     do this
# else:
#   do this

#############################

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

print("\nSecond Improvement:\n") #############################

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

print("\nThird Improvement:\n") #############################
  
# < 12 "5$"
# 12 - 18 "$7"
# > 18 "$12"

# if / elif / else
# if condition1:
#   do A
# elif condition2:
#   do B
# else:
#   do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

print("\n34. Multiple If Statements in Succession\n")
# 34. Multiple If Statements in Succession

# if / elif / else      # Multiple if
# if condition1:        # if condition1:
#   do A                #   do A
# elif condition2:      # if condition2:
#   do B                #   do B
# else:                 # if condition3:
#   do C                #   do C

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    # Add $3 to their bill
    bill += 3  # bill = bill + 2

  print(f"Your final bill is ${bill}")
    
else:
  print("Sorry, you have to grow taller before you can ride.")

print("\n36. Logical Operators\n")
# 36. Logical Operators

# if condition1 & condition2 & condition3:
#   do this
# else:
#    do this

# Logical Operators

#   A  and  B
#   True  and  True  =  True
#     Both A and B have to be true,
#     for the entire line of code to be true.
#   False  and  True  =  False
#     If just one of them is true,
#     then the overall thing evaluates to false.

a = 12
a > 15  # False
a > 10  # True
a > 10 and a < 13  # True  and  True  =  True
a > 15 and a < 13  # False  and  True  =  False

#   C or D
#   False  or  True  =  True
#   True  or  False  =  True
#   True  or  True  =  True
#   False or False  =  False

#   not E
#     reverses a condition

a = 12
not a > 15  # True

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    # Add $3 to their bill
    bill += 3  # bill = bill + 2

  print(f"Your final bill is ${bill}")
    
else:
  print("Sorry, you have to grow taller before you can ride.")
