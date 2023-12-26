import random

insect_list = ["Ladybugs", "Cockroach", "Mantis"]

guess = input("Guess a letter: ").lower()

chosen_word = random.choice(insect_list)

word_length = len(chosen_word)

dash = []

for i in range(word_length):
    dash += "_"


def letter_check():
    for j in range(word_length):

        letter = chosen_word[j]
        if letter == guess:
            dash[j] = letter
        else:
            dash[j] = "_"


a = True


while a:
    i = 0
    if not dash[i] == "_":
        letter_check()
    else:
        a = False

    i += 1


print(dash)