#Heads or Tails toss with computer
import random
choice = (input("Please enter your choice: Heads or Tails? : ")).lower()
random_toss = random.randint(0,1)

if random_toss == 0:
    outcome = "heads"
else:
    outcome = "tails"

if choice == outcome:
    print("You won")
else:
    print("Computer wins")