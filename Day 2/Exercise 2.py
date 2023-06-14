# Exercise 2 - BMI Calculator
# Program that calculates the Body Mass Index (BMI) from a user's weight and height.

# BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_float = float(height)
weight_float = float(weight)

BMI = weight_float / height_float ** 2

# bmi = int(weight) / float(height) ** 2

BMI_int = int(BMI)
print(BMI_int)

# Alternate
print(int(BMI))
