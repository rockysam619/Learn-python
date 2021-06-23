############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
from art import logo
def clear(): 
    os.system('cls')

def deal_card():
    #returns a random card from the deck.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(list_of_cards):
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0

    if sum(list_of_cards) > 21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        return sum(list_of_cards)

    return sum(list_of_cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over, you lose."
    if user_score == computer_score:
        return "It's a Draw!"
    elif user_score == 0 or user_score == 21:
        return "You win with a blackjack!"
    elif computer_score == 0 or computer_score == 21:
        return "Dealer wins with a blackjack!"
    elif user_score > 21:
        return "You went over, you lose."
    elif computer_score > 21:
        return "Dealer went over, you win!"
    elif user_score > computer_score:
        return "Dealer wins!"
    else:
        return "You win!"

def play_blackjack():
    user_cards = []
    computer_cards = []
    is_game_over = False
    print(logo)

    for _ in range(2):
        user_cards.append(deal_card())

    for _ in range(2):
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_total = calculate_score(user_cards)
        computer_total = calculate_score(computer_cards)
        print(f"\nYour cards: {user_cards}, Current score: {user_total}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_total == 0 or computer_total == 0 or user_total == 21 or computer_total > 21 or user_total > 21:
            is_game_over = True

        else:    
            next_draw = input("Do you wanna hit or stay? : ").lower()
            if next_draw == 'hit':
                user_cards.append(deal_card())

            else:
                is_game_over = True

    while computer_total !=0 and computer_total < 17:
        computer_cards.append(deal_card())
        computer_total = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, Final score: {user_total}")
    print(f"Dealer cards: {computer_cards}, Dealer final score: {computer_total} ")
    print(compare(user_total, computer_total))

while input("\nDo you wanna play blackjack? y or n: ")  == "y":
        clear()
        play_blackjack()
