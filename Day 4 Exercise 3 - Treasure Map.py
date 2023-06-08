# Exercise 3 - Treasure Map
# Program that mark a spot or a square on the map with an X using a two-digit system.

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

# nested list
map = [row1, row2, row3]
# [['⬜️','⬜️','⬜️'],['⬜️','⬜️','⬜️'],['⬜️','⬜️','⬜️']]

# format the 3 lists to be printed as a 3 by 3 square, each on a new line.
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

# The first digit in the input will specify the column (the position on the horizontal axis).
column = int(position[0])-1
# The second digit in the input will specify the row number (the position on the vertical axis).
row = int(position[1])-1

# change items in the list
# e.g. Pennsylvania not spelled Pennsylvania
# change it to Pencilvania
# states_of_america[1] = "Pencilvania"

map[row][column] = "X"


print(f"{row1}\n{row2}\n{row3}")

