# Exercise 3 - Life in Weeks
# Program that used maths and f-Strings that tell us the number of days, weeks, months left if lived until 90 years old.

age = input("What is your current age? ")

lives = 90
years = lives - int(age)
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
days = 365
x = days * years

weeks = 52
y = weeks * years

months = 12
z = months * years

# output
# You have x days, y weeks, and z months left.
print(f"You have {x} days, {y} weeks, and {z} months left.")
