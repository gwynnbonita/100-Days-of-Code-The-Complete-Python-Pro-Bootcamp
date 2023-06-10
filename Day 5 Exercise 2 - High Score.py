# Exercise 1 - Average Height
# Program that calculates the highest score from a List of scores.

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

"""
highest_score = 0
for x in student_scores:
    for y in student_scores:
        if x > y:
            highest_score = x
        elif x < y:
            highest_score = y
print(f"The highest score in the class is: {highest_score}")
"""

highest_score = 0
for score in student_scores:
    # if highest_score == 0 or highest_score < score:
    if score > highest_score:
        highest_score = score
        # print(highest_score)
    
print(f"The highest score in the class is: {highest_score}")

# get the index of the highest score
# print(student_scores.inex(highest_score))

# index_highest_score = student_scores.index(highest_score)
# print(index_highest_score)
