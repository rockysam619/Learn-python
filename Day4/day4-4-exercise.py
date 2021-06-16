#Rock Paper Scissors
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
choicelist =[0, 1, 2]

option = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if option == 0:
    print(rock)
elif option == 1:
    print(paper)
elif option == 2:
    print(scissors)
else:
    print("Please type 0, 1 or 2 only")
    exit()

print("Computer Chose:")
computer_choice = random.choice(choicelist)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)


if option == computer_choice:
    print("Draw")
elif option == 0 and computer_choice == 1:
    print("Computer won")
elif option == 1 and computer_choice == 0:
    print("You won") 
elif option == 0 and computer_choice == 2:
    print("You won")
elif option == 2 and computer_choice == 0:
    print("Computer won")
elif option == 2 and computer_choice == 1:
    print("You won")
elif option == 1 and computer_choice == 2:
    print("Computer won")
else:
    print("It's a game, sometimes there are no winners.")

