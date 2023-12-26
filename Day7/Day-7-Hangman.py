import random

insect_list = ["Ladybugs", "Cockroach", "Mantis"]

guess = input("Guess a letter: ").lower()

chosen_word = random.choice(insect_list)

word_length = len(chosen_word)

dash = []

for i in range(word_length):
    dash += "_"

for j in range(word_length):
    letter = chosen_word[j]

    if letter == guess:
        dash[j] = letter
    else:
        dash[j] = "_"

print(dash)