# Exercise 2 - BMI 2.0
# Program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# use the exponent operator
BMI = weight / height ** 2
# round result to the nearest whole number
round_BMI = round(BMI)
message = f"Your BMI is {round_BMI}, you"

# interpretation of BMI based on the BMI value
if BMI < 18.5:  # Under 18.5 they are underweight
    # "Your BMI is 18, you are underweight."
    print(message, "are underweight.")
elif BMI > 18.5 and BMI < 25:   # Over 18.5 but below 25 they have a normal weight
    # "Your BMI is 22, you have a normal weight."
    print(message, "have a normal weight.")
elif BMI > 25 and BMI < 30: # Over 25 but below 30 they are slightly overweight
    # "Your BMI is 28, you are slightly overweight."
    print(message, "are slightly overweight.")
elif BMI < 30 and BMI > 35: # Over 30 but below 35 they are obese
    # "Your BMI is 33, you are obese."
    print(message, "are obese.")
elif BMI < 35:  # Above 35 they are clinically obese.
    # "Your BMI is 40, you are clinically obese."
    print(message, "are clinically obese.")
