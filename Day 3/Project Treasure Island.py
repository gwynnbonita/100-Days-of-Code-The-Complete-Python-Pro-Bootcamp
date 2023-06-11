# Day 3 Project: Treasure Island

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("left or right? \n").lower()
if (not left_or_right == "left") and (left_or_right == "right"):
    print("Fall into a hole. Game Over.")
elif left_or_right == "left":
    swim_or_wait = input("swim or wait \n").lower()
    if (not swim_or_wait == "wait") and (swim_or_wait == "swim"):
        print("Attacked by trout. Game Over.")
    elif swim_or_wait == "wait":
        which_door = input("Which door? \n Red, Blue, or Yellow \n").lower()
        if which_door == "red":
            print("Burned by fire. Game Over.")
        elif which_door == "blue":
            print("Eaten by beasts. Game Over.")
        elif which_door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
