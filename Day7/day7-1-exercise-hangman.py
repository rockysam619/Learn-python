# The Hangman Game
import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

no_of_lives = 6
print(logo)
#Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

# Create a list of dashes with legth equal to chosen word 

dash_list = []
for i in chosen_word:
    dash_list += "_"

end_of_game = False
guess_list = []
#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    
# Display the hangman art or the chosen alphabet at the right places if it exists in the chosen word
    if guess in guess_list:
        print(f"You already chose {guess}") 
    guess_list.append(guess)
    
    if guess not in chosen_word:
        no_of_lives-=1
        print("\nWrong guess")
        print(stages[no_of_lives])

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            dash_list[i] = guess
        

    print(dash_list) 

    if "_" not in dash_list:
        end_of_game = True
        print("\nYou won")
    if no_of_lives == 0:
        end_of_game = True
        print("\nYou Lose")
        print(f"The letter was {chosen_word}")
