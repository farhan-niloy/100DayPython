from art import logo
import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_cards():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_scores(cards):
    """Takes a list of cards and return the calculated score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(11)

    return sum(cards)


user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

user_score = calculate_scores(user_cards)
computer_score = calculate_scores(computer_cards)
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first cards: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True










