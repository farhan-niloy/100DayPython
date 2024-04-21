from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high!")
        turns -= 1
    elif guess < answer:
        print("Too low!")
        turns -= 1
    else:
        print(f"You got it! The answer is {answer}")
    return turns


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level.lower() == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = set_difficulty()

    guess = 0

    true = True
    while guess != answer and true:
        print(f"You have {turns} guesses left.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            true = False
            print("\tYou lose!")


game()
