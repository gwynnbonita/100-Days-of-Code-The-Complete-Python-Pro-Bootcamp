#Password Generator Project
#Eazy Level - Order not randomised:            18
#Hard Level - Order of characters randomised:  89
# password-generator-end                       136
#Eazy Level                                    148
#Hard Level                                    162

import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Main Solution - For Loop
list_generated_password = []  # variable for first solution
string_generated_password = ""  # variable for second solution

for timesx in range(nr_letters):
    # random.choice(seq)
    chosen_letters = random.choice(letters)
    # print(chosen_letters)
    list_generated_password.append(chosen_letters)  # list - first solution
    # print(list_generated_password)
    string_generated_password += chosen_letters  # string - second solution
    # print(string_generated_password)

for timesy in range(nr_symbols):
    chosen_symbols = random.choice(symbols)
    list_generated_password.append(chosen_symbols)  # list - first solution
    string_generated_password += chosen_symbols  # string - second solution

for timesz in range(nr_numbers):
    chosen_numbers = random.choice(numbers)
    list_generated_password.append(chosen_numbers)  # list - first solution
    string_generated_password += chosen_numbers  # string - second solution

# Convert a List to a String
# list2string_generated_password = ''.join([str(items) for items in list_generated_password])
list2string_generated_password = ''.join(list_generated_password)

# Password Printer
print(
    f'\nHere is your (Eazy Level) password:\n{list_generated_password}\n[List] Converted to "String": {list2string_generated_password}'
)
print(
    f'\nHere is your (Eazy Level) password:\n"String": {string_generated_password}'
)

# Second Alternaive Solution - random.sample(population, k)
# without the use of For Loop or For Loop with Range

# generated_password_ver2 = []

chosen_letters_ver2 = random.sample(letters, nr_letters)
chosen_symbols_ver2 = random.sample(symbols, nr_symbols)
chosen_numbers_ver2 = random.sample(numbers, nr_numbers)

joined_chosen_letters_ver2 = ''.join(chosen_letters_ver2)
joined_chosen_symbols_ver2 = ''.join(chosen_symbols_ver2)
joined_chosen_numbers_ver2 = ''.join(chosen_numbers_ver2)

# ''.join(random.sample(letters, nr_letters))
# ''.join(random.sample(symbols, nr_symbols))
# ''.join(random.sample(numbers, nr_numbers))

generated_password_ver2 = ''.join(joined_chosen_letters_ver2 +
                                  joined_chosen_symbols_ver2 +
                                  joined_chosen_numbers_ver2)
# generated_password_ver2 = ''.join(random.sample(letters, nr_letters) + random.sample(symbols, nr_symbols) + random.sample(numbers, nr_numbers))
"""
generated_password_ver2.append(chosen_letters_ver2)
generated_password_ver2.append(chosen_symbols_ver2)
generated_password_ver2.append(chosen_numbers_ver2)

# generated_password_ver2.append(random.sample(letters, nr_letters))
# generated_password_ver2.append(random.sample(symbols, nr_symbols))
# generated_password_ver2.append(random.sample(numbers, nr_numbers))

# concatenate the lists  =>  randomise  =>  convert into a string
"""

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Main Solution - random.shuffle(x)  =>  random.sample(x, len(x))

# accessing "list_generated_password"from Eazy Level

# list - first option: random.shuffle(x)
# returns None and cannot be stored in a new list
random.shuffle(list_generated_password)
# list - second option: random.sample(x, len(x))
# "randomised_list_generated_password" - new randomly-shuffled list
randomised_list_generated_password = random.sample(
    list_generated_password, len(list_generated_password))

# Converting the List into a String
# first option: accessing the randomised "list_generated_password" from Eazy Level as list,
# and stored in variable "list2string_randomised_generated_password"
# list2string_randomised_generated_password = ''.join([str(items) for items in list_generated_password])
list2string_randomised_generated_password = ''.join(list_generated_password)
# second option: "randomised_list_generated password" as list,
# and stored in variable "2string_randomised_list_generated_password"
# string_randomised_list_generated_password = ''.join([str(items) for items in randomised_list_generated_password])
string_randomised_list_generated_password = ''.join(
    randomised_list_generated_password)

# Password Printer
print(
    f"\nHere is your (Hard Level and randomised) password:\nfrom Eazy Level: {list2string_randomised_generated_password}\nstored in new randomly-shuffled list: {string_randomised_list_generated_password}"
)
"""
# Hard Level - Incorrect Outputs:

# Second Alternative Solution - random.choice(seq)
hard_level_2nd = ""

for times in range(nr_letters + nr_symbols + nr_numbers):
  chosen = random.choice(letters + symbols + numbers)
  hard_level_ver2 += chosen  # string

# Third Alternative Solution - random.sample(population, k)
hard_level_ver3 = random.sample(letters + symbols + numbers, nr_letters + nr_symbols + nr_numbers)  # list
# Converting the List into a String
list2string_hard_level_ver3 = ''.join([str(items) for items in hard_level_ver2])
print(f"\nHere is your password: hard_level_ver2 {hard_level_ver2} hard_level_ver3 {list2string_hard_level_ver3}")
"""

# password-generator-end
#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
