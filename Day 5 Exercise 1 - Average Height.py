# Exercise 1 - Average Height
# Program that calculates the average height from a List of heights.

input_heights = input("Input a list of student heights ")

# Convert a String to a List
# names = names_string.split(" ")
student_heights = input_heights.split(" ")

"""
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
"""

total = 0
counter = 0

for height in student_heights:
    # print(type(height))
    total += int(height)        # total of heights
    counter += 1                # number of heights

average_height = total / counter
print(round(average_height))    # average height rounded to the nearest whole number
                                # round() function to round the average height

# Alternative Solution

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
average_height = round(total_height / number_of_students)
print(average_height)

"""
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)
"""
