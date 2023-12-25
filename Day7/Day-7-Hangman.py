import random

insect_list = ["Ladybugs", "Cockroach", "Mantis"]

guess = input("Guess a letter: ").lower()

chosen_word = random.choice(insect_list)

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")
