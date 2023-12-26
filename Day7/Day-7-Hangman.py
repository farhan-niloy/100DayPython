import random

insect_list = ["Ladybugs", "Cockroach", "Mantis"]

guess = input("Guess a letter: ").lower()

chosen_word = random.choice(insect_list)

dash = [""] * len(chosen_word)

for i, letter in enumerate(chosen_word):

    if letter == guess:
        dash[i] = "p"
    else:
        dash[i] = "_"

print(dash)