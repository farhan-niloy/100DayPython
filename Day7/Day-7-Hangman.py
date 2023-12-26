import random

insect_list = ["Ladybugs", "Cockroach", "Mantis"]
guess = input("Guess a letter: ").lower()
chosen_word = random.choice(insect_list)
word_length = len(chosen_word)

display = []
for i in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position].lower()
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")