# Day 4 Project: Rock Paper Scissors
# https://replit.com/@appbrewery/rock-paper-scissors-start

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ["rock", "paper", "scissors"]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player == 0:
    print(rock)
elif player == 1:
    print(paper)
elif player == 2:
    print(scissors)

print("Computer chose:")
computer = random.choice(choices)

if computer == "rock":
    print(rock)
elif computer == "paper":
    print(paper)
elif computer == "scissors":
    print(scissors)

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

if (player == 0) and (computer == "scissors"):
    print("You won")
elif (player == 2) and (computer == "paper"):
    print("You won")
elif (player == 1) and (computer == "rock"):
    print("You won")
else:
    print("You lose")

# rock-paper-scissors-end
# https://replit.com/@appbrewery/rock-paper-scissors-end

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

figure = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(figure[player])

computer = random.randint(0, 2)
print("Computer chose:")
print(figure[computer])

if player >= 3 or player < 0: 
  print("You typed an invalid number, you lose!") 
elif player == 0 and computer == 2:
  print("You win!")
elif computer == 0 and player == 2:
  print("You lose")
elif computer > player:
  print("You lose")
elif player > computer:
  print("You win!")
elif computer == player:
  print("It's a draw")

# This code will give you an IndexError when type 5 as input
# and point to line print(figure[player]) as the issue
# But on line if player >= 3 or player < 0:
# prevents a crash by detecting
# any numbers great than or equal to 3 or less than 0.

# rock-paper-scissors-debugged-end
# https://repl.it/@appbrewery/rock-paper-scissors-debugged-end

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

figure = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player >= 3 or player < 0: 
    print("You typed an invalid number, you lose!") 
else:
    print(figure[player])

    computer = random.randint(0, 2)
    print("Computer chose:")
    print(figure[computer])


    if player == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and player == 2:
        print("You lose")
    elif computer > player:
        print("You lose")
    elif player > computer:
        print("You win!")
    elif computer == player:
        print("It's a draw")

