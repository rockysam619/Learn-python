# Gues the number
import random
import os
from art import logo

print(logo)

def clear(): 
    os.system('cls')

def set_difficulty():      
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        tries = 10
    else:
        tries = 5
    return tries

def check_answer(guess, answer):
    if guess > answer:
        return "Too high. Guess Again."
    elif guess < answer:
        return "Too low. Guess Again."
    else:
        return f"You got it! The answer was {answer}."

def guess_game(): 
    
    print("""
    Welcome to the number guessing game!!
    I am thinking of a number between 1 and 100.
    Please choose numbers between 1 and 100: 
    """)

    answer = random.randint(0, 100)
    
    tries = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {tries} tries remaining")
        guess = int(input("Make a guess: "))
        print(f"\n{check_answer(guess, answer)}")
        if tries == 0:
            print("You are out of tries!!")
            return
        tries-=1


guess_game()
while input("\nWould you like to play another guessing game? y or n : ") == "y":
    clear()
    guess_game()