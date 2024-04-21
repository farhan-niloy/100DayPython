from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer):
    if guess > answer:
        print("Too high!")
    if guess < answer:
        print("Too low!")
    else:
        print(f"You got it! The answer is {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level.lower() == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)

turns = set_difficulty()
print(f"You have {turns} guesses left.")
guess = int(input("Make a guess: "))



