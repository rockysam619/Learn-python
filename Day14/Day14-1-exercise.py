#Higher Lower Game
from art import logo
from art import vs
from game_data import data
import random

def choose_data(data):
    A = random.choice(data)
    B = random.choice(data)
    if A == B:
        B = random.choice(data)
    return A, B

def compare(A, B):
    if A['follower_count'] > B['follower_count']:
        return "A"
    else:
        return "B"

def high_low_game():
    current_score = 0
    winning = True
    A, B = choose_data(data)
    while winning:
        print(logo)
        print(f"\nCompare A: {A['name']}, {A['description']}, from {A['country']}")
        print(vs)
        print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")
        u_choice = input("\nWho has more followers? Type A or B: ")
        if compare(A, B) == u_choice:
            current_score+=1
            print(f"\nYou're right! Current score: {current_score}")
            A = B
            B = random.choice(data)
        else:
            print(f"\nSorry, that's wrong. Final score: {current_score}")
            winning = False


high_low_game()
while input("\nWould you like to play again? y or n: ") == "y":
    print(logo)
    high_low_game()