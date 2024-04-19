import os

from art import logo

print(logo)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


bids = {}
bidding_finish = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if int(bid_amount) > int(highest_bid):
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finish:
    name = input("What's your name? ")
    price = input("What's your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? (y/n)")
    if should_continue == "n":
        bidding_finish = True
        find_highest_bidder(bids)
    elif should_continue == "y":
        clear_terminal()




