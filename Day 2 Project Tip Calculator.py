# Day 2 Project: Tip Calculator

print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? $"))
#If the bill was $150.00, split between 5 people, with 12% tip. 
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# To convert tip percentage to decimal, divide it into 100
tip_decimal = tip / 100

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
split = int(input("How many people to split the bill? "))
result = (total_bill / split) * tip_decimal
#Tip: There are 2 ways to round a number.
result2decimalplaces = round(result, 2)

print(f"Each person should pay: ${result2decimalplaces}")
