# Day 2 - Data Types, Numbers, Operations, Type Conversion, f-Strings
# 19. Python Primitive Data Types                    7
# 20. Type Error, Type Checking and Type Conversion  52
# 22. Mathematical Operations in Python              93
# 24. Number Manipulation and F Strings in Python    125

print("\n19. Python Primitive Data Types\n")
# 19. Python Primitive Data Types

len("Hello")
print(len("Hello"))  # 5

# print(len(12352))
# TypeError: object of type 'int' has no len()

#Data Types

# String

"Hello"[0]
print("Hello"[0])  # H
# Subscript
# [0],[1],[2],[3],[4]
"Hello"[4]  # o

print("123" + "345")  # 123345
print("hello" + "world")

# Integer
# - whole numbers, numbers without any decimal places

print(123 + 345)

123456789
123_456_789

# Large Integers
342,654,896
342_654_896

# Float
# - floating-point number

3.14159
3141.59

# Boolean

True
False

print("\n20. Type Error, Type Checking and Type Conversion\n")
# 20. Type Error, Type Checking and Type Conversion

len("Hello")

# Type Error
# len(4837)

num_char = len(input("What is your name?"))

# Type Error
# print("Your name has " + num_char + " characters.")
# TypeError: can only concatenate str (not "int") to str

# Type Checking
print(type(num_char))

# Type Conversion
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))
# <class 'int'>

a = str(123)
print(type(a))
# <class 'str'>

a = float(123)
print(type(a))
# <class 'float'>

print(70 + float("100.5"))
# 170.5
# converting the string, "100.5" to float
# and adding to 70

print(str(70) + str(100))
# 70100

print("\n22. Mathematical Operations in Python\n")
# 22. Mathematical Operations in Python

3 + 5
7 - 4
3 * 2
6 / 3
print(6 / 3)  # float => 2.0
print(type(6 / 3))

2 ** 2
print(2 ** 2)
print(2 ** 3)  # 2 * 2 * 2

# PEMDAS
# Parentheses      ()
# Exponents        **
# Multiplication   *
# Division         /
# Addition         +
# Subtraction      -

# *  /
# +  -
# most to the left
# is the priority

print(3 * 3 + 3 / 3 - 3)

# PEMDASLR
print(3 / 3 + 3 * 3 - 3)

print("\n24. Number Manipulation and F Strings in Python\n")
# 24. Number Manipulation and F Strings in Python

print(8 / 3)
print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2))
print(round(2.666666666666, 2))

print(8 // 3)  # floor division
print(type(8 // 3))  # <class 'int'>
print(type(8 / 3))  # <class 'float'>
print(type(4 / 2))  # <class 'float'>
print(4 / 2)

result = 4 / 2  # 2
result /= 2  # 1
print(result)  # 1

score = 0
# User scores a point
# score = score + 1
score += 1
# +=, -=, *=, /=
print(score)

score = 0
height = 1.8
isWinning = True
# f-String
print("your score is " + str(score))
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
