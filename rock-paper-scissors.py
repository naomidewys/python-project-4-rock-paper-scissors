import random

# Game option images
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

# Game option list
game_options = [rock, paper, scissors]

print("Welcome to Rock Paper Scissors")

# User selection
user = int(input("What do you choose? Type '0' for Rock, '1' for Paper, or '2' for Scissors\n"))
print("You chose:")
print(game_options[user])

# Computer selection
computer = random.randint(0, 2)
print("Computer chose:")
print(game_options[computer])

#Rules for game results
if user >= 3 or user <0:
    print("Invalid number. Please try again!")
elif user == computer:
    print("It's a draw!")
elif user == 0 and computer == 1:
    print("You lose!")
elif user == 0 and computer == 2:
    print("You win!")
elif user == 1 and computer == 0:
    print("You win!")
elif user == 1 and computer == 2:
    print("You lose!")
elif user == 2 and computer == 0:
    print("You lose!")
elif user == 2 and computer == 1:
    print("You win!")
