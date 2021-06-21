# The bidding program
import os
def clear(): 
    os.system('cls')

from art import logo
looping = True
winner = ""
maximum = 0

while looping:
    print(logo)
    name = input("What is your name? : ")
    bid = int(input("What is your bid amount? : $"))

    bid_dict = {}
    bid_dict[name] = bid
    for key in bid_dict:
        if bid_dict[key] > maximum:
            maximum = bid_dict[key]
            winner = key

    more_bids = input("\n Are there any more bids? Yes or No? : ").lower()
    if more_bids == "no":
        print(f"\nThe bid winner is {winner} with a bid of ${maximum}")
        looping = False

    else:
        clear()




